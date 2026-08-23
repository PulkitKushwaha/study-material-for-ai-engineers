# 14 - Agent2Agent (A2A) Protocol

> A practical, interview-focused guide to Agent2Agent communication, agent discovery, Agent Cards, task lifecycles, artifacts, long-running work, security, and the relationship between A2A, MCP, and LangGraph.

---

## Table of Contents

1. What Is A2A?
2. Why A2A Exists
3. A2A vs MCP vs LangGraph
4. Core A2A Concepts
5. A2A Lifecycle
6. Intermediate Interview Questions and Answers
7. Advanced Interview Questions and Answers
8. Enterprise Architecture Example
9. KM 2.0 A2A Use Case
10. Security and Governance
11. Observability and Evaluation
12. Common Mistakes
13. Production Best Practices
14. Quick Revision Sheet
15. References

---

# 1. What Is A2A?

A2A stands for:

```text
Agent2Agent Protocol
```

It is an open interoperability standard designed to let independent AI agents communicate and collaborate even when they are built using different frameworks, programming languages, vendors, or cloud platforms.

A2A focuses on:

```text
Agent Discovery
Task Delegation
Structured Messaging
Progress Updates
Artifact Exchange
Long-Running Workflows
Cross-Framework Interoperability
```

The fundamental idea is:

```text
Agent A
    ↓
Discovers Agent B
    ↓
Delegates a Task
    ↓
Agent B Performs Work
    ↓
Agent B Returns Progress and Artifacts
```

---

# 2. Why A2A Exists

Without a common agent communication protocol, every multi-agent integration becomes custom.

```text
LangGraph Agent
    ↓ custom integration
CrewAI Agent

Semantic Kernel Agent
    ↓ another custom integration
External Vendor Agent
```

This creates:

```text
Tight Coupling
Vendor Lock-In
Duplicate Integration Logic
Difficult Governance
Difficult Capability Discovery
```

A2A provides a common interaction model.

```text
Any A2A-Compatible Agent
    ↓
A2A Protocol
    ↓
Any Other A2A-Compatible Agent
```

A2A agents collaborate based on declared capabilities and exchanged information without needing access to each other's internal prompts, private memory, reasoning state, or tool implementation.

---

# 3. A2A vs MCP vs LangGraph

## MCP

MCP standardizes communication between an AI application and tools, resources, and prompts.

```text
Agent
    ↓
MCP Client
    ↓
MCP Server
    ↓
Database / API / SharePoint / ServiceNow
```

Mental model:

```text
MCP = Agent-to-Tool Integration
```

## A2A

A2A standardizes collaboration between independent agents.

```text
Supervisor Agent
    ↓
A2A
    ↓
Finance Agent
```

Mental model:

```text
A2A = Agent-to-Agent Collaboration
```

## LangGraph

LangGraph is an orchestration framework for stateful workflows.

```text
State
Nodes
Edges
Conditional Routing
Loops
Checkpoints
```

Mental model:

```text
LangGraph = Workflow Orchestration
```

## Combined Architecture

```text
User
    ↓
LangGraph Supervisor
    ↓
A2A Client
    ├── Finance Agent
    ├── Support Agent
    └── Procurement Agent
             ↓
            MCP
             ↓
      Tools and Enterprise Systems
```

A concise distinction:

```text
LangGraph decides the workflow.
A2A lets independent agents collaborate.
MCP lets an agent use tools and data.
```

---

# 4. Core A2A Concepts

## 4.1 Agent Card

An Agent Card is a machine-readable description of an agent.

It communicates information such as:

```text
Agent Identity
Agent Description
Capabilities
Skills
Supported Interaction Modes
Endpoint Information
Authentication Requirements
```

Mental model:

```text
Agent Card = Agent Resume + API Contract
```

Conceptual example:

```json
{
  "name": "IT Support Agent",
  "description": "Resolves enterprise IT support issues",
  "skills": [
    {
      "id": "resolve_vpn_issue",
      "name": "VPN Issue Resolution",
      "description": "Diagnoses VPN issues and creates support incidents"
    }
  ],
  "url": "https://agents.company.example/support",
  "capabilities": {
    "streaming": true,
    "pushNotifications": true
  }
}
```

The exact schema depends on the A2A specification version and SDK being used.

---

## 4.2 Discovery

Discovery is the process by which one agent learns that another agent exists and understands its capabilities.

```text
Client Agent
    ↓
Retrieve Agent Card
    ↓
Inspect Skills and Requirements
    ↓
Decide Whether the Remote Agent Can Help
```

Discovery answers:

```text
Which agent can perform this work?
What input does it accept?
What output can it produce?
How should I authenticate?
Does it support streaming or long-running tasks?
```

---

## 4.3 Task

A task is a stateful unit of delegated work.

Example:

```text
Investigate unresolved VPN issue
```

A task can transition through states such as:

```text
Submitted
Working
Input Required
Completed
Failed
Canceled
```

The exact state names and semantics should follow the A2A specification version used by the implementation.

---

## 4.4 Message

Messages are the conversational or instructional exchanges associated with a task.

Examples:

```text
Client Agent:
Investigate this VPN issue.

Remote Agent:
I need the device ID.

Client Agent:
The device ID is LAP-1042.
```

Messages make A2A more flexible than a one-shot function call.

---

## 4.5 Part

A message or artifact can contain multiple parts.

Examples:

```text
Text
Structured JSON
File Reference
Image Reference
Form Data
```

This enables multimodal and structured communication.

---

## 4.6 Artifact

An artifact is an output produced by an agent while completing a task.

Examples:

```text
Investigation Summary
PDF Report
Structured JSON Result
Invoice
Generated Configuration
Risk Assessment
```

Mental model:

```text
Message = Communication
Artifact = Deliverable
```

---

## 4.7 Streaming and Progress Updates

A2A supports interactions where work may take time.

```text
Task Submitted
    ↓
Agent Working
    ↓
Progress Update
    ↓
Input Required
    ↓
Work Resumed
    ↓
Artifact Produced
```

This is useful for:

```text
Research
Compliance Reviews
Data Analysis
Document Generation
Human Approval Workflows
```

---

# 5. A2A Lifecycle

Use case:

```text
A workplace assistant needs a detailed grant-risk report.
```

## Step 1: User Request

```text
Prepare a risk report for the active malaria grants.
```

## Step 2: Supervisor Decomposes the Goal

```text
Need grant data
Need audit findings
Need risk analysis
Need final report
```

## Step 3: Agent Discovery

The supervisor discovers available Agent Cards:

```text
Grant Data Agent
Audit Research Agent
Risk Analysis Agent
Report Generation Agent
```

## Step 4: Capability Selection

The supervisor selects agents whose skills match the required subtasks.

## Step 5: Task Delegation

```text
Supervisor → Grant Agent:
Retrieve active malaria grants.
```

## Step 6: Task Execution

The Grant Agent may internally use MCP to query Azure SQL or another structured source.

```text
Grant Agent
    ↓
MCP Client
    ↓
Database MCP Server
    ↓
Azure SQL
```

## Step 7: Progress or Input Request

The agent can report:

```text
Working
```

or request additional input:

```text
Which reporting period should I use?
```

## Step 8: Artifact Returned

```json
{
  "active_grants": 12,
  "countries": ["Country A", "Country B"],
  "reporting_period": "current"
}
```

## Step 9: Agent-to-Agent Handoff

The supervisor sends the grant artifact and audit evidence to the Risk Analysis Agent.

## Step 10: Final Composition

The Report Agent combines the outputs into a final report.

## Step 11: Completion

The user receives:

```text
Final Risk Report
Supporting Evidence
Source List
Agent Execution Trace
```

---

# 6. Intermediate Interview Questions and Answers

## Q1. How do agents discover each other?

Agents discover each other through machine-readable Agent Cards. An Agent Card describes an agent's identity, endpoint, capabilities, skills, supported interaction modes, and security requirements. A client agent retrieves and inspects the card before deciding whether the remote agent can perform a requested task.

A simplified flow is:

```text
Client Agent
    ↓
Retrieve Agent Card
    ↓
Inspect Skills
    ↓
Match User Goal to Capability
    ↓
Send Task or Message
```

Discovery should not be confused with selection. Discovery identifies what agents are available. Selection decides which discovered agent should receive a particular task.

---

## Q2. Why use Agent Cards?

Agent Cards provide a standard capability contract between otherwise independent agents.

They help answer:

```text
Who is this agent?
What can it do?
Where is it hosted?
What input and output modes does it support?
Does it support streaming?
How should the caller authenticate?
```

Without Agent Cards, agent capabilities would need to be hardcoded into every orchestrator, creating tight coupling.

Agent Cards support:

- Dynamic discovery
- Capability-based routing
- Cross-vendor interoperability
- Reduced integration coupling
- Security negotiation
- Better governance and inventory management

---

## Q3. How are long-running tasks handled?

A2A models work as stateful tasks rather than assuming every interaction completes in one immediate request-response cycle.

A long-running flow may look like:

```text
Submitted
    ↓
Working
    ↓
Progress Update
    ↓
Input Required
    ↓
Working
    ↓
Completed
```

The client can receive progress through streaming mechanisms or asynchronous notifications, depending on the protocol binding and implementation. The task identifier allows the client to query or correlate task state over time.

This makes A2A suitable for research, report generation, compliance checks, and human-in-the-loop workflows.

---

## Q4. What are artifacts?

Artifacts are the deliverables generated by an agent while completing a task.

Examples:

- A report
- A JSON result
- A document
- A generated file
- A risk assessment
- A set of extracted records

Messages are used for communication, while artifacts represent task outputs.

```text
Message:
I have completed the analysis.

Artifact:
risk_report.pdf
```

Artifacts can contain multiple parts, such as text, structured data, or file references.

---

## Q5. How is A2A different from normal APIs?

A standard API usually exposes predefined operations:

```text
GET /orders
POST /tickets
```

A2A exposes an agent as a collaborative system capable of:

- Advertising skills through an Agent Card
- Receiving goal-oriented messages
- Managing stateful tasks
- Requesting additional input
- Streaming progress
- Returning multimodal artifacts
- Operating without revealing internal reasoning or tools

A2A still builds on familiar web protocol concepts, but its interaction model is agent- and task-oriented rather than only endpoint-oriented.

A normal API call often means:

```text
Call operation → Receive response
```

A2A can mean:

```text
Delegate goal
→ negotiate details
→ monitor progress
→ provide additional input
→ receive artifacts
```

---

# 7. Advanced Interview Questions and Answers

## Q6. A2A vs LangGraph?

LangGraph and A2A solve different problems.

### LangGraph

LangGraph orchestrates a stateful workflow inside an application.

It provides:

```text
State
Nodes
Edges
Conditional Routing
Loops
Reducers
Checkpoints
Human-in-the-Loop
```

### A2A

A2A standardizes communication between independent agent systems.

It provides concepts for:

```text
Agent Discovery
Capability Advertisement
Task Delegation
Messages
Progress Updates
Artifacts
Cross-Framework Interoperability
```

### Combined Use

A LangGraph workflow can act as an A2A client, A2A server, or both.

```text
LangGraph Supervisor
    ↓ A2A
Remote Finance Agent
```

The remote Finance Agent may itself be implemented with LangGraph, CrewAI, Semantic Kernel, or another framework. The client should not need to know its internals.

Interview answer:

> LangGraph is an orchestration framework for building and controlling stateful agent workflows. A2A is an interoperability protocol for communication between independent agents. LangGraph controls the internal workflow, while A2A defines how that workflow collaborates with remote agents.

---

## Q7. A2A vs MCP?

MCP and A2A are complementary.

### MCP

```text
Agent ↔ Tool / Data / Resource
```

Examples:

```text
Agent → SharePoint
Agent → SQL
Agent → ServiceNow
```

### A2A

```text
Agent ↔ Agent
```

Examples:

```text
Supervisor Agent → Risk Agent
Support Agent → Identity Agent
Procurement Agent → Supplier Agent
```

### Combined Architecture

```text
Supervisor Agent
    ↓ A2A
Support Agent
    ↓ MCP
ServiceNow Tool
```

Interview answer:

> MCP standardizes how an agent consumes tools, resources, and prompts. A2A standardizes how independent agents discover one another, delegate tasks, exchange messages, and return artifacts. An A2A remote agent may internally use MCP to access tools and enterprise systems.

---

## Q8. How would you design a multi-agent architecture using A2A?

Start by defining domain boundaries rather than creating many agents immediately.

Example enterprise architecture:

```text
User
    ↓
Supervisor / Concierge Agent
    ├── A2A → Knowledge Agent
    ├── A2A → SQL Analytics Agent
    ├── A2A → Risk Agent
    └── A2A → Service Management Agent
```

Each remote agent should:

1. Publish a clear Agent Card.
2. Expose focused domain skills.
3. Accept well-defined messages or tasks.
4. Return structured artifacts.
5. Authenticate callers.
6. Emit traces and task-status events.
7. Enforce authorization independently.

The supervisor should:

1. Understand the user goal.
2. Discover or load available Agent Cards.
3. Select the appropriate agent.
4. Delegate subtasks.
5. Track task identifiers and state.
6. Handle input-required responses.
7. Aggregate artifacts.
8. Apply timeout, retry, and fallback policies.
9. Return a coherent final response.

Avoid making the supervisor responsible for every domain detail. It should coordinate rather than duplicate specialist behavior.

---

## Q9. How could KM 2.0 use A2A?

A possible future KM 2.0 architecture could separate independent specialist agents.

```text
KM 2.0 Concierge
    ├── A2A → Policy Knowledge Agent
    ├── A2A → Procedural Guidance Agent
    ├── A2A → NL2SQL Analytics Agent
    ├── A2A → Investigation Agent
    └── A2A → ServiceNow Support Agent
```

Example question:

```text
Summarize the policy, identify affected grants,
and raise a ticket if the required document is missing.
```

Possible flow:

```text
1. Concierge discovers specialist agents.
2. Policy Agent retrieves and summarizes policy evidence.
3. Analytics Agent identifies affected grants.
4. Concierge combines both artifacts.
5. If evidence is missing, Support Agent creates a ticket.
6. Final answer includes citations, structured results, and ticket ID.
```

Each specialist may internally use MCP:

```text
Policy Agent
    ↓ MCP
Azure AI Search / SharePoint

Analytics Agent
    ↓ MCP
Azure SQL

Support Agent
    ↓ MCP
ServiceNow
```

A2A would be beneficial only if these are truly independent agents or independently deployed domain services. If all capabilities are simple nodes inside one KM 2.0 application, a single LangGraph may be simpler.

---

## Q10. What are the security concerns in agent communication?

A2A communication introduces both traditional API risks and agent-specific risks.

### Authentication

The caller and remote agent must verify each other's identities using enterprise-standard mechanisms supported by the deployment.

### Authorization

An authenticated agent should only be allowed to invoke permitted skills and access permitted data.

```text
Authenticated ≠ Authorized
```

### Delegation and User Identity

When Agent A delegates to Agent B, the system must define whether Agent B acts:

- As Agent A
- As the end user
- As a service identity
- Under a constrained delegated token

Avoid blindly forwarding credentials.

### Least Privilege

Each agent should receive only the permissions required for its domain.

### Prompt Injection and Untrusted Content

A remote agent or artifact may return malicious instructions. Treat remote messages and artifacts as untrusted data, not system-level instructions.

### Data Leakage

The delegating agent must minimize the context it shares. Do not send an entire conversation when only a small structured subset is required.

### Agent Impersonation

Agent Cards and endpoints must be validated so a malicious service cannot impersonate an approved agent.

### Replay and Tampering

Task requests, messages, and notifications should be protected using secure transport, authentication, appropriate freshness controls, and integrity validation.

### Over-Delegation

A remote agent should not be allowed to recursively delegate sensitive work without policy controls.

### Unsafe Actions

High-impact actions should use:

```text
Approval Gates
Policy Checks
Idempotency Keys
Rate Limits
Audit Logs
Human-in-the-Loop
```

### Observability and Auditability

Record:

```text
Calling Agent
Remote Agent
Task ID
User Context
Skill Selected
Messages
Artifacts
Authorization Decision
Final Outcome
```

Sensitive prompts, credentials, and restricted data should be redacted from telemetry.

---

# 8. Enterprise Architecture Example

Use case:

```text
An employee requests a laptop for a new joiner.
```

Architecture:

```text
Employee Assistant
    ↓ A2A
HR Agent
    ↓ Artifact: employee and start-date details

Employee Assistant
    ↓ A2A
IT Asset Agent
    ↓ MCP
Inventory Database
    ↓ Artifact: available devices

Employee Assistant
    ↓ A2A
Procurement Agent
    ↓ MCP
Purchasing System
    ↓ Artifact: order confirmation
```

Possible lifecycle:

```text
1. Discover HR, IT Asset, and Procurement agents.
2. Ask HR Agent to validate the new joiner.
3. Ask IT Asset Agent to check inventory.
4. If stock exists, reserve a device.
5. If stock does not exist, delegate purchase to Procurement Agent.
6. Stream progress to the user.
7. Return the reservation or order artifact.
```

---

# 9. KM 2.0 A2A Use Case

Question:

```text
Which policy applies to this grant issue,
what procedure should the user follow,
and is escalation required?
```

Possible agents:

```text
Policy Agent
Procedure Agent
Risk Agent
Support Agent
```

Flow:

```text
KM Concierge
    ↓ A2A
Policy Agent
    ↓
Policy Artifact

KM Concierge
    ↓ A2A
Procedure Agent
    ↓
Procedure Artifact

KM Concierge
    ↓ A2A
Risk Agent
    ↓
Escalation Recommendation

If escalation required:
KM Concierge
    ↓ A2A
Support Agent
    ↓ MCP
ServiceNow
    ↓
Ticket Artifact
```

The final response should distinguish:

- Evidence from agent artifacts
- Generated synthesis
- Actions actually completed
- Actions requiring user approval

---

# 10. Security and Governance

An enterprise A2A governance model should cover:

```text
Agent Registration
Agent Card Validation
Identity and Authentication
Skill-Level Authorization
Data Classification
Delegation Policy
Approval Requirements
Rate Limits
Task Timeouts
Artifact Retention
Audit Logging
Incident Response
Agent Decommissioning
```

Recommended controls:

- Maintain an approved agent registry.
- Sign or validate trusted Agent Card distribution.
- Apply least privilege per skill.
- Use explicit data-sharing contracts.
- Redact sensitive data before delegation.
- Validate artifacts before downstream use.
- Require approval for destructive actions.
- Define timeout, retry, and cancellation behavior.
- Use correlation IDs across agent boundaries.
- Version Agent Cards and skill contracts.

---

# 11. Observability and Evaluation

Monitor A2A at three levels.

## Operational Metrics

```text
Task Latency
Agent Availability
Message Failures
Streaming Disconnects
Retry Count
Cancellation Rate
Artifact Delivery Failures
```

## Agent Quality Metrics

```text
Agent Selection Accuracy
Task Completion Rate
Goal Accuracy
Handoff Accuracy
Artifact Correctness
Unnecessary Delegation Rate
Human Override Rate
```

## Business Metrics

```text
Resolution Rate
Escalation Rate
Automation Rate
User Satisfaction
Cost per Completed Task
```

A distributed trace should link:

```text
User Request
    ↓
Supervisor Trace
    ↓
A2A Task ID
    ↓
Remote Agent Trace
    ↓
MCP Tool Trace
    ↓
Final Artifact
```

---

# 12. Common Mistakes

## Using A2A for Simple Function Calls

If the capability is a simple deterministic function, MCP or a normal API may be more appropriate.

## Creating Too Many Agents

Do not turn every function into an agent.

## Sharing Private Internal Reasoning

A2A does not require agents to expose private chain-of-thought or internal state.

## No Task Termination Policy

Long-running tasks require timeouts, cancellation, retry limits, and failure handling.

## Trusting Remote Artifacts Automatically

Validate remote output before using it in high-impact decisions or tool calls.

## No Idempotency

Retries can duplicate purchases, tickets, or transactions unless actions are idempotent.

## Ignoring Versioning

Agent Cards, skills, payloads, and artifacts should be versioned.

---

# 13. Production Best Practices

- Prefer focused domain agents.
- Use A2A only when agent independence and interoperability add value.
- Use MCP for tool and data access inside agents.
- Keep Agent Cards clear and versioned.
- Use structured artifacts rather than prose where possible.
- Apply least privilege at agent and skill level.
- Treat all remote content as untrusted.
- Add timeouts, retries, cancellation, and idempotency.
- Trace every cross-agent call with correlation IDs.
- Evaluate selection, handoffs, outcomes, latency, and cost.
- Add human approval for destructive or regulated actions.
- Avoid exposing private reasoning, secrets, or complete memory stores.

---

# 14. Quick Revision Sheet

```text
A2A
===
Agent-to-Agent communication and collaboration

Agent Card
==========
Machine-readable agent identity, endpoint, skills,
capabilities, and security requirements

Discovery
=========
Find agents and understand what they can do

Selection
=========
Choose the best agent for the task

Task
====
Stateful unit of delegated work

Message
=======
Communication during task execution

Artifact
========
Task deliverable such as JSON, report, or file

MCP
===
Agent-to-tool/data integration

LangGraph
=========
Stateful workflow orchestration

A2A
===
Independent agent interoperability
```

## Memorize This Interview Answer

> A2A is an open interoperability protocol for communication between independent AI agents. Agents advertise capabilities through Agent Cards, discover each other, exchange messages, manage stateful and potentially long-running tasks, and return artifacts. A2A complements MCP: MCP connects agents to tools and data, while A2A connects agents to other agents. LangGraph can orchestrate the internal workflow of an agent and use A2A to delegate work to remote agents.

---

# 15. References

- [A2A Protocol Specification](https://a2a-protocol.org/latest/specification/)
- [Google Announcement: Agent2Agent Protocol](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/)
- [Google A2A Codelab](https://codelabs.developers.google.com/intro-a2a-purchasing-concierge)
- [IBM Overview of Agent2Agent Protocol](https://www.ibm.com/think/topics/agent2agent-protocol)
