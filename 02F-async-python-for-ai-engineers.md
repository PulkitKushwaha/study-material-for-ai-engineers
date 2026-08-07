# 02F - Async Python for AI Engineers

> A practical guide to Async Python for FastAPI, LangGraph, LangChain, MCP, and Production Agentic AI Systems.
>
> Goal:
>
> - Understand the problem Async solves
> - Understand Coroutines
> - Understand async / await
> - Understand the Event Loop
> - Understand asyncio.gather()
> - Understand Async vs Threading
> - Understand Async vs Multiprocessing
> - Understand Async in FastAPI, LangChain, LangGraph and MCP
> - Master common interview questions

---

# Table of Contents

1. Why Async Exists
2. The Waiter Analogy
3. Blocking vs Non-Blocking Code
4. Coroutines
5. async def
6. await
7. Event Loop
8. asyncio.run()
9. asyncio.gather()
10. asyncio.create_task()
11. Async vs Threading
12. Async vs Multiprocessing
13. Async and the GIL
14. Async in FastAPI
15. Async in LangChain
16. Async in LangGraph
17. Async in MCP
18. Interview Questions and Answers
19. Production Best Practices
20. Mental Models

---

# Why Async Exists

Most modern AI applications spend very little time computing.

Instead they spend most of their time:

```text
Waiting for OpenAI
Waiting for Azure AI Search
Waiting for SQL
Waiting for APIs
Waiting for Storage
```

Async exists to make use of this waiting time.

---

# The Waiter Analogy

Imagine a waiter.

Customer says:

```text
Please bring me coffee.
```

Coffee machine needs:

```text
5 minutes.
```

---

## Bad Waiter

```text
Waiter waits at machine
for 5 minutes.
```

Nothing else gets done.

---

## Smart Waiter

```text
Coffee starts brewing

↓

Take another order

↓

Serve another customer

↓

Return when coffee is ready
```

This is Async.

---

# Blocking vs Non-Blocking

---

## Blocking

```python
import time

time.sleep(5)
```

Program pauses.

Nothing else happens.

---

## Non-Blocking

```python
await asyncio.sleep(5)
```

Current task pauses.

Event loop continues doing work.

---

# What Is A Coroutine?

A coroutine is a function defined using:

```python
async def
```

Example:

```python
async def greet():

    return "Hello"
```

A coroutine can be paused and resumed.

---

# async def

When Python sees:

```python
async def get_answer():
```

it creates a coroutine function.

---

Example:

```python
async def get_user():

    return {
        "name": "Pulkit"
    }
```

---

# await

The most important Async keyword.

Example:

```python
response = await llm.ainvoke(prompt)
```

Meaning:

```text
Pause this task

BUT

Allow other tasks to run
```

---

# Event Loop

The Event Loop is the scheduler of Async Python.

Think:

```text
Traffic Controller
```

or

```text
Super Waiter
```

---

It decides:

```text
Task A waiting

↓

Run Task B

↓

Run Task C

↓

Task A becomes ready

↓

Resume Task A
```

---

# Visual Example

Without Async:

```text
Task 1
5 sec

Task 2
5 sec

Task 3
5 sec

Total = 15 sec
```

---

With Async:

```text
Start Task 1
Start Task 2
Start Task 3

↓

Wait together

↓

Finish together

Total ≈ 5 sec
```

---

# asyncio.run()

Used to start the event loop.

Example:

```python
import asyncio


async def hello():

    print("Hello")


asyncio.run(hello())
```

---

# First Async Example

```python
import asyncio


async def greet():

    print("Hello")

    await asyncio.sleep(2)

    print("World")


asyncio.run(greet())
```

Output:

```text
Hello

(wait 2 seconds)

World
```

---

# asyncio.gather()

The most important Async API.

Used when you want multiple tasks to run concurrently.

---

Example

```python
import asyncio


async def task(name):

    print(f"{name} started")

    await asyncio.sleep(2)

    print(f"{name} completed")


async def main():

    await asyncio.gather(
        task("A"),
        task("B"),
        task("C")
    )


asyncio.run(main())
```

---

Output

```text
A started
B started
C started

(wait)

A completed
B completed
C completed
```

---

# Why gather() Matters

Suppose:

```python
call_openai()
call_search()
call_database()
```

Each takes:

```text
2 seconds
```

Sequential:

```text
6 seconds
```

Concurrent:

```python
asyncio.gather(...)
```

Approximately:

```text
2 seconds
```

---

# asyncio.create_task()

Used for background concurrent execution.

---

Example

```python
task = asyncio.create_task(
    fetch_documents()
)

answer = await generate_answer()

docs = await task
```

---

Useful when tasks are independent.

---

# Async vs Threading

---

## Threading

```text
Many Waiters
```

Example:

```text
Thread A

Thread B

Thread C
```

---

## Async

```text
One Super Waiter
```

Example:

```text
One Thread

Many Tasks

Event Loop
```

---

# Memory Usage

Threading:

```text
Thread Per Task
```

---

Async:

```text
One Thread

Many Coroutines
```

Usually more efficient.

---

# Async vs Multiprocessing

---

## Async

Best for:

```text
Waiting Work
```

Examples:

```python
OpenAI
Azure Search
SQL
REST APIs
Blob Storage
```

---

## Multiprocessing

Best for:

```text
Heavy CPU Work
```

Examples:

```python
Training Models

Image Processing

Data Science

Feature Engineering
```

---

# Async and the GIL

A very common interview question.

---

Many people think:

```text
GIL breaks Async.
```

Wrong.

---

The GIL affects:

```text
CPU-bound work
```

---

Async focuses on:

```text
Waiting work
```

---

Most GenAI systems are:

```text
I/O Bound
```

so Async works extremely well.

---

# Async in FastAPI

Instead of:

```python
@app.post("/chat")
def chat():
```

Use:

```python
@app.post("/chat")
async def chat():
```

---

Why?

Because:

```text
FastAPI handles many waiting requests efficiently.
```

---

# Async in LangChain

Synchronous:

```python
response = llm.invoke(prompt)
```

---

Async:

```python
response = await llm.ainvoke(prompt)
```

---

# Async in Retrieval

Synchronous:

```python
docs = retriever.retrieve(query)
```

---

Async:

```python
docs = await retriever.aretrieve(query)
```

---

# Async in LangGraph

Nodes can be asynchronous.

Example:

```python
async def retrieve_documents(state):

    docs = await retriever.aretrieve(
        state["question"]
    )

    return {
        "docs": docs
    }
```

---

Useful for:

```text
Tool Calls

Retrievers

Database Queries

API Requests
```

---

# Async in MCP

MCP servers frequently expose:

```python
async def tool():
```

because tools often call:

```text
Databases

LLMs

External APIs
```

---

# Interview Questions

---

## What Is Async Programming?

**Answer**

Async programming is a concurrency model that allows a program to perform other work while waiting for long-running I/O operations.

---

## What Is A Coroutine?

**Answer**

A coroutine is a function defined with `async def` that can pause and resume execution.

---

## What Does await Do?

**Answer**

`await` pauses the current coroutine while allowing other coroutines to execute.

---

## What Is The Event Loop?

**Answer**

The Event Loop schedules, executes, pauses, and resumes asynchronous tasks.

---

## Why Does FastAPI Use Async?

**Answer**

Because web applications spend significant time waiting on I/O operations such as databases, APIs, search systems, and LLMs.

---

## What Does asyncio.gather() Do?

**Answer**

Runs multiple coroutines concurrently and waits for all of them to complete.

---

## Async vs Threading?

**Answer**

Threading uses multiple threads. Async uses a single thread and an event loop. Async is typically more resource-efficient for large numbers of I/O tasks.

---

## Async vs Multiprocessing?

**Answer**

Async is ideal for I/O-bound workloads while multiprocessing is ideal for CPU-bound workloads.

---

## Why Is Async Important For AI Systems?

**Answer**

Because AI systems spend most of their time waiting on external services such as LLM APIs, vector databases, search engines, storage systems, and web services.

---

# Production Best Practices

✅ Use Async for all I/O-heavy operations

✅ Use asyncio.gather() for independent calls

✅ Avoid blocking operations inside async functions

✅ Use async database clients

✅ Use async HTTP clients

✅ Use async SDKs whenever available

✅ Keep CPU-heavy work out of async endpoints

✅ Offload CPU-heavy work to separate processes

---

# Mental Models

---

## Coroutine

```text
Pause
 ↓
Resume
 ↓
Pause
 ↓
Resume
```

---

## Event Loop

```text
Task A waiting

↓

Run Task B

↓

Run Task C

↓

Resume Task A
```

---

## Async

```text
One Smart Waiter
```

---

## Threading

```text
Many Waiters
```

---

## Multiprocessing

```text
Many Restaurants
```

---

## AI Engineering Decision Tree

Need:

```text
OpenAI
Search
SQL
Storage
APIs
```

↓

```text
Async
```

Need:

```text
Training
Image Processing
Heavy Compute
```

↓

```text
Multiprocessing
```

---

# Key Takeaways

✅ Async solves waiting problems.

✅ async def creates coroutines.

✅ await pauses without blocking.

✅ The Event Loop schedules coroutines.

✅ asyncio.gather() enables concurrent execution.

✅ Async is ideal for modern GenAI systems.

✅ FastAPI heavily relies on Async.

✅ LangChain and LangGraph support Async operations.

✅ MCP tools are frequently asynchronous.

✅ Async is one of the highest ROI topics for Agentic AI interviews.
