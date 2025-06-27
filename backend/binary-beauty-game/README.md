# 🎮 Binary Beauty Game Challenge

[![Difficulty](https://img.shields.io/badge/Difficulty-⭐⭐⭐-yellow.svg)]()
[![Category](https://img.shields.io/badge/Category-Backend-blue.svg)]()
[![Duration](https://img.shields.io/badge/Duration-2--4%20hours-green.svg)]()
[![Skills](https://img.shields.io/badge/Skills-Algorithm%20Design%20|%20Game%20Theory-purple.svg)]()

## 🎯 Overview

In this algorithmic challenge, you'll implement the logic for a mathematical game where the "beauty" of a number is defined as the count of 1s in its binary representation. Two players compete optimally, making strategic moves based on this beauty value.

## 🔍 Problem Statement

### Game Rules

The **beauty** of a number `X` is the number of 1s in its binary representation.

Two players play alternately with a number `n` on a blackboard:

1. **Player's Turn**: Choose an integer `k` such that `0 ≤ k` and `2^k < n`
2. **Constraint**: `n - 2^k` must have the same beauty as `n`
3. **Action**: Replace `n` with `n - 2^k`
4. **Win Condition**: The player who cannot make a valid move loses

**Determine the winner** assuming both players play optimally.

### Input Format

```
T                    # Number of test cases (0 ≤ T ≤ 5)
n₁                   # First test case number (1 ≤ n ≤ 10⁹)
n₂                   # Second test case number
...
nₜ                   # T-th test case number
```

### Output Format

For each test case, output:
- `"First Player"` if the first player wins
- `"Second Player"` if the second player wins

## 📋 Example

### Input
```
7
1
2
8
16
42
1000
123
```

### Output
```
Second Player
First Player
First Player
Second Player
Second Player
First Player
Second Player
```

### Explanation

- **n = 1**: Binary `1` (beauty = 1). No valid moves exist, so Second Player wins.
- **n = 2**: Binary `10` (beauty = 1). First Player can subtract `2⁰ = 1` → `n = 1` (beauty = 1). Second Player cannot move, so First Player wins.

## 🎯 Requirements

### Functional Requirements
- [ ] **Input Validation**: Handle edge cases and invalid inputs gracefully
- [ ] **Optimal Algorithm**: Implement an efficient solution for large numbers (up to 10⁹)
- [ ] **Correct Logic**: Accurately determine the winner for all test cases
- [ ] **Performance**: Solution should run efficiently for the given constraints

### Technical Requirements
- [ ] **Language**: Python 3.8+ (preferred) or any modern language
- [ ] **Code Quality**: Clean, readable, and well-documented code
- [ ] **Testing**: Include unit tests for various scenarios
- [ ] **Documentation**: Comprehensive README with approach explanation

## 🧠 Solution Approach

### Key Insights
1. **Beauty Preservation**: The constraint that `n - 2^k` must have the same beauty as `n` is crucial
2. **Game Theory**: This is an impartial game - use Sprague-Grundy theorem concepts
3. **Binary Analysis**: Analyze the binary representation to find valid moves

### Suggested Strategy
1. **Analyze Binary Pattern**: Study how subtracting powers of 2 affects beauty
2. **Identify Winning/Losing Positions**: Determine which positions are winning vs losing
3. **Implement Recursion/DP**: Use memoization for efficiency
4. **Optimize**: Handle large numbers efficiently

## 🏗️ Implementation Structure

```
backend/binary-beauty-game/
├── README.md              # This file
├── solution.py            # Main solution implementation
├── tests/
│   ├── test_solution.py   # Unit tests
│   └── test_cases.txt     # Additional test cases
├── input.txt              # Sample input file
└── requirements.txt       # Dependencies (if any)
```

## 🧪 Testing

### Test Cases
Your solution should handle:
- **Edge Cases**: n = 1, n = 2, powers of 2
- **Small Numbers**: Verify against manual calculation
- **Large Numbers**: Test efficiency with n close to 10⁹
- **Binary Patterns**: Numbers with different binary representations

### Sample Test
```python
def test_basic_cases():
    assert solve(1) == "Second Player"
    assert solve(2) == "First Player"
    assert solve(8) == "First Player"
    assert solve(16) == "Second Player"
```

## 📊 Evaluation Criteria

| Criterion | Weight | Description |
|-----------|---------|-------------|
| **Correctness** | 30% | All test cases pass, handles edge cases |
| **Algorithm Efficiency** | 25% | Optimal time/space complexity |
| **Code Quality** | 20% | Clean, readable, maintainable code |
| **Documentation** | 15% | Clear explanations and comments |
| **Testing** | 10% | Comprehensive test coverage |

## 🚀 Getting Started

1. **Understand the Problem**: Read through the problem statement carefully
2. **Analyze Examples**: Work through the provided examples manually
3. **Design Algorithm**: Plan your approach before coding
4. **Implement Solution**: Write clean, efficient code
5. **Test Thoroughly**: Verify with provided and additional test cases
6. **Document Approach**: Explain your solution in comments/README

## 💡 Hints

<details>
<summary>Click to reveal hints</summary>

1. **Beauty Analysis**: When you subtract `2^k` from a number, what happens to its binary representation?
2. **Move Validity**: For `n - 2^k` to have the same beauty as `n`, what constraint does this place on the binary representation?
3. **Game Theory**: Consider whether certain numbers are inherently winning or losing positions.
4. **Pattern Recognition**: Look for patterns in small numbers first.

</details>

## 📚 References

- [Game Theory Basics](https://en.wikipedia.org/wiki/Game_theory)
- [Sprague-Grundy Theorem](https://en.wikipedia.org/wiki/Sprague%E2%80%93Grundy_theorem)
- [Binary Number System](https://en.wikipedia.org/wiki/Binary_number)

---

<div align="center">
  <strong>Happy Coding! 🚀</strong><br>
  <em>May your algorithms be efficient and your logic be sound.</em>
</div>