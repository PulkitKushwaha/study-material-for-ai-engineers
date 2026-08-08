# 05 - LangChain for Agentic AI

> A practical guide to LangChain, LCEL, Chains, Tools, RAG, Agents, and how LangChain fits with LangGraph.
>
> Goal:
>
> - Understand LangChain fundamentals
> - Understand Chains
> - Understand LCEL
> - Understand Prompts
> - Understand Output Parsers
> - Understand Tools
> - Understand Agents
> - Understand RAG
> - Understand LangChain vs LangGraph
> - Master Interview Questions

---

# Table of Contents

1. Why LangChain Exists
2. LangChain Mental Model
3. Core Components
4. Models
5. Prompts
6. Output Parsers
7. Chains
8. LCEL
9. Tools
10. Agents
11. RAG
12. LangChain + LangGraph
13. Production Architecture
14. Interview Questions
15. Best Practices

---

# Why LangChain Exists

Before LangChain:

```python
response = llm.invoke(prompt)
```

Simple.

But real applications need:

```text
Prompting

Retrieval

Tools

Memory

Output Parsing

Workflows
```

Managing everything manually becomes difficult.

---

# What Is LangChain?

Think:

```text
LangChain

=

LLM Application Framework
```

It provides building blocks for:

```text
LLMs

Prompts

Chains

Tools

Retrievers

Agents
```

---

# The LangChain Mental Model

Think:

```text
LEGO Blocks
```

You combine components to build applications.

---

# Core Components

```text
Model

Prompt

Parser

Retriever

Tool

Agent
```

---

# Typical Flow

```text
User Question

↓

Prompt

↓

LLM

↓

Parser

↓

Response
```

---

# Models

Models generate output.

Example:

```python
from langchain_openai import AzureChatOpenAI
```

---

```python
llm = AzureChatOpenAI(
    temperature=0
)
```

---

# Invoke Model

```python
response = llm.invoke(
    "What is malaria?"
)
```

---

# Prompt Templates

Hardcoding prompts is bad.

Instead:

```python
from langchain_core.prompts import ChatPromptTemplate
```

---

```python
prompt = ChatPromptTemplate.from_template(
    """
    Answer the following question:

    {question}
    """
)
```

---

# Invoke Prompt

```python
prompt.invoke(
    {
        "question": "What is malaria?"
    }
)
```

---

# Why Prompt Templates?

Benefits:

```text
Reusable

Parameterized

Easier Maintenance
```

---

# Output Parsers

Without parser:

```text
Raw Text
```

---

With parser:

```text
Structured Data
```

---

Example

```python
from pydantic import BaseModel
```

---

```python
class Answer(BaseModel):

    answer: str

    confidence: float
```

---

Agent returns:

```json
{
  "answer": "...",
  "confidence": 0.91
}
```

---

# Chains

Old LangChain concept.

Think:

```text
Step A

↓

Step B

↓

Step C
```

---

Example

```text
Question

↓

Prompt

↓

LLM

↓

Output
```

---

Pseudo Code

```python
chain = (
    prompt
    | llm
    | parser
)
```

---

# LCEL

Very important modern LangChain topic.

LCEL:

```text
LangChain Expression Language
```

---

# LCEL Mental Model

Think UNIX pipes.

```bash
command1 | command2 | command3
```

Equivalent idea:

```python
prompt | llm | parser
```

---

# Example

```python
chain = prompt | llm
```

---

Invoke

```python
result = chain.invoke(
    {
        "question":
        "What is malaria?"
    }
)
```

---

# Why LCEL?

Benefits:

```text
Less Boilerplate

Easy Composition

Easy Testing

Easy Reuse
```

---

# Tools

One of the most important concepts.

---

# What Is A Tool?

A tool is a function an LLM can call.

---

Example

```python
from langchain_core.tools import tool
```

---

```python
@tool
def get_weather(
    city: str
):
    return f"Weather for {city}"
```

---

# Why Tools?

LLMs do not know:

```text
Current Weather

SQL Results

SharePoint Content

ServiceNow Tickets
```

Tools provide access.

---

# Tool Mental Model

```text
LLM Brain

+

Tool Hands
```

---

# Multiple Tools

```python
tools = [
    get_weather,
    search_documents,
    sql_tool
]
```

---

# Retrievers

Retrievers are special components.

Purpose:

```text
Find Relevant Documents
```

---

Pseudo Flow

```text
Question

↓

Retriever

↓

Documents
```

---

# Example

```python
docs = retriever.invoke(
    "What is malaria?"
)
```

---

# RAG Using LangChain

Flow:

```text
Question

↓

Retriever

↓

Context

↓

Prompt

↓

LLM

↓

Answer
```

---

Pseudo Code

```python
docs = retriever.invoke(
    question
)

prompt = f"""

Question:
{question}

Context:
{docs}

"""
```

---

# Agent

One of the most important topics.

---

# What Is An Agent?

Traditional:

```text
Question

↓

Prompt

↓

LLM

↓

Answer
```

---

Agent:

```text
Question

↓

Reason

↓

Choose Tool

↓

Call Tool

↓

Observe

↓

Answer
```

---

# Agent Mental Model

Think:

```text
Employee
```

instead of:

```text
Calculator
```

---

# Example

User:

```text
How many grants exist?
```

---

Agent Decides:

```text
Need SQL Tool
```

---

Calls:

```python
sql_tool()
```

---

Generates Answer.

---

# Tool Calling Flow

```text
Question

↓

LLM

↓

Tool Decision

↓

Tool Execution

↓

Result

↓

Final Answer
```

---

# ReAct Pattern

Classic agent pattern.

```text
Thought

↓

Action

↓

Observation

↓

Thought

↓

Action

↓

Observation
```

---

# LangChain Agent Example

Pseudo Code

```python
agent = create_agent(
    llm,
    tools
)
```

---

```python
agent.invoke(
    {
        "input":
        question
    }
)
```

---

# Memory

Older topic.

Less common now.

---

Stores:

```text
Previous Messages

User Context

Conversation History
```

---

# Modern Recommendation

For long-running agents:

```text
LangGraph State
```

instead of classic memory.

---

# LangChain vs LangGraph

Very common interview question.

---

# LangChain

Provides:

```text
Prompts

Chains

Tools

Retrievers

Models

Output Parsers
```

---

# LangGraph

Provides:

```text
State

Nodes

Edges

Reducers

Checkpoints

Workflow Control
```

---

# Mental Model

```text
LangChain
      ↓
Components

LangGraph
      ↓
Orchestration
```

---

# Example

LangChain:

```python
prompt
|
llm
|
parser
```

---

LangGraph:

```text
Node

↓

Node

↓

Conditional Edge

↓

Node
```

---

# Production Architecture

KM 2.0 Example:

```text
FastAPI

↓

LangGraph

↓

LangChain Components

├── Azure OpenAI

├── Azure AI Search

├── Tools

└── Output Parsers

↓

Response
```

---

# KM 2.0 RAG Example

```python
docs = retriever.invoke(
    question
)

prompt = prompt_template.invoke(
    {
        "question": question,
        "context": docs
    }
)

response = llm.invoke(prompt)
```

---

# KM 2.0 Tool Example

```python
@tool
async def search_policies(
    query: str
):
    ...
```

---

```python
@tool
async def query_sql(
    question: str
):
    ...
```

---

```python
tools = [
    search_policies,
    query_sql
]
```

---

# LCEL Production Example

```python
chain = (
    prompt
    | llm
    | parser
)
```

---

```python
result = chain.invoke(
    {
        "question":
        question
    }
)
```

---

# Common Interview Questions

---

## What Is LangChain?

Answer:

> LangChain is a framework that provides reusable components for building LLM applications, including prompts, models, chains, retrievers, tools, output parsers, and agents.

---

## What Is LCEL?

Answer:

> LCEL (LangChain Expression Language) is a composition framework that allows LangChain components to be connected using pipe operators, creating modular and reusable workflows.

---

## What Is A Chain?

Answer:

> A Chain is a sequence of components where the output of one step becomes the input of the next.

---

## What Is A Tool?

Answer:

> A Tool is a callable function that an LLM or agent can invoke to access external capabilities such as APIs, databases, retrieval systems, or business services.

---

## What Is A Retriever?

Answer:

> A Retriever fetches relevant documents from a knowledge source and is commonly used in RAG pipelines.

---

## What Is An Agent?

Answer:

> An Agent is an LLM-powered system that can reason, choose tools, execute actions, observe results, and continue iterating until a goal is achieved.

---

## LangChain vs LangGraph?

Answer:

> LangChain provides reusable building blocks, while LangGraph provides stateful workflow orchestration. In production systems, LangGraph often orchestrates LangChain components.

---

## When Would You Use LangGraph Instead Of LangChain?

Answer:

> Use LangGraph when you need state management, loops, conditional routing, checkpoints, human approvals, or multi-agent workflows.

---

## What Is LCEL Good For?

Answer:

> LCEL simplifies composing prompts, models, retrievers, and parsers into reusable pipelines with minimal boilerplate.

---

# Common Mistakes

❌ Building everything as an agent

❌ Using agents when a chain is enough

❌ No output parsing

❌ Massive prompts

❌ No retrieval grounding

❌ No evaluation

❌ No observability

---

# Production Best Practices

✅ Use LCEL

✅ Structured Outputs

✅ Use Retrievers for Knowledge

✅ Use Agents Only When Needed

✅ Add Tracing

✅ Add Evaluation

✅ Add Retries

✅ Add Guardrails

✅ Use LangGraph For Complex Workflows

---

# Ultimate Mental Model

```text
LLM
 ↓
LangChain
 ↓
Prompts
Tools
Retrievers
Parsers

↓

LangGraph

↓

Workflow

↓

Production Agent
```

---

# 60 Second Interview Answer

"LangChain is a framework that provides the core building blocks for LLM applications, including prompts, models, retrievers, chains, tools, and agents. LCEL allows these components to be composed through simple pipelines. LangGraph builds on top of these concepts by adding state management, workflow orchestration, routing, loops, checkpoints, and multi-agent coordination. In production systems such as KM 2.0, I would typically use LangChain components inside LangGraph workflows."

ConversationBufferMemory
    Entire Chat

BufferWindowMemory
    Last N Messages

TokenBufferMemory
    Last N Tokens

SummaryMemory
    Conversation Summary

SummaryBufferMemory
    Recent Chat + Summary

EntityMemory
    Important Entities

KGMemory
    Knowledge Graph

VectorStoreMemory
    RAG-style Memory

Modern LangGraph
    State + Checkpoints
