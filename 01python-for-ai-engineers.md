# Python for AI Engineering

> First topic in the Agentic AI Developer Roadmap.
>
> Goal: Learn the Python concepts that directly power FastAPI, LangChain, LangGraph, MCP Servers, RAG systems, evaluation frameworks, and production AI applications.

---

# PART 1: THEORY

## Why Python Dominates GenAI

Nearly every major GenAI framework is Python-first:

- LangChain
- LangGraph
- FastAPI
- FastMCP
- OpenAI SDK
- Azure OpenAI SDK
- LlamaIndex
- CrewAI
- AutoGen
- DSPy
- Haystack

### Why?

```text
Research
↓
Machine Learning
↓
LLMs
↓
Agent Frameworks
↓
Python
```

As an Agentic AI Developer, Python is not just a programming language.

It becomes the language used to build:

- Tools
- Agents
- RAG Pipelines
- APIs
- MCP Servers
- Evaluation Frameworks
- Monitoring Integrations

---

## Everything in Python is an Object

Example:

```python
x = 5
name = "Pulkit"

print(type(x))
print(type(name))
```

Output:

```python
<class 'int'>
<class 'str'>
```

### Interview Answer

**Q: What is Object-Oriented Programming (OOP)?**

> OOP is a programming paradigm where data and behavior are bundled together inside objects. Python treats nearly everything as an object, enabling encapsulation, inheritance, polymorphism, and abstraction.

---

# Variables

```python
user_name = "Pulkit"
age = 30
is_active = True
```

### Interview Answer

**Q: Is Python statically typed or dynamically typed?**

> Python is dynamically typed. Variable types are determined at runtime rather than compile time.

---

# Mutable vs Immutable

One of the most common Python interview topics.

---

## Mutable Objects

Can be modified after creation.

```python
my_list = [1, 2, 3]

my_list.append(4)
```

Output:

```python
[1, 2, 3, 4]
```

Examples:

```python
list
dict
set
```

---

## Immutable Objects

Cannot be modified after creation.

```python
name = "Pulkit"

name[0] = "A"
```

Produces:

```python
TypeError
```

Examples:

```python
str
int
float
tuple
bool
```

---

### Interview Answer

**Q: Difference between List and Tuple?**

| List | Tuple |
|--------|--------|
| Mutable | Immutable |
| Uses [] | Uses () |
| Slightly slower | Slightly faster |
| Can be modified | Cannot be modified |

Example:

```python
my_list = [1, 2]
my_tuple = (1, 2)
```

---

# Functions

Functions are the foundation of Agentic AI.

Basic syntax:

```python
def greet(name):
    return f"Hello {name}"
```

Usage:

```python
result = greet("Pulkit")
```

Output:

```python
Hello Pulkit
```

---

## Why Functions Matter in LangGraph

A LangGraph node is often just a Python function.

Example:

```python
def classify_question(state):
    return state
```

Used as:

```python
builder.add_node(
    "classifier",
    classify_question
)
```

If you are comfortable with Python functions, LangGraph becomes significantly easier.

---

# Type Hints

Extremely important for modern Python and AI engineering.

Example:

```python
def add(a: int, b: int) -> int:
    return a + b
```

Meaning:

```text
a = int
b = int
returns int
```

---

## Why Type Hints Matter

Without Type Hints:

```python
def process(data):
    ...
```

Hard to understand.

With Type Hints:

```python
def process(data: list[str]) -> dict:
    ...
```

Self-documenting and editor-friendly.

---

### Interview Answer

**Q: Are Type Hints enforced at runtime?**

> No. Type hints improve readability, IDE support, documentation, and static analysis. Python does not enforce them by default.

---

# Collections

Collections are used everywhere in AI systems.

---

## List

```python
countries = [
    "India",
    "Kenya",
    "Nigeria"
]
```

Access:

```python
countries[0]
```

Output:

```python
India
```

---

## Dictionary

The most important data structure in AI systems.

```python
user = {
    "name": "Pulkit",
    "role": "Consultant"
}
```

Access:

```python
user["name"]
```

Output:

```python
Pulkit
```

---

### Why Dictionaries Matter

LLM responses often look like:

```python
{
    "answer": "...",
    "sources": [...]
}
```

Agent state often looks like:

```python
{
    "question": "...",
    "answer": "...",
    "route": "rag"
}
```

---

# Loops

Example:

```python
countries = ["India", "Kenya", "Nigeria"]

for country in countries:
    print(country)
```

Output:

```python
India
Kenya
Nigeria
```

---

### Interview Answer

**Q: Difference between for and while loops?**

#### For Loop

```python
for item in collection:
    ...
```

Used when iterating over a collection.

#### While Loop

```python
while condition:
    ...
```

Used until a condition becomes False.

---

# List Comprehension

Very common in AI codebases.

Instead of:

```python
squares = []

for x in range(5):
    squares.append(x*x)
```

Use:

```python
squares = [x*x for x in range(5)]
```

Output:

```python
[0,1,4,9,16]
```

---

### Interview Answer

**Q: Why use List Comprehensions?**

> They are concise, readable, and often faster than equivalent loops.

---

# Exception Handling

Critical in production AI systems.

Without exception handling:

```python
result = 10 / 0
```

Application crashes.

Correct approach:

```python
try:
    result = 10 / 0

except ZeroDivisionError:
    print("Division by zero")
```

Output:

```python
Division by zero
```

---

## AI Example

```python
try:
    response = llm.invoke(...)
except Exception as e:
    logger.error(e)
```

Tool call example:

```python
try:
    result = sql_tool(...)
except Exception:
    ...
```

---

### Interview Answer

**Q: Difference between Exception and Error?**

> Exceptions are runtime issues that can often be handled gracefully. Errors usually represent more serious failures that should not normally occur.

---

# Classes

Classes are everywhere in modern AI frameworks.

Example:

```python
class Employee:

    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"My name is {self.name}"
```

Usage:

```python
emp = Employee("Pulkit")

print(emp.introduce())
```

Output:

```python
My name is Pulkit
```

---

# Why Classes Matter

FastAPI:

```python
class UserRequest(BaseModel):
    ...
```

LangChain:

```python
class CustomRetriever:
    ...
```

Tools:

```python
class SearchTool:
    ...
```

Agents:

```python
class MyAgent:
    ...
```

---

# Dataclasses

Frequently used in Agentic AI systems.

Traditional approach:

```python
class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Dataclass approach:

```python
from dataclasses import dataclass


@dataclass
class User:
    name: str
    age: int
```

Cleaner and more maintainable.

---

# TypedDict

One of the most important concepts for LangGraph.

Example:

```python
from typing import TypedDict


class AgentState(TypedDict):
    question: str
    answer: str
```

State example:

```python
state = {
    "question": "What is RAG?",
    "answer": ""
}
```

### Why TypedDict Matters

LangGraph commonly uses TypedDict-based state definitions.

Benefits:

- Type safety
- Better IDE support
- Clear state contracts
- Easier debugging

---

# PART 2: CODE EXERCISES

## Exercise 1

Create a function:

```python
def classify_question(question):
```

Rules:

```text
contains "count" → SQL
contains "policy" → RAG
otherwise → CLARIFICATION
```

Expected:

```python
classify_question(
    "What is the audit policy?"
)
```

Output:

```python
RAG
```

---

## Exercise 2

Create AgentState

```python
from typing import TypedDict


class AgentState(TypedDict):
    question: str
    route: str
    answer: str
```

Create sample state:

```python
state = {
    "question": "How many audit reports exist?",
    "route": "sql",
    "answer": ""
}
```

---

## Exercise 3

Create an Employee Dataclass

```python
from dataclasses import dataclass


@dataclass
class Employee:
    name: str
    role: str
    department: str
```

Instantiate:

```python
emp = Employee(
    name="Pulkit",
    role="Consultant",
    department="AI Engineering"
)

print(emp)
```

---

# PART 3: INTERVIEW QUESTIONS

## Easy

### Q1

Difference between List and Tuple?

### Q2

Difference between Mutable and Immutable?

### Q3

What is a Dictionary?

### Q4

What is a Function?

### Q5

What is a Class?

---

## Medium

### Q6

What are Type Hints?

### Q7

What is a Dataclass?

### Q8

What is TypedDict?

### Q9

Why is TypedDict useful in LangGraph?

### Q10

What is Exception Handling?

---

## Advanced

### Q11

Difference between Dataclass and Pydantic BaseModel?

### Q12

When would you use TypedDict instead of a Dataclass?

### Q13

Why do modern AI frameworks heavily use Type Hints?

### Q14

How would you model Agent State?

### Q15

How would you structure Python code for a production AI system?

---

# PART 4: SYSTEM DESIGN QUESTIONS

## Design Question 1

You are building a multi-agent system.

How would you represent:

```text
Question
Route
Retrieved Documents
Final Answer
Sources
```

Expected Answer:

Use:

```python
TypedDict
```

or

```python
Pydantic Model
```

to define strongly typed state.

---

## Design Question 2

You need 10 tools.

Would you create:

```python
10 giant functions
```

or

```python
10 separate reusable modules/classes
```

Expected Answer:

Create separate reusable modules.

Benefits:

- Maintainability
- Scalability
- Easier testing
- Better organization

---

# PART 5: PRODUCTION BEST PRACTICES

## Always Use Type Hints

Good:

```python
def retrieve_docs(
    question: str
) -> list[str]:
    ...
```

Avoid:

```python
def retrieve_docs(question):
    ...
```

---

## Always Log

```python
logger.info("Retrieval started")
```

```python
logger.error(error)
```

---

## Never Do This

```python
except:
    pass
```

This hides issues and makes debugging difficult.

---

## Prefer Structured Models

Use:

```python
TypedDict
```

```python
Dataclass
```

```python
Pydantic Models
```

instead of large untyped dictionaries whenever possible.

---

## Organize Projects

Example:

```text
app/
├── api/
├── services/
├── agents/
├── tools/
├── models/
├── tests/
```

---

# Mental Model

Think of Python in Agentic AI like this:

```text
Functions
    ↓
Tools
    ↓
Nodes
    ↓
Agents
    ↓
Multi-Agent Systems
```

Master:

1. Functions
2. Classes
3. Type Hints
4. Dataclasses
5. TypedDict

and learning FastAPI, LangChain, LangGraph, MCP, and RAG becomes dramatically easier.

---

# Key Takeaways

✅ Python is the foundation of Agentic AI.

✅ Functions become tools and LangGraph nodes.

✅ Dictionaries and TypedDict power agent state.

✅ Type Hints improve readability and maintainability.

✅ Classes and Dataclasses simplify complex systems.

✅ Exception Handling is essential for production AI.

✅ Structured code is easier to scale, test, and debug.

---

# Python for AI Engineering: Interview Answers and Data Modeling Concepts

> This note answers the interview questions from Part 1 of Python for AI Engineering.
>
> Special focus:
>
> - Normal Classes
> - Dataclasses
> - TypedDict
> - Pydantic Models
> - Why they matter in FastAPI, LangChain, LangGraph, RAG, MCP, and Agentic AI systems

---

# 1. Easy Interview Questions

---

## Q1. Difference between List and Tuple?

A **list** and a **tuple** are both used to store multiple values in Python, but the key difference is mutability.

| Feature | List | Tuple |
|---|---|---|
| Mutability | Mutable | Immutable |
| Syntax | `[]` | `()` |
| Can modify values? | Yes | No |
| Used for | Dynamic collections | Fixed collections |
| Example | `[1, 2, 3]` | `(1, 2, 3)` |

### Example

```python
numbers = [1, 2, 3]
numbers.append(4)

print(numbers)
```

Output:

```python
[1, 2, 3, 4]
```

Tuple example:

```python
coordinates = (10, 20)

coordinates[0] = 15
```

This will produce an error because tuples are immutable.

### Interview Answer

> A list is mutable, meaning its values can be changed after creation. A tuple is immutable, meaning its values cannot be changed after creation. Lists are useful when data needs to change, while tuples are useful for fixed data.

---

## Q2. Difference between Mutable and Immutable?

A **mutable object** can be changed after it is created.

An **immutable object** cannot be changed after it is created.

### Mutable Examples

```python
list
dict
set
```

Example:

```python
items = ["a", "b"]
items.append("c")

print(items)
```

Output:

```python
["a", "b", "c"]
```

### Immutable Examples

```python
str
int
float
tuple
bool
```

Example:

```python
name = "Pulkit"
name[0] = "A"
```

This gives an error because strings are immutable.

### Interview Answer

> Mutable objects can be modified after creation, such as lists and dictionaries. Immutable objects cannot be modified after creation, such as strings, integers, and tuples.

---

## Q3. What is a Dictionary?

A dictionary is a key-value data structure.

It stores data in this format:

```python
{
    "key": "value"
}
```

### Example

```python
user = {
    "name": "Pulkit",
    "role": "Consultant",
    "department": "AI Engineering"
}

print(user["name"])
```

Output:

```python
Pulkit
```

### Why Dictionaries Matter in AI Engineering

Most AI systems pass data as dictionaries.

Example LLM response:

```python
{
    "answer": "RAG means Retrieval-Augmented Generation.",
    "sources": ["document1.pdf", "document2.pdf"]
}
```

Example agent state:

```python
{
    "question": "What is RAG?",
    "route": "rag",
    "answer": ""
}
```

### Interview Answer

> A dictionary is a key-value data structure in Python. It is commonly used to represent structured data, configuration, JSON-like payloads, API responses, and agent state.

---

## Q4. What is a Function?

A function is a reusable block of code that performs a specific task.

### Example

```python
def greet(name):
    return f"Hello {name}"
```

Usage:

```python
message = greet("Pulkit")
print(message)
```

Output:

```python
Hello Pulkit
```

### Why Functions Matter in Agentic AI

In LangGraph, a node is often just a Python function.

Example:

```python
def classify_question(state):
    return state
```

This can later become:

```python
builder.add_node("classifier", classify_question)
```

### Interview Answer

> A function is a reusable block of code that accepts inputs, performs logic, and optionally returns output. In AI systems, functions are often used as tools, graph nodes, validators, retrievers, and service methods.

---

## Q5. What is a Class?

A class is a blueprint for creating objects.

It bundles data and behavior together.

### Example

```python
class Employee:

    def __init__(self, name, role):
        self.name = name
        self.role = role

    def introduce(self):
        return f"My name is {self.name} and I work as a {self.role}"
```

Usage:

```python
emp = Employee("Pulkit", "Consultant")
print(emp.introduce())
```

Output:

```python
My name is Pulkit and I work as a Consultant
```

### Interview Answer

> A class is a blueprint for creating objects. It combines attributes and methods into a single structure. Classes are useful when we need to model real-world entities or reusable components.

---

# 2. Medium Interview Questions

---

## Q6. What are Type Hints?

Type hints are annotations that describe the expected type of variables, function parameters, and return values.

### Example

```python
def add(a: int, b: int) -> int:
    return a + b
```

This means:

```text
a should be an integer
b should be an integer
return value should be an integer
```

### Are Type Hints Enforced at Runtime?

No.

Python does not enforce type hints by default.

Example:

```python
def add(a: int, b: int) -> int:
    return a + b

print(add("hello", "world"))
```

This still works and returns:

```python
helloworld
```

### Why Type Hints Matter

They improve:

- Readability
- IDE autocomplete
- Static analysis
- Documentation
- Code maintainability
- Team collaboration

### Interview Answer

> Type hints describe the expected types of variables, function inputs, and outputs. They are not enforced by Python at runtime by default, but they improve readability, editor support, documentation, and static checking.

---

## Q7. What is a Dataclass?

A dataclass is a special Python class designed mainly to store data.

It reduces boilerplate code by automatically generating methods like:

```python
__init__
__repr__
__eq__
```

### Normal Class

```python
class User:

    def __init__(self, id, name, role):
        self.id = id
        self.name = name
        self.role = role

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, role={self.role})"
```

### Dataclass Version

```python
from dataclasses import dataclass


@dataclass
class User:
    id: int
    name: str
    role: str
```

Usage:

```python
user = User(
    id=1,
    name="Pulkit",
    role="Consultant"
)

print(user)
```

Output:

```python
User(id=1, name='Pulkit', role='Consultant')
```

### Important Point

Standard Python dataclasses do **not** perform runtime validation by default. They mainly reduce class boilerplate and are useful for internal trusted data structures. Pydantic documentation also notes that Pydantic dataclasses add validation to standard dataclass-style usage, but they are not a full replacement for Pydantic `BaseModel`. 【1-8aa09f】

### Interview Answer

> A dataclass is a Python class optimized for storing data. It automatically generates boilerplate methods like `__init__`, `__repr__`, and `__eq__`. It is useful for internal application data where we want clean structured objects without writing a lot of class boilerplate.

---

## Q8. What is TypedDict?

`TypedDict` allows us to define the expected structure of a dictionary.

It is useful when the data is still a dictionary, but we want type hints for its keys and values.

### Example

```python
from typing import TypedDict


class AgentState(TypedDict):
    question: str
    route: str
    answer: str
```

Usage:

```python
state: AgentState = {
    "question": "What is RAG?",
    "route": "rag",
    "answer": ""
}
```

### Important Point

`TypedDict` does not create a new object type like a normal class or dataclass.

At runtime, the data is still just a normal dictionary.

Its main benefit is static typing and readability.

### Interview Answer

> TypedDict is used to define the expected structure of a dictionary. It helps type checkers and IDEs understand what keys and value types a dictionary should have. It is commonly used for structured dictionary state, especially in LangGraph.

---

## Q9. Why is TypedDict useful in LangGraph?

LangGraph workflows maintain a shared state.

That state is often represented as a dictionary.

Example:

```python
{
    "question": "...",
    "route": "...",
    "answer": "...",
    "sources": [...]
}
```

Using `TypedDict`, we can define that state clearly.

### Example

```python
from typing import TypedDict


class AgentState(TypedDict):
    question: str
    route: str
    retrieved_docs: list[str]
    answer: str
    sources: list[str]
```

Each LangGraph node receives and returns this state.

```python
def router_node(state: AgentState) -> AgentState:
    question = state["question"]

    if "count" in question.lower():
        route = "sql"
    else:
        route = "rag"

    return {
        **state,
        "route": route
    }
```

### Why This Helps

- Makes state structure explicit
- Reduces confusion between nodes
- Helps IDE autocomplete
- Makes graph easier to debug
- Makes interview explanations stronger

### Interview Answer

> TypedDict is useful in LangGraph because graph state is usually dictionary-based. TypedDict lets us define the expected keys and types of that state, making node inputs and outputs easier to understand, validate mentally, debug, and maintain.

---

## Q10. What is Exception Handling?

Exception handling allows the program to gracefully handle runtime errors instead of crashing.

### Example Without Exception Handling

```python
result = 10 / 0
```

This crashes with:

```python
ZeroDivisionError
```

### Example With Exception Handling

```python
try:
    result = 10 / 0

except ZeroDivisionError:
    print("Cannot divide by zero")
```

Output:

```python
Cannot divide by zero
```

### AI Engineering Example

```python
try:
    response = llm.invoke(prompt)

except Exception as e:
    logger.error(f"LLM call failed: {e}")
    response = "Sorry, I could not process the request."
```

### Interview Answer

> Exception handling is a way to handle runtime errors gracefully using `try`, `except`, `finally`, and `raise`. In production AI systems, it is important because LLM calls, API calls, database queries, vector searches, and tool calls can fail.

---

# 3. Advanced Interview Questions

---

## Q11. Difference between Dataclass and Pydantic BaseModel?

Both are used to model structured data, but they solve different problems.

| Feature | Dataclass | Pydantic BaseModel |
|---|---|---|
| Built into Python | Yes | No, third-party |
| Main purpose | Reduce boilerplate for data classes | Runtime validation and parsing |
| Runtime validation | No, not by default | Yes |
| Type coercion | No, not by default | Yes |
| JSON serialization | Manual or extra work | Built-in support |
| FastAPI integration | Limited | Excellent |
| Best for | Internal trusted data | External input, APIs, requests, responses |
| Performance | Lightweight | More overhead due to validation |

Pydantic documentation states that Pydantic dataclasses provide functionality similar to standard dataclasses with the addition of Pydantic validation, but they are not a replacement for Pydantic models. 【1-8aa09f】

### Dataclass Example

```python
from dataclasses import dataclass


@dataclass
class User:
    id: int
    name: str


user = User(id="123", name=456)

print(user)
```

Possible output:

```python
User(id='123', name=456)
```

The dataclass accepts the values as given. It does not automatically validate that `id` is really an integer or that `name` is really a string.

### Pydantic Example

```python
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str


user = User(id="123", name="Pulkit")

print(user)
```

Output:

```python
id=123 name='Pulkit'
```

Pydantic validates and can coerce compatible values.

### Interview Answer

> A dataclass is mainly for reducing boilerplate in simple data-holding classes. Pydantic BaseModel is for runtime validation, parsing, serialization, and API-boundary data modeling. I would use dataclasses for trusted internal state and Pydantic for external inputs such as FastAPI request and response models.

---

## Q12. When would you use TypedDict instead of a Dataclass?

Use `TypedDict` when the data is naturally a dictionary and should remain a dictionary.

Use `dataclass` when you want a real object with attributes.

### TypedDict Example

```python
from typing import TypedDict


class AgentState(TypedDict):
    question: str
    route: str
    answer: str


state: AgentState = {
    "question": "What is RAG?",
    "route": "rag",
    "answer": ""
}
```

Access:

```python
state["question"]
```

### Dataclass Example

```python
from dataclasses import dataclass


@dataclass
class AgentState:
    question: str
    route: str
    answer: str


state = AgentState(
    question="What is RAG?",
    route="rag",
    answer=""
)
```

Access:

```python
state.question
```

### When to Use TypedDict

Use `TypedDict` when:

- Your framework expects dictionaries
- You are working with JSON-like data
- You are modeling LangGraph state
- You do not need methods
- You want lightweight structure

### When to Use Dataclass

Use `dataclass` when:

- You want object-style access
- You are modeling internal domain objects
- You want auto-generated `__init__`, `__repr__`, and `__eq__`
- You may add simple methods later

### Interview Answer

> I would use TypedDict when the data should remain a dictionary, such as LangGraph state or JSON-like payloads. I would use a dataclass when I want an actual Python object for internal domain modeling.

---

## Q13. Why do modern AI frameworks heavily use Type Hints?

Modern AI frameworks use type hints because AI applications pass complex structured data between many components.

Example components:

```text
FastAPI route
↓
Pydantic request model
↓
LangGraph state
↓
LangChain tool
↓
Retriever
↓
LLM response
↓
Evaluator
```

Without type hints, it becomes difficult to know:

- What input a function expects
- What output a function returns
- What keys exist in state
- What a tool requires
- What a node modifies
- What response shape is expected

### Example Without Type Hints

```python
def retrieve(data):
    ...
```

Unclear.

### Example With Type Hints

```python
def retrieve(question: str, top_k: int) -> list[str]:
    ...
```

Clear.

### Interview Answer

> Modern AI frameworks use type hints because agentic systems pass structured data across chains, tools, graph nodes, retrievers, evaluators, and APIs. Type hints make contracts explicit, improve readability, reduce bugs, and help IDEs and static analyzers catch mistakes earlier.

---

## Q14. How would you model Agent State?

For LangGraph-style workflows, I would usually start with `TypedDict`.

### Example

```python
from typing import TypedDict, Literal


class AgentState(TypedDict):
    user_id: str
    session_id: str
    question: str
    route: Literal["rag", "sql", "clarify"]
    retrieved_docs: list[str]
    answer: str
    sources: list[str]
```

### Example State

```python
state: AgentState = {
    "user_id": "user_123",
    "session_id": "session_456",
    "question": "Summarize the audit findings",
    "route": "rag",
    "retrieved_docs": [],
    "answer": "",
    "sources": []
}
```

### Why TypedDict Here?

Because LangGraph state is usually dictionary-like.

Each node receives a dictionary and returns updates.

```python
def classify_node(state: AgentState) -> AgentState:
    question = state["question"]

    if "count" in question.lower():
        route = "sql"
    else:
        route = "rag"

    return {
        **state,
        "route": route
    }
```

### Interview Answer

> For a LangGraph agent, I would model agent state using TypedDict because the state is dictionary-based and passed between graph nodes. I would include fields such as user_id, session_id, question, route, retrieved_docs, answer, sources, and metadata. If the state enters the system from an API request, I would validate it first using Pydantic.

---

## Q15. How would you structure Python code for a production AI system?

A production AI system should be modular.

Example structure:

```text
app/
├── api/
│   ├── routes.py
│   └── dependencies.py
│
├── models/
│   ├── request_models.py
│   ├── response_models.py
│   └── state_models.py
│
├── agents/
│   ├── graph.py
│   ├── nodes.py
│   └── router.py
│
├── tools/
│   ├── sql_tool.py
│   ├── search_tool.py
│   └── mcp_tools.py
│
├── services/
│   ├── retrieval_service.py
│   ├── llm_service.py
│   └── evaluation_service.py
│
├── config/
│   └── settings.py
│
├── observability/
│   ├── logging.py
│   └── tracing.py
│
└── tests/
    ├── test_api.py
    ├── test_nodes.py
    └── test_tools.py
```

This aligns well with production chatbot architecture patterns in your KM 2.0 context, where the backend uses FastAPI, LangChain orchestration, Azure OpenAI, Azure AI Search, Cosmos DB, Azure SQL, Azure Blob Storage, and Application Insights for observability. 【2-f56d1a】

### Interview Answer

> I would structure a production AI system into separate layers: API routes, request and response models, services, tools, agents, configuration, observability, and tests. This keeps the code modular, testable, maintainable, and easier to scale.

---

# 4. Deep Dive: Normal Class vs Dataclass vs TypedDict vs Pydantic

This is extremely important for AI engineering interviews.

---

## 4.1 Normal Class

A normal class gives maximum flexibility.

### Example

```python
class User:

    def __init__(self, id, name, role):
        self.id = id
        self.name = name
        self.role = role

    def display_name(self):
        return f"{self.name} ({self.role})"
```

### Pros

- Very flexible
- Can contain methods
- Can enforce custom logic
- Can represent complex behavior

### Cons

- More boilerplate
- Must manually write `__init__`
- Must manually write `__repr__`
- Must manually write equality logic if needed
- No automatic validation

### Best For

Use normal classes when the object has both:

```text
Data + Behavior
```

Example:

```python
class SQLValidator:
    def validate(self, sql: str) -> bool:
        ...
```

---

## 4.2 Dataclass

A dataclass is best when the class mostly stores data.

### Example

```python
from dataclasses import dataclass


@dataclass
class User:
    id: int
    name: str
    role: str
```

Python automatically creates:

```python
__init__
__repr__
__eq__
```

### Equivalent Normal Class

```python
class User:

    def __init__(self, id: int, name: str, role: str):
        self.id = id
        self.name = name
        self.role = role

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, role={self.role})"

    def __eq__(self, other):
        return (
            self.id == other.id
            and self.name == other.name
            and self.role == other.role
        )
```

Dataclass saves us from writing this boilerplate.

### Important Limitation

Standard dataclasses do not validate types at runtime.

```python
from dataclasses import dataclass


@dataclass
class User:
    id: int
    name: str


user = User(id="not-an-int", name=123)

print(user)
```

This may still create the object.

### Best For

Use dataclasses for:

- Internal domain objects
- Trusted data
- Simple structured state
- Lightweight models
- Configuration-like objects
- Data passed inside services

### Example in AI Engineering

```python
from dataclasses import dataclass


@dataclass
class RetrievedDocument:
    content: str
    source: str
    score: float
```

---

## 4.3 TypedDict

`TypedDict` is not a real object model.

It is a way to describe the shape of a dictionary.

### Example

```python
from typing import TypedDict


class RetrievedDocument(TypedDict):
    content: str
    source: str
    score: float
```

Usage:

```python
doc: RetrievedDocument = {
    "content": "Some text",
    "source": "audit_report.pdf",
    "score": 0.91
}
```

Access:

```python
doc["content"]
```

### Important Difference

This is still just a dictionary at runtime.

```python
print(type(doc))
```

Output:

```python
<class 'dict'>
```

### Best For

Use `TypedDict` when:

- The data should remain a dictionary
- You work with JSON-like objects
- You work with LangGraph state
- You pass state between graph nodes
- You want type hints but not object conversion
- You do not need runtime validation

### Example in LangGraph

```python
from typing import TypedDict, Literal


class AgentState(TypedDict):
    question: str
    route: Literal["rag", "sql", "clarify"]
    answer: str
```

---

## 4.4 Pydantic BaseModel

Pydantic is used when you need validation.

This is especially important at system boundaries.

Examples of boundaries:

```text
HTTP request
JSON payload
API response
Environment config
Tool input
LLM structured output
External system data
```

### Example

```python
from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    user_id: str
    session_id: str
    question: str = Field(min_length=1)
```

Usage:

```python
request = ChatRequest(
    user_id="u1",
    session_id="s1",
    question="What is RAG?"
)
```

### Invalid Example

```python
request = ChatRequest(
    user_id="u1",
    session_id="s1",
    question=""
)
```

This fails because `question` must have at least one character.

### Why Pydantic Is Important in FastAPI

FastAPI heavily uses Pydantic models for request and response validation.

Example:

```python
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class ChatRequest(BaseModel):
    user_id: str
    question: str


class ChatResponse(BaseModel):
    answer: str
    route: str


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    return ChatResponse(
        answer="This is a response",
        route="rag"
    )
```

### Best For

Use Pydantic for:

- FastAPI request models
- FastAPI response models
- External data validation
- Config validation
- Tool argument schemas
- LLM structured outputs
- API boundary contracts

---

# 5. Comparison Table

| Concept | Normal Class | Dataclass | TypedDict | Pydantic BaseModel |
|---|---|---|---|---|
| Main purpose | Data + behavior | Lightweight data object | Typed dictionary shape | Runtime validation |
| Runtime object | Custom object | Custom object | Plain dict | Pydantic object |
| Runtime validation | Manual | No, not by default | No | Yes |
| Boilerplate | High | Low | Very low | Medium |
| Methods allowed | Yes | Yes | No | Yes |
| Attribute access | `obj.name` | `obj.name` | `dict["name"]` | `obj.name` |
| Best for | Complex behavior | Internal trusted data | Dict-based state | API boundaries |
| FastAPI use | Services | Internal models | Rare | Request/response models |
| LangGraph use | Less common | Possible | Very common | Boundary validation |
| LangChain tools | Tool classes | Internal tool data | Tool state | Tool input schema |
| Performance | Good | Very lightweight | Lightweight | More overhead |

---

# 6. Simple Mental Model

## Normal Class

Use when you need:

```text
Data + Behavior
```

Example:

```python
class SQLValidator:
    def validate(self, sql: str) -> bool:
        ...
```

---

## Dataclass

Use when you need:

```text
Clean object for internal trusted data
```

Example:

```python
@dataclass
class RetrievedChunk:
    text: str
    source: str
    score: float
```

---

## TypedDict

Use when you need:

```text
A dictionary with a known shape
```

Example:

```python
class AgentState(TypedDict):
    question: str
    route: str
    answer: str
```

---

## Pydantic

Use when you need:

```text
Validation of external or untrusted data
```

Example:

```python
class ChatRequest(BaseModel):
    user_id: str
    question: str
```

---

# 7. Boundary vs Internal Data

This is the best way to understand the difference.

## At the Boundary: Use Pydantic

Boundary means data enters your system.

Examples:

```text
User sends API request
LLM returns structured JSON
Tool receives arguments
Config loaded from environment
External API sends response
```

Use Pydantic:

```python
from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    user_id: str
    question: str = Field(min_length=1)
```

Why?

Because the data may be invalid.

---

## Inside the System: Use Dataclass

Once data is validated and trusted, use dataclasses for internal movement.

```python
from dataclasses import dataclass


@dataclass
class RetrievedChunk:
    text: str
    source: str
    score: float
```

---

## Graph State: Use TypedDict

When working with LangGraph, use TypedDict for graph state.

```python
from typing import TypedDict


class AgentState(TypedDict):
    question: str
    route: str
    answer: str
```

---

# 8. Practical AI Engineering Example

Imagine a user sends a question to your FastAPI backend.

## Step 1: Validate Request with Pydantic

```python
from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    user_id: str
    session_id: str
    question: str = Field(min_length=1)
```

---

## Step 2: Use TypedDict for LangGraph State

```python
from typing import TypedDict, Literal


class AgentState(TypedDict):
    user_id: str
    session_id: str
    question: str
    route: Literal["rag", "sql", "clarify"]
    answer: str
    sources: list[str]
```

---

## Step 3: Use Dataclass for Internal Retrieved Documents

```python
from dataclasses import dataclass


@dataclass
class RetrievedDocument:
    content: str
    source: str
    score: float
```

---

## Step 4: Return Response with Pydantic

```python
from pydantic import BaseModel


class ChatResponse(BaseModel):
    answer: str
    route: str
    sources: list[str]
```

---

# 9. Complete Mini Example

```python
from dataclasses import dataclass
from typing import TypedDict, Literal
from pydantic import BaseModel, Field


# 1. API boundary input
class ChatRequest(BaseModel):
    user_id: str
    session_id: str
    question: str = Field(min_length=1)


# 2. LangGraph-style state
class AgentState(TypedDict):
    user_id: str
    session_id: str
    question: str
    route: Literal["rag", "sql", "clarify"]
    answer: str
    sources: list[str]


# 3. Internal trusted object
@dataclass
class RetrievedDocument:
    content: str
    source: str
    score: float


# 4. API boundary output
class ChatResponse(BaseModel):
    answer: str
    route: str
    sources: list[str]


def classify_question(question: str) -> Literal["rag", "sql", "clarify"]:
    question_lower = question.lower()

    if any(word in question_lower for word in ["count", "total", "average"]):
        return "sql"

    if len(question.strip()) < 5:
        return "clarify"

    return "rag"


def build_initial_state(request: ChatRequest) -> AgentState:
    route = classify_question(request.question)

    return {
        "user_id": request.user_id,
        "session_id": request.session_id,
        "question": request.question,
        "route": route,
        "answer": "",
        "sources": []
    }


def mock_retrieve_documents(question: str) -> list[RetrievedDocument]:
    return [
        RetrievedDocument(
            content="RAG combines retrieval with generation.",
            source="rag_notes.md",
            score=0.91
        )
    ]


def answer_question(state: AgentState) -> AgentState:
    if state["route"] == "clarify":
        return {
            **state,
            "answer": "Could you please provide more detail?"
        }

    if state["route"] == "sql":
        return {
            **state,
            "answer": "This would be answered using a SQL tool."
        }

    docs = mock_retrieve_documents(state["question"])

    return {
        **state,
        "answer": docs[0].content,
        "sources": [doc.source for doc in docs]
    }


def create_response(state: AgentState) -> ChatResponse:
    return ChatResponse(
        answer=state["answer"],
        route=state["route"],
        sources=state["sources"]
    )


request = ChatRequest(
    user_id="u1",
    session_id="s1",
    question="What is RAG?"
)

state = build_initial_state(request)
state = answer_question(state)
response = create_response(state)

print(response)
```

---

# 10. Final Interview Summary

If asked:

## "Why not just use normal classes everywhere?"

Answer:

> Normal classes are flexible but require more boilerplate. For simple data containers, dataclasses are cleaner. For dictionary-shaped state, TypedDict is lighter. For external input validation, Pydantic is stronger. In production AI systems, I choose the modeling tool based on where the data is used.

---

## "When would you use Pydantic?"

Answer:

> I use Pydantic at system boundaries where data must be validated, such as FastAPI requests, API responses, tool inputs, configuration, and LLM structured outputs.

---

## "When would you use Dataclass?"

Answer:

> I use dataclasses for internal trusted data objects where I want clean object-style access without writing boilerplate constructors and repr methods.

---

## "When would you use TypedDict?"

Answer:

> I use TypedDict when the data should remain a dictionary but needs a clear structure, especially for LangGraph state and JSON-like intermediate data.

---

## "How do these apply to Agentic AI?"

Answer:

> In an agentic AI application, I may use Pydantic to validate the user request, TypedDict to define LangGraph state, dataclasses to represent retrieved documents or internal records, and Pydantic again to validate the final API response. This gives both flexibility and safety.

---

# 11. Key Takeaways

- Use **normal classes** when you need behavior and custom logic.
- Use **dataclasses** for clean internal data objects.
- Use **TypedDict** for dictionary-shaped state, especially LangGraph state.
- Use **Pydantic** for runtime validation, especially FastAPI request and response models.
- Dataclasses and TypedDict do not provide runtime validation by default.
- Pydantic is especially useful at trust boundaries.
- In production AI systems, these are not competing concepts. They are complementary tools.

---

# 12. Quick Decision Rule

```text
Is the data coming from outside the system?
    → Use Pydantic

Is the data internal, trusted, and object-like?
    → Use Dataclass

Is the data dictionary-shaped and should remain a dict?
    → Use TypedDict

Does the object need complex behavior and methods?
    → Use Normal Class
```

---

# 13. Best AI Engineering Pattern

```text
FastAPI Request
    ↓
Pydantic Model

LangGraph State
    ↓
TypedDict

Retrieved Documents / Internal Records
    ↓
Dataclass

FastAPI Response
    ↓
Pydantic Model
```

This is a clean and production-friendly pattern for GenAI and Agentic AI systems.
