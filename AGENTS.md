# AGENTS.md - Trading Project

## Project Overview

This is a Python trading project that provides tools for fetching stock price data (from JoinQuant), storing it in PostgreSQL, and performing analysis. It uses SQLAlchemy for database operations, pandas for data manipulation, and integrates with OpenAI/Qwen for analysis.

## Requirements

- Python 3.11+
- PostgreSQL database
- Dependencies: See `pyproject.toml`

## Build & Installation

```bash
# Install dependencies
pip install -e .

# Or install from requirements.txt
pip install -r requirements.txt
```

## Testing

This project does not currently have a formal test framework. The `test_hist.py` file is a development script, not a test file.

To add tests in the future, consider using pytest:

```bash
# Run all tests
pytest

# Run a single test file
pytest tests/test_file.py

# Run a specific test function
pytest tests/test_file.py::test_function_name

# Run tests matching a pattern
pytest -k "test_pattern"
```

## Linting & Code Quality

No linting configuration is currently set up. Recommended tools:

```bash
# Install ruff (fast linter/formatter)
pip install ruff

# Run linter
ruff check src/

# Auto-fix issues
ruff check --fix src/

# Format code
ruff format src/

# Type checking with mypy
pip install mypy
mypy src/
```

## Code Style Guidelines

### Imports

- Use absolute imports within the package: `from trading.base_data import get_day_price`
- Group imports in order: standard library, third-party, local
- Avoid unused imports

### Formatting

- Follow PEP 8 style guide
- Use 4 spaces for indentation
- Maximum line length: 100 characters (recommended)
- Use blank lines to separate functions and classes (two blank lines between top-level definitions)

### Type Hints

- Add type hints for function parameters and return values
- Use `from typing import` for complex types

```python
from typing import List, Optional

def get_price(security: str, fre: str, s_date: str, e_date: str) -> Optional[pd.DataFrame]:
    ...
```

### Naming Conventions

- Functions/variables: `snake_case`
- Classes: `PascalCase`
- Constants: `UPPER_SNAKE_CASE`
- Private functions: prefix with underscore `_private_func`

### Error Handling

- Use try/except blocks for operations that may fail
- Catch specific exceptions rather than using bare `except:`
- Log errors appropriately

```python
try:
    result = some_operation()
except ValueError as e:
    logger.error(f"Invalid value: {e}")
    raise
```

### Database Operations

- Use SQLAlchemy ORM as shown in `models/security_price.py`
- Always close sessions or use scoped sessions
- Use transactions appropriately

### Documentation

- Use docstrings for all public functions and classes
- Follow Google or NumPy docstring format
- Write docstrings in English (or Chinese if the codebase uses Chinese comments)

```python
def function_name(param: str) -> bool:
    """
    Short description.

    Args:
        param: Description of parameter.

    Returns:
        Description of return value.

    Raises:
        ValueError: When param is invalid.
    """
```

## Project Structure

```
trading/
├── src/trading/
│   ├── base_data/      # Price data fetching
│   ├── models/         # Database models
│   └── analysis/       # Analysis modules
├── pyproject.toml
└── requirements.txt
```

## Common Tasks

### Run main script
```bash
python -m src.trading.main
```

### Add new dependency
Edit `pyproject.toml` and add the package to `dependencies`, then run `pip install -e .`
