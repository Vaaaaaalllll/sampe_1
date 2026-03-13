# WARNING: template code, may need edits
# Calculator API Documentation

## Overview

The Sample Python Calculator provides a simple and extensible API for performing basic arithmetic operations.

## Classes

### Calculator

Main calculator class that provides arithmetic operations and history tracking.

#### Constructor

```python
Calculator()
```

Initializes a new calculator instance with empty history.

#### Methods

##### add(a, b)

Add two numbers.

**Parameters:**
- `a` (int | float): First number
- `b` (int | float): Second number

**Returns:**
- (int | float): Sum of a and b

**Example:**
```python
calc = Calculator()
result = calc.add(5, 3)  # Returns 8
```

##### subtract(a, b)

Subtract b from a.

**Parameters:**
- `a` (int | float): First number
- `b` (int | float): Second number

**Returns:**
- (int | float): Difference of a and b

**Example:**
```python
result = calc.subtract(10, 3)  # Returns 7
```

##### multiply(a, b)

Multiply two numbers.

**Parameters:**
- `a` (int | float): First number
- `b` (int | float): Second number

**Returns:**
- (int | float): Product of a and b

**Example:**
```python
result = calc.multiply(5, 3)  # Returns 15
```

##### divide(a, b)

Divide a by b.

**Parameters:**
- `a` (int | float): Numerator
- `b` (int | float): Denominator

**Returns:**
- (float): Quotient of a and b

**Raises:**
- `DivisionByZeroError`: If b is zero

**Example:**
```python
result = calc.divide(10, 2)  # Returns 5.0
```

##### power(a, b)

Raise a to the power of b.

**Parameters:**
- `a` (int | float): Base
- `b` (int | float): Exponent

**Returns:**
- (int | float): a raised to the power of b

**Example:**
```python
result = calc.power(2, 3)  # Returns 8
```

##### modulo(a, b)

Calculate a modulo b.

**Parameters:**
- `a` (int | float): Dividend
- `b` (int | float): Divisor

**Returns:**
- (int | float): Remainder of a divided by b

**Raises:**
- `DivisionByZeroError`: If b is zero

**Example:**
```python
result = calc.modulo(10, 3)  # Returns 1
```

##### get_history()

Get the calculation history.

**Returns:**
- (list): List of calculation strings

**Example:**
```python
history = calc.get_history()
for operation in history:
    print(operation)
```

##### clear_history()

Clear the calculation history.

**Returns:**
- None

**Example:**
```python
calc.clear_history()
```

## Exceptions

### DivisionByZeroError

Raised when attempting to divide or perform modulo by zero.

**Example:**
```python
try:
    calc.divide(5, 0)
except DivisionByZeroError as e:
    print(f"Error: {e}")
```

## Module Functions

The `operations` module provides standalone functions for each operation:

- `add(a, b)` - Addition
- `subtract(a, b)` - Subtraction
- `multiply(a, b)` - Multiplication
- `divide(a, b)` - Division
- `power(a, b)` - Exponentiation
- `modulo(a, b)` - Modulo

These functions can be used independently without creating a Calculator instance.

**Example:**
```python
from src.operations import add, multiply

result1 = add(5, 3)  # Returns 8
result2 = multiply(4, 5)  # Returns 20
```

## CLI Usage

The calculator includes a command-line interface:

```bash
python -m src.cli
```

This launches an interactive menu-driven calculator with the following features:
- Perform all arithmetic operations
- View calculation history
- Clear history
- User-friendly error handling
