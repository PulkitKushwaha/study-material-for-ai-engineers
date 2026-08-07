# 03 - LangGraph Fundamentals for Agentic AI

> The most important framework for building production-grade AI agents.
>
> Goal:
>
> - Understand why LangGraph exists
> - State, Nodes, Edges
> - Conditional Routing
> - Reducers
> - Checkpointing
> - Human-in-the-Loop
> - Multi-Agent Systems
> - Production LangGraph Architecture
> - LangGraph Interview Questions

---

# Table of Contents

1. Why LangGraph Exists
2. LangChain vs LangGraph
3. LangGraph Mental Model
4. Core Components
5. State
6. Nodes
7. Edges
8. Conditional Routing
9. Reducers
10. Checkpoints
11. Human-in-the-Loop
12. Multi-Agent Systems
13. Pseudo Code Examples
14. Production Code Examples
15. Architecture Patterns
16. Interview Questions
17. Common Mistakes
18. Production Best Practices

---

# Why LangGraph Exists

Imagine a simple chatbot:

```text
User Question
      ↓
LLM
      ↓
Answer
```

This works.

But what if we need:

```text
Classify Intent

↓

Retrieve Documents

↓

Call SQL

↓

Call Tool

↓

Request Human Approval

↓

Generate Answer
```

A linear chain becomes difficult to manage.

LangGraph solves this by modelling workflows as graphs made of:

- State
- Nodes
- Edges

where state flows through the graph. 【2-49075c】【3-690748】

---

# LangChain vs LangGraph

## LangChain

Mental Model:

```text
Step 1
  ↓
Step 2
  ↓
Step 3
```

Linear.

---

## LangGraph

Mental Model:

```text
          Search
         ↗
User → Router
         ↘
          SQL

            ↓

       Final Answer
```

Graph-based.

Supports branching, loops, parallel execution, checkpoints, and stateful workflows. 【2-49075c】【4-ed78ba】

---

# Ultimate Mental Model

Imagine a company.

---

## State

Shared notebook.

Contains:

```text
Question
Retrieved Docs
SQL Results
Final Answer
```

Everybody can read it.

---

## Nodes

Employees.

They do work.

Examples:

```text
Classifier Node

Retriever Node

SQL Node

Answer Node
```

---

## Edges

Workflow rules.

Examples:

```text
If finance question
    → SQL Agent

If policy question
    → RAG Agent
```

---

## Graph

Entire business workflow.

---

# Core Components

LangGraph revolves around:

```text
State
Nodes
Edges
Reducers
Checkpointers
```

【2-49075c】【3-690748】

---

# State

The most important concept.

State is the shared snapshot of your application. 【2-49075c】【1-11176e】

---

## Example

```python
from typing import TypedDict

class GraphState(TypedDict):

    question: str

    documents: list

    answer: str
```

---

Think:

```text
Shared Notebook
```

Every node can:

```text
Read State
Update State
Pass State Forward
```

---

# Nodes

Nodes perform work.

A node receives state and returns updates. 【2-49075c】【3-690748】

---

## Example

```python
def retrieve_documents(
    state: GraphState
):

    docs = search(
        state["question"]
    )

    return {
        "documents": docs
    }
```

---

Mental Model:

```text
Employee

Reads Notebook

Adds Information

Returns Notebook
```

---

# Edges

Edges determine what node executes next. 【2-49075c】

---

## Simple Edge

```text
START
  ↓
Classifier
  ↓
Retriever
  ↓
Answer
  ↓
END
```

---

## Code

```python
builder.add_edge(
    "retriever",
    "answer"
)
```

---

# Conditional Routing

One of the biggest reasons LangGraph is powerful.

---

## Problem

Not every question needs the same flow.

Example:

```text
How many grants exist?

Need SQL.
```

vs

```text
What is the malaria strategy?

Need RAG.
```

---

## Pseudo Code

```text
Question

↓

Classify

↓

IF count question

    SQL Agent

ELSE

    RAG Agent
```

---

## Code

```python
def route(state):

    if state["intent"] == "sql":
        return "sql_agent"

    return "rag_agent"
```

---

# Reducers

Very important interview topic.

Reducers define how state updates get combined when multiple nodes update the same field. 【2-49075c】【3-690748】

---

## Problem

Suppose:

```text
Retriever A

Retriever B

Retriever C
```

all return documents.

How do we combine them?

---

Reducer:

```python
documents_a
+
documents_b
+
documents_c
```

---

Mental Model:

```text
Merge Results
```

---

# Checkpoints

One of LangGraph's killer features.

Checkpoints store a snapshot of graph state. 【1-11176e】【5-54707a】

---

## Why Needed?

Imagine:

```text
35-Step Workflow
```

Step 34 fails.

Without checkpoints:

```text
Restart Everything
```

---

With checkpoints:

```text
Resume From Last Snapshot
```

---

## Enterprise Benefits

```text
Failure Recovery

Long Running Agents

Human Approval Flows

Auditing

Debugging
```

---

# Human-in-the-Loop

A major enterprise use case.

---

Pseudo Code:

```text
Generate Remediation Plan

↓

Pause

↓

Human Review

↓

Approve?

YES → Continue

NO → Revise
```

---

Used heavily in:

```text
Risk Systems

Compliance

Finance

Security
```

---

# Multi-Agent Systems

One of the hottest interview topics.

Internal enterprise presentations also highlight supervision/routing architectures for multi-agent systems. 【1-11176e】

---

# Single Agent

```text
User
 ↓
Agent
 ↓
Tools
```

---

# Multi-Agent

```text
User
  ↓

Supervisor

 ├─ Research Agent

 ├─ SQL Agent

 ├─ Finance Agent

 └─ Reporting Agent
```

---

Benefits:

```text
Less Tool Overload

Better Context Management

Specialized Expertise
```

【1-11176e】

---

# Production Pseudo Code

```text
Receive Question

↓

Classify Intent

↓

Retrieve Documents

↓

Call Database

↓

Aggregate Results

↓

Generate Answer

↓

Store Checkpoint

↓

Return Response
```

---

# Minimal Working Graph

```python
from typing import TypedDict
from langgraph.graph import (
    StateGraph,
    START,
    END
)

class State(TypedDict):

    question: str

    answer: str


def generate_answer(state):

    return {
        "answer":
        f"Answering {state['question']}"
    }


builder = StateGraph(State)

builder.add_node(
    "answer",
    generate_answer
)

builder.add_edge(
    START,
    "answer"
)

builder.add_edge(
    "answer",
    END
)

graph = builder.compile()

result = graph.invoke(
    {
        "question": "Hello"
    }
)
```

StateGraph, nodes, edges and graph compilation are core LangGraph concepts. 【2-49075c】【3-690748】

---

# Enterprise RAG Architecture

```text
User

 ↓

Intent Router

 ↓

Retriever Node

 ↓

Azure AI Search

 ↓

Reranker

 ↓

Answer Node

 ↓

GPT-4o

 ↓

Response
```

---

# Multi-Agent Architecture

```text
User

 ↓

Supervisor

 ├── Grant Agent

 ├── Finance Agent

 ├── Procurement Agent

 └── Reporting Agent

            ↓

      Aggregation Node

            ↓

      Final Response
```

---

# Interview Questions

---

## What is LangGraph?

**Answer**

LangGraph is a framework for building stateful agent workflows using graphs composed of state, nodes, and edges. 【2-49075c】【3-690748】

---

## What is State?

**Answer**

State is the shared snapshot of the application that nodes read and update throughout execution. 【2-49075c】【1-11176e】

---

## What is a Node?

**Answer**

A node is a function that performs work and returns state updates. 【2-49075c】

---

## What is an Edge?

**Answer**

An edge controls the transition from one node to another. 【2-49075c】

---

# Why Are Reducers Needed?

Reducers define how updates to the same state field should be combined.

This becomes important when:

```text
Multiple Nodes
        ↓
Update The Same State Field
```

Without reducers:

```text
Last Update Wins
```

which can accidentally overwrite data.

---

# Example Without Reducers

Assume state:

```python
{
    "documents": []
}
```

---

Retriever A returns:

```python
{
    "documents": ["Doc1"]
}
```

Retriever B returns:

```python
{
    "documents": ["Doc2"]
}
```

---

Final State:

```python
{
    "documents": ["Doc2"]
}
```

Doc1 is lost.

---

# Example With Reducers

Reducer:

```python
operator.add
```

---

State Updates:

```python
["Doc1"]
+
["Doc2"]
```

---

Final State:

```python
["Doc1", "Doc2"]
```

---

# Production Example

```python
from typing import Annotated
from typing import TypedDict
from operator import add


class State(TypedDict):

    documents: Annotated[
        list,
        add
    ]
```

Now multiple nodes can safely contribute documents.

---

# Mental Model

Think:

```text
Node A
   ↓

Node B

   ↓

Merge Results

   ↓

Reducer
```

---

# Checkpointing

One of the biggest reasons enterprises love LangGraph.

A checkpoint is a snapshot of graph state.

LangGraph supports checkpointing as a first-class concept for state persistence and workflow recovery. 【1-bf6db0】【2-1d08b5】

---

# Problem Without Checkpoints

Imagine:

```text
Step 1

↓

Step 2

↓

Step 3

↓

Step 4

↓

Step 5
```

Step 5 fails.

---

Without checkpoints:

```text
Start Again From Step 1
```

---

# With Checkpoints

```text
Step 1 ✅

Step 2 ✅

Step 3 ✅
    ↑

Checkpoint Saved

↓

Step 4 ✅

↓

Step 5 ❌
```

Resume from:

```text
Step 3
```

instead of starting over.

---

# Why Enterprises Need Checkpoints

Imagine:

```text
Document Review

20 Minutes
```

or

```text
Large Investigation Workflow

45 Minutes
```

or

```text
Human Approval Process

Several Hours
```

Restarting is unacceptable.

Checkpointing solves this.

---

# Benefits

✅ Recovery After Failure

✅ Long Running Agents

✅ Human Approval Workflows

✅ Auditing

✅ Debugging

✅ State Persistence

---

# Human In The Loop (HITL)

A huge Enterprise AI topic.

---

# What Is HITL?

Sometimes an agent should not make the final decision.

Example:

```text
Generate Risk Assessment

↓

Human Review

↓

Approve?

YES
 ↓
Continue

NO
 ↓
Revise
```

---

# Why HITL Matters

Industries:

```text
Healthcare

Finance

Audit

Compliance

Cybersecurity
```

often require approval.

---

# LangGraph Pattern

```text
Node A

↓

Node B

↓

Approval Node

↓

Human Decision

↓

Continue
```

---

# Multi-Agent Systems

Very commonly asked.

---

# Single Agent Architecture

```text
User

↓

Agent

↓

Tools

↓

Answer
```

Simple.

---

# Problem

As tools increase:

```text
Search

SQL

Email

Calendar

Jira

SAP

CRM
```

Agent becomes overloaded.

---

# Multi-Agent Architecture

```text
User

↓

Supervisor Agent

 ├── Research Agent

 ├── SQL Agent

 ├── Reporting Agent

 └── Email Agent

↓

Final Response
```

This specialization is one of the common reasons for using multi-agent patterns. 【1-bf6db0】

---

# Why Multiple Agents?

Benefits:

```text
Reduced Tool Confusion

Better Context Management

Smaller Prompts

Specialized Expertise

Easier Testing

Better Scalability
```

---

# LangGraph Workflow Example

## Business Scenario

Question:

```text
How many malaria grants are active and summarize key risks?
```

---

Pseudo Flow:

```text
User Question

↓

Router

↓

SQL Agent
    finds grant count

↓

RAG Agent
    retrieves risk findings

↓

Aggregator

↓

Final Response
```

---

# Pseudo Code Example

```text
Receive Question

↓

Classify Intent

↓

Retrieve Documents

↓

Run SQL Query

↓

Combine Results

↓

Generate Answer

↓

Save Checkpoint

↓

Return Response
```

---

# Production Code Example

## Step 1: Define State

```python
from typing import TypedDict


class State(TypedDict):

    question: str

    documents: list

    answer: str
```

---

## Step 2: Create Nodes

```python
def retrieve_documents(state):

    docs = search(
        state["question"]
    )

    return {
        "documents": docs
    }
```

---

```python
def generate_answer(state):

    answer = llm.invoke(
        state["question"]
    )

    return {
        "answer": answer
    }
```

---

## Step 3: Build Graph

```python
from langgraph.graph import (
    StateGraph,
    START,
    END
)

builder = StateGraph(State)

builder.add_node(
    "retriever",
    retrieve_documents
)

builder.add_node(
    "answer",
    generate_answer
)
```

---

## Step 4: Add Edges

```python
builder.add_edge(
    START,
    "retriever"
)

builder.add_edge(
    "retriever",
    "answer"
)

builder.add_edge(
    "answer",
    END
)
```

---

## Step 5: Compile

```python
graph = builder.compile()
```

---

## Step 6: Execute

```python
result = graph.invoke(
    {
        "question":
        "What is malaria?"
    }
)
```

---

# Architecture Patterns

## Pattern 1: Router + Specialists

```text
User

↓

Router

├── SQL Agent

├── Search Agent

└── Documentation Agent

↓

Response
```

---

## Pattern 2: Supervisor Pattern

```text
Supervisor

↓

Delegates Tasks

↓

Workers Execute

↓

Supervisor Combines
```

---

## Pattern 3: Research + Writer

```text
User

↓

Research Agent

↓

Writer Agent

↓

Final Answer
```

---

# Common Interview Questions

## What Is LangGraph?

Answer:

> LangGraph is a framework for building stateful agent workflows using nodes, edges, and shared state.

---

## Why Not Just Use LangChain?

Answer:

> LangChain is excellent for chains and components, while LangGraph is better suited for stateful workflows, branching, loops, checkpoints, and multi-agent orchestration.

---

## What Is State?

Answer:

> State is the shared data structure passed between nodes throughout graph execution.

---

## What Is A Node?

Answer:

> A node is a function that performs work and returns state updates.

---

## What Is An Edge?

Answer:

> An edge controls workflow transitions between nodes.

---

## What Is A Reducer?

Answer:

> A reducer defines how updates to the same state field are merged when multiple nodes modify that field.

---

## What Is Checkpointing?

Answer:

> Checkpointing stores graph state snapshots so workflows can be resumed, audited, or debugged.

---

## Why Are Checkpoints Important?

Answer:

> They enable failure recovery, persistence, long-running workflows
