# 🎯 K-th Largest Number Game Challenge

[![Difficulty](https://img.shields.io/badge/Difficulty-⭐⭐⭐-yellow.svg)]()
[![Category](https://img.shields.io/badge/Category-Backend-blue.svg)]()
[![Duration](https://img.shields.io/badge/Duration-3--5%20hours-green.svg)]()
[![Skills](https://img.shields.io/badge/Skills-Combinatorics%20|%20Algorithm%20Design-purple.svg)]()

## 🎯 Overview

Solve a complex combinatorial problem involving N friends playing a number selection game. Each friend chooses a number from their personal list, and the game administrator announces the K-th largest number from the selected values. Your task is to determine how many different numbers could possibly be announced as the K-th largest.

## 🔍 Problem Statement

### Game Description

N friends are playing a strategic number game where:

1. **Setup**: Each friend has a personal list of unique numbers
2. **Selection**: Each friend chooses exactly one number from their list
3. **Sorting**: The administrator sorts all selected numbers
4. **Announcement**: The administrator announces the K-th largest number
5. **Challenge**: Count all possible numbers that could be announced

### Mathematical Framework

Given:
- `N` friends, each with their own list of numbers
- All numbers across all lists are unique
- Each friend must select exactly one number
- We need the count of possible K-th largest values

### Input Format

```
T                           # Number of test cases
N K                         # N friends, K-th largest position
a₁ num₁₁ num₁₂ ... num₁ₐ₁   # Friend 1's list (a₁ numbers)
a₂ num₂₁ num₂₂ ... num₂ₐ₂   # Friend 2's list (a₂ numbers)
...
aₙ numₙ₁ numₙ₂ ... numₙₐₙ   # Friend N's list (aₙ numbers)
```

### Output Format

For each test case, output the count of numbers that could be the K-th largest.

## 📋 Example

### Input
```
2
3 3
3 2 5 3
3 8 1 6
3 7 4 9
20 11
1 3
1 2
11 1 4 55 6 80 8 9 19 11 12 13
15 14 177 16 17 18 10 20 21 22 37 24 25 26 27 28
7 190 30 31 32 33 34 35
12 81 23 195 39 40 41 42 43 49 45 46 47
15 48 44 50 51 52 53 54 5 121 57 58 59 98 61 62
3 63 64 65
10 66 67 68 69 70 71 72 73 74 75
4 76 91 29 79
11 7 36 82 83 84 85 86 96 88 89 90
17 77 92 93 172 95 87 97 60 99 100 101 102 103 135 186 106 107
10 108 109 110 111 112 113 114 115 116 117
1 118
8 119 120 56 122 123 124 125 126
9 127 128 129 130 131 132 133 134 104
11 136 137 138 139 140 141 142 143 144 145 146
20 147 148 149 150 151 152 153 154 159 156 157 158 155 180 161 162 163 164 165 166
18 167 168 169 170 171 94 173 174 175 176 15 178 179 160 181 182 183 184
17 185 105 187 188 189 78 191 192 193 194 38 196 197 198 199 200 201
```

### Output
```
6
89
```

### Explanation

**Test Case 1:**
- N = 3, K = 3 (need 3rd largest)
- Lists: {2, 5, 3}, {8, 1, 6}, {7, 4, 9}
- Possible K-th largest values: {4, 5, 6, 7, 8, 9}
- Count: 6

**Analysis of Test Case 1:**
- If we select (2, 1, 4): sorted = [1, 2, 4], 3rd largest = 4
- If we select (3, 6, 7): sorted = [3, 6, 7], 3rd largest = 7
- If we select (5, 8, 9): sorted = [5, 8, 9], 3rd largest = 9
- And so on...

## 🎯 Requirements

### Functional Requirements
- [ ] **Input Parsing**: Handle multiple test cases with varying list sizes
- [ ] **Algorithm Design**: Efficient solution for large inputs
- [ ] **Combinatorial Logic**: Generate all valid combinations systematically
- [ ] **Performance**: Handle constraints (N ≤ 1000, list sizes ≤ N)
- [ ] **Edge Cases**: Single friend, K=1, K=N scenarios

### Technical Requirements
- [ ] **Language**: Python 3.8+ (preferred) or any modern language
- [ ] **Time Complexity**: Optimize for the given constraints
- [ ] **Memory Usage**: Efficient memory management for large inputs
- [ ] **Code Quality**: Clean, readable, and well-documented
- [ ] **Testing**: Comprehensive test coverage

## 🧠 Solution Approach

### Brute Force Approach
```python
def solve_brute_force(lists, k):
    """
    Generate all possible combinations and count unique K-th largest values.
    Time Complexity: O(∏(len(list_i)))
    """
    from itertools import product
    
    possible_kth = set()
    for combination in product(*lists):
        sorted_combo = sorted(combination, reverse=True)
        kth_largest = sorted_combo[k-1]
        possible_kth.add(kth_largest)
    
    return len(possible_kth)
```

### Optimized Approach
```python
def solve_optimized(lists, k):
    """
    Use mathematical insights to avoid generating all combinations.
    Key insight: A number can be K-th largest if there exist valid
    selections that place exactly (k-1) numbers above it.
    """
    all_numbers = []
    for i, lst in enumerate(lists):
        for num in lst:
            all_numbers.append((num, i))  # (value, list_index)
    
    all_numbers.sort(reverse=True)  # Sort descending
    
    possible_kth = set()
    
    for target_num, target_list in all_numbers:
        if can_be_kth_largest(lists, target_num, target_list, k):
            possible_kth.add(target_num)
    
    return len(possible_kth)

def can_be_kth_largest(lists, target_num, target_list, k):
    """
    Check if target_num can be the K-th largest by verifying
    if we can select exactly (k-1) numbers larger than target_num.
    """
    # Implementation details...
    pass
```

### Key Insights

1. **Constraint Analysis**: For a number to be K-th largest, exactly (K-1) numbers must be larger
2. **List Dependencies**: Each friend contributes exactly one number
3. **Uniqueness**: All numbers are unique across all lists
4. **Feasibility Check**: Verify if required larger numbers are available from other friends

## 🏗️ Implementation Structure

```
backend/kth-largest-game/
├── README.md              # This file
├── solution.py            # Main solution implementation
├── input.txt              # Sample input file
├── tests/
│   ├── test_solution.py   # Unit tests
│   ├── test_cases/        # Additional test cases
│   │   ├── small.txt      # Small test cases
│   │   ├── large.txt      # Large test cases
│   │   └── edge.txt       # Edge cases
│   └── test_performance.py # Performance benchmarks
├── algorithms/
│   ├── brute_force.py     # Brute force implementation
│   ├── optimized.py       # Optimized solution
│   └── mathematical.py    # Mathematical approach
└── utils/
    ├── input_parser.py    # Input parsing utilities
    ├── validator.py       # Solution validation
    └── benchmark.py       # Performance testing
```

## 🧪 Testing

### Test Categories

#### Basic Functionality
```python
def test_basic_cases():
    # Test case from example
    lists = [[2, 5, 3], [8, 1, 6], [7, 4, 9]]
    assert solve(lists, 3) == 6
    
    # Single friend case
    assert solve([[1, 2, 3]], 1) == 3
    
    # K = 1 case (maximum)
    assert solve([[1, 5], [2, 6], [3, 7]], 1) == 3  # 5, 6, 7
```

#### Edge Cases
```python
def test_edge_cases():
    # All friends have single number
    assert solve([[1], [2], [3]], 2) == 1  # Only 2 can be 2nd largest
    
    # K equals N
    assert solve([[5, 1], [6, 2], [7, 3]], 3) == 3  # 1, 2, 3
    
    # Large numbers
    assert solve([[1000000], [999999], [999998]], 1) == 1
```

#### Performance Tests
```python
def test_performance():
    # Test with maximum constraints
    import random
    
    lists = []
    for i in range(1000):  # 1000 friends
        friend_list = random.sample(range(i*1000, (i+1)*1000), 
                                   random.randint(1, 1000))
        lists.append(friend_list)
    
    start_time = time.time()
    result = solve(lists, 500)
    end_time = time.time()
    
    assert end_time - start_time < 5.0  # Should complete within 5 seconds
```

## 📊 Algorithm Analysis

### Complexity Comparison

| Algorithm | Time Complexity | Space Complexity | Feasibility |
|-----------|----------------|------------------|-------------|
| Brute Force | O(∏aᵢ) | O(∏aᵢ) | Exponential - Not practical |
| Optimized | O(M log M + M·N) | O(M) | Polynomial - Practical |
| Mathematical | O(M log M) | O(M) | Best - Recommended |

Where:
- M = Total number of unique numbers across all lists
- N = Number of friends
- aᵢ = Size of friend i's list

### Sample Complexity Analysis

For the example:
- N = 3 friends
- Lists: [3, 3, 3] numbers each
- Brute force: 3³ = 27 combinations
- Optimized: 9 log 9 + 9·3 = 19 + 27 = 46 operations

## 🚀 Getting Started

### Quick Start
```bash
# Clone and setup
git clone <repository-url>
cd backend/kth-largest-game

# Run with sample input
python solution.py < input.txt

# Run tests
python -m pytest tests/ -v

# Performance benchmark
python utils/benchmark.py
```

### Input Format Validation
```python
def validate_input(lines):
    """Validate input format and constraints."""
    t = int(lines[0])
    assert 1 <= t <= 5, "Invalid number of test cases"
    
    line_idx = 1
    for _ in range(t):
        n, k = map(int, lines[line_idx].split())
        assert 1 <= n <= 1000, "Invalid N"
        assert 1 <= k <= n, "Invalid K"
        
        for i in range(n):
            line_idx += 1
            parts = list(map(int, lines[line_idx].split()))
            a_i = parts[0]
            numbers = parts[1:]
            assert len(numbers) == a_i, f"Inconsistent list size for friend {i}"
        
        line_idx += 1
```

## 💡 Implementation Tips

### Optimization Strategies
1. **Pruning**: Eliminate impossible candidates early
2. **Sorting**: Sort numbers to enable binary search operations
3. **Memoization**: Cache intermediate results for repeated subproblems
4. **Early Termination**: Stop when solution bounds are reached

### Mathematical Insights
```python
def count_ways_to_achieve_kth(target_num, target_list, lists, k):
    """
    Count the number of ways target_num can be the K-th largest.
    
    For target_num to be K-th largest:
    1. Exactly (k-1) friends must select numbers > target_num
    2. Friend with target_list must select target_num
    3. Remaining friends can select any valid numbers
    """
    # Get lists of friends who can select numbers > target_num
    larger_options = []
    for i, lst in enumerate(lists):
        if i != target_list:
            larger_count = sum(1 for x in lst if x > target_num)
            larger_options.append(larger_count)
    
    # Use dynamic programming to count valid selections
    return count_combinations(larger_options, k-1)
```

## 🏆 Evaluation Criteria

| Criterion | Weight | Description |
|-----------|---------|-------------|
| **Correctness** | 35% | All test cases pass, handles edge cases |
| **Algorithm Efficiency** | 25% | Optimal time/space complexity |
| **Code Quality** | 20% | Clean, readable, maintainable code |
| **Problem Analysis** | 10% | Understanding of combinatorial aspects |
| **Testing** | 10% | Comprehensive test coverage |

## 🔗 Advanced Extensions

### Bonus Challenges
1. **Dynamic K**: Handle queries with different K values efficiently
2. **Updates**: Support adding/removing numbers from friend lists
3. **Probability**: Calculate probability distribution of K-th largest values
4. **Visualization**: Create visual representation of solution space

### Mathematical Connections
- **Combinatorics**: Stars and bars, inclusion-exclusion principle
- **Graph Theory**: Model as selection constraints
- **Dynamic Programming**: Optimal substructure properties

## 📚 Resources

- [Combinatorics Fundamentals](https://en.wikipedia.org/wiki/Combinatorics)
- [Order Statistics](https://en.wikipedia.org/wiki/Order_statistic)
- [Dynamic Programming Patterns](https://leetcode.com/discuss/general-discussion/458695/dynamic-programming-patterns)
- [Algorithm Design Manual](https://www.algorist.com/)

---

<div align="center">
  <strong>Master combinatorial complexity! 🎯</strong><br>
  <em>Where mathematics meets algorithmic elegance.</em>
</div>