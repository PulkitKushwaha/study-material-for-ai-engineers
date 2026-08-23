# 09 - Agent and RAG Evaluation Metrics

> A practical guide to calculating, interpreting, and operationalizing evaluation metrics for RAG pipelines and AI agents.
>
> This note focuses on the difference between retrieval quality, answer quality, agent behavior, operational health, and business outcomes.

---

## Table of Contents

1. Why Evaluation Matters
2. Monitoring vs Evaluation vs Observability
3. Evaluation Workflow
4. Gold Evaluation Dataset
5. RAG Evaluation Metrics
6. Agent Evaluation Metrics
7. Operational and Efficiency Metrics
8. Deterministic Metrics vs LLM-as-a-Judge
9. Evaluating Scores and Setting Thresholds
10. End-to-End KM 2.0 Example
11. Code Examples
12. Interview Questions and Answers
13. Production Best Practices
14. Quick Revision Sheet
15. References

---

# 1. Why Evaluation Matters

A working demo is not the same as a reliable production system.

An agent can fail at several points:

```text
User Question
    ↓
Intent Routing
    ↓
Retrieval
    ↓
Tool Selection
    ↓
Tool Execution
    ↓
Answer Generation
    ↓
Final Outcome
```

Possible failure modes include:

- Wrong route
- Wrong or unnecessary tool
- Missing knowledge
- Irrelevant retrieved chunks
- Hallucinated claims
- Incomplete answer
- Failure to complete the requested task
- Excessive latency, cost, retries, or loops

Evaluation helps answer:

```text
Did the system retrieve correctly?
Did it generate a grounded answer?
Did the agent make correct decisions?
Did it achieve the user's goal?
Was it efficient and useful?
```

---

# 2. Monitoring vs Evaluation vs Observability

## Monitoring

Monitoring measures the health and behavior of the running system.

Examples:

- Latency
- Error rate
- Request volume
- Token usage
- Cost
- Tool failures
- Retry count

Mental model:

```text
Monitoring = Is the system healthy?
```

## Evaluation

Evaluation measures whether the system's output and behavior are good.

Examples:

- Faithfulness
- Answer relevancy
- Context precision
- Context recall
- Routing accuracy
- Tool-call accuracy
- Agent goal accuracy

Mental model:

```text
Evaluation = Is the system correct and useful?
```

## Observability

Observability is the ability to understand why the system behaved as it did.

An agent trace may contain:

```text
Input
Route Selected
Documents Retrieved
LLM Prompt
Tool Calls
Tool Arguments
Tool Results
State Transitions
Final Answer
```

Mental model:

```text
Observability = Can we explain why it happened?
```

---

# 3. Evaluation Workflow

A production-friendly evaluation lifecycle is:

```text
Create Gold Dataset
    ↓
Run Agent
    ↓
Capture Trace
    ↓
Calculate Per-Case Metrics
    ↓
Aggregate Metrics
    ↓
Segment by Use Case
    ↓
Compare with Baseline and Thresholds
    ↓
Inspect Failed Traces
    ↓
Improve and Re-run
```

Evaluation should happen at two stages:

## Offline Evaluation

Run before deployment against a controlled test dataset.

Use it for:

- Regression testing
- Model comparison
- Prompt comparison
- Retriever tuning
- Tool-routing validation
- Release gates

## Online Evaluation

Run after deployment using production traces and sampled interactions.

Use it for:

- Drift detection
- User feedback analysis
- Latency and cost monitoring
- Failure analysis
- Business KPI tracking

---

# 4. Gold Evaluation Dataset

A gold dataset contains the expected behavior for representative questions.

```python
evaluation_case = {
    "question": "How do I restore SharePoint access?",
    "reference_answer": (
        "Verify the account status, confirm the required role, "
        "and submit the access request through the approved process."
    ),
    "reference_contexts": [
        "SharePoint Access SOP content...",
        "Identity and Access Policy content..."
    ],
    "expected_sources": [
        "SharePoint Access SOP",
        "Identity and Access Policy"
    ],
    "expected_route": "rag",
    "expected_tool_calls": [
        {
            "name": "search_knowledge_base",
            "args": {
                "query": "restore SharePoint access"
            }
        }
    ],
    "expected_outcome": {
        "answer_with_citations": True
    }
}
```

A strong dataset includes:

- Normal questions
- Ambiguous questions
- Multi-turn questions
- Out-of-scope requests
- Missing-document cases
- Conflicting-document cases
- Unauthorized-document cases
- Tool-failure cases
- Prompt-injection cases
- Questions for each route and category

For KM 2.0, segment cases by:

```text
Policy Clarification
Procedural Questions
Document Lookup
Summarization
NL2SQL
Access-Control Scenarios
```

---

# 5. RAG Evaluation Metrics

RAG evaluation has three core layers:

```text
Retrieval Quality
    ↓
Grounding Quality
    ↓
Answer Quality
```

---

## 5.1 Faithfulness

Faithfulness asks:

> Are the claims made in the answer supported by the retrieved context?

Formula:

```text
Faithfulness
=
Supported Answer Claims
───────────────────────
Total Answer Claims
```

RAGAS calculates faithfulness by identifying claims in the response, checking whether each claim can be inferred from retrieved context, and dividing supported claims by total claims.

### Example

Retrieved context:

```text
The VPN issue may be caused by expired credentials.
Users should verify MFA and restart the VPN client.
```

Generated answer:

```text
1. Restart the VPN client.
2. Verify MFA.
3. Reinstall Windows.
4. Check whether credentials have expired.
```

| Claim | Supported? |
|---|---:|
| Restart VPN | Yes |
| Verify MFA | Yes |
| Reinstall Windows | No |
| Check expired credentials | Yes |

```text
Faithfulness = 3 / 4 = 0.75
```

Interpretation:

```text
The answer contains one unsupported claim.
```

---

## 5.2 Context Recall

Context Recall asks:

> Did retrieval find enough information to support the expected answer?

Formula:

```text
Context Recall
=
Reference Claims Supported by Retrieved Context
──────────────────────────────────────────────
Total Claims in Reference Answer
```

### Example

Reference answer requires:

```text
1. Check account status.
2. Verify MFA.
3. Check device compliance.
4. Restart the VPN client.
```

Retrieved context supports:

```text
Verify MFA.
Restart the VPN client.
```

```text
Context Recall = 2 / 4 = 0.50
```

Interpretation:

```text
The retriever missed half of the information needed for a complete answer.
```

---

## 5.3 Context Precision

Context Precision asks:

> Were relevant chunks ranked above irrelevant chunks?

Precision at rank `k`:

```text
Precision@k
=
Relevant Chunks in Top k
────────────────────────
Total Chunks in Top k
```

Context Precision is based on precision values at positions containing relevant chunks.

### Good Ranking

```text
Rank 1: Relevant
Rank 2: Relevant
Rank 3: Irrelevant
Rank 4: Irrelevant
```

```text
Precision@1 = 1 / 1 = 1.00
Precision@2 = 2 / 2 = 1.00
Context Precision = 1.00
```

### Poor Ranking

```text
Rank 1: Irrelevant
Rank 2: Relevant
Rank 3: Irrelevant
Rank 4: Relevant
```

```text
Precision@2 = 1 / 2 = 0.50
Precision@4 = 2 / 4 = 0.50
Context Precision = 0.50
```

Interpretation:

```text
Both runs found the same relevant chunks, but the second run ranked them poorly.
```

---

## 5.4 Answer Relevancy

Answer Relevancy asks:

> Does the answer directly address the user's question?

A common RAGAS approach is:

1. Generate several artificial questions from the answer.
2. Embed the generated questions.
3. Embed the original question.
4. Compute cosine similarities.
5. Average the similarity values.

Formula:

```text
Answer Relevancy
=
1/N × Σ cosine_similarity(
    generated_question_i,
    original_question
)
```

Important:

```text
Relevancy does not prove factual correctness.
A response can be relevant but incorrect.
```

---

## 5.5 Precision vs Recall

```text
Precision:
Did we retrieve too much irrelevant content?

Recall:
Did we miss required content?
```

| Precision | Recall | Interpretation |
|---|---|---|
| High | High | Ideal retrieval |
| High | Low | Clean results, but important evidence is missing |
| Low | High | Required evidence found, but with excessive noise |
| Low | Low | Retrieval pipeline requires major improvement |

---

# 6. Agent Evaluation Metrics

RAG evaluation measures retrieval and generation. Agent evaluation measures decisions, actions, trajectories, and outcomes.

```text
RAG Evaluation
=
Did we retrieve and answer correctly?

Agent Evaluation
=
Did we reason, route, act, and complete the goal correctly?
```

---

## 6.1 Routing Accuracy

Routing Accuracy asks:

> Did the request go to the correct route or specialist?

Per-case score:

```text
1 if actual_route == expected_route
0 otherwise
```

Dataset score:

```text
Routing Accuracy
=
Correct Routes
──────────────
Total Cases
```

### Example

```text
Expected route: SQL
Actual route: RAG
Score: 0
```

Also use a confusion matrix to see which routes are confused.

---

## 6.2 Tool Call Accuracy

Tool Call Accuracy asks:

> Did the agent call the correct tools, with the correct arguments, and optionally in the correct order?

Example expected calls:

```python
expected_tool_calls = [
    {
        "name": "search_sharepoint",
        "args": {"query": "VPN access"}
    },
    {
        "name": "create_servicenow_ticket",
        "args": {"priority": "medium"}
    }
]
```

Strict mode checks:

- Tool names
- Tool arguments
- Sequence

Flexible mode can ignore order when calls are independent or parallel.

---

## 6.3 Tool Precision, Recall, and F1

Definitions:

```text
True Positive:
Expected tool call made with correct arguments

False Positive:
Unexpected or unnecessary tool call

False Negative:
Expected tool call not made
```

Formulas:

```text
Tool Precision = TP / (TP + FP)

Tool Recall = TP / (TP + FN)

Tool F1 = 2 × Precision × Recall
          ──────────────────────
             Precision + Recall
```

### Example

Expected:

```text
search_sharepoint
search_jira
create_ticket
```

Actual:

```text
search_sharepoint
search_jira
search_blob
```

```text
TP = 2
FP = 1
FN = 1

Precision = 2 / 3 = 0.67
Recall    = 2 / 3 = 0.67
F1        = 0.67
```

---

## 6.4 Agent Goal Accuracy

Agent Goal Accuracy asks:

> Did the final state satisfy the user's requested outcome?

It is commonly treated as a binary metric:

```text
1 = Goal achieved
0 = Goal not achieved
```

### Example

User goal:

```text
Create a ServiceNow incident for my unresolved VPN issue.
```

Successful final state:

```python
{
    "ticket_created": True,
    "ticket_id": "INC0012345"
}
```

Score:

```text
1
```

If the agent only explains how to create a ticket but does not create it:

```text
0
```

---

## 6.5 Task Completion Rate

```text
Task Completion Rate
=
Successfully Completed Tasks
────────────────────────────
Total Eligible Tasks
```

Example:

```text
170 successful tasks / 200 eligible tasks = 0.85
```

Completion criteria must be explicit.

For KM 2.0:

```text
Knowledge question:
Answer generated with authorized citations

SQL question:
Validated read-only SQL executed and answer produced

Ticket request:
Valid ServiceNow ticket ID returned
```

---

## 6.6 Planning Quality

Planning Quality asks:

> Did the agent create a sensible sequence of actions?

Example good plan:

```text
Search Audit Reports
    ↓
Extract Findings
    ↓
Validate Evidence
    ↓
Generate Summary
```

Possible evaluation methods:

- Compare with a reference plan
- Check required steps
- Penalize irrelevant steps
- Use an LLM judge with a rubric
- Evaluate final outcome when multiple plans are acceptable

---

## 6.7 Trajectory Evaluation

Trajectory evaluation checks the complete sequence of actions.

```text
State 1 → Tool A → State 2 → Tool B → State 3 → Final Answer
```

Evaluate:

- Correct sequence
- Required steps present
- Unnecessary steps absent
- Safe termination
- No infinite loop
- Correct handoffs between agents

Use strict trajectory evaluation when order matters. Use outcome evaluation when many valid paths exist.

---

## 6.8 Escalation Accuracy

For support or human-in-the-loop agents:

```text
Did the agent escalate when escalation was required?
```

Possible outcomes:

```text
True Positive:
Required escalation occurred

False Positive:
Unnecessary escalation occurred

False Negative:
Required escalation was missed

True Negative:
No escalation was needed and none occurred
```

Track escalation precision, recall, and false-negative rate.

---

## 6.9 Human Override Rate

```text
Human Override Rate
=
Agent Decisions Overridden by Humans
────────────────────────────────────
Total Reviewed Agent Decisions
```

A high override rate often indicates weak recommendations, routing, or safety controls. Interpret it by decision type because high-risk workflows may intentionally require frequent human review.

---

# 7. Operational and Efficiency Metrics

These metrics come directly from traces and telemetry.

---

## 7.1 Latency

```text
Total Latency
=
Final Response Time - Request Start Time
```

Track:

- Total graph latency
- Retrieval latency
- LLM latency
- Tool latency
- Queue latency
- Time spent waiting for human input

Aggregate using:

```text
P50
P95
P99
```

---

## 7.2 Token Usage

Track:

```text
Input Tokens
Output Tokens
Tokens per Node
Tokens per Tool-Augmented Turn
```

---

## 7.3 Cost per Request

```text
Request Cost
=
Input Token Cost
+
Output Token Cost
+
Embedding Cost
+
Search Cost
+
Tool Infrastructure Cost
```

Track cost by:

- Route
- Model
- Tenant
- Use case
- Successful vs failed task

---

## 7.4 Tool-Call Efficiency

Track:

```text
Average tool calls per task
Unnecessary tool-call rate
Retries per tool
Loop count
Duplicate calls
```

A custom efficiency ratio may be:

```text
Reference Tool Calls / Actual Tool Calls
```

Use it carefully because multiple valid tool trajectories may exist.

---

# 8. Deterministic Metrics vs LLM-as-a-Judge

## Deterministic Metrics

Calculated directly from logs or expected values.

Examples:

- Routing accuracy
- Exact tool-call matching
- Latency
- Token usage
- HTTP success
- Ticket created
- Exact match

Advantages:

```text
Repeatable
Cheap
Easy to debug
```

## LLM-as-a-Judge Metrics

Used for semantic judgments.

Examples:

- Faithfulness
- Relevancy
- Correctness
- Goal completion
- Planning quality
- Rubric-based answer quality

Advantages:

```text
Handles paraphrasing
Understands semantic equivalence
Works for open-ended answers
```

Limitations:

```text
Evaluator variability
Token cost
Judge-model bias
Prompt sensitivity
```

Best practices:

- Fix the evaluator model and version
- Use low temperature
- Version evaluator prompts and rubrics
- Validate judge scores against human-labeled samples
- Repeat borderline evaluations when needed
- Keep deterministic checks wherever possible

---

# 9. Evaluating Scores and Setting Thresholds

A metric alone is not useful without interpretation.

Compare scores against:

1. Baseline system
2. Previous release
3. Acceptance threshold
4. Human-reviewed sample
5. Segment-specific requirements

Example:

```text
Faithfulness:       0.93
Answer Relevancy:   0.89
Context Precision:  0.61
Context Recall:     0.84
Routing Accuracy:   0.96
Tool Call F1:       0.88
Goal Accuracy:      0.91
```

Interpretation:

```text
Generation is well grounded.
Answers are relevant.
Routing is strong.
Retrieval precision is weak.
```

Likely engineering investigations:

- Review chunking
- Review metadata filters
- Tune hybrid-search weights
- Tune top-k
- Add or improve reranking
- Remove stale or duplicate chunks

Do not rely only on a global average.

Segment by:

```text
Question Category
Process Area
Route
Document Type
Language
User Group
Tool
Failure Type
```

Example:

```text
Overall Faithfulness: 0.90
Policy Questions:     0.96
Procedural Questions: 0.74
```

The overall average hides the weakness in procedural responses.

---

# 10. End-to-End KM 2.0 Example

Question:

```text
What steps should I follow when my VPN is not connecting?
```

Expected behavior:

```text
Route: RAG
Tools:
  search_sharepoint
  search_jira

Reference claims:
  verify network
  verify MFA
  check device compliance
  restart VPN client
```

Actual execution:

```text
Route: RAG

Tools:
  search_sharepoint
  search_jira
  search_blob

Retrieved context supports:
  verify network
  verify MFA
  restart VPN

Generated answer claims:
  verify network
  verify MFA
  restart VPN
  reinstall Windows
```

Metrics:

```text
Routing Accuracy
= 1

Tool Precision
= 2 correct / 3 actual
= 0.67

Tool Recall
= 2 correct / 2 expected
= 1.00

Tool F1
= 2 × 0.67 × 1.00 / (0.67 + 1.00)
≈ 0.80

Context Recall
= 3 supported reference claims / 4 reference claims
= 0.75

Faithfulness
= 3 supported answer claims / 4 answer claims
= 0.75
```

Diagnosis:

```text
Routing worked.
All required tools were called.
One unnecessary tool was called.
One required fact was not retrieved.
One unsupported troubleshooting step was hallucinated.
```

This is far more actionable than saying:

```text
The answer looked acceptable.
```

---

# 11. Code Examples

## 11.1 Simple Metric Functions

```python
from dataclasses import dataclass


@dataclass
class ConfusionCounts:
    true_positive: int
    false_positive: int
    false_negative: int


def precision(counts: ConfusionCounts) -> float:
    denominator = counts.true_positive + counts.false_positive
    return counts.true_positive / denominator if denominator else 0.0


def recall(counts: ConfusionCounts) -> float:
    denominator = counts.true_positive + counts.false_negative
    return counts.true_positive / denominator if denominator else 0.0


def f1_score(precision_value: float, recall_value: float) -> float:
    denominator = precision_value + recall_value
    if denominator == 0:
        return 0.0

    return 2 * precision_value * recall_value / denominator


counts = ConfusionCounts(
    true_positive=2,
    false_positive=1,
    false_negative=1,
)

p = precision(counts)
r = recall(counts)
f1 = f1_score(p, r)

print({
    "precision": round(p, 2),
    "recall": round(r, 2),
    "f1": round(f1, 2),
})
```

Expected output:

```python
{
    "precision": 0.67,
    "recall": 0.67,
    "f1": 0.67
}
```

---

## 11.2 Routing Accuracy

```python
def routing_accuracy(cases: list[dict]) -> float:
    if not cases:
        return 0.0

    correct = sum(
        1
        for case in cases
        if case["expected_route"] == case["actual_route"]
    )

    return correct / len(cases)


cases = [
    {
        "question": "How many reports exist?",
        "expected_route": "sql",
        "actual_route": "sql",
    },
    {
        "question": "Explain the grant policy.",
        "expected_route": "rag",
        "actual_route": "rag",
    },
    {
        "question": "Summarize the architecture.",
        "expected_route": "summarize",
        "actual_route": "rag",
    },
]

print(routing_accuracy(cases))
```

---

## 11.3 Tool Call Matching

```python
def normalize_tool_call(tool_call: dict) -> tuple:
    return (
        tool_call["name"],
        tuple(sorted(tool_call.get("args", {}).items())),
    )


def tool_call_metrics(
    expected_calls: list[dict],
    actual_calls: list[dict],
) -> dict:
    expected = {
        normalize_tool_call(call)
        for call in expected_calls
    }

    actual = {
        normalize_tool_call(call)
        for call in actual_calls
    }

    true_positive = len(expected & actual)
    false_positive = len(actual - expected)
    false_negative = len(expected - actual)

    counts = ConfusionCounts(
        true_positive=true_positive,
        false_positive=false_positive,
        false_negative=false_negative,
    )

    p = precision(counts)
    r = recall(counts)

    return {
        "precision": p,
        "recall": r,
        "f1": f1_score(p, r),
        "true_positive": true_positive,
        "false_positive": false_positive,
        "false_negative": false_negative,
    }
```

---

## 11.4 RAGAS-Style Pseudocode

```python
# Pseudocode because evaluator APIs can change by version.

for case in evaluation_dataset:
    result = await agent.ainvoke({
        "question": case["question"]
    })

    faithfulness = await faithfulness_metric.score(
        response=result["answer"],
        retrieved_contexts=result["retrieved_contexts"],
    )

    context_recall = await context_recall_metric.score(
        reference=case["reference_answer"],
        retrieved_contexts=result["retrieved_contexts"],
    )

    context_precision = await context_precision_metric.score(
        user_input=case["question"],
        reference=case["reference_answer"],
        retrieved_contexts=result["retrieved_contexts"],
    )

    answer_relevancy = await answer_relevancy_metric.score(
        user_input=case["question"],
        response=result["answer"],
    )

    save_scores({
        "case_id": case["case_id"],
        "faithfulness": faithfulness,
        "context_recall": context_recall,
        "context_precision": context_precision,
        "answer_relevancy": answer_relevancy,
    })
```

---

# 12. Interview Questions and Answers

## Q1. How do you evaluate a RAG system?

> I evaluate retrieval quality using Context Precision and Context Recall, grounding using Faithfulness, and answer quality using Answer Relevancy and Correctness. I use a gold dataset containing questions, reference answers, and expected contexts, run the pipeline, calculate per-case scores, aggregate by category, and inspect failed traces.

## Q2. How is Faithfulness calculated?

> The generated answer is broken into claims. Each claim is checked against the retrieved context. Faithfulness is the number of supported claims divided by the total number of answer claims.

## Q3. What is the difference between Context Precision and Context Recall?

> Context Precision measures how much retrieved content is relevant and whether relevant chunks are ranked early. Context Recall measures whether retrieval found enough of the information required to support the reference answer.

## Q4. How is Answer Relevancy different from Correctness?

> Relevancy measures whether the answer addresses the user's intent. Correctness measures whether the answer is factually right. A response can be highly relevant but factually incorrect.

## Q5. How do you evaluate an AI agent?

> I evaluate routing accuracy, tool-call precision and recall, tool argument correctness, trajectory quality, agent goal accuracy, task completion, latency, cost, and business outcomes. For RAG-enabled agents, I also include retrieval and grounding metrics.

## Q6. How is Tool Call F1 calculated?

> Correct expected calls are true positives, unnecessary calls are false positives, and missed expected calls are false negatives. Precision and recall are calculated from these values, and F1 is their harmonic mean.

## Q7. What is Agent Goal Accuracy?

> It measures whether the final state of the workflow satisfies the user's requested outcome. It is commonly represented as 1 for success and 0 for failure, although rubric-based versions can use graded scores.

## Q8. What is trajectory evaluation?

> Trajectory evaluation checks the complete sequence of agent decisions, tool calls, observations, and state transitions. It is useful when the order of operations matters or when unsafe or unnecessary actions must be detected.

## Q9. What is LLM-as-a-Judge?

> It uses an evaluator model to score semantic properties such as faithfulness, relevancy, correctness, or goal completion. It handles open-ended responses better than string matching, but must be calibrated against human labels because it can be variable and biased.

## Q10. How do you prevent evaluation from becoming unreliable?

> I combine deterministic checks with LLM-based metrics, use a fixed evaluator model and versioned rubric, validate judge scores against human-labeled samples, segment results by use case, and inspect traces for failed or borderline examples.

## Q11. How do you evaluate multi-agent systems?

> I evaluate each specialist agent, routing and handoffs, shared-state correctness, tool usage, trajectory quality, final goal completion, latency, and cost. I also check whether information is lost or distorted during agent-to-agent handoffs.

## Q12. How do you decide whether a new agent version is safe to release?

> I run an offline regression suite, compare it with the current production baseline, enforce thresholds for critical metrics, verify that no important segment regresses, inspect safety failures, and then monitor a controlled production rollout.

---

# 13. Production Best Practices

- Build a curated, versioned gold dataset.
- Include difficult, adversarial, and failure cases.
- Evaluate components separately before evaluating the whole agent.
- Use deterministic checks whenever possible.
- Calibrate LLM judges against human labels.
- Capture complete traces for failed cases.
- Segment scores instead of trusting only global averages.
- Track quality, latency, cost, safety, and business outcomes together.
- Add regression tests to CI/CD.
- Use authorization-aware evaluation cases for enterprise RAG.
- Re-evaluate after changing prompts, models, chunking, embeddings, routing, or tools.
- Never optimize one metric in isolation.

---

# 14. Quick Revision Sheet

```text
RAG METRICS
===========

Faithfulness
= Supported answer claims / all answer claims

Context Recall
= Retrieved-supported reference claims / all reference claims

Context Precision
= Are relevant chunks ranked early?

Answer Relevancy
= Does the answer address the question?


AGENT METRICS
=============

Routing Accuracy
= Correct routes / total cases

Tool Precision
= Correct calls / all actual calls

Tool Recall
= Correct calls / all expected calls

Tool F1
= Harmonic mean of tool precision and recall

Goal Accuracy
= Did the final state satisfy the user's goal?

Task Completion Rate
= Successful tasks / eligible tasks

Trajectory Quality
= Were the decisions and actions appropriate?


OPERATIONS
==========

Latency
Token Usage
Cost per Request
Retries
Loop Count
Tool Failure Rate


OBSERVABILITY
=============

Inputs
Routes
Retrieved Context
Prompts
Tool Calls
State Transitions
Outputs
```

---

# 15. References

- [RAGAS Faithfulness](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/faithfulness/)
- [RAGAS Context Precision](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/context_precision/)
- [RAGAS Context Recall](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/context_recall/)
- [RAGAS Answer Relevancy](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/answer_relevance/)
- [RAGAS Agent and Tool-Use Metrics](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/agents/)

---

# Final Mental Model

```text
RAG Evaluation
==============
Did we retrieve and answer correctly?

Agent Evaluation
================
Did we route, plan, act, and complete the goal correctly?

Monitoring
==========
Is the production system healthy and efficient?

Observability
=============
Can we explain why the system behaved that way?
```
