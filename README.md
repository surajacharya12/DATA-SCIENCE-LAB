# DATA-SCIENCE-LAB

  #  lab 1
  # Code Examples in this Notebook

This document provides a summary of the Python code examples present in this Jupyter notebook.

## 1. List Concatenation

**Code:**
```python
A= [1,2,3,4,5]
B= [6,7,8,9,10]

print(A+B)
```
**Description:** This example demonstrates basic list concatenation in Python.

## 2. Dictionary Operations with `for` Loop

**Code:**
```python
my_dict = {}

my_dict['apple'] = 1
my_dict['banana'] = 2
my_dict['cherry'] = 3

print("Original dictionary:", my_dict)


print("\nIterating through dictionary items:")
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")
```
**Description:** This example shows how to create, populate, and iterate through a Python dictionary using a `for` loop.

## 3. Type Hinting and Function Definition

**Code:**
```python
from typing import List, Dict, Optional

def process_items(items: List[str], config: Dict[str, int]) -> Optional[str]:
    if not items:
        return None
    return f"Processed {len(items)} items with config {config}"
```
**Description:** This example illustrates function definition with type hints for clarity and readability, using `List`, `Dict`, and `Optional` from the `typing` module.

## 4. String Manipulation with `for` Loop

**Code:**
```python
new_word = ''
for char_code in range(ord('h'), ord('o') + 1):
    new_word += chr(char_code)
print("Built string:", new_word)

message = "Hello Python!"
print("\nCharacters in message:")
for char in message:
    print(char)
```
**Description:** This example demonstrates string manipulation using `for` loops, `range()`, `ord()`, and `chr()` to build a string and iterate through characters.

## 5. Simple Function Definition and Call

**Code:**
```python
def add_two_numbers(num1, num2):
    "This function adds two numbers and returns their sum."
    sum_result = num1 + num2
    return sum_result

result1 = add_two_numbers(5, 3)
print("Sum of 5 and 3:", result1)

result2 = add_two_numbers(10, 20)
print("Sum of 10 and 20:", result2)
```
**Description:** A basic example of defining a function that takes two arguments, performs an operation, and returns a value, followed by multiple calls to the function.

## 6. Function Using `range` and a `for` Loop to Generate a Sequence

**Code:**
```python
def generate_sequence(start, end):
    """Generates a list of numbers from start (inclusive) to end (exclusive)."""
    numbers = []
    for i in range(start, end):
        numbers.append(i)
    return numbers


sequence1 = generate_sequence(1, 6)
print("Sequence from 1 to 5:", sequence1)

sequence2 = generate_sequence(0, 3)
print("Sequence from 0 to 2:", sequence2)
```
**Description:** This function uses `range()` and a `for` loop to generate a list of sequential numbers.

## 7. Using a `lambda` Function

**Code:**
```python
doubler = lambda x: x * 2

print("Double of 5:", doubler(5))
print("Double of 10:", doubler(10))


numbers = [1, 2, 3, 4, 5]
doubled_numbers = list(map(lambda x: x * 2, numbers))
print("Original numbers:", numbers)
print("Doubled numbers (using map and lambda):", doubled_numbers)
```
**Description:** This example showcases the use of `lambda` functions for simple, anonymous function definitions, including its application with `map()`.

## 8. Generating Numbers with a `while` Loop

**Code:**
```python
def process_numbers_normal(limit):
    "Generates a list of numbers from 0 up to (but not including) the limit using a while loop."
    results = []
    i = 0
    while i < limit:
        results.append(i)
        i += 1
    return results


print("Normal function output:", process_numbers_normal(5))
```
**Description:** A function demonstrating how to generate a sequence of numbers using a `while` loop.

## 9. Generating Numbers with `range` and a `for` Loop

**Code:**
```python
def process_numbers_range_loop(limit):
    "Generates numbers using range() and a for loop."
    results = []
    for i in range(limit):
        results.append(i)
    return results


print("Range and loop function output:", process_numbers_range_loop(5))
```
**Description:** Another method for generating a sequence of numbers, this time utilizing `range()` within a `for` loop.

## 10. Generating Numbers Incorporating a `lambda` Function with `map`

**Code:**
```python
def process_numbers_lambda(limit):
    "Generates numbers using lambda and map()."

    return list(map(lambda x: x, range(limit)))


print("Lambda function output:", process_numbers_lambda(5))
```
**Description:** This example combines `lambda` and `map()` with `range()` to generate a list of numbers concisely.

## 11. Area of a Circle Calculator

**Code:**
```python
import math

def area_of_circle(radius):
    "Calculates the area of a circle given its radius."
    return math.pi * (radius ** 2)

radius_input = input("Enter the radius of the circle: ")
radius = float(radius_input)
area = area_of_circle(radius)
print(f"The area of a circle with radius {radius} is: {area:.2f}")
```
**Description:** A function to calculate the area of a circle, prompting the user for the radius and displaying the formatted result.


# DATA-SCIENCE-LAB

## Lab 2: Iterators, Generators, and Decorators (Python)

This document contains **Lab 2** of the Data Science Lab. The lab is focused on understanding advanced Python concepts that help write efficient, clean, and reusable code: **Iterators, Generators, and Decorators**.

---

## 🎯 Lab Objectives

* Understand the concept of iterators and how iteration works in Python
* Learn how generators simplify iterator creation and improve memory efficiency
* Understand decorators and how they modify function behavior
* Identify the role of `for` loops in iteration

---

## 1️⃣ Iterator

### Definition

An **iterator** is an object that allows traversal through all the elements of a collection (such as a list) one by one. It follows the **Iterator Protocol**, which consists of two methods:

* `__iter__()`
* `__next__()`

### Syntax Example

```python
my_list = [1, 2, 3]
it = iter(my_list)   # Get iterator
print(next(it))      # Get next element
print(next(it))
print(next(it))
```

---

## 2️⃣ Generator

### Definition

A **generator** is a simpler and cleaner way to create iterators using a function. Instead of `return`, it uses the `yield` keyword. Generators generate values **on the fly**, making them memory-efficient.

### Syntax Example

```python
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()

for value in gen:
    print(value)
```

---

## 3️⃣ Decorator

### Definition

A **decorator** is a function that takes another function as input and extends its behavior without modifying the original function. It works as a **wrapper** around the function.

### Syntax Example

```python
def my_decorator(func):
    def wrapper():
        print("Before the function")
        func()
        print("After the function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

---

## 4️⃣ Is a `for` Loop an Iterator?

**No.** A `for` loop is a control flow statement, not an iterator itself.

However, a `for` loop internally uses an iterator. When you write:

```python
for item in my_list:
    print(item)
```

Python automatically calls:

* `iter(my_list)`
* `next()` repeatedly until items are exhausted

---

## 5️⃣ Iterator vs Generator Comparison

| Feature          | Iterator                                      | Generator                  |
| ---------------- | --------------------------------------------- | -------------------------- |
| Implementation   | Uses class with `__iter__()` and `__next__()` | Uses function with `yield` |
| Code Complexity  | More code                                     | Less and cleaner code      |
| State Management | Manual                                        | Automatic                  |
| Memory Usage     | Higher                                        | Memory-efficient           |

---

## 6️⃣ Combined Example: Decorator with Generator

This example demonstrates how **decorators and generators** can be used together in a real-world scenario.

```python
def log_status(func):
    def wrapper(*args, **kwargs):
        print(f"--- Starting {func.__name__} ---")
        result = func(*args, **kwargs)
        print(f"--- Finished {func.__name__} ---")
        return result
    return wrapper

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

@log_status
def get_passing_students(students):
    for student in students:
        if student.score >= 50:
            yield student.name

classroom = [
    Student("Ram", 90),
    Student("Shyam", 40),
    Student("Hari", 75)
]

for name in get_passing_students(classroom):
    print(f"Passed: {name}")
```

---

## ✅ Lab Conclusion

In this lab, we studied how Python handles iteration internally and how generators and decorators help write efficient, readable, and modular code. These concepts are widely used in **data science, backend development, and large-scale Python applications**.

---

**Lab Number:** 2
**Subject:** Data Science Lab
**Topic:** Iterators, Generators, and Decorators

