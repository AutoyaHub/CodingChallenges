### Challenge: Binary Beauty Game

In this game, the "beauty" of a number \( X \) is defined as the number of 1s in its binary representation.

Two players are playing a game with a number \( n \) written on a blackboard. The game proceeds as follows:

1. A player chooses an integer \( k \) such that \( 0 \le k \) and \( 2^k < n \).
2. The chosen \( k \) must ensure that \( n - 2^k \) has the same beauty as \( n \).
3. The player then replaces \( n \) on the blackboard with \( n - 2^k \).
4. Players take turns alternately.

The player who cannot make a valid move loses the game.

The first player starts the game. Assuming both players play optimally, determine the winner.

#### Input:

- The first line contains an integer \( T \), the number of test cases. \( 0 \le T \le 5 \).
- The following \( T \) lines each contain an integer \( n \) (\( 1 \le n \le 10^9 \)).

#### Output:

- For each test case, print "First Player" if the first player can guarantee a win, and "Second Player" otherwise.

#### Example:

##### Input
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

##### Output
```
Second Player
First Player
First Player
Second Player
Second Player
First Player
Second Player
```

#### Explanation:

- For \( n = 1 \): The first player cannot make a move, so the second player wins.
- For \( n = 2 \): The first player can subtract \( 2^0 = 1 \) to make \( n = 1 \). The second player cannot make a move, so the first player wins.

### Constraints

- \( 1 \le n \le 10^9 \)
- \( 0 \le T \le 5 \)

Consider this modified and unique version of the problem to evaluate the winner based on the optimal plays of both players.