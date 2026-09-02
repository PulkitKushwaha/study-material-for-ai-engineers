# 02A - OOP Deep Dive for AI Engineers

> A practical OOP guide for GenAI, Agentic AI, LangChain, LangGraph, MCP, and FastAPI interviews.
>
> Goal:
>
> Understand not only OOP theory, but how OOP appears in modern AI systems and how to answer OOP interview questions confidently.

---

# Table of Contents

1. Why OOP Matters in AI Engineering
2. The Four Pillars of OOP
3. Composition vs Inheritance
4. Instance Variables vs Class Variables
5. Static Methods vs Class Methods
6. Magic Methods
7. Method Overriding
8. Method Overloading
9. Duck Typing
10. MRO (Method Resolution Order)
11. Abstract Base Classes
12. super()
13. Dependency Injection
14. OOP in FastAPI, LangChain, LangGraph and MCP
15. Interview Questions and Answers
16. Production Best Practices
17. OOP Mental Model for Agentic AI

---

# Why OOP Matters in AI Engineering

Modern AI frameworks are heavily object-oriented.

Examples:

```python
FastAPI()

AzureChatOpenAI()

StateGraph()

BaseModel()

FastMCP()
```

Every one of these creates an object.

Example:

```python
from fastapi import FastAPI

app = FastAPI()
```

Here:

```text
FastAPI = Class
app = Object
```

Understanding OOP makes it easier to understand:

- FastAPI
- LangChain
- LangGraph
- MCP
- Pydantic
- Azure SDKs

---

# The Four Pillars of OOP

The most common OOP interview question.

---

# 1. Encapsulation

## Definition

Encapsulation means:

> Bundling data and behavior together while restricting direct access to implementation details.

---

## Example

```python
class BankAccount:

    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
```

Usage:

```python
account = BankAccount()

account.deposit(100)

print(account.get_balance())
```

Output:

```python
100
```

---

## Why Encapsulation Matters

Users should interact with:

```python
agent.save_memory()
agent.retrieve_documents()
```

not manipulate internal state directly.

Good:

```python
agent.save_memory("important fact")
```

Bad:

```python
agent.internal_vector_store = None
```

---

## Interview Answer

> Encapsulation is the practice of bundling related data and behavior inside a class while restricting direct access to internal implementation details.

---

# 2. Inheritance

## Definition

Inheritance allows one class to reuse another class's functionality.

---

## Example

```python
class Tool:

    def run(self):
        pass


class SearchTool(Tool):

    def run(self):
        return "Searching..."
```

Structure:

```text
Tool
  ↓
SearchTool
```

---

## Why It Matters

Instead of building every tool from scratch:

```python
SearchTool
SQLTool
WeatherTool
EmailTool
```

all can inherit from:

```python
Tool
```

---

## AI Example

```python
class BaseRetriever:
    ...

class AzureSearchRetriever(BaseRetriever):
    ...
```

---

## Interview Answer

> Inheritance allows a child class to acquire properties and methods from a parent class, promoting code reuse and extensibility.

---

# 3. Polymorphism

## Definition

Different objects respond to the same interface differently.

---

## Example

```python
class Dog:

    def speak(self):
        return "Woof"


class Cat:

    def speak(self):
        return "Meow"
```

Usage:

```python
animals = [Dog(), Cat()]

for animal in animals:
    print(animal.speak())
```

Output:

```text
Woof
Meow
```

---

## AI Example

```python
retriever.retrieve()
```

Could be:

```python
AzureSearchRetriever
VectorRetriever
ElasticSearchRetriever
```

but the caller doesn't care.

---

## Interview Answer

> Polymorphism allows multiple classes to implement the same interface while providing different behaviors.

---

# 4. Abstraction

## Definition

Show what something does.

Hide how it does it.

---

## Example

You use:

```python
llm.invoke()
```

You don't need to know:

```text
HTTP requests
Inference infrastructure
Token generation
Retries
Connection pooling
```

---

## Example

```python
from abc import ABC
from abc import abstractmethod


class Retriever(ABC):

    @abstractmethod
    def retrieve(self):
        pass
```

Implementation:

```python
class AzureSearchRetriever(Retriever):

    def retrieve(self):
        return "Documents"
```

---

## Interview Answer

> Abstraction hides implementation details and exposes only essential functionality.

---

# Composition vs Inheritance

One of the most important senior-level questions.

---

# Inheritance

```python
class Engine:
    pass


class Car(Engine):
    pass
```

Meaning:

```text
Car IS AN Engine
```

Not logically correct.

---

# Composition

```python
class Engine:
    pass


class Car:

    def __init__(self):
        self.engine = Engine()
```

Meaning:

```text
Car HAS AN Engine
```

Correct.

---

# Interview Answer

> Use inheritance when there is a genuine "is-a" relationship. Use composition when there is a "has-a" relationship. Modern software architecture typically favors composition because it is more flexible and easier to maintain.

---

# Instance Variables vs Class Variables

---

## Instance Variables

Each object has its own copy.

```python
class Employee:

    def __init__(self, name):
        self.name = name
```

---

Example:

```python
e1 = Employee("Pulkit")
e2 = Employee("Mark")
```

Different values.

---

## Class Variables

Shared across all instances.

```python
class Employee:

    company = "The Global Fund"
```

Usage:

```python
print(Employee.company)
```

---

## Interview Answer

> Instance variables belong to individual objects, while class variables are shared across all instances of the class.

---

# Static Methods

## Definition

Methods that don't need:

```python
self
```

or

```python
cls
```

---

## Example

```python
class MathUtils:

    @staticmethod
    def add(a, b):
        return a + b
```

Usage:

```python
MathUtils.add(3, 5)
```

---

## Use Cases

- Utility functions
- Validators
- Converters
- Calculators

---

## Interview Answer

> A static method belongs to a class namespace but does not require access to either instance state or class state.

---

# Class Methods

## Definition

Methods that receive:

```python
cls
```

instead of:

```python
self
```

---

## Example

```python
class Employee:

    count = 0

    @classmethod
    def get_count(cls):
        return cls.count
```

Usage:

```python
Employee.get_count()
```

---

## Interview Answer

> A class method operates on class-level state and receives the class itself through the cls parameter.

---

# Method Overriding

## Definition

A child class provides its own implementation of a parent class method.

---

## Example

```python
class Retriever:

    def retrieve(self):
        return "Base Retrieval"


class AzureRetriever(Retriever):

    def retrieve(self):
        return "Azure Search Retrieval"
```

---

## Interview Answer

> Method overriding occurs when a child class replaces the implementation of a method inherited from a parent class.

---

# Method Overloading

## Does Python Support It?

Not in the same way as Java or C#.

---

Instead we use:

```python
default parameters

*args

**kwargs
```

---

Example

```python
def add(a, b=0):
    return a + b
```

---

## Interview Answer

> Python does not support true compile-time method overloading. Similar behavior is achieved using default arguments, *args, and **kwargs.

---

# Duck Typing

Very common Python question. 
---

## Example

```python
class Duck:

    def speak(self):
       return "Quack"


class Person:

  def speak(self):
        return "Hello"


def make_sound(obj):
    printt(obj.speak())
```

Both work:

```python
make_sound(Duck())
make_sound(Person())
```

---

## Interview Answer

> Python follows Duck Typing. If an object behaves like the expected type and exposes the required methods, Python allows it to be used regardless of inheritance hierarchy.

---

# Magic Methods

Special methods automatically understood by Python.

---

## __init__

Constructor.

```python
class User:
    def __init__(self, name):
        self.name = name
```

---

## __str__

Human-readable representation.

```python
def __str__(self):
    return self.name
```

---

## __repr__

Developer-friendly representation.

```python
def __repr__(self):
    return f"User({self.name})"
```

---

## __eq__

Equality comparison.

```python
def __eq__(self, other):
    return self.name == other.name
```

---

## Why Dataclasses are Popular

Dataclasses automatically generate:

```python
__init__
__repr__
__eq__
```

for us.

---

# Method Resolution Order (MRO)

Defines how Python searches for methods.

---

## Example

```python
class A:
    pass


class B(A):
    pass


class C(B):
    pass
```

MRO:

```text
C
↓
B
↓
A
↓
object
```

Check:

```python
print(C.mro())
```

---

## Interview Answer

> MRO (Method Resolution Order) defines the order in which Python searches for methods and attributes in inheritance hierarchies.

---

# Abstract Base Classes (ABC)

Used to enforce contracts.

---

## Example

```python
from abc import ABC
from abc import abstractmethod


class Tool(ABC):

    @abstractmethod
    def execute(self):
        pass
```

Implementation:

```python
class SearchTool(Tool):

    def execute(self):
        return "Searching..."
```

---

## Interview Answer

> Abstract Base Classes define contracts that subclasses must implement, ensuring consistency across implementations.

---

# super()

Allows a child class to invoke parent methods.

---

## Example

```python
class Tool:

    def __init__(self):
        self.name = "Tool"


class SearchTool(Tool):

    def __init__(self):
        super().__init__()
        self.type = "Search"
```

---

## Interview Answer

> super() allows a child class to access methods and behavior from its parent class. It is commonly used to initialize parent state before adding child-specific logic.

---

# Dependency Injection

Extremely important because FastAPI uses it heavily.

---

## Bad

```python
class Agent:

    def __init__(self):
        self.llm = AzureChatOpenAI()
```

Hard to test.

---

## Better

```python
class Agent:

    def __init__(self, llm):
        self.llm = llm
```

Now we can inject:

```python
RealLLM
MockLLM
TestLLM
```

---

## Interview Answer

> Dependency Injection means supplying dependencies from outside an object rather than creating them internally. This improves flexibility, maintainability, and testing.

---

# OOP in AI Frameworks

---

# FastAPI

```python
app = FastAPI()
```

Class instantiation.

---

# Pydantic

```python
class ChatRequest(BaseModel):
```

Inheritance.

---

# LangChain

```python
class CustomRetriever(BaseRetriever):
```

Inheritance and abstraction.

---

# LangGraph

```python
graph = StateGraph(...)
```

Object-oriented framework design.

---

# MCP

```python
mcp = FastMCP("Server")
```

Object instantiation.

---

# Interview Questions and Answers

---

# Easy Questions

## Q1. What are the four pillars of OOP?

### Answer

1. Encapsulation
2. Inheritance
3. Polymorphism
4. Abstraction

---

## Q2. Difference between a class and an object?

### Answer

A class is a blueprint or template.

An object is an instance created from that blueprint.

Example:

```python
class User:
    pass

user = User()
```

`User` is the class.

`user` is the object.

---

## Q3. What is encapsulation?

### Answer

Encapsulation is bundling data and behavior together while restricting direct access to internal implementation details.

---

## Q4. What is inheritance?

### Answer

Inheritance allows a child class to inherit methods and properties from a parent class for code reuse and extensibility.

---

## Q5. What is polymorphism?

### Answer

Polymorphism allows different classes to provide different implementations of the same interface or method while allowing callers to use a common interface.

Example:

```python
class AzureRetriever:
    def retrieve(self):
        return "Azure Search"


class VectorRetriever:
    def retrieve(self):
        return "Vector DB"


retrievers = [
    AzureRetriever(),
    VectorRetriever()
]

for r in retrievers:
    print(r.retrieve())
```

---

## Q6. What is abstraction?

### Answer

Abstraction hides implementation details and exposes only essential functionality to the user.

For example:

```python
llm.invoke("Hello")
```

The user does not need to know about:

- API calls
- Tokenization
- Retry logic
- Authentication
- Connection pooling

---

## Q7. Difference between composition and inheritance?

### Answer

Inheritance represents an "is-a" relationship.

Example:

```python
Dog is an Animal
```

Composition represents a "has-a" relationship.

Example:

```python
Car has an Engine
```

Modern software systems usually prefer composition because it is more flexible and easier to maintain.

---

## Q8. Difference between static methods and class methods?

### Answer

Static methods:

- Use `@staticmethod`
- Receive neither `self` nor `cls`
- Used for utility functions

Class methods:

- Use `@classmethod`
- Receive `cls`
- Operate on class-level state

---

## Q9. What is method overriding?

### Answer

Method overriding occurs when a child class provides its own implementation of a parent class method.

Example:

```python
class Tool:
    def execute(self):
        return "Base Execution"


class SearchTool(Tool):
    def execute(self):
        return "Search Execution"
```

---

## Q10. Does Python support method overloading?

### Answer

Not in the same way as Java or C#.

Python achieves similar behavior through:

```python
default arguments
*args
**kwargs
```

Example:

```python
def add(a, b=0):
    return a + b
```

---

## Q11. What is Duck Typing?

### Answer

If an object provides the required behavior, Python allows it to be used regardless of its actual type.

Example:

```python
class Duck:
    def speak(self):
        return "Quack"


class Person:
    def speak(self):
        return "Hello"


def make_sound(obj):
    print(obj.speak())
```
