# 15 - LLM Fine-Tuning Complete Guide

## Learning Objectives

Understand:

- Fine-Tuning Fundamentals
- SFT (Supervised Fine-Tuning)
- PEFT
- LoRA
- QLoRA
- RLHF
- DPO
- Fine-Tuning vs RAG
- Fine-Tuning vs Prompt Engineering
- Enterprise Use Cases
- Azure AI Foundry Relevance
- Interview Questions and Answers

---

# What is Fine-Tuning?

Fine-tuning is the process of taking a pretrained language model and continuing training on a smaller, task-specific dataset to adapt the model for a particular behavior, style, domain, or task.

```text
Pretrained Model
      ↓
Custom Dataset
      ↓
Fine-Tuned Model
```

Examples:

- Financial assistant
- Legal copilot
- Cybersecurity analyst
- Medical summarizer
- Internal enterprise assistant

---

# Three Ways to Customize an LLM

## 1. Prompt Engineering

```text
Base Model
+ Prompt
```

Pros:

- No training
- Fast
- Cheap

Cons:

- Inconsistent
- Long prompts
- Not permanent

---

## 2. Fine-Tuning

```text
Base Model
+ Training Data
```

Pros:

- Permanent behavior change
- Better consistency
- Better format adherence

Cons:

- Training cost
- Requires data

---

## 3. Training From Scratch

```text
Random Weights
      ↓
Massive Compute
      ↓
Foundation Model
```

Used by:

- OpenAI
- Anthropic
- Google
- Meta

---

# What Fine-Tuning Improves

## Behavior

Examples:

```text
Helpful
Professional
Technical
Friendly
```

## Formatting

Examples:

```json
{
  "risk":"high"
}
```

## Domain Adaptation

Examples:

```text
Healthcare
Finance
Cybersecurity
Legal
```

## Task Specialization

Examples:

```text
Classification
Summarization
Extraction
Code Generation
```

---

# What Fine-Tuning Does NOT Improve

Fine-tuning is not the best solution for:

```text
Frequently Changing Knowledge
Daily Document Updates
Real-Time Information
```

Example:

```text
Enterprise Knowledge Base
```

Use RAG instead.

---

# Fine-Tuning Workflow

```text
Prepare Dataset
      ↓
Choose Model
      ↓
Fine Tune
      ↓
Evaluate
      ↓
Deploy
```

---

# SFT (Supervised Fine-Tuning)

## What is SFT?

SFT uses labeled examples.

Example:

```text
Input:
What is RAG?

Output:
Retrieval-Augmented Generation...
```

The model learns:

```text
Input
  ↓
Expected Output
```

---

## SFT Dataset

```json
{
  "instruction": "Explain RAG",
  "response": "RAG combines retrieval and generation"
}
```

Thousands of examples are used.

---

## Why SFT Matters

SFT teaches:

```text
Instruction Following
Desired Style
Task Behavior
```

---

# Full Fine-Tuning

Traditional approach.

```text
Update All Parameters
```

Example:

```text
7 Billion Parameters
Updated
```

Advantages:

- Maximum flexibility

Disadvantages:

- Expensive
- Large GPUs
- Large storage
- Long training time

---

# PEFT (Parameter Efficient Fine-Tuning)

## What is PEFT?

Instead of updating:

```text
All Parameters
```

Update:

```text
Very Small Subset
```

Examples:

```text
0.1%
0.5%
1%
```

---

## Why PEFT Exists

Benefits:

```text
Less Memory
Less Storage
Less Cost
Faster Training
```

---

## PEFT Techniques

```text
LoRA
QLoRA
Adapters
Prefix Tuning
Prompt Tuning
IA3
```

Most common:

```text
LoRA
```

---

# LoRA (Low-Rank Adaptation)

## Core Idea

Freeze original weights.

Train:

```text
Tiny Trainable Adapters
```

Instead of:

```text
Entire Model
```

---

## LoRA Architecture

Without LoRA:

```text
Input
 ↓
Model Weights
 ↓
Output
```

With LoRA:

```text
Input
 ↓
Frozen Model
 +
LoRA Adapter
 ↓
Output
```

---

## Benefits of LoRA

```text
Low GPU Cost
Low Storage
Fast Training
Easy Deployment
```

---

## Real Enterprise Use Case

Train:

```text
Enterprise Writing Style
Response Templates
Industry Terminology
```

without modifying the whole model.

---

# QLoRA (Quantized LoRA)

## Problem With LoRA

Even with LoRA:

```text
Large Base Model
must remain in memory
```

---

## QLoRA Solution

```text
Quantize Model
+
Apply LoRA
```

Typical:

```text
4-Bit Quantization
```

---

## Why QLoRA Matters

Benefits:

```text
Lower Memory
Lower Cost
Consumer GPUs Possible
Large Models Become Trainable
```

---

## QLoRA Pipeline

```text
Model
 ↓
4-Bit Quantization
 ↓
Frozen
 ↓
LoRA Training
```

---

# RLHF (Reinforcement Learning from Human Feedback)

## Problem

SFT teaches:

```text
Correct Answers
```

But not necessarily:

```text
Helpful
Safe
Aligned
```

---

## RLHF Goal

Improve:

```text
Helpfulness
Harmlessness
Honesty
Alignment
```

---

## RLHF Workflow

```text
Pretraining
 ↓
SFT
 ↓
Human Feedback
 ↓
Reward Model
 ↓
RL Optimization
 ↓
Aligned Model
```

---

## Human Ranking Example

Question:

```text
How should I learn Python?
```

Humans compare:

```text
Answer A
vs
Answer B
```

Preferred answer receives higher reward.

---

# Reward Model

Learns:

```text
What Humans Prefer
```

Example:

```text
Answer A = 9
Answer B = 2
```

---

# DPO (Direct Preference Optimization)

## Motivation

RLHF is complicated.

Needs:

```text
Reward Model
Reinforcement Learning
```

---

## DPO Idea

Use:

```text
Human Preferences
```

Directly.

No separate reward model.

---

## DPO Dataset

```text
Prompt

Chosen Answer

Rejected Answer
```

---

## Why Industry Likes DPO

```text
Simpler
More Stable
Cheaper
Easier Training
```

---

# Fine-Tuning vs Prompt Engineering

| Prompt Engineering | Fine-Tuning |
|----------|----------|
| No training | Training required |
| Cheap | More expensive |
| Temporary behavior | Permanent behavior |
| Long prompts | Short prompts |
| Less consistency | More consistency |

---

# Fine-Tuning vs RAG

This is one of the most important interview topics.

## Use RAG When

```text
Knowledge Changes Frequently
Need Latest Documents
Need Citations
Enterprise Search
```

Examples:

```text
KM 2.0
COLIN
SharePoint Search
Knowledge Management Bots
```

---

## Use Fine-Tuning When

```text
Need Behavior Changes
Need Formatting Consistency
Need Domain Style
Need Specialized Tasks
```

Examples:

```text
Medical Assistant
Financial Report Generator
Classification Engine
```

---

# Would You Fine-Tune KM 2.0?

Recommended Answer:

```text
No for document retrieval.

Use RAG because knowledge changes frequently.

Possible Fine-Tuning Uses:
- Response Formatting
- Writing Style
- Classification
- Domain Terminology
```

---

# Enterprise Decision Framework

## Prompt Engineering

Use When:

```text
Quick Prototype
Low Volume
No Training Data
```

## Fine-Tuning

Use When:

```text
Need Consistency
Need Behavior Changes
Need Domain Adaptation
```

## RAG

Use When:

```text
Knowledge Changes Often
Need Traceability
Need Source Citations
```

---

# Fine-Tuning in Azure AI Foundry

Common Flow:

```text
Select Base Model
 ↓
Upload Dataset
 ↓
Launch Fine-Tuning Job
 ↓
Evaluate
 ↓
Deploy Endpoint
```

Supported Concepts:

```text
Model Catalog
Fine-Tuning Jobs
Evaluations
Tracing
Safety Validation
Deployment
```

---

# Interview Questions and Answers

## What is Fine-Tuning?

Fine-tuning is continuing the training of a pretrained model on a task-specific dataset to adapt its behavior, style, or capabilities.

---

## What is SFT?

Supervised Fine-Tuning trains a model using labeled input-output examples.

---

## What is PEFT?

Parameter Efficient Fine-Tuning updates only a small fraction of model parameters, reducing memory and compute requirements.

---

## What is LoRA?

LoRA freezes base model weights and trains small low-rank adapters instead.

---

## What is QLoRA?

QLoRA combines quantization and LoRA to reduce memory usage while enabling efficient fine-tuning.

---

## What is RLHF?

RLHF aligns a model to human preferences using human rankings, reward models, and reinforcement learning.

---

## What is DPO?

DPO directly optimizes models from preference pairs without requiring a separate reward model.

---

## Fine-Tuning vs RAG?

Fine-tuning changes behavior.

RAG provides dynamic external knowledge.

---

## Would You Fine-Tune Enterprise Knowledge Bases?

Generally no.

Enterprise knowledge changes frequently and is better handled by RAG.

---

# Complete Mental Model

```text
Pretraining
     ↓
Foundation Model

SFT
     ↓
Instruction Following

PEFT
     ↓
Efficient Training

LoRA
     ↓
Adapter Tuning

QLoRA
     ↓
Quantized Adapter Tuning

RLHF
     ↓
Human Alignment

DPO
     ↓
Simplified Alignment

RAG
     ↓
Dynamic Knowledge
```

---

# Final Interview Answer

Modern LLM customization typically starts with supervised fine-tuning (SFT) using instruction-response datasets. To reduce training costs, organizations commonly use PEFT methods such as LoRA and QLoRA, which train small adapters instead of all model weights. Model alignment is improved with RLHF or DPO using human preference data. For dynamic knowledge bases such as enterprise documents, RAG is generally preferred over fine-tuning because it can retrieve current information without retraining.
