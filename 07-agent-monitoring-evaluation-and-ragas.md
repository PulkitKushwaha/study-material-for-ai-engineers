# 07 - Agent Monitoring, Evaluation & RAGAS

> A practical guide to monitoring GenAI systems, evaluating RAG pipelines, measuring agent performance, and using RAGAS.
>
> Goal:
>
> - Understand Agent Monitoring
> - Understand Agent Evaluation
> - Understand RAG Evaluation
> - Understand RAGAS
> - Understand Agent Observability
> - Understand Enterprise Monitoring
> - Master Interview Questions

---

# Table of Contents

1. Why Monitoring Matters
2. Monitoring vs Evaluation
3. Agent Observability
4. Agent Monitoring Layers
5. Agent Metrics
6. RAG Metrics
7. What Is RAGAS?
8. Faithfulness
9. Answer Relevancy
10. Context Precision
11. Context Recall
12. Agent Evaluation Metrics
13. LangSmith and Tracing
14. Production Monitoring Dashboard
15. Evaluation Datasets
16. Common Interview Questions
17. Best Practices
18. Mental Models

---

# Why Monitoring Matters

Traditional software:

```text
Input
 ↓
Processing
 ↓
Output
```

If output is wrong:

```text
Fix Bug
```

Simple.

---

AI Systems:

```text
Input
 ↓
Retriever
 ↓
LLM
 ↓
Tool Calls
 ↓
Reasoning
 ↓
Output
```

Many more failure points.

---

Possible Failures

```text
Wrong Retrieval

Wrong Tool

Hallucination

Wrong Reasoning

Bad Routing

Infinite Loop

High Cost

High Latency
```

Monitoring becomes critical.

---

# Monitoring vs Evaluation

One of the most important interview concepts.

---

# Monitoring

Measures:

```text
What happened in production?
```

Examples:

```text
Latency

Failures

Cost

Token Usage
```

---

# Evaluation

Measures:

```text
Was the answer any good?
```

Examples:

```text
Faithfulness

Relevance

Correctness

Tool Accuracy
```

---

# Mental Model

```text
Monitoring
     ↓
Health

Evaluation
     ↓
Quality
```

---

# Agent Observability

Observability means:

```text
Can we understand
what happened inside
the agent?
```

---

Without Observability

```text
User says:

Wrong answer.
```

No clue why.

---

With Observability

```text
Question

↓

Retriever

↓

Tool Call

↓

LLM

↓

Answer
```

You can inspect every step.

---

# Agent Monitoring Layers

Think of a pyramid.

```text
Business Metrics
        ↑

Quality Metrics
        ↑

Agent Metrics
        ↑

Infrastructure Metrics
```

---

# Layer 1: Infrastructure Metrics

Traditional application metrics.

Examples:

```text
CPU Usage

Memory Usage

Network Latency

API Errors

Request Count
```

Tools:

```text
Azure Monitor

Application Insights

Prometheus

Datadog
```

---

# Layer 2: Agent Metrics

Measures agent behavior.

Examples:

```text
Latency

Token Usage

Cost

Steps Executed

Tool Calls

Retries

Loop Count
```

---

Example

Question:

```text
How many malaria grants exist?
```

Expected:

```text
1 SQL query
```

Actual:

```text
8 Tool Calls
```

Inefficient agent.

---

# Layer 3: Quality Metrics

Measures response quality.

Examples:

```text
Faithfulness

Correctness

Grounding

Relevance
```

---

# Layer 4: Business Metrics

The metrics leadership usually cares about.

Examples:

```text
Ticket Deflection

Resolution Rate

User Satisfaction

Escalation Rate

Agent Adoption
```

---

# Example

Questions Received:

```text
1000
```

Resolved Successfully:

```text
850
```

---

Resolution Rate

```text
85%
```

---

# Agent Evaluation

Agent evaluation focuses on:

```text
Did the agent accomplish
its goal correctly?
```

---

Evaluate:

```text
Planning

Routing

Tool Usage

Final Outcome
```

---

# Evaluation Levels

```text
Component Level

RAG Level

Agent Level

Business Level
```

---

# Component Evaluation

Evaluate:

```text
Retriever

Reranker

LLM

Tool
```

individually.

---

# RAG Evaluation

Evaluate:

```text
Retrieval Quality

Answer Quality

Grounding Quality
```

---

# Agent Evaluation

Evaluate:

```text
Task Completion

Tool Selection

Goal Success
```

---

# Business Evaluation

Evaluate:

```text
Customer Value

User Success

Cost Savings
```

---

# What Is RAGAS?

RAGAS stands for:

```text
Retrieval-Augmented Generation
Assessment Suite
```

RAGAS is an evaluation framework specifically designed for RAG and agentic systems. It provides metrics for retrieval quality, answer quality, grounding, and agent/tool-use workflows. 【1-f31450】【2-c8de4f】

---

# Why Not BLEU or ROUGE?

Traditional NLP metrics:

```text
BLEU

ROUGE
```

look at text similarity.

Problem:

```text
Correct Answer

Different Wording

Bad Score
```

---

RAG systems need:

```text
Grounding

Context Quality

Faithfulness

Retrieval Quality
```

which RAGAS measures directly. 【2-c8de4f】【3-9d1477】

---

# The Four Most Important RAGAS Metrics

Remember these.

---

# 1. Faithfulness

The most important metric.

Question:

```text
Is the answer supported by
the retrieved documents?
```

Faithfulness is a core RAGAS metric and is commonly used to evaluate grounding and detect hallucinations. 【4-88b177】【5-46a115】

---

Example

Retrieved:

```text
Malaria is spread by mosquitoes.
```

Answer:

```text
Malaria is spread by mosquitoes.
```

Faithful ✅

---

Answer:

```text
Malaria spreads through drinking water.
```

Not Faithful ❌

Hallucination.

---

# Mental Model

```text
Faithfulness
     ↓
Hallucination Check
```

---

# 2. Answer Relevancy

Question:

```text
Does the answer address
the user's question?
```

Answer/Response Relevancy is a core RAGAS metric. 【4-88b177】【1-f31450】

---

Question:

```text
How is malaria transmitted?
```

Answer:

```text
The Global Fund funds health programs.
```

True.

But irrelevant.

---

Low Relevancy.

---

# Mental Model

```text
Relevancy

=

Did We Answer
The Question?
```

---

# 3. Context Precision

Question:

```text
Were the retrieved chunks
actually relevant?
```

Context Precision is one of the primary retrieval metrics in RAGAS. 【4-88b177】【1-f31450】

---

Question:

```text
Malaria Treatment
```

Retrieved:

```text
Malaria Guideline

Malaria Drug Information

Malaria SOP
```

High Precision.

---

Retrieved:

```text
Football Article

Cooking Article

Malaria Guideline
```

Low Precision.

---

# Mental Model

```text
Precision

=

Signal / Noise
```

---

# 4. Context Recall

Question:

```text
Did retrieval find enough
of the required information?
```

Context Recall is another core retrieval metric provided by RAGAS. 【4-88b177】【1-f31450】

---

Needed:

```text
Step 1

Step 2

Step 3

Step 4
```

Retrieved:

```text
Only Step 1
```

Low Recall.

---

Retrieved:

```text
All Steps
```

High Recall.

---

# Mental Model

```text
Recall

=

Coverage
```

---

# RAGAS Cheat Sheet

```text
Faithfulness
    ↓
Grounded?

Answer Relevancy
    ↓
Question Answered?

Context Precision
    ↓
Relevant Chunks?

Context Recall
    ↓
Missing Chunks?
```

---

# Agent Evaluation Metrics

Agent-specific evaluation often focuses on whether the agent selected the right actions and achieved the user's goal. RAGAS also includes metrics for agent/tool-use scenarios such as tool-call accuracy and agent goal accuracy. 【1-f31450】

---

# Tool Call Accuracy

Question:

```text
Did the agent call
the correct tool?
```

---

Example

User:

```text
Create ServiceNow Ticket
```

Agent:

```text
Calls Jira Tool
```

Wrong.

---

Tool Accuracy:

```text
0
```

---

# Goal Accuracy

Question:

```text
Did the agent
complete the task?
```

---

Example

User:

```text
Create Incident
```

Result:

```text
Incident Created
```

Success ✅

---

# Task Completion Rate

Example:

```text
100 Requests

90 Successful
```

Metric:

```text
90%
```

---

# User Satisfaction

Example:

```text
Helpful?

Yes / No
```

Simple.

But powerful.

---

# LangSmith and Tracing

One of the most common observability tools.

Mental Model:

```text
Application Insights

for Agents
```

---

Trace Example

```text
Question

↓

Retriever

↓

Tool

↓

LLM

↓

Answer
```

---

What Can We Debug?

```text
Wrong Retrieval

Wrong Tool

Wrong Prompt

Hallucination
```

---

# Production Monitoring Dashboard

For KM 2.0 style systems, I would monitor:

---

## Infrastructure

```text
CPU

Memory

Error Rate

Response Time
```

---

## Retrieval

```text
Precision

Recall

Hit Rate
```

---

## Generation

```text
Faithfulness

Relevancy

Hallucination Rate
```

---

## Agent

```text
Tool Accuracy

Goal Accuracy

Task Completion
```

---

## Business

```text
User Satisfaction

Ticket Deflection

Resolution Rate

Escalation Rate
```

---

# Gold Evaluation Dataset

One of the best practices.

Create:

```text
Question

Reference Answer

Expected Documents
```

---

Example

```text
Question:
How do I create a grant?

Expected:
Step 1...
Step 2...
Step 3...

Expected Docs:
Grant SOP
Grant Policy
```

---

Run:

```text
100 Questions

↓

Evaluate Using RAGAS
```

---

# Interview Questions

---

## What Is Monitoring?

Answer:

> Monitoring measures how a system behaves in production, including latency, failures, costs, token usage, and execution patterns.

---

## What Is Evaluation?

Answer:

> Evaluation measures quality, correctness, grounding, retrieval effectiveness, and task success.

---

## Monitoring vs Evaluation?

Answer:

> Monitoring focuses on operational health, while evaluation focuses on answer quality and business effectiveness.

---

## What Is Observability?

Answer:

> Observability is the ability to understand how an agent reached its result by inspecting traces, tool calls, retrieval steps, and reasoning paths.

---

## What Is RAGAS?

Answer:

> RAGAS is an evaluation framework designed specifically for Retrieval-Augmented Generation and agentic systems. It provides metrics for retrieval quality, grounding, answer quality, and tool-usage evaluation. 【1-f31450】【2-c8de4f】

---

## What Is Faithfulness?

Answer:

> Faithfulness measures whether an answer is supported by the retrieved context and is the primary metric used to identify hallucinations. 【4-88b177】【5-46a115】

---

## What Is Context Precision?

Answer:

> Context Precision measures the relevance of retrieved chunks relative to the user's query. 【4-88b177】【1-f31450】

---

## What Is Context Recall?

Answer:

> Context Recall measures whether retrieval found enough information to answer the question completely. 【4-88b177】【1-f31450】

---

## What Is Answer Relevancy?

Answer:

> Answer Relevancy measures whether the generated answer actually addresses the user's question. 【4-88b177】【1-f31450】

---

## How Would You Evaluate A RAG System?

Answer:

> I would evaluate retrieval quality using context precision and recall, answer quality using faithfulness and relevancy, and business success through user satisfaction and resolution rate.

---

## How Would You Evaluate An Agent?

Answer:

> I would measure tool-call accuracy, goal completion rate, task success rate, user satisfaction, latency, and business outcomes.

---

## How Do You Detect Hallucinations?

Answer:

> Faithfulness evaluation compares generated answers against retrieved context and identifies unsupported or invented claims. 【4-88b177】【5-46a115】

---

# Common Mistakes

❌ Measuring only latency

❌ Ignoring retrieval quality

❌ No ground-truth dataset

❌ No tracing

❌ Evaluating only final answers

❌ Ignoring business metrics

---

# Production Best Practices

✅ Create Gold Evaluation Datasets

✅ Track Faithfulness

✅ Track Retrieval Metrics

✅ Enable Tracing

✅ Measure Tool Accuracy

✅ Measure Business Outcomes

✅ Continuously Evaluate

✅ Use Human Feedback

---

# Ultimate Mental Model

```text
Infrastructure
     ↓
Healthy?

Agent
     ↓
Efficient?

Retriever
     ↓
Relevant?

LLM
     ↓
Faithful?

Business
     ↓
Useful?
```

---

# 60-Second Interview Answer

"To evaluate an AI system, I separate monitoring from evaluation. Monitoring focuses on latency, token usage, failures, and execution traces. Evaluation focuses on answer quality and business outcomes. For RAG systems, I use metrics like Faithfulness, Context Precision, Context Recall, and Answer Relevancy using frameworks such as RAGAS. For agents, I additionally measure tool-call accuracy, task completion rate, goal success rate, and user satisfaction. Finally, I track business metrics such as resolution rate, escalation rate, and ticket deflection."
