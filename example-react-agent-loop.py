import asyncio
from operator import add
from typing import Annotated, Literal
from typing_extensions import TypedDict

from langgraph.graph import StateGraph, START, END


# ============================================================
# 1. STATE
# ============================================================

class RetrievedDocument(TypedDict):
    content: str
    source: str
    score: float


class AgentState(TypedDict):
    original_question: str
    current_query: str

    # Multiple search attempts can add documents.
    retrieved_docs: Annotated[list[RetrievedDocument], add]

    search_attempts: int
    max_attempts: int

    evidence_status: Literal["enough", "not_enough"]
    answer: str


# ============================================================
# 2. MOCK SEARCH TOOL
# ============================================================

async def mock_km_search(query: str) -> list[RetrievedDocument]:
    """
    Mock replacement for:
    - Azure AI Search
    - SharePoint search
    - Blob indexed document search
    - Dataverse search

    In real KM 2.0, this would call Azure AI Search with:
    - vector search
    - keyword search
    - semantic ranking
    - RBAC filters
    """

    await asyncio.sleep(0.2)

    if "malaria audit risk" in query.lower():
        return [
            {
                "content": "Audit reports mention procurement delays and weak stock monitoring for malaria grants.",
                "source": "Malaria_Audit_Report_2024.pdf",
                "score": 0.91,
            },
            {
                "content": "Key risks include delayed implementation, weak supplier oversight, and inconsistent data reporting.",
                "source": "Grant_Risk_Assessment.docx",
                "score": 0.88,
            },
        ]

    if "malaria" in query.lower():
        return [
            {
                "content": "The malaria program includes prevention, treatment, and supply chain components.",
                "source": "Malaria_Program_Overview.docx",
                "score": 0.70,
            }
        ]

    return []


# ============================================================
# 3. NODE: SEARCH DOCUMENTS
# ============================================================

async def search_documents_node(state: AgentState) -> dict:
    """
    Search documents using current query.
    """

    print(f"Searching with query: {state['current_query']}")

    docs = await mock_km_search(state["current_query"])

    return {
        "retrieved_docs": docs,
        "search_attempts": state["search_attempts"] + 1,
    }


# ============================================================
# 4. NODE: EVALUATE EVIDENCE
# ============================================================

def evaluate_evidence_node(state: AgentState) -> dict:
    """
    Decide whether the retrieved evidence is enough.

    In production, this could be:
    - heuristic based on number of docs and scores
    - LLM-based relevance evaluator
    - RAGAS-style context precision/recall evaluation
    """

    docs = state["retrieved_docs"]

    high_quality_docs = [
        doc for doc in docs
        if doc["score"] >= 0.85
    ]

    if len(high_quality_docs) >= 2:
        status = "enough"
    else:
        status = "not_enough"

    print(f"Evidence status: {status}")

    return {
        "evidence_status": status
    }


# ============================================================
# 5. CONDITIONAL ROUTER
# ============================================================

def route_after_evidence_check(
    state: AgentState
) -> Literal["generate_answer", "refine_query", "end"]:
    """
    This creates the loop.

    If evidence is enough:
        go to generate_answer

    If evidence is not enough and attempts remain:
        go to refine_query

    If max attempts reached:
        stop and generate best-effort answer
    """

    if state["evidence_status"] == "enough":
        return "generate_answer"

    if state["search_attempts"] >= state["max_attempts"]:
        return "generate_answer"

    return "refine_query"


# ============================================================
# 6. NODE: REFINE QUERY
# ============================================================

def refine_query_node(state: AgentState) -> dict:
    """
    Refine query to improve retrieval.

    In production, this could call an LLM query rewriter.
    """

    original_question = state["original_question"]

    refined_query = f"{original_question} audit risk findings"

    print(f"Refined query: {refined_query}")

    return {
        "current_query": refined_query
    }


# ============================================================
# 7. NODE: GENERATE ANSWER
# ============================================================

def generate_answer_node(state: AgentState) -> dict:
    """
    Generate final answer from retrieved documents.

    In production, this would call Azure OpenAI.
    """

    docs = state["retrieved_docs"]

    if not docs:
        answer = (
            "I could not find enough relevant documents to answer this question confidently."
        )
    else:
        context = "\n\n".join(
            [
                f"Source: {doc['source']}\nContent: {doc['content']}"
                for doc in docs
            ]
        )

        answer = f"""
Based on the retrieved KM 2.0 documents, the key risks are:

1. Procurement delays
2. Weak supplier oversight
3. Weak stock monitoring
4. Inconsistent data reporting
5. Delayed implementation

Evidence used:

{context}
"""

    return {
        "answer": answer
    }


# ============================================================
# 8. BUILD GRAPH
# ============================================================

builder = StateGraph(AgentState)

builder.add_node(
    "search_documents",
    search_documents_node
)

builder.add_node(
    "evaluate_evidence",
    evaluate_evidence_node
)

builder.add_node(
    "refine_query",
    refine_query_node
)

builder.add_node(
    "generate_answer",
    generate_answer_node
)

builder.add_edge(
    START,
    "search_documents"
)

builder.add_edge(
    "search_documents",
    "evaluate_evidence"
)

builder.add_conditional_edges(
    "evaluate_evidence",
    route_after_evidence_check,
    {
        "generate_answer": "generate_answer",
        "refine_query": "refine_query",
        "end": END,
    }
)

# This edge creates the loop.
builder.add_edge(
    "refine_query",
    "search_documents"
)

builder.add_edge(
    "generate_answer",
    END
)

graph = builder.compile()


# ============================================================
# 9. RUN DEMO
# ============================================================

async def main():
    initial_state: AgentState = {
        "original_question": "What are the key risks for malaria grants?",
        "current_query": "malaria",
        "retrieved_docs": [],
        "search_attempts": 0,
        "max_attempts": 3,
        "evidence_status": "not_enough",
        "answer": "",
    }

    result = await graph.ainvoke(initial_state)

    print("\n==============================")
    print("FINAL ANSWER")
    print("==============================")
    print(result["answer"])

    print("\nSearch attempts:", result["search_attempts"])


if __name__ == "__main__":
    asyncio.run(main())
