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

# Duck T***ng

Very common Python question.***--

## Example

```python
class ***k:

    def speak(self):
       ***turn "Quack"


class Person:

  ***ef speak(self):
        return "***lo"


def make_sound(obj):
    p***t(obj.speak())
```

Both work:

***python
make_sound(Duck())
make_s***d(Person())
```

---

## Intervi***Answer

> Python follows Duck Ty***g. If an object behaves like the***pected type and exposes the requ***d methods, Python allows it to b***sed regardless of inheritance hi***rchy.

---

# Magic Methods

Spe***l methods automatically understo***by Python.

---

## __init__

Co***ructor.

```python
class User:

*** def __init__(self, name):
     ***self.name = name
```

---

## __***__

Human-readable representatio***
```python
def __str__(self):
  ***eturn self.name
```

---

## __r***__

Developer-friendly represent***on.

```python
def __repr__(self***    return f"User({self.name})"
***

---

## __eq__

Equality compa***on.

```python
def __eq__(self, ***er):
    return self.name == oth***name
```

---

## Why Dataclasse***re Popular

Dataclasses automati***ly generate:

```python
__init__***repr__
__eq__
```

for us.

---
***Method Resolution Order (MRO)

D***nes how Python searches for meth***.

---

## Example

```python
cl*** A:
    pass


class B(A):
    p***


class C(B):
    pass
```

MRO***```text
C
↓
B
↓
A
↓
object
```

***ck:

```python
print(C.mro())
``***---

## Interview Answer

> MRO ***thod Resolution Order) defines t***order in which Python searches f***methods and attributes in inheri***ce hierarchies.

---

# Abstract***se Classes (ABC)

Used to enforc***ontracts.

---

## Example

```p***on
from abc import ABC
from abc ***ort abstractmethod


class Tool(***):

    @abstractmethod
    def ***cute(self):
        pass
```

--***Implementation:

```python
class***archTool(Tool):

    def execute***lf):
        return "Searching..***```

---

## Interview Answer

>***stract Base Classes define contr***s that subclasses must implement***nsuring consistency across imple***tations.

---

# super()

Allows***child class to invoke parent met***s.

---

## Example

```python
c***s Tool:

    def __init__(self):***      self.name = "Tool"


class***archTool(Tool):

    def __init_***elf):
        super().__init__()***      self.type = "Search"
```

***

## Interview Answer

> super()***lows a child class to access met***s and behavior from its parent c***s. It is commonly used to initia***e parent state before adding chi***specific logic.

---

# Dependen***Injection

Extremely important b***use FastAPI uses it heavily.

--***## Bad

```python
class Agent:

*** def __init__(self):
        sel***lm = AzureChatOpenAI()
```

Hard*** test.

---

## Better

```pytho***lass Agent:

    def __init__(se*** llm):
        self.llm = llm
``***Now we can inject:

```python
Re***LM
MockLLM
TestLLM
```

---

## ***erview Answer

> Dependency Inje***on means supplying dependencies ***m outside an object rather than ***ating them internally. This impr***s flexibility, maintainability, *** testing.

---

# OOP in AI Fram***rks

---

# FastAPI

```python
a***= FastAPI()
```

Class instantia***n.

---

# Pydantic

```python
c***s ChatRequest(BaseModel):
```

I***ritance.

---

# LangChain

```p***on
class CustomRetriever(BaseRet***ver):
```

Inheritance and abstr***ion.

---

# LangGraph

```pytho***raph = StateGraph(...)
```

Obje***oriented framework design.

---
***MCP

```python
mcp = FastMCP("Se***r")
```

Object instantiation.

***

# Interview Questions and Answ***

---

# Easy Questions

## Q1. ***t are the four pillars of OOP?

***nswer**

1. Encapsulation
2. Inh***tance
3. Polymorphism
4. Abstrac***n

---

## Q2. Difference betwee*** class and an object?

**Answer****A class is a blueprint or templa***

An object is an instance creat***from that blueprint.

Example:

***python
class User:
    pass

use*** User()
```

`User` is the class***`user` is the object.

---

## Q***What is encapsulation?

**Answer***
Encapsulation is bundling data *** behavior together while restric***g direct access to internal deta***.

---

## Q4. What is inheritan***

**Answer**

Inheritance allows***child class to inherit methods a***properties from a parent class f***code reuse and extensibility.

-***
## Q5. What is polymorphism?

****
