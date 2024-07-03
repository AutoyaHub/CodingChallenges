import sympy as sp

def probability_mass_function_validity(s):
    """
    Check the validity of the probability mass function P(x = n).

    Parameters:
    s (float): The parameter 's' for the probability mass function.

    Returns:
    sympy.Expr: The sum of the probability mass function P(x = n) over all n from 1 to infinity.
    """
    n = sp.Symbol('n', integer=True, positive=True)
    P_x_n = 1 / (n**s * sp.zeta(s))
    sum_P_x_n = sp.summation(P_x_n, (n, 1, sp.oo))
    return sum_P_x_n

def probability_mass_function_validity_for_all_s():
    """
    Check the validity of the probability mass function P(x = n) for all positive integer values of s.

    Returns:
    sympy.Expr: The sum of the probability mass function P(x = n) over all n from 1 to infinity, expressed symbolically for any s.
    """
    n = sp.Symbol('n', integer=True, positive=True)
    s = sp.Symbol('s', integer=True, positive=True)
    P_x_n = 1 / (n**s * sp.zeta(s))
    sum_P_x_n = sp.summation(P_x_n, (n, 1, sp.oo))
    return sum_P_x_n

def probability_divisibility_by_k(s, k):
    """
    Calculate the probability that x is divisible by k.

    Parameters:
    s (float): The parameter 's' for the probability mass function.
    k (int): The divisor.

    Returns:
    sympy.Expr: The probability that x is divisible by k.
    """
    n = sp.Symbol('n', integer=True, positive=True)
    P_x_n = 1 / (n**s * sp.zeta(s))
    P_x_kn = P_x_n.subs(n, k * n)
    sum_P_x_kn = sp.summation(P_x_kn, (n, 1, sp.oo))
    P_E_k = sp.simplify(sum_P_x_kn)
    return P_E_k

def probability_intersection_E2_E3(s):
    """
    Calculate the probability that x is divisible by both 2 and 3.

    Parameters:
    s (float): The parameter 's' for the probability mass function.

    Returns:
    sympy.Expr: The probability that x is divisible by both 2 and 3.
    """
    lcm_2_3 = 6
    P_E_2_cap_E_3 = 1 / (lcm_2_3**s)
    return P_E_2_cap_E_3

def probability_intersection_all_primes(s):
    """
    Calculate the probability of the intersection of E_p over all primes p.

    Parameters:
    s (float): The parameter 's' for the probability mass function.

    Returns:
    sympy.Expr: The product of (1 - 1/p^s) over all primes p.
    """
    primes = list(sp.primerange(2, 100))
    product_term = [1 - 1 / (p**s) for p in primes]
    intersection_prob = sp.prod(product_term)
    return intersection_prob

def main():
  
    s = sp.Float(5)  # Example value for s

    # Task 1: Validity of the probability mass function
    validity = probability_mass_function_validity(s)
    print("Sum of P(x = n) from n=1 to infinity (should be 1):", validity.evalf())

    validity_all_s = probability_mass_function_validity_for_all_s()
    print("Sum of P(x = n) from n=1 to infinity (should be 1):", validity_all_s.evalf())
    
    # Task 2: Probability of divisibility by k
    k_value = 6  # Example value for k
    P_E_k = probability_divisibility_by_k(s, k_value)
    print(f"Probability that x is divisible by {k_value}:", P_E_k.evalf())
    
    # Task 3: Probability of intersection E2 and E3
    P_E_2_E_3 = probability_intersection_E2_E3(s)
    print("Probability that x is divisible by both 2 and 3:", P_E_2_E_3.evalf())
    
    # Follow-up: Probability of the intersection of E_p over all primes
    intersection_all_primes = probability_intersection_all_primes(s)
    print("Probability of the intersection of E_p over all primes:", intersection_all_primes.evalf())

if __name__ == "__main__":
    main()
