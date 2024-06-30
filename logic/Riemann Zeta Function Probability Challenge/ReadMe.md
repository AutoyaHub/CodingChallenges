# Riemann Zeta Function and Probability Mass Function

You are given the Riemann zeta function \( \zeta(s) \), which converges for all \( s > 1 \), where \( s \) is a real number. The Riemann zeta function is defined as:

$$
\zeta(s) = \sum_{n=1}^{\infty} \frac{1}{n^s}
$$

Given a random variable \( x \), we define a probability mass function 

$$
P(x = n) = \frac{1}{n^s \cdot \zeta(s)}
$$ 

where \( n \geq 1 \) and \( n \) is an integer.

## Task 1: Validity of the Probability Mass Function

Show that \( P(x = n) \) is a valid probability mass function. Specifically, demonstrate that the sum of \( P(x = n) \) over all possible \( n \) from 1 to infinity is equal to 1.

## Task 2: Probability of Divisibility by \( k \)

Given an integer \( k \geq 2 \), find \( P(x) \) where \( x \) is divisible by \( k \).

## Task 3: Intersection of Events

Let \( E_k \) be the event that \( x \) is divisible by \( k \).

1. Determine \( P(E_2 \cap E_3) \).
2. Follow-up: What is the probability of the intersection of \( E_p \) over all primes \( p \)?

   **Hint:** Consider the probability of the complement of the intersection of \( E_p \) not happening over all primes.
