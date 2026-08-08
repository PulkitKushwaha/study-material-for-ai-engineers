"""
langgraph_agent.py

Goal:
Build a LangGraph agent with:

1. Intent classification
2. Tools
   - RAG retrieval tool
   - NL2SQL tool
   - Summarization tool
3. Retry mechanism
4. Conditional routing
5. Final answer generation
6. Basic evaluation / confidence check

This is a learning-friendly skeleton.
Replace mock implementations with your real KM 2.0 services:
- Azure AI Search
- Azure OpenAI
- Azure SQL
- Cosmos DB
- Blob Storage
- RBAC filters
"""

import asyncio
import functools
from typing import Annotated, Literal, Optional
from typing_extensions import TypedDict
from operator import add

from langgraph.graph import StateGraph, START, END
from langchain_core.tools import tool


# ============================================================
# 1. SIMPLE ASYNC RETRY DECORATOR
# ============================================================

def async_retry(
    max_attempts: int = 3,
    delay_seconds: float = 1.0,
    backoff_factor: float = 2.0,
):
    """
    Simple async retry decorator.

    Use this around:
    - LLM calls
    - Azure AI Search calls
    - SQL calls
    - external API calls

    Interview point:
    Retry is important because LLMs, DBs, vector stores,
    and external services can fail transiently.
    """

    def decorator(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            attempt = 1
            delay = delay_seconds

            while attempt <= max_attempts:
                try:
                    return await func(*args, **kwargs)

                except Exception as e:
                    print(
                        f"[RETRY] {func.__name__} failed. "
                        f"Attempt {attempt}/{max_attempts}. Error: {e}"
                    )

                    if attempt == max_attempts:
                        raise

                    await asyncio.sleep(delay)
                    delay *= backoff_factor
                    attempt += 1

        return wrapper

    return decorator


# ============================================================
# 2. STATE DEFINITION
# ============================================================

class RetrievedDocument(TypedDict):
    content: str
    source: str
    score: float


class KM2AgentState(TypedDict):
    user_id: str
    question: str

    route: Literal["rag", "sql", "summarize", "clarify"]

    # Reducer example:
    # If multiple nodes contribute docs later, add will merge lists.
    retrieved_docs: Annotated[list[RetrievedDocument], add]

    sql_result: Optional[str]
    answer: str
    sources: list[str]
    confidence: float
    errors: Annotated[list[str], add]


# ============================================================
# 3. MOCK EXTERNAL SERVICES
# Replace these with real KM 2.0 implementations.
# ============================================================

@async_retry(max_attempts=3)
async def call_azure_ai_search(
    question: str,
    user_id: str,
    top_k: int = 5,
) -> list[RetrievedDocument]:
    """
    Replace with:
    - Azure AI Search hybrid/vector search
    - RBAC filters from Entra ID groups
    - semantic ranking
    - citation metadata
    """

    await asyncio.sleep(0.2)

    return [
        {
            "content": (
                "KM 2.0 uses retrieval-grounded generation over indexed "
                "enterprise documents with source attribution."
            ),
            "source": "KM2_Solution_Architecture.docx",
            "score": 0.91,
        },
        {
            "content": (
                "RBAC filters ensure users only retrieve documents they are "
                "authorized to access."
            ),
            "source": "KM2_RBAC_Design.docx",
            "score": 0.87,
        },
    ]


@async_retry(max_attempts=3)
async def call_llm(prompt: str) -> str:
    """
    Replace with:
    - AzureChatOpenAI.ainvoke()
    - Azure OpenAI SDK
    - LangChain LCEL chain
    """

    await asyncio.sleep(0.2)

    return f"LLM generated answer based on prompt:\n\n{prompt[:500]}..."


@async_retry(max_attempts=3)
async def generate_sql_from_question(question: str) -> str:
    """
    Replace with your NL2SQL chain.
    """

    await asyncio.sleep(0.2)

    return "SELECT COUNT(*) AS total_records FROM reports;"


@async_retry(max_attempts=3)
async def execute_sql_query(sql: str) -> str:
    """
    Replace with:
    - pyodbc
    - SQLAlchemy
    - Azure SQL connection
    """

    await asyncio.sleep(0.2)

    return "total_records = 128"


# ============================================================
# 4. SAFETY HELPERS
# ============================================================

BLOCKED_SQL_KEYWORDS = [
    "INSERT",
    "UPDATE",
    "DELETE",
    "DROP",
    "ALTER",
    "TRUNCATE",
    "MERGE",
]


def validate_sql(sql: str) -> None:
    """
    Basic SQL safety gate.

    Interview point:
    Never directly execute LLM-generated SQL without validation.
    """

    sql_upper = sql.upper().strip()

    if not sql_upper.startswith("SELECT"):
        raise ValueError("Only SELECT queries are allowed.")

    for keyword in BLOCKED_SQL_KEYWORDS:
        if keyword in sql_upper:
            raise ValueError(f"Blocked SQL keyword detected: {keyword}")


def format_docs_for_prompt(docs: list[RetrievedDocument]) -> str:
    """
    Convert retrieved documents into clean context.
    """

    blocks = []

    for idx, doc in enumerate(docs, start=1):
        blocks.append(
            f"""
Source {idx}
Document: {doc["source"]}
Score: {doc["score"]}

Content:
{doc["content"]}
"""
        )

    return "\n\n".join(blocks)


# ============================================================
# 5. LANGCHAIN TOOLS
# ============================================================

@tool
async def rag_retrieval_tool(
    question: str,
    user_id: str,
) -> list[RetrievedDocument]:
    """
    Retrieve relevant KM 2.0 documents using Azure AI Search.
    """

    docs = await call_azure_ai_search(
        question=question,
        user_id=user_id,
        top_k=5,
    )

    return docs


@tool
async def nl2sql_tool(
    question: str,
) -> str:
    """
    Convert a natural language analytical question into safe SQL,
    validate it, execute it, and return the result.
    """

    sql = await generate_sql_from_question(question)

    validate_sql(sql)

    result = await execute_sql_query(sql)

    return f"SQL Used:\n{sql}\n\nResult:\n{result}"


@tool
async def summarization_tool(
    question: str,
    user_id: str,
) -> str:
    """
    Retrieve relevant documents and summarize them.
    """

    docs = await call_azure_ai_search(
        question=question,
        user_id=user_id,
        top_k=5,
    )

    context = format_docs_for_prompt(docs)

    prompt = f"""
You are summarizing retrieved KM 2.0 content.

User question:
{question}

Retrieved context:
{context}

Task:
Provide a concise, source-grounded summary.
Do not invent unsupported claims.
"""

    summary = await call_llm(prompt)

    return summary


# ============================================================
# 6. ROUTING NODE
# ============================================================

async def classify_intent_node(
    state: KM2AgentState,
) -> dict:
    """
    Decide which path to take.

    In production:
    - Use a small LLM classifier
    - Or rules + LLM fallback
    - Log route decisions for evaluation

    Route options:
    - sql
    - summarize
    - rag
    - clarify
    """

    question = state["question"].lower()

    if len(question.strip()) < 5:
        route = "clarify"

    elif any(
        keyword in question
        for keyword in ["how many", "count", "total", "average", "trend"]
    ):
        route = "sql"

    elif any(
        keyword in question
        for keyword in ["summarize", "summary", "brief"]
    ):
        route = "summarize"

    else:
        route = "rag"

    return {
        "route": route
    }


def route_selector(
    state: KM2AgentState,
) -> Literal["rag_node", "sql_node", "summarize_node", "clarify_node"]:
    """
    Conditional edge function.
    """

    if state["route"] == "sql":
        return "sql_node"

    if state["route"] == "summarize":
        return "summarize_node"

    if state["route"] == "clarify":
        return "clarify_node"

    return "rag_node"


# ============================================================
# 7. RAG NODE
# ============================================================

async def rag_node(
    state: KM2AgentState,
) -> dict:
    """
    RAG path:
    1. Retrieve documents using tool
    2. Generate grounded answer
    """

    try:
        docs = await rag_retrieval_tool.ainvoke(
            {
                "question": state["question"],
                "user_id": state["user_id"],
            }
        )

        context = format_docs_for_prompt(docs)

        prompt = f"""
You are KM 2.0 assistant.

Answer the user's question using only the retrieved context.

User question:
{state["question"]}

Retrieved context:
{context}

Instructions:
1. Answer clearly.
2. Use only the provided context.
3. Mention sources.
4. If the context is insufficient, say so.
"""

        answer = await call_llm(prompt)

        sources = list(
            {
                doc["source"]
                for doc in docs
            }
        )

        confidence = 0.85 if len(docs) >= 2 else 0.55

        return {
            "retrieved_docs": docs,
            "answer": answer,
            "sources": sources,
            "confidence": confidence,
        }

    except Exception as e:
        return {
            "answer": "I could not complete retrieval due to an internal error.",
            "confidence": 0.0,
            "errors": [str(e)],
        }


# ============================================================
# 8. SQL NODE
# ============================================================

async def sql_node(
    state: KM2AgentState,
) -> dict:
    """
    SQL path:
    Use NL2SQL tool.
    """

    try:
        result = await nl2sql_tool.ainvoke(
            {
                "question": state["question"]
            }
        )

        prompt = f"""
You are a data analyst.

The user asked:
{state["question"]}

The SQL result is:
{result}

Explain the result clearly in business language.
"""

        answer = await call_llm(prompt)

        return {
            "sql_result": result,
            "answer": answer,
            "sources": ["Azure SQL"],
            "confidence": 0.80,
        }

    except Exception as e:
        return {
            "answer": "I could not safely answer this SQL question.",
            "confidence": 0.0,
            "errors": [str(e)],
        }


# ============================================================
# 9. SUMMARIZATION NODE
# ============================================================

async def summarize_node(
    state: KM2AgentState,
) -> dict:
    """
    Summarization path:
    Use summarization tool.
    """

    try:
        summary = await summarization_tool.ainvoke(
            {
                "question": state["question"],
                "user_id": state["user_id"],
            }
        )

        return {
            "answer": summary,
            "sources": ["Retrieved KM documents"],
            "confidence": 0.75,
        }

    except Exception as e:
        return {
            "answer": "I could not generate the summary.",
            "confidence": 0.0,
            "errors": [str(e)],
        }


# ============================================================
# 10. CLARIFICATION NODE
# ============================================================

def clarify_node(
    state: KM2AgentState,
) -> dict:
    """
    Ask a clarifying question.
    """

    return {
        "answer": (
            "Could you please provide more detail so I can route your question "
            "to retrieval, summarization, or data analysis?"
        ),
        "confidence": 0.0,
    }


# ============================================================
# 11. BASIC EVALUATION NODE
# ============================================================

def evaluate_answer_node(
    state: KM2AgentState,
) -> dict:
    """
    Lightweight evaluation node.

    In real production:
    - Use RAGAS
    - Use LangSmith dataset evaluation
    - Check faithfulness
    - Check source coverage
    - Track route accuracy
    """

    errors = state.get("errors", [])

    if errors:
        return {
            "confidence": 0.0
        }

    answer = state.get("answer", "")
    sources = state.get("sources", [])

    if not answer:
        return {
            "confidence": 0.0,
            "errors": ["Empty answer generated."],
        }

    if state["route"] == "rag" and not sources:
        return {
            "confidence": 0.3,
            "errors": ["RAG answer produced without sources."],
        }

    return {}


# ============================================================
# 12. BUILD LANGGRAPH
# ============================================================

builder = StateGraph(KM2AgentState)

builder.add_node(
    "classify_intent",
    classify_intent_node,
)

builder.add_node(
    "rag_node",
    rag_node,
)

builder.add_node(
    "sql_node",
    sql_node,
)

builder.add_node(
    "summarize_node",
    summarize_node,
)

builder.add_node(
    "clarify_node",
    clarify_node,
)

builder.add_node(
    "evaluate_answer",
    evaluate_answer_node,
)

builder.add_edge(
    START,
    "classify_intent",
)

builder.add_conditional_edges(
    "classify_intent",
    route_selector,
    {
        "rag_node": "rag_node",
        "sql_node": "sql_node",
        "summarize_node": "summarize_node",
        "clarify_node": "clarify_node",
    },
)

builder.add_edge(
    "rag_node",
    "evaluate_answer",
)

builder.add_edge(
    "sql_node",
    "evaluate_answer",
)

builder.add_edge(
    "summarize_node",
    "evaluate_answer",
)

builder.add_edge(
    "clarify_node",
    END,
)

builder.add_edge(
    "evaluate_answer",
    END,
)

km2_graph = builder.compile()


# ============================================================
# 13. RUN DEMOS
# ============================================================

async def run_demo(question: str):
    initial_state: KM2AgentState = {
        "user_id": "pulkit",
        "question": question,
        "route": "rag",
        "retrieved_docs": [],
        "sql_result": None,
        "answer": "",
        "sources": [],
        "confidence": 0.0,
        "errors": [],
    }

    result = await km2_graph.ainvoke(initial_state)

    print("\n==============================")
    print("QUESTION:")
    print(question)

    print("\nROUTE:")
    print(result["route"])

    print("\nANSWER:")
    print(result["answer"])

    print("\nSOURCES:")
    print(result["sources"])

    print("\nCONFIDENCE:")
    print(result["confidence"])

    print("\nERRORS:")
    print(result["errors"])
    print("==============================\n")


async def main():
    await run_demo(
        "What is KM 2.0 and how does it answer user questions?"
    )

    await run_demo(
        "How many reports are available?"
    )

    await run_demo(
        "Summarize the KM 2.0 architecture."
    )

    await run_demo(
        "Hi"
    )


if __name__ == "__main__":
    asyncio.run(main())
