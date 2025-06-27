# 🤝 Contributing to Autoya Coding Challenges

Thank you for your interest in contributing to our coding challenges repository! This guide will help you understand how to contribute effectively and maintain the high quality standards we strive for.

## 📋 Table of Contents
- [Code of Conduct](#code-of-conduct)
- [How to Contribute](#how-to-contribute)
- [Challenge Development Guidelines](#challenge-development-guidelines)
- [Documentation Standards](#documentation-standards)
- [Code Quality Requirements](#code-quality-requirements)
- [Testing Standards](#testing-standards)
- [Pull Request Process](#pull-request-process)
- [Issue Guidelines](#issue-guidelines)

## 🌟 Code of Conduct

We are committed to providing a welcoming and inclusive environment for all contributors. Please read and follow our [Code of Conduct](CODE_OF_CONDUCT.md).

## 🚀 How to Contribute

### Types of Contributions

We welcome several types of contributions:

1. **New Challenges**: Create new coding challenges for any category
2. **Challenge Improvements**: Enhance existing challenges with better examples, clearer instructions, or additional test cases
3. **Documentation**: Improve README files, add tutorials, or create guides
4. **Bug Fixes**: Fix issues in existing challenges or infrastructure
5. **Infrastructure**: Improve CI/CD, testing frameworks, or tooling
6. **Templates**: Create new templates for different roles or challenge types

### Getting Started

1. **Fork the Repository**
   ```bash
   git clone https://github.com/your-username/CodingChallenges.git
   cd CodingChallenges
   ```

2. **Create a Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/issue-number
   ```

3. **Make Your Changes**
   - Follow our [coding standards](#code-quality-requirements)
   - Ensure all tests pass
   - Add documentation where needed

4. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "feat: add new distributed caching challenge"
   ```

5. **Push and Create Pull Request**
   ```bash
   git push origin feature/your-feature-name
   ```

## 💡 Challenge Development Guidelines

### Challenge Categories

Ensure your challenge fits into one of our categories:
- **Backend**: Server-side logic, APIs, databases, system design
- **Frontend**: UI/UX, JavaScript frameworks, responsive design
- **Full-Stack**: End-to-end applications, system integration
- **Logic**: Algorithms, mathematical problems, data structures

### Challenge Structure

Every challenge should follow this structure:

```
category/challenge-name/
├── README.md              # Main challenge description
├── requirements.txt       # Dependencies (if applicable)
├── .env.example          # Environment variables template
├── input.txt             # Sample input (for algorithmic challenges)
├── tests/
│   ├── test_*.py         # Unit tests
│   └── fixtures/         # Test data
├── docs/                 # Additional documentation
└── examples/             # Sample solutions (optional)
```

### Naming Conventions

- **Directories**: Use kebab-case (e.g., `distributed-task-scheduler`)
- **Files**: Use snake_case for Python (e.g., `test_solution.py`)
- **README files**: Always use `README.md` (not `ReadMe.md` or `readme.md`)

### Difficulty Levels

Rate your challenge using our 5-star system:
- ⭐ **Beginner**: Basic concepts, simple implementation
- ⭐⭐ **Easy**: Fundamental algorithms, straightforward logic
- ⭐⭐⭐ **Medium**: Complex logic, multiple components
- ⭐⭐⭐⭐ **Hard**: Advanced concepts, system design
- ⭐⭐⭐⭐⭐ **Expert**: Complex systems, distributed computing

## 📚 Documentation Standards

### README Template

Every challenge must include a comprehensive README with:

```markdown
# 🎯 Challenge Title

[![Difficulty](https://img.shields.io/badge/Difficulty-⭐⭐⭐-yellow.svg)]()
[![Category](https://img.shields.io/badge/Category-Backend-blue.svg)]()
[![Duration](https://img.shields.io/badge/Duration-4--6%20hours-green.svg)]()
[![Skills](https://img.shields.io/badge/Skills-Skill1%20|%20Skill2-purple.svg)]()

## 🎯 Overview
Clear, concise description of what the challenge entails.

## 🔍 Problem Statement
Detailed problem description with examples.

## 🎯 Requirements
- Functional requirements checklist
- Technical requirements checklist
- Optional bonus features

## 📋 API Specification (if applicable)
Clear API documentation with examples.

## 🏗️ Project Structure
Expected file and folder organization.

## 🚀 Getting Started
Step-by-step setup instructions.

## 🧪 Testing
Testing requirements and examples.

## 🏆 Evaluation Criteria
Clear rubric for assessment.

## 📚 Resources
Helpful links and references.
```

### Writing Guidelines

- **Clarity**: Use clear, concise language
- **Examples**: Provide concrete examples for complex concepts
- **Accessibility**: Consider different skill levels
- **Consistency**: Follow the same format across all challenges
- **Emojis**: Use emojis consistently for visual appeal (but don't overuse)

## 🔧 Code Quality Requirements

### General Principles

1. **Readability**: Code should be self-documenting
2. **Modularity**: Break down complex problems into smaller functions
3. **Error Handling**: Include proper error handling and validation
4. **Performance**: Consider time and space complexity
5. **Security**: Follow security best practices

### Python Standards

```python
"""
Module docstring describing the purpose.
"""

from typing import List, Dict, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def function_name(param1: int, param2: str) -> Optional[Dict[str, Any]]:
    """
    Function description.
    
    Args:
        param1 (int): Description of param1
        param2 (str): Description of param2
        
    Returns:
        Optional[Dict[str, Any]]: Description of return value
        
    Raises:
        ValueError: When input is invalid
    """
    if param1 < 0:
        raise ValueError("param1 must be non-negative")
    
    # Implementation here
    return result
```

### JavaScript/TypeScript Standards

```typescript
/**
 * Interface description
 */
interface ChallengeConfig {
  readonly name: string;
  readonly difficulty: number;
  readonly duration: string;
}

/**
 * Function description
 * @param config - Configuration object
 * @returns Promise resolving to result
 */
export async function processChallenge(
  config: ChallengeConfig
): Promise<ChallengeResult> {
  if (!config.name) {
    throw new Error('Challenge name is required');
  }
  
  // Implementation here
  return result;
}
```

## 🧪 Testing Standards

### Test Coverage Requirements

- **Unit Tests**: All core functions must have unit tests
- **Integration Tests**: API endpoints and system interactions
- **Edge Cases**: Test boundary conditions and error scenarios
- **Performance Tests**: For challenges with specific performance requirements

### Test Structure

```python
import pytest
from your_module import your_function

class TestYourFunction:
    """Test suite for your_function."""
    
    def test_basic_functionality(self):
        """Test basic use case."""
        result = your_function("input")
        assert result == "expected_output"
    
    def test_edge_cases(self):
        """Test edge cases."""
        with pytest.raises(ValueError):
            your_function(None)
    
    @pytest.mark.parametrize("input,expected", [
        ("test1", "result1"),
        ("test2", "result2"),
    ])
    def test_multiple_inputs(self, input, expected):
        """Test multiple input scenarios."""
        assert your_function(input) == expected
```

### Performance Testing

For challenges with performance requirements:

```python
import time
import pytest

def test_performance():
    """Test that solution meets performance requirements."""
    large_input = generate_large_test_case()
    
    start_time = time.time()
    result = your_function(large_input)
    execution_time = time.time() - start_time
    
    assert execution_time < 5.0  # Should complete within 5 seconds
    assert result is not None
```

## 🔄 Pull Request Process

### Before Submitting

1. **Run Tests**: Ensure all tests pass locally
   ```bash
   pytest tests/ -v
   ```

2. **Check Code Quality**: Run linting and formatting
   ```bash
   black .
   flake8 .
   mypy .
   ```

3. **Update Documentation**: Ensure README is updated if needed

4. **Test Manually**: Verify your challenge works end-to-end

### Pull Request Template

When creating a pull request, include:

```markdown
## Description
Brief description of changes made.

## Type of Change
- [ ] New challenge
- [ ] Bug fix
- [ ] Documentation update
- [ ] Infrastructure improvement

## Testing
- [ ] All existing tests pass
- [ ] New tests added for new functionality
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] Changes generate no new warnings
```

### Review Process

1. **Automated Checks**: CI/CD pipeline runs automatically
2. **Code Review**: At least one maintainer reviews the PR
3. **Testing**: Reviewers test the changes manually if needed
4. **Approval**: PR is approved and merged

## 🐛 Issue Guidelines

### Bug Reports

When reporting bugs, include:

```markdown
## Bug Description
Clear description of the bug.

## Steps to Reproduce
1. Step one
2. Step two
3. ...

## Expected Behavior
What should happen.

## Actual Behavior
What actually happens.

## Environment
- OS: [e.g., Ubuntu 20.04]
- Python version: [e.g., 3.9.0]
- Browser: [if applicable]

## Additional Context
Screenshots, logs, or other relevant information.
```

### Feature Requests

For new features:

```markdown
## Feature Description
Clear description of the proposed feature.

## Motivation
Why is this feature needed?

## Proposed Solution
How should this feature work?

## Alternatives Considered
Other approaches you've considered.

## Additional Context
Any other relevant information.
```

## 🏆 Recognition

We value all contributions! Contributors will be:

- **Acknowledged**: Listed in our contributors section
- **Featured**: Outstanding contributions highlighted in releases
- **Credited**: Proper attribution in challenge documentation

## 📞 Getting Help

If you need help:

1. **Check Documentation**: Review existing docs and FAQs
2. **Search Issues**: Look for similar questions or problems
3. **Create Discussion**: Start a discussion for questions
4. **Contact Maintainers**: Email hiring@autoya.de for urgent matters

## 📝 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

<div align="center">
  <strong>Thank you for making our challenges better! 🙏</strong><br>
  <em>Every contribution, no matter how small, makes a difference.</em>
</div> 