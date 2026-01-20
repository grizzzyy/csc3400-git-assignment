import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: You cannot divide by 0"
    return x / y

def square_root(x):
    if x < 0:
        return "naurrr! Square root of negative number."
    return math.sqrt(x)
