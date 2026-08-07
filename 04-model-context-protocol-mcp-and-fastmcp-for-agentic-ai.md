# 04 - Model Context Protocol (MCP) & FastMCP for Agentic AI

> A practical guide to MCP, FastMCP, Enterprise Integrations, LangGraph + MCP Architectures, and Interview Preparation.
>
> Goal:
>
> - Understand why MCP exists
> - Understand MCP Client & Server architecture
> - Understand Tools, Resources, and Prompts
> - Understand FastMCP
> - Understand MCP vs Traditional Tool Calling
> - Understand MCP + LangGraph
> - Understand Enterprise MCP Architectures
> - Master MCP Interview Questions

---

# Table of Contents

1. Why MCP Exists
2. The USB-C Analogy
3. Problems Before MCP
4. MCP Architecture
5. MCP Core Components
6. Tools
7. Resources
8. Prompts
9. MCP Servers
10. MCP Clients
11. FastMCP
12. FastMCP Tools
13. FastMCP Resources
14. FastMCP Prompts
15. MCP vs Function Calling
16. MCP + LangGraph
17. Enterprise MCP Architectures
18. Interview Questions
19. Common Mistakes
20. Production Best Practices

---

# Why MCP Exists

Imagine building an Agent.

It needs access to:

```text
SharePoint

Jira

GitHub

SQL Database

ServiceNow

SAP

Azure Storage
```

Without MCP:

```text
Every Agent

↓

Needs Custom Integration

↓

For Every Tool
```

This becomes difficult to maintain.

---

# The USB-C Analogy

The best analogy.

Before USB-C:

```text
Phone A → Charger A

Phone B → Charger B

Phone C → Charger C
```

---

After USB-C:

```text
One Standard Connector
```

---

MCP does the same thing.

Instead of:

```text
Every LLM

↓

Different Integration Logic
```

we create:

```text
Standard MCP Protocol
```

that every MCP-compatible client and server understands. MCP provides a standardized way for LLM applications to interact with tools, resources, and prompts. 【1-c8ba86】【2-612fe2】

---

# Problem Before MCP

Traditional architecture:

```text
Agent

├── Jira Integration

├── GitHub Integration

├── SharePoint Integration

├── SQL Integration

└── ServiceNow Integration
```

---

Problems:

```text
Tightly Coupled

Hard To Reuse

Duplicate Logic

Maintenance Nightmare
```

---

# MCP Solution

```text
Agent

↓

MCP Client

↓

MCP Server

↓

Tool / Resource
```

The agent talks to MCP.

The MCP server handles the integration.

---

# High Level Architecture

```text
LLM Agent

↓

MCP Client

↓

MCP Server

↓

External System
```

Examples:

```text
GitHub MCP Server

Jira MCP Server

SAP MCP Server

SharePoint MCP Server
```

---

# MCP Components

Three core concepts:

```text
Tools

Resources

Prompts
```

These are the primary capabilities exposed by MCP servers. 【1-c8ba86】【2-612fe2】

---

# Tools

Tools perform actions.

Think:

```text
POST Endpoint
```

Mental Model:

```text
Do Something
```

---

Examples:

```text
Create Ticket

Send Email

Execute SQL

Generate Report

Create Work Item
```

---

Pseudo Code

```text
User

↓

Create Jira Ticket

↓

MCP Tool

↓

Jira
```

---

# Resource

Resources expose data.

Think:

```text
GET Endpoint
```

Mental Model:

```text
Read Something
```

---

Examples:

```text
Policy Document

Configuration

Knowledge Base

Grant Metadata

Audit Report
```

MCP resources are typically read-oriented sources of information. 【2-612fe2】【1-c8ba86】

---

# Prompt

Reusable instruction templates.

Example:

```text
Summarize Audit Findings

Risk Assessment Template

Board Summary Template
```

MCP allows reusable prompts to be exposed by servers. 【1-c8ba86】【2-612fe2】

---

# Mental Model

```text
Tool
    ↓
Action

Resource
    ↓
Data

Prompt
    ↓
Instructions
```

---

# MCP Server

An MCP Server exposes:

```text
Tools

Resources

Prompts
```

to MCP Clients.

---

Example:

```text
Jira MCP Server
```

May expose:

```text
Create Ticket

Get Ticket

Search Tickets
```

---

# MCP Client

The MCP Client is used by:

```text
Agent

Assistant

LangGraph Workflow
```

The client discovers and interacts with MCP servers.

---

# FastMCP

FastMCP is a Python framework for building MCP servers and clients more easily. It provides decorators and abstractions for tools, resources, prompts, transports, validation, and server management. 【1-c8ba86】【3-b7cab1】

---

# Creating A FastMCP Server

```python
from fastmcp import FastMCP

mcp = FastMCP(
    "Demo Server"
)
```

A FastMCP server starts from a simple Python object and can then expose tools, resources and prompts. 【3-b7cab1】【1-c8ba86】

---

# FastMCP Tool

Tool Example:

```python
from fastmcp import FastMCP

mcp = FastMCP("Demo")


@mcp.tool()
def add(
    a: int,
    b: int
) -> int:

    return a + b
```

FastMCP exposes Python functions as MCP tools using decorators. 【1-c8ba86】【2-612fe2】

---

# What Happens?

User asks:

```text
What is 5 + 7?
```

↓

```text
LLM

↓

MCP Tool

↓

add()

↓

12
```

---

# FastMCP Resource

Example:

```python
@mcp.resource(
    "config://version"
)
def version():

    return "1.0"
```

Resources expose information that the LLM can retrieve. 【1-c8ba86】

---

# FastMCP Prompt

Example:

```python
@mcp.prompt()
def summarize():

    return """
    Summarize the following text.
    """
```

Reusable prompts are another MCP capability. 【1-c8ba86】【2-612fe2】

---

# Running FastMCP

Example:

```python
if __name__ == "__main__":

    mcp.run()
```

FastMCP manages transport and protocol details while exposing the MCP server. 【3-b7cab1】【1-c8ba86】

---

# MCP vs Traditional Function Calling

This is a VERY common interview question.

---

# Traditional Function Calling

```text
Agent

↓

Tool Definition

↓

Execute Tool
```

Everything is defined locally.

---

# MCP

```text
Agent

↓

MCP Client

↓

Remote MCP Server

↓

Tool
```

Distributed architecture.

---

# Traditional Tool Calling

Pros:

```text
Simple

Fast

Good For Small Apps
```

---

Cons:

```text
Poor Reusability

Strong Coupling

Hard Scaling
```

---

# MCP

Pros:

```text
Reusable

Standardized

Enterprise Friendly

Decoupled
```

---

Cons:

```text
More Infrastructure

More Components
```

---

# LangGraph + MCP

One of the hottest interview topics.

---

# Architecture

```text
LangGraph Agent

↓

MCP Client

↓

MCP Server

↓

Tool
```

---

# Example

Question:

```text
Create Jira ticket for vulnerability.
```

Workflow:

```text
Classifier

↓

Security Agent

↓

Jira MCP Tool

↓

Ticket Created
```

---

# Enterprise Architecture

Imagine KM 2.0 Version 5.

---

```text
Supervisor Agent

↓

MCP Client

├── SharePoint MCP

├── Jira MCP

├── ServiceNow MCP

├── GitHub MCP

├── Databricks MCP

└── SAP MCP
```

---

Benefits:

```text
One Integration Pattern

Reusable Components

Governance

Security

Scalability
```

---

# Multi-Agent + MCP Example

```text
Supervisor

├── Audit Agent

├── Finance Agent

├── Fraud Agent

└── Reporting Agent

↓

Each Agent

↓

Own MCP Tools

↓

Aggregate Results
```

---

# Pseudo Code Example

```text
Receive User Question

↓

Classify Intent

↓

Select Agent

↓

Connect To MCP Tool

↓

Execute Operation

↓

Update State

↓

Generate Response

↓

Return Result
```

---

# Real World Examples

## GitHub MCP

Tools:

```text
Create PR

Create Issue

Read Repository
```

---

## Jira MCP

Tools:

```text
Create Ticket

Update Ticket

Search Ticket
```

---

## SharePoint MCP

Resources:

```text
Policies

Knowledge Base

Documents
```

---

## Databricks MCP

Tools:

```text
Execute Query

Run Job

Read Metadata
```

---

# Common Interview Questions

---

## What Is MCP?

Answer:

> MCP is a standardized protocol that enables AI applications to interact with tools, resources, and prompts through MCP servers. It promotes interoperability and decouples agent logic from system integrations. 【1-c8ba86】【2-612fe2】

---

## Why Was MCP Created?

Answer:

> To provide a consistent integration standard between LLM applications and external systems, avoiding custom integrations for every tool.

---

## What Are MCP Tools?

Answer:

> MCP Tools perform actions and side effects such as creating tickets, running queries, or invoking APIs. 【1-c8ba86】【2-612fe2】

---

## What Are MCP Resources?

Answer:

> MCP Resources expose read-oriented data that LLMs can access as context. 【1-c8ba86】【2-612fe2】

---

## What Are MCP Prompts?

Answer:

> MCP Prompts are reusable templates that can guide model interactions. 【1-c8ba86】【2-612fe2】

---

## What Is FastMCP?

Answer:

> FastMCP is a Python framework that simplifies the development of MCP servers and clients using decorators and high-level abstractions. 【1-c8ba86】【3-b7cab1】

---

## MCP vs Function Calling?

Answer:

> Function calling is typically local to an application, while MCP enables standardized communication with local or remote MCP servers, improving reusability and interoperability.

---

## Why MCP For Enterprises?

Answer:

> MCP standardizes integrations, improves governance, promotes reusability, and allows multiple agent systems to leverage common integrations.

---

# Common Mistakes

❌ Confusing MCP with LangGraph

❌ Thinking MCP replaces agents

❌ Using MCP when a simple local tool is enough

❌ Exposing dangerous actions without security controls

❌ Making one giant MCP server

---

# Production Best Practices

✅ Domain-specific MCP servers

✅ Authentication and Authorization

✅ Audit Logging

✅ Tool Input Validation

✅ Async Tool Execution

✅ Separation of Concerns

✅ Reusable Resources

✅ Small Focused Tools

---

# Ultimate Mental Model

```text
LangGraph
      ↓
Orchestrates Work

MCP
      ↓
Connects To Systems

FastMCP
      ↓
Builds MCP Servers

Tools
      ↓
Do Things

Resources
      ↓
Read Things

Prompts
      ↓
Guide Things
```

---

# 60 Second Interview Answer

"MCP is a standardized protocol that allows AI systems to interact with tools, resources, and prompts in a consistent way. MCP servers expose capabilities, MCP clients consume them, and frameworks like FastMCP make it easy to build production-ready MCP integrations. LangGraph orchestrates agent workflows, while MCP provides a standardized mechanism for agents to access external systems."


# Full Code Example: LangGraph + MCP Issue Resolution Agent

> Use case:
>
> User needs issue-resolution steps.
>
> Knowledge could exist in:
>
> - SharePoint
> - Jira
> - Azure Blob Storage
> - Dataverse
>
> If the user is not satisfied with the generated answer, create a ServiceNow ticket.

---

# 1. Architecture

```text
User
  ↓
LangGraph Workflow
  ↓
Knowledge Retrieval Node
  ├── SharePoint MCP Server
  ├── Jira MCP Server
  ├── Azure Blob MCP Server
  └── Dataverse MCP Server
  ↓
Answer Generation Node
  ↓
Satisfaction Check Node
  ↓
Conditional Edge
  ├── User Satisfied → END
  └── User Not Satisfied → ServiceNow Ticket Node
```

---

# 2. Transport Reminder

MCP supports transport mechanisms for communication between client and server. Commonly discussed transports include:

```text
STDIO
    Local subprocess communication.

Streamable HTTP
    HTTP-based communication for remote / production MCP servers.

SSE
    Older HTTP + Server-Sent Events pattern still seen in examples.
```

MCP uses JSON-RPC messages over supported transports. The MCP specification describes `stdio` and Streamable HTTP as standard transports in the referenced version, while older versions describe HTTP with SSE. 【1-6aee74】【2-0f5d57】

FastMCP also provides client transport abstractions for connecting to MCP servers using options like STDIO and HTTP. 【3-fd2fa9】【4-7f1bf0】

---

# 3. Key Design Idea

```text
LangGraph
    → controls workflow, state, routing, conditional edges

MCP
    → standardizes access to external systems

FastMCP
    → helps build MCP servers and clients in Python
```

---

# 4. Required Packages

```bash
pip install langgraph langchain-openai langchain-mcp-adapters pydantic
```

If building your own MCP servers:

```bash
pip install fastmcp
```

---

# 5. Full LangGraph + MCP Code

> Important:
>
> This is a realistic skeleton, not a directly runnable enterprise app.
>
> You must replace:
>
> - MCP URLs
> - Auth tokens
> - Tool names
> - Azure OpenAI details
> - Actual ServiceNow fields
>
> based on your environment.

```python
import asyncio
from operator import add
from typing import Annotated, Literal, Optional

from typing_extensions import TypedDict

from langgraph.graph import StateGraph, START, END
from langchain_openai import AzureChatOpenAI
from langchain_mcp_adapters.client import MultiServerMCPClient


# ============================================================
# 1. LLM SETUP
# ============================================================

llm = AzureChatOpenAI(
    azure_endpoint="https://YOUR-AZURE-OPENAI-ENDPOINT.openai.azure.com/",
    api_key="YOUR_AZURE_OPENAI_KEY",
    api_version="2024-02-15-preview",
    azure_deployment="gpt-4.1",
    temperature=0
)


# ============================================================
# 2. MCP CLIENT SETUP
# ============================================================

"""
MultiServerMCPClient lets one client layer connect to multiple MCP servers.

Conceptual MCP servers:
- SharePoint MCP
- Jira MCP
- Azure Blob MCP
- Dataverse MCP
- ServiceNow MCP

Each server exposes tools.
"""

mcp_client = MultiServerMCPClient(
    {
        "sharepoint": {
            "transport": "http",
            "url": "https://mcp.company.com/sharepoint/mcp",
            "headers": {
                "Authorization": "Bearer YOUR_TOKEN"
            }
        },
        "jira": {
            "transport": "http",
            "url": "https://mcp.company.com/jira/mcp",
            "headers": {
                "Authorization": "Bearer YOUR_TOKEN"
            }
        },
        "blob": {
            "transport": "http",
            "url": "https://mcp.company.com/blob/mcp",
            "headers": {
                "Authorization": "Bearer YOUR_TOKEN"
            }
        },
        "dataverse": {
            "transport": "http",
            "url": "https://mcp.company.com/dataverse/mcp",
            "headers": {
                "Authorization": "Bearer YOUR_TOKEN"
            }
        },
        "servicenow": {
            "transport": "http",
            "url": "https://mcp.company.com/servicenow/mcp",
            "headers": {
                "Authorization": "Bearer YOUR_TOKEN"
            }
        }
    }
)


# ============================================================
# 3. STATE DEFINITIONS
# ============================================================

class Evidence(TypedDict):
    source: str
    title: str
    content: str
    url: Optional[str]


class IssueResolutionState(TypedDict):
    user_id: str
    issue: str

    # Reducer:
    # Multiple retrieval sources can contribute evidence.
    evidence: Annotated[list[Evidence], add]

    answer: str
    confidence: float

    # In a real UI, this is captured after user sees the answer.
    user_satisfied: Optional[bool]

    ticket_id: Optional[str]
    final_message: str


# ============================================================
# 4. MCP TOOL HELPERS
# ============================================================

async def get_tool_by_name(tool_name: str):
    """
    Fetch available MCP tools and return the matching tool.

    In production, tool names may be namespaced.
    Example:
    - search_sharepoint_knowledge
    - search_jira_articles
    - create_servicenow_ticket
    """

    tools = await mcp_client.get_tools()

    for tool in tools:
        if tool.name == tool_name:
            return tool

    raise ValueError(f"Tool not found: {tool_name}")


async def call_mcp_tool(tool_name: str, args: dict):
    """
    Invoke a tool exposed by one of the MCP servers.
    """

    tool = await get_tool_by_name(tool_name)
    result = await tool.ainvoke(args)

    return result


async def safe_search_tool(
    tool_name: str,
    args: dict,
    source_name: str
) -> list[Evidence]:
    """
    Safe wrapper for retrieval tools.

    If one source fails, we do not fail the entire workflow.
    We return an empty evidence list for that source.
    """

    try:
        result = await call_mcp_tool(
            tool_name=tool_name,
            args=args
        )

        evidence: list[Evidence] = []

        for item in result:
            evidence.append(
                {
                    "source": source_name,
                    "title": item.get("title", "Untitled"),
                    "content": item.get("content", ""),
                    "url": item.get("url")
                }
            )

        return evidence

    except Exception as e:
        print(f"[WARN] MCP retrieval failed for {source_name}: {e}")
        return []


# ============================================================
# 5. LANGGRAPH NODE: RETRIEVE KNOWLEDGE
# ============================================================

async def retrieve_knowledge_node(
    state: IssueResolutionState
) -> dict:
    """
    Search SharePoint, Jira, Azure Blob and Dataverse concurrently.
    """

    issue = state["issue"]

    sharepoint_task = safe_search_tool(
        tool_name="search_sharepoint_knowledge",
        args={
            "query": issue,
            "top_k": 5
        },
        source_name="SharePoint"
    )

    jira_task = safe_search_tool(
        tool_name="search_jira_articles",
        args={
            "query": issue,
            "top_k": 5
        },
        source_name="Jira"
    )

    blob_task = safe_search_tool(
        tool_name="search_blob_documents",
        args={
            "query": issue,
            "top_k": 5
        },
        source_name="Azure Blob"
    )

    dataverse_task = safe_search_tool(
        tool_name="search_dataverse_records",
        args={
            "query": issue,
            "top_k": 5
        },
        source_name="Dataverse"
    )

    results = await asyncio.gather(
        sharepoint_task,
        jira_task,
        blob_task,
        dataverse_task
    )

    merged_evidence: list[Evidence] = []

    for source_items in results:
        merged_evidence.extend(source_items)

    return {
        "evidence": merged_evidence
    }


# ============================================================
# 6. LANGGRAPH NODE: GENERATE RESOLUTION ANSWER
# ============================================================

async def generate_resolution_node(
    state: IssueResolutionState
) -> dict:
    """
    Generate resolution steps from retrieved knowledge.
    """

    issue = state["issue"]
    evidence = state["evidence"]

    if not evidence:
        return {
            "answer": (
                "I could not find enough relevant information in the available "
                "knowledge sources to confidently provide resolution steps."
            ),
            "confidence": 0.2
        }

    context_blocks = []

    for index, item in enumerate(evidence, start=1):
        context_blocks.append(
            f"""
Source {index}
System: {item["source"]}
Title: {item["title"]}
URL: {item.get("url")}

Content:
{item["content"]}
"""
        )

    context = "\n\n".join(context_blocks)

    prompt = f"""
You are an enterprise IT support assistant.

The user has reported this issue:

{issue}

You retrieved the following knowledge-base evidence:

{context}

Instructions:
1. Provide clear step-by-step resolution guidance.
2. Mention the sources used.
3. Do not invent unsupported troubleshooting steps.
4. If evidence is weak, say confidence is limited.
5. Keep the answer practical and user-friendly.
6. Format the response in Markdown.
"""

    response = await llm.ainvoke(prompt)

    answer = response.content

    # Simple demo confidence heuristic.
    # Production systems should use retrieval scores, source trust,
    # answer evaluation, citation coverage and user feedback.
    if len(evidence) >= 3:
        confidence = 0.85
    elif len(evidence) == 2:
        confidence = 0.70
    else:
        confidence = 0.50

    return {
        "answer": answer,
        "confidence": confidence
    }


# ============================================================
# 7. LANGGRAPH NODE: CHECK USER SATISFACTION
# ============================================================

def check_satisfaction_node(
    state: IssueResolutionState
) -> dict:
    """
    In a real application:
    - First graph invocation generates answer.
    - UI asks: "Was this helpful?"
    - Second invocation passes user_satisfied=True/False.

    This node reads state["user_satisfied"] and prepares message.
    """

    if state["user_satisfied"] is True:
        return {
            "final_message": "Glad the resolution steps helped."
        }

    if state["user_satisfied"] is False:
        return {
            "final_message": (
                "The user was not satisfied. Creating a ServiceNow ticket."
            )
        }

    return {
        "final_message": (
            "Resolution steps generated. Waiting for user feedback."
        )
    }


# ============================================================
# 8. CONDITIONAL EDGE
# ============================================================

def route_after_satisfaction(
    state: IssueResolutionState
) -> Literal["create_ticket", "end"]:
    """
    Conditional edge:
    If user is not satisfied, route to ServiceNow ticket creation.
    Otherwise, end.
    """

    if state["user_satisfied"] is False:
        return "create_ticket"

    return "end"


# ============================================================
# 9. LANGGRAPH NODE: CREATE SERVICENOW TICKET
# ============================================================

async def create_servicenow_ticket_node(
    state: IssueResolutionState
) -> dict:
    """
    Create a ServiceNow ticket using an MCP tool.
    """

    result = await call_mcp_tool(
        tool_name="create_servicenow_ticket",
        args={
            "user_id": state["user_id"],
            "short_description": f"Issue not resolved: {state['issue']}",
            "description": f"""
User reported issue:

{state["issue"]}

Generated resolution steps:

{state["answer"]}

User indicated the resolution was not satisfactory.
""",
            "priority": "medium",
            "category": "IT Support"
        }
    )

    ticket_id = result.get("ticket_id")

    if ticket_id:
        final_message = (
            f"I created a ServiceNow ticket for you: {ticket_id}"
        )
    else:
        final_message = (
            "I attempted to create a ServiceNow ticket, "
            "but no ticket ID was returned."
        )

    return {
        "ticket_id": ticket_id,
        "final_message": final_message
    }


# ============================================================
# 10. BUILD LANGGRAPH
# ============================================================

builder = StateGraph(IssueResolutionState)

builder.add_node(
    "retrieve_knowledge",
    retrieve_knowledge_node
)

builder.add_node(
    "generate_resolution",
    generate_resolution_node
)

builder.add_node(
    "check_satisfaction",
    check_satisfaction_node
)

builder.add_node(
    "create_ticket",
    create_servicenow_ticket_node
)

builder.add_edge(
    START,
    "retrieve_knowledge"
)

builder.add_edge(
    "retrieve_knowledge",
    "generate_resolution"
)

builder.add_edge(
    "generate_resolution",
    "check_satisfaction"
)

builder.add_conditional_edges(
    "check_satisfaction",
    route_after_satisfaction,
    {
        "create_ticket": "create_ticket",
        "end": END
    }
)

builder.add_edge(
    "create_ticket",
    END
)

graph = builder.compile()


# ============================================================
# 11. DEMO: USER SATISFIED
# ============================================================

async def demo_user_satisfied():
    result = await graph.ainvoke(
        {
            "user_id": "user_123",
            "issue": "My VPN is not connecting from my laptop.",
            "evidence": [],
            "answer": "",
            "confidence": 0.0,
            "user_satisfied": True,
            "ticket_id": None,
            "final_message": ""
        }
    )

    print("\n=== USER SATISFIED ===")
    print(result["answer"])
    print(result["final_message"])


# ============================================================
# 12. DEMO: USER NOT SATISFIED
# ============================================================

async def demo_user_not_satisfied():
    result = await graph.ainvoke(
        {
            "user_id": "user_123",
            "issue": "My VPN is not connecting from my laptop.",
            "evidence": [],
            "answer": "",
            "confidence": 0.0,
            "user_satisfied": False,
            "ticket_id": None,
            "final_message": ""
        }
    )

    print("\n=== USER NOT SATISFIED ===")
    print(result["answer"])
    print(result["final_message"])
    print("Ticket ID:", result["ticket_id"])


# ============================================================
# 13. MAIN
# ============================================================

if __name__ == "__main__":
    asyncio.run(demo_user_not_satisfied())
```

---

# 6. Alternative Design: Separate Retrieval Nodes

The previous code uses one node:

```python
retrieve_knowledge_node()
```

and calls all MCP sources concurrently using:

```python
asyncio.gather()
```

This is simple and practical.

But LangGraph can also model each source as a separate node:

```text
START
  ↓
Query Router
  ├── SharePoint Retrieval Node
  ├── Jira Retrieval Node
  ├── Blob Retrieval Node
  └── Dataverse Retrieval Node
        ↓
    Aggregator Node
        ↓
    Answer Generator
```

In that architecture, reducers become important.

Example:

```python
from typing import Annotated
from operator import add
from typing_extensions import TypedDict


class State(TypedDict):
    evidence: Annotated[list[Evidence], add]
```

Meaning:

```text
SharePoint evidence
+
Jira evidence
+
Blob evidence
+
Dataverse evidence
=
Merged evidence
```

Without a reducer, one update may overwrite another.

---

# 7. FastMCP Server Example

Below is a simplified FastMCP server showing what the server side may look like.

In production, you may split this into multiple domain-specific MCP servers:

```text
SharePoint MCP Server

Jira MCP Server

Blob MCP Server

Dataverse MCP Server

ServiceNow MCP Server
```

---

```python
from fastmcp import FastMCP

mcp = FastMCP("Enterprise Support MCP Server")


@mcp.tool()
async def search_sharepoint_knowledge(
    query: str,
    top_k: int = 5
) -> list[dict]:
    """
    Search SharePoint knowledge base.
    """

    # Replace this mock with Microsoft Graph / SharePoint search.
    return [
        {
            "title": "VPN Troubleshooting Guide",
            "content": (
                "Check internet connectivity, restart the VPN client, "
                "verify MFA, confirm device compliance, and reset VPN profile."
            ),
            "url": "https://sharepoint.company.com/sites/it/vpn-guide"
        }
    ]


@mcp.tool()
async def search_jira_articles(
    query: str,
    top_k: int = 5
) -> list[dict]:
    """
    Search Jira issues or Jira knowledge base.
    """

    # Replace this mock with Jira API logic.
    return [
        {
            "title": "Known VPN Issue With Client Version 5.2",
            "content": (
                "Users on VPN client version 5.2 may experience connection "
                "failures. Upgrade to version 5.3 and retry."
            ),
            "url": "https://jira.company.com/browse/IT-123"
        }
    ]


@mcp.tool()
async def search_blob_documents(
    query: str,
    top_k: int = 5
) -> list[dict]:
    """
    Search documents stored in Azure Blob Storage.
    """

    # Replace this mock with Azure Blob + Azure AI Search logic.
    return [
        {
            "title": "Remote Access FAQ",
            "content": (
                "If VPN fails, confirm the device compliance status, "
                "network profile, and conditional access requirements."
            ),
            "url": "https://storage.company.com/docs/remote-access-faq.pdf"
        }
    ]


@mcp.tool()
async def search_dataverse_records(
    query: str,
    top_k: int = 5
) -> list[dict]:
    """
    Search Dataverse support records.
    """

    # Replace this mock with Dataverse API logic.
    return [
        {
            "title": "VPN Support Case Pattern",
            "content": (
                "Common VPN failures are caused by expired credentials, "
                "MFA mismatch, or non-compliant device state."
            ),
            "url": "https://dataverse.company.com/support/vpn-pattern"
        }
    ]


@mcp.tool()
async def create_servicenow_ticket(
    user_id: str,
    short_description: str,
    description: str,
    priority: str,
    category: str
) -> dict:
    """
    Create a ServiceNow incident ticket.
    """

    # Replace this mock with ServiceNow API logic.
    return {
        "ticket_id": "INC0012345",
        "url": (
            "https://servicenow.company.com/nav_to.do?"
            "uri=incident.do?sysparm_query=number=INC0012345"
        )
    }


if __name__ == "__main__":
    mcp.run(
        transport="http",
        host="127.0.0.1",
        port=8000
    )
```

---

# 8. STDIO FastMCP Client Example

For local development, you can use STDIO.

With STDIO, the client launches the MCP server as a subprocess and communicates using stdin/stdout. 【1-6aee74】【3-fd2fa9】

```python
import asyncio
from fastmcp import Client


client = Client("enterprise_support_mcp_server.py")


async def main():
    async with client:
        result = await client.call_tool(
            "search_sharepoint_knowledge",
            {
                "query": "VPN is not connecting",
                "top_k": 3
            }
        )

        print(result)


if __name__ == "__main__":
    asyncio.run(main())
```

---

# 9. HTTP FastMCP Client Example

For production-style remote servers, HTTP transport is commonly used.

```python
import asyncio
from fastmcp import Client


client = Client(
    "https://mcp.company.com/support/mcp"
)


async def main():
    async with client:
        result = await client.call_tool(
            "create_servicenow_ticket",
            {
                "user_id": "user_123",
                "short_description": "VPN not connecting",
                "description": "User tried generated steps but issue remains.",
                "priority": "medium",
                "category": "IT Support"
            }
        )

        print(result)


if __name__ == "__main__":
    asyncio.run(main())
```

---

# 10. How This Works In A Real App

## First User Message

```text
My VPN is not connecting from my laptop.
```

Backend invokes graph with:

```python
{
    "user_id": "user_123",
    "issue": "My VPN is not connecting from my laptop.",
    "user_satisfied": None
}
```

Graph flow:

```text
Retrieve knowledge
  ↓
Generate answer
  ↓
Return resolution steps
```

---

## UI Follow-Up

The UI asks:

```text
Was this helpful?
```

User selects:

```text
No
```

---

## Second Invocation

Backend invokes graph again with:

```python
{
    "user_id": "user_123",
    "issue": "My VPN is not connecting from my laptop.",
    "answer": previous_answer,
    "user_satisfied": False
}
```

Graph routes to:

```text
create_servicenow_ticket_node
```

and returns:

```text
INC0012345
```

---

# 11. Interview Explanation

If asked:

> How would you design an issue-resolution agent using LangGraph and MCP?

Say:

```text
I would use LangGraph for orchestration and MCP for integrations.

LangGraph would maintain state across the workflow:
issue, retrieved evidence, generated answer, user feedback, and ticket ID.

The retrieval node would call multiple MCP servers, such as SharePoint, Jira,
Blob Storage and Dataverse, preferably concurrently.

The answer generation node would synthesize resolution steps from retrieved evidence.

Then a satisfaction node would check user feedback.

A conditional edge would route:
- satisfied users to END
- unsatisfied users to a ServiceNow MCP tool that creates a ticket

This keeps workflow logic in LangGraph and enterprise integrations behind MCP servers.
```

---

# 12. Why This Is A Strong Architecture

```text
LangGraph
    Handles state, routing, conditional edges and workflow control.

MCP
    Standardizes access to enterprise systems.

FastMCP
    Simplifies building MCP servers.

Reducers
    Merge evidence from multiple sources.

Conditional Edges
    Route to ServiceNow only when needed.

Async
    Enables parallel calls to multiple knowledge sources.
```

---

# 13. Production Improvements

For a real production implementation, I would add:

```text
1. Authentication and authorization for every MCP server

2. RBAC filtering inside knowledge retrieval

3. Source citations in the final answer

4. Confidence scoring

5. LLM-based evaluation for answer groundedness

6. LangGraph checkpointing

7. Audit logging

8. Rate limiting

9. Retry strategy

10. Observability with traces and metrics
```

---

# 14. Key Takeaways

```text
One LangGraph workflow can use many MCP servers.

One MCP client layer can connect to multiple MCP servers.

MCP servers can expose tools for actions and resources for context.

LangGraph decides what happens next.

MCP performs the external system interaction.

FastMCP makes MCP server development Pythonic.
```

