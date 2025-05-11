# Simple Calculator Application

A basic calculator application that performs four fundamental arithmetic operations.

## Features

- Addition
- Subtraction
- Multiplication
- Division

## Usage

1. Run the calculator.py script
2. Choose an operation (1-4)
3. Enter two numbers
4. View the result

## Error Handling

- Division by zero is handled with an error message
- Invalid operation choices are handled with an error message

## Code Details

### F-Strings
The program uses f-strings (formatted string literals), introduced in Python 3.6+. The `f` prefix before strings (like `f"{num1} + {num2} = {result}"`) allows embedding expressions inside string literals using curly braces {}. This makes string formatting more readable and convenient.

Example:
```python
num1 = 5
num2 = 3
result = 8
print(f"{num1} + {num2} = {result}")  # Outputs: 5 + 3 = 8
```

This is more concise than older formatting methods like `.format()` or `%` operator.
