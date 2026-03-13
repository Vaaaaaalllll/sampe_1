# WARNING: template code, may need edits

# Sample Python Calculator

A simple, extensible Python calculator with support for basic arithmetic operations.

## Features

- Basic arithmetic operations (addition, subtraction, multiplication, division)
- Power and modulo operations
- Error handling for invalid operations
- Command-line interface
- Comprehensive test suite

## Installation

```bash
# Clone the repository
git clone <repository-url>
cd sampe_1

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

### As a Module

```python
from src.calculator import Calculator

calc = Calculator()
result = calc.add(5, 3)
print(result)  # Output: 8
```

### Command Line Interface

```bash
python -m src.cli
```

## Running Tests

```bash
pytest tests/
```

## Project Structure

```
sampe_1/
├── src/
│   ├── __init__.py
│   ├── calculator.py
│   ├── operations.py
│   └── cli.py
├── tests/
│   ├── __init__.py
│   ├── test_calculator.py
│   └── test_operations.py
├── docs/
│   └── API.md
├── .gitignore
├── requirements.txt
├── setup.py
└── README.md
```

## License

MIT License
