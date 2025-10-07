# Contributing to Data Structures and Algorithms

Thank you for your interest in contributing! This guide will help you get started.

## Getting Started

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/data-structures-algorithms.git
   cd data-structures-algorithms
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Project Structure

```
data-structures-algorithms/
├── data_structures/    # Data structure implementations
├── algorithms/         # Algorithm implementations
└── tests/             # Unit tests
```

## Adding New Implementations

### 1. Create the Implementation

- Place in appropriate directory (`data_structures/` or `algorithms/`)
- Include comprehensive docstrings
- Add time/space complexity analysis
- Include example usage in `if __name__ == "__main__"` block

### 2. Code Style

- Follow PEP 8 guidelines
- Use descriptive variable names
- Add comments for complex logic
- Include type hints where helpful

Example structure:
```python
"""
Algorithm/Data Structure Name

Time Complexity: O(...)
Space Complexity: O(...)

Brief description of the algorithm/data structure.
"""


class YourClass:
    """Class docstring."""
    
    def method(self, param):
        """Method docstring with complexity analysis."""
        pass


if __name__ == "__main__":
    # Example usage
    pass
```

### 3. Add Tests

Create tests in the `tests/` directory:
```python
class TestYourImplementation:
    """Test cases for Your Implementation."""
    
    def test_basic_case(self):
        # Test code
        assert expected == actual
```

### 4. Run Tests

Ensure all tests pass:
```bash
python3 -m pytest tests/ -v
```

### 5. Submit Pull Request

- Create a new branch for your feature
- Commit with clear messages
- Push to your fork
- Open a Pull Request with description

## What to Contribute

- New data structures (graphs, heaps, tries, etc.)
- New algorithms (dynamic programming, greedy, backtracking)
- Performance improvements
- Bug fixes
- Documentation improvements
- Additional test cases

## Code Review Process

All contributions will be reviewed for:
- Correctness of implementation
- Code quality and style
- Test coverage
- Documentation completeness

## Questions?

Feel free to open an issue for discussion before starting work on major contributions.
