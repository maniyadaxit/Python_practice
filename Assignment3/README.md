# Assignment 3

## Task 1: Calculate Factorial Using a Function

```python
  a = int(input("Enter number: "))
factorial_value = 1

def factorial(a):
    global factorial_value
    if a != 0:
        factorial_value *= a
        factorial(a-1)
    return factorial_value

print(factorial(a))
```

## Task 2: Using the Math Module for Calculations

```python
import math

a = int(input("Enter a number : "))

print(math.sqrt(a))
print(math.log(a))
print(math.sin(a))
```
