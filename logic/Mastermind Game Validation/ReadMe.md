### Challenge: Mastermind Game Validation

Mastermind is a game played by two players. The first player decides a secret key, which is a sequence \((s_1, s_2, \ldots, s_k)\) where \(0 < s_i \le n\). The second player then makes guesses in rounds, each guess being a sequence \((g_1, g_2, \ldots, g_k)\). After each guess, the first player calculates the score, which is the number of positions \(i\) where \(g_i = s_i\).

For example, if the secret key is \((4, 2, 5, 3, 1)\) and the guess is \((1, 2, 3, 7, 1)\), the score is 2 because \(g_2 = s_2\) and \(g_5 = s_5\).

Given a sequence of guesses and their scores, determine if there exists at least one secret key that generates those exact scores.

#### Input Format:

- The first line of input contains a single integer \( C \) (\(1 \leq C \leq 100\)), the number of test cases.
- Each test case starts with a line containing three integers \( n \), \( k \), and \( q \) (\(1 \leq n, k \leq 11\); \(1 \leq q \leq 8\)).
- The next \( q \) lines each contain \( k \) integers representing a guess, followed by an integer representing the score for that guess. 

#### Output Format:

- For each test case, output "Yes" if there exists at least one secret key that generates those exact scores, otherwise output "No".

#### Sample Input:

```
2
4 4 2
2 1 2 2 0
2 2 1 1 1
4 4 2
1 2 3 4 4
4 3 2 1 1
```

#### Sample Output:

```
Yes
No
```

#### Explanation:

In the first test case:
- \( n = 4 \), \( k = 4 \), \( q = 2 \)
- Guesses and scores:
  - \((2, 1, 2, 2)\) with score 0
  - \((2, 2, 1, 1)\) with score 1

It is possible to find a secret key that matches these scores.

In the second test case:
- \( n = 4 \), \( k = 4 \), \( q = 2 \)
- Guesses and scores:
  - \((1, 2, 3, 4)\) with score 4
  - \((4, 3, 2, 1)\) with score 1

It is not possible to find a secret key that matches these scores.

### Constraints:

- \( 1 \leq C \leq 100 \)
- \( 1 \leq n, k \leq 11 \)
- \( 1 \leq q \leq 8 \)
- \( 1 \leq g_{i,j} \leq n \) for all \( 1 \leq i \leq q \), \( 1 \leq j \leq k \)
- \( 0 \leq b_i \leq k \)

### Solution Outline:

1. For each test case, read the values of \( n \), \( k \), and \( q \).
2. Read each guess and its corresponding score.
3. Check if there exists a secret key that could produce the given scores for the provided guesses. This can be done by brute-force generating all possible keys (since \( n \) and \( k \) are small) and checking if they match all the guess-score pairs.
4. Print "Yes" if at least one valid secret key exists; otherwise, print "No".

This problem can be efficiently solved using a brute-force approach due to the constraints on \( n \) and \( k \).