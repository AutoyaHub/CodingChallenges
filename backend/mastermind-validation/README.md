# 🧩 Mastermind Game Validation Challenge

[![Difficulty](https://img.shields.io/badge/Difficulty-⭐⭐⭐-yellow.svg)]()
[![Category](https://img.shields.io/badge/Category-Backend-blue.svg)]()
[![Duration](https://img.shields.io/badge/Duration-2--4%20hours-green.svg)]()
[![Skills](https://img.shields.io/badge/Skills-Logic%20|%20Constraint%20Satisfaction-purple.svg)]()

## 🎯 Overview

Implement a validation system for the classic Mastermind game! Given a sequence of guesses and their corresponding scores, determine whether there exists at least one secret key that could generate those exact scores. This challenge tests your logical reasoning and constraint satisfaction skills.

## 🔍 Problem Statement

### Game Rules

**Mastermind** is a logical deduction game between two players:

1. **Codemaker** (Player 1): Creates a secret key sequence `(s₁, s₂, ..., sₖ)` where `0 < sᵢ ≤ n`
2. **Codebreaker** (Player 2): Makes guesses `(g₁, g₂, ..., gₖ)` 
3. **Scoring**: For each guess, the score equals the number of positions where `gᵢ = sᵢ`

### Challenge

Given multiple guesses and their scores, determine if there exists **at least one** secret key that could produce those exact scores.

### Input Format

```
C                                    # Number of test cases (1 ≤ C ≤ 100)
n k q                               # n: max value, k: sequence length, q: number of guesses
g₁₁ g₁₂ ... g₁ₖ score₁              # First guess and its score
g₂₁ g₂₂ ... g₂ₖ score₂              # Second guess and its score
...
gq₁ gq₂ ... gqₖ scoreq              # q-th guess and its score
```

### Output Format

For each test case:
- `"Yes"` if there exists at least one valid secret key
- `"No"` if no secret key can produce the given scores

### Constraints

- `1 ≤ C ≤ 100` (test cases)
- `1 ≤ n, k ≤ 11` (small search space)
- `1 ≤ q ≤ 8` (number of guesses)
- `1 ≤ gᵢⱼ ≤ n` (guess values)
- `0 ≤ scoreᵢ ≤ k` (valid scores)

## 📋 Example

### Input
```
2
4 4 2
2 1 2 2 0
2 2 1 1 1
4 4 2
1 2 3 4 4
4 3 2 1 1
```

### Output
```
Yes
No
```

### Explanation

**Test Case 1:**
- Parameters: n=4, k=4, q=2
- Guess 1: `[2, 1, 2, 2]` → Score: 0
- Guess 2: `[2, 2, 1, 1]` → Score: 1

Analysis: Let's try secret key `[1, 2, 1, 2]`:
- Against guess 1: `[2,1,2,2]` vs `[1,2,1,2]` → Matches at position 0: **Score = 0** ✓
- Against guess 2: `[2,2,1,1]` vs `[1,2,1,2]` → Matches at position 2: **Score = 1** ✓

**Test Case 2:**
- Guess 1: `[1, 2, 3, 4]` → Score: 4 (perfect match)
- Guess 2: `[4, 3, 2, 1]` → Score: 1

Analysis: If the secret key matches guess 1 perfectly, it must be `[1, 2, 3, 4]`. But then against guess 2 `[4, 3, 2, 1]`, there would be **0 matches**, not 1. Contradiction!

## 🧠 Solution Approach

### Brute Force Strategy
```python
def solve_mastermind(n, k, guesses_and_scores):
    """
    Try all possible secret keys and check consistency.
    Time Complexity: O(n^k * q * k)
    """
    from itertools import product
    
    # Generate all possible secret keys
    for secret_key in product(range(1, n+1), repeat=k):
        valid = True
        
        # Check if this secret key is consistent with all guesses
        for guess, expected_score in guesses_and_scores:
            actual_score = calculate_score(secret_key, guess)
            if actual_score != expected_score:
                valid = False
                break
        
        if valid:
            return "Yes"
    
    return "No"

def calculate_score(secret, guess):
    """Calculate the Mastermind score between secret and guess."""
    return sum(1 for i in range(len(secret)) if secret[i] == guess[i])
```

### Constraint Satisfaction Approach
```python
def solve_with_constraints(n, k, guesses_and_scores):
    """
    Use constraint satisfaction to prune the search space.
    """
    # Start with all possible values for each position
    domains = [set(range(1, n+1)) for _ in range(k)]
    
    # Apply constraints from each guess
    for guess, score in guesses_and_scores:
        domains = apply_guess_constraint(domains, guess, score)
        if any(len(domain) == 0 for domain in domains):
            return "No"  # No solution possible
    
    # Check if remaining domain combinations satisfy all constraints
    return check_remaining_combinations(domains, guesses_and_scores)
```

## 🏗️ Implementation Structure

```
backend/mastermind-validation/
├── README.md                  # This file
├── solution.py               # Main solution implementation
├── input.txt                 # Sample input file
├── algorithms/
│   ├── brute_force.py        # Brute force approach
│   ├── constraint_sat.py     # Constraint satisfaction
│   └── optimized.py          # Optimized solution
├── tests/
│   ├── test_solution.py      # Unit tests
│   ├── test_edge_cases.py    # Edge case testing
│   └── test_performance.py   # Performance benchmarks
├── utils/
│   ├── validator.py          # Input validation
│   ├── game_logic.py         # Mastermind game utilities
│   └── test_generator.py     # Generate test cases
└── docs/
    ├── game_rules.md         # Detailed game explanation
    └── algorithm_analysis.md # Complexity analysis
```

## 🧪 Testing

### Test Categories

#### Basic Functionality
```python
def test_basic_cases():
    # Example test cases
    assert solve(4, 4, [([2,1,2,2], 0), ([2,2,1,1], 1)]) == "Yes"
    assert solve(4, 4, [([1,2,3,4], 4), ([4,3,2,1], 1)]) == "No"
    
    # Single guess cases
    assert solve(2, 2, [([1,1], 2)]) == "Yes"  # Secret could be [1,1]
    assert solve(2, 2, [([1,1], 0)]) == "Yes"  # Secret could be [2,2]
```

#### Edge Cases
```python
def test_edge_cases():
    # Perfect score (guess equals secret)
    assert solve(3, 3, [([1,2,3], 3)]) == "Yes"
    
    # Zero score (no matches)
    assert solve(2, 2, [([1,1], 0)]) == "Yes"  # Secret: [2,2]
    
    # Impossible score
    assert solve(2, 2, [([1,2], 3)]) == "No"  # Score > k
    
    # Multiple perfect scores (contradiction)
    assert solve(2, 2, [([1,1], 2), ([2,2], 2)]) == "No"
```

#### Constraint Validation
```python
def test_constraints():
    # Maximum constraints
    n, k, q = 11, 11, 8
    guesses = [([i]*k, 0) for i in range(1, min(q+1, n+1))]
    result = solve(n, k, guesses)
    assert result in ["Yes", "No"]
    
    # Minimum constraints  
    assert solve(1, 1, [([1], 1)]) == "Yes"
    assert solve(1, 1, [([1], 0)]) == "No"  # Impossible with n=1
```

### Performance Testing
```python
def test_performance():
    """Test worst-case performance scenarios."""
    import time
    
    # Maximum search space: n=11, k=11 → 11^11 possibilities
    n, k = 11, 11
    guesses = [([1]*k, 0)]  # Force checking many possibilities
    
    start_time = time.time()
    result = solve(n, k, guesses)
    execution_time = time.time() - start_time
    
    assert execution_time < 10.0  # Should complete within 10 seconds
    print(f"Execution time: {execution_time:.2f}s")
```

## 📊 Algorithm Analysis

### Complexity Analysis

| Algorithm | Time Complexity | Space Complexity | Best Case | Worst Case |
|-----------|----------------|------------------|-----------|------------|
| Brute Force | O(n^k × q × k) | O(1) | First key works | Check all keys |
| Constraint Satisfaction | O(n^k) | O(n × k) | Early contradiction | No pruning |
| Optimized | O(min(n^k, exponential pruning)) | O(n × k) | Quick elimination | Complex constraints |

### Search Space Analysis

For the given constraints:
- **Maximum search space**: 11^11 ≈ 285 billion combinations
- **Practical scenarios**: Most cases have contradictions that enable early termination
- **Optimization opportunity**: Use constraint propagation to reduce domain sizes

### Sample Complexity
```python
# Example: n=4, k=4, q=2
# Search space: 4^4 = 256 possible secret keys
# With 2 guesses providing constraints, typically <50 keys need checking
```

## 🚀 Getting Started

### Quick Start
```bash
# Clone and setup
git clone <repository-url>
cd backend/mastermind-validation

# Run with sample input
python solution.py < input.txt

# Run tests
python -m pytest tests/ -v

# Performance analysis
python utils/performance_test.py
```

### Solution Template
```python
def mastermind_validator():
    """Main solution function."""
    c = int(input())
    
    for _ in range(c):
        n, k, q = map(int, input().split())
        guesses_and_scores = []
        
        for _ in range(q):
            line = list(map(int, input().split()))
            guess = line[:k]
            score = line[k]
            guesses_and_scores.append((guess, score))
        
        result = solve_mastermind(n, k, guesses_and_scores)
        print(result)

if __name__ == "__main__":
    mastermind_validator()
```

## 💡 Implementation Tips

### Optimization Strategies

1. **Early Termination**: Stop as soon as you find one valid secret key
2. **Constraint Propagation**: Eliminate impossible values early
3. **Smart Ordering**: Try more constrained positions first
4. **Memoization**: Cache intermediate constraint states

### Common Pitfalls

```python
# ❌ Wrong: Comparing entire sequences
def wrong_score(secret, guess):
    return 1 if secret == guess else 0

# ✅ Correct: Position-by-position comparison  
def correct_score(secret, guess):
    return sum(1 for i in range(len(secret)) if secret[i] == guess[i])
```

### Debugging Helpers
```python
def debug_secret_key(secret, guesses_and_scores):
    """Verify a secret key against all guesses."""
    print(f"Testing secret key: {secret}")
    for i, (guess, expected) in enumerate(guesses_and_scores):
        actual = calculate_score(secret, guess)
        status = "✓" if actual == expected else "✗"
        print(f"  Guess {i+1}: {guess} → {actual} (expected {expected}) {status}")
```

## 🏆 Evaluation Criteria

| Criterion | Weight | Description |
|-----------|---------|-------------|
| **Correctness** | 40% | All test cases pass, handles edge cases |
| **Algorithm Efficiency** | 25% | Optimal approach for given constraints |
| **Code Quality** | 20% | Clean, readable, well-structured |
| **Problem Understanding** | 10% | Demonstrates understanding of game logic |
| **Testing** | 5% | Comprehensive test coverage |

## 🔗 Advanced Extensions

### Bonus Challenges
1. **Score Optimization**: Find the secret key that minimizes/maximizes total score
2. **Partial Information**: Handle incomplete guess data
3. **Multiple Solutions**: Count all possible secret keys
4. **Interactive Version**: Build a playable Mastermind game

### Real-World Applications
- **Code Breaking**: Cryptographic pattern analysis
- **Genetic Algorithms**: Constraint satisfaction in optimization
- **Game AI**: Strategy development for logical games
- **Testing**: Validation of complex system behaviors

## 📚 Resources

- [Mastermind Game Rules](https://en.wikipedia.org/wiki/Mastermind_(board_game))
- [Constraint Satisfaction Problems](https://en.wikipedia.org/wiki/Constraint_satisfaction_problem)
- [Backtracking Algorithms](https://www.geeksforgeeks.org/backtracking-algorithms/)
- [Game Theory Applications](https://www.coursera.org/learn/game-theory-1)

---

<div align="center">
  <strong>Crack the code with logic! 🧩</strong><br>
  <em>Where deduction meets algorithmic precision.</em>
</div>