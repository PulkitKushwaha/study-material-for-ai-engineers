# 02B-02C - Decorators, Generators & Iterators for AI Engineers

> One of the most important Python topics for FastAPI, LangChain, LangGraph, MCP, Streaming LLMs, and Agentic AI interviews.
>
> Goal:
>
> Understand how decorators work internally and why they appear everywhere in modern AI frameworks.
>
> Understand generators and iterators since they power streaming responses, token streaming, event streaming, and memory-efficient processing.

---

# Table of Contents

1. Why These Topics Matter in AI Engineering
2. Decorators
3. Higher Order Functions
4. Closures
5. Building Decorators from Scratch
6. Decorators with Arguments
7. Real AI Framework Examples
8. Generators
9. Iterators
10. Generator Expressions
11. Yield vs Return
12. Streaming LLM Responses
13. Interview Questions and Answers
14. Production Best Practices
15. Mental Models

---

# Why These Topics Matter in AI Engineering

If you see:

```python
@app.post("/chat")

@tool

@mcp.tool()

@retry

@traceable
```

Those are decorators.

---

If you see:

```python
yield token

yield chunk

yield event
```

Those are generators.

---

Whenever you stream:

```text
ChatGPT
Claude
Copilot
Gemini
```

under the hood you are often interacting with generators.

---

# PART 1: DECORATORS

---

# What is a Decorator?

## Simple Definition

A decorator is a function that modifies or extends another function without changing its source code.

Think:

```text
Original Function
       ↓

Decorator Adds Extra Behavior

       ↓

Enhanced Function
```

---

# Higher-Order Functions

Before decorators, understand this.

In Python:

```python
Functions are objects.
```

Meaning:

```python
def greet():
    print("Hello")
```

can be assigned:

```python
x = greet
```

and executed:

```python
x()
```

Output:

```python
Hello
```

---

# Functions Can Be Passed Around

```python
def greet():
    print("Hello")


def execute(func):
    func()


execute(greet)
```

Output:

```python
Hello
```

This concept enables decorators.

---

# First Decorator

## Step 1

Create normal function.

```python
def greet():
    print("Hello")
```

---

## Step 2

Create decorator.

```python
def log(func):

    def wrapper():

        print("Before")

        func()

        print("After")

    return wrapper
```

---

## Step 3

Apply decorator.

```python
@log
def greet():
    print("Hello")
```

---

Equivalent to:

```python
greet = log(greet)
```

---

Output:

```text
Before
Hello
After
```

---

# Visualizing Decorators

Without decorator:

```python
greet()
```

Output:

```text
Hello
```

---

With decorator:

```python
@log
def greet():
    print("Hello")
```

Output:

```text
Before
Hello
After
```

Decorator wraps function execution.

---

# Decorator With Arguments

Basic decorator fails for arguments.

Need:

```python
def log(func):

    def wrapper(*args, **kwargs):

        print("Before")

        result = func(*args, **kwargs)

        print("After")

        return result

    return wrapper
```

---

Usage:

```python
@log
def add(a, b):
    return a + b
```

Output:

```python
add(3, 5)
```

```text
Before
After
8
```

---

# Why *args and **kwargs?

Because we don't know:

```python
Function name

Number of parameters

Parameter types
```

ahead of time.

---

# Closures

Important interview concept.

A closure occurs when an inner function remembers variables from its outer function.

---

Example:

```python
def outer():

    message = "Hello"

    def inner():
        print(message)

    return inner
```

Usage:

```python
func = outer()

func()
```

Output:

```python
Hello
```

Even though:

```python
outer()
```

already finished.

---

# Why Decorators Use Closures

The wrapper function remembers:

```python
original function
```

through closure behavior.

---

# Decorators With Parameters

Very common interview question.

---

Example:

```python
def repeat(n):

    def decorator(func):

        def wrapper(*args, **kwargs):

            for _ in range(n):
                func(*args, **kwargs)

        return wrapper

    return decorator
```

Usage:

```python
@repeat(3)
def hello():
    print("Hello")
```

Output:

```text
Hello
Hello
Hello
```

---

# Real AI Examples

---

# FastAPI

```python
@app.post("/chat")
```

Meaning:

```text
Register this function
as POST endpoint
```

---

Code:

```python
@app.post("/chat")
async def chat():
    ...
```

---

# LangChain

```python
@tool
def search():
    ...
```

Turns a normal function into a LangChain tool.

---

# FastMCP

```python
@mcp.tool()
```

Turns a normal function into an MCP tool.

---

Example:

```python
@mcp.tool()
def get_weather(city):
    ...
```

---

# Retry Decorator

Very common production pattern.

```python
@retry
def call_llm():
    ...
```

Automatically retries failures.

---

# Logging Decorator

```python
@log_execution
def retrieve():
    ...
```

Useful for observability.

---

# Timing Decorator

```python
import time


def timer(func):

    def wrapper(*args, **kwargs):

        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print(end - start)

        return result

    return wrapper
```

---

# Decorator Interview Questions

---

## Q1. What is a Decorator?

**Answer**

A decorator is a higher-order function that wraps another function and modifies or extends its behavior without changing its source code.

---

## Q2. Why are Decorators Useful?

**Answer**

Decorators allow reusable functionality such as logging, authentication, retries, validation, metrics, and tracing without modifying business logic.

---

## Q3. What Enables Decorators?

**Answer**

Decorators rely on:

- Functions being first-class objects
- Closures
- Higher-order functions

---

## Q4. What Is a Closure?

**Answer**

A closure is a function that remembers variables from its outer scope even after the outer function has finished executing.

---

## Q5. Explain @tool in LangChain.

**Answer**

The `@tool` decorator converts a plain Python function into a LangChain-compatible tool that agents can invoke.

---

# PART 2: GENERATORS

---

# Problem with Normal Functions

Normal functions return everything at once.

Example:

```python
def get_numbers():

    return [1, 2, 3]
```

Output:

```python
[1, 2, 3]
```

Entire result stored in memory.

---

# What is a Generator?

A generator produces values lazily.

Instead of:

```python
return
```

we use:

```python
yield
```

---

Example:

```python
def get_numbers():

    yield 1
    yield 2
    yield 3
```

Usage:

```python
for n in get_numbers():
    print(n)
```

Output:

```text
1
2
3
```

---

# What Happens Internally?

Function pauses at:

```python
yield
```

and remembers its state.

---

Visualization:

```text
yield 1
pause

yield 2
pause

yield 3
pause
```

---

# Yield vs Return

| return | yield |
|----------|----------|
| Ends function | Pauses function |
| Returns once | Produces many values |
| Loads everything immediately | Lazy evaluation |
| Higher memory usage | Lower memory usage |

---

Example

```python
def normal():
    return [1,2,3]
```

---

Generator:

```python
def lazy():

    yield 1
    yield 2
    yield 3
```

---

# Large Dataset Example

Bad:

```python
rows = load_100_million_rows()
```

Huge memory consumption.

---

Better:

```python
def rows():

    for row in database:
        yield row
```

One row at a time.

---

# Infinite Generator

```python
def counter():

    n = 1

    while True:
        yield n

        n += 1
```

Usage:

```python
c = counter()

print(next(c))
print(next(c))
print(next(c))
```

Output:

```text
1
2
3
```

---

# Iterator

## Definition

An iterator is an object that implements:

```python
__iter__()

__next__()
```

---

Example:

```python
numbers = iter([1,2,3])

print(next(numbers))
print(next(numbers))
```

Output:

```text
1
2
```

---

# Generator vs Iterator

Most common interview question.

---

## Iterator

Manually implements:

```python
__iter__
__next__
```

---

## Generator

Automatically provides iterator behavior through:

```python
yield
```

---

### Interview Answer

> Every generator is an iterator, but not every iterator is a generator.

---

# Custom Iterator

Example:

```python
class Counter:

    def __init__(self):
        self.value = 0

    def __iter__(self):
        return self

    def __next__(self):

        self.value += 1

        if self.value > 5:
            raise StopIteration

        return self.value
```

Usage:

```python
for v in Counter():
    print(v)
```

Output:

```text
1
2
3
4
5
```

---

# Generator Expression

Similar to list comprehension.

List:

```python
squares = [x*x for x in range(1000)]
```

Loads all values.

---

Generator:

```python
squares = (x*x for x in range(1000))
```

Creates lazily.

---

# Streaming LLM Responses

Very important for AI inte*views.

---

Instead of:

```python
response = llm.invoke(prompt)
```
returning everything at once,

you can stream.

Example:

```python
for token in llm.stream(prompt):
   print(token)
```

Internally it b*haves similarly to:

```python
yield token
```

---

# FastAPI Stream*ng

```python
from fastapi.responses import StreamingResponse
```

---

Example

```python
def stream():
    yield "Hello"

    yield "World"
```

---

Used as:

```python
StreamingResponse*stream*))
```

---

**Generator Interview Questions

---

## Q1. What is a Generator?

**Answer**

A generator is a function that produces values lazily using the `yield` key*ord.

---

## Q2. Difference between yield and return?

**Answer**

`return` terminates a function and returns a value once.

`yield` pauses execution and produces values incrementally.

---

## Q3. Why use Generators?

**Answer**

Generators improve memory efficiency by producing values on demand instead of storing everything in memory.

---

## Q4. What is an Iterator?

**Answer**

An iterator is an object that supports the `__iter__()` and `__next__()` methods.

---

## Q5. Difference between Generator and Iterator?*
**Answer**

Every generator is an iterator, but generators automatically implement iterator behavior through `yield`.

---

## Q6. How do generators help AI applications?

**Answer**

Generators support:

- Streaming responses
- Token streaming
- Processing large datasets
- Efficient memory utilization

---

# P*oduction Best Practices

✅ Use decorators for:

- Authentication
- Logging
- Retry logic
- Metrics
- Tracing

✅ Use generators for:

- Streaming LLM outputs
- Large file processing
- Large database processing

✅ Prefer generator expressions over large lists when memory matters

✅ Keep decorators focused on a single responsibility

✅ Use `functools.wraps()` for production decorators

---

# Mental Models

---

# Decorator

```text
Function
    ↓
Decorator
    ↓
Enhanced Function
```

---

# Generator

```text
Data Source
    ↓
yield one item
    ↓
process
    ↓
yield next item
```

---

# Iterator

```text
next()
 ↓
next()
 ↓
next()
 ↓
StopIteration
```

---

# How This Connects to Agentic AI

```text
FastAPI
    ↓
@app.post()

LangChain
    ↓
@tool

FastMCP
    ↓
@mcp.tool()

Streaming LLM
    ↓
yield token

Streaming API
    ↓
StreamingResponse

Agent Events
    ↓
yield event
```

If OOP teaches you how AI frameworks are structured, decorators and generators teach you how those frameworks actually work under the hood.
