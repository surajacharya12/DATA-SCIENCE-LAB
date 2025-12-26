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
