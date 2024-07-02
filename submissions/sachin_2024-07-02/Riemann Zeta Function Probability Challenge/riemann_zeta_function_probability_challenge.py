import logging
from sympy import primerange

# Set up logging
logging.basicConfig(level=logging.INFO)

def riemann_zeta(s, terms=1000):
    """
    Calculate the Riemann zeta function for a given s using a finite number of terms.
    
    Args:
        s (float): The parameter s in the Riemann zeta function.
        terms (int): The number of terms to use in the series approximation.
    
    Returns:
        float: The value of the Riemann zeta function.
    """
    return sum(1 / (n ** s) for n in range(1, terms + 1))

def probability_mass_function(n, s):
    """
    Calculate the probability mass function P(x = n).
    
    Args:
        n (int): The value of the random variable x.
        s (float): The parameter s in the probability mass function.
    
    Returns:
        float: The probability P(x = n).
    """
    zeta_s = riemann_zeta(s)
    return 1 / (n ** s * zeta_s)

def validate_pmf(s, terms=1000):
    """
    Validate that the probability mass function sums to 1 over all possible n.
    
    Args:
        s (float): The parameter s in the probability mass function.
        terms (int): The number of terms to use in the validation.
    
    Returns:
        float: The sum of the probabilities over all n.
    """
    zeta_s = riemann_zeta(s)
    return sum(1 / (n ** s * zeta_s) for n in range(1, terms + 1))

def probability_divisible_by_k(k, s):
    """
    Calculate the probability that x is divisible by k.
    
    Args:
        k (int): The divisor.
        s (float): The parameter s in the probability mass function.
    
    Returns:
        float: The probability that x is divisible by k.
    """
    return 1 / k ** s

def probability_intersection_e2_e3(s):
    """
    Calculate the probability that x is divisible by both 2 and 3 (i.e., 6).
    
    Args:
        s (float): The parameter s in the probability mass function.
    
    Returns:
        float: The probability that x is divisible by 6.
    """
    return 1 / 6 ** s

def probability_intersection_all_primes(s, num_primes=100):
    """
    Calculate the probability of the intersection of E_p over the first num_primes primes p.
    
    Args:
        s (float): The parameter s in the probability mass function.
        num_primes (int): The number of primes to consider.
    
    Returns:
        float: The probability of the intersection of E_p over the considered primes.
    """
    primes = list(primerange(1, num_primes * 10))[:num_primes]
    product = 1.0
    for p in primes:
        product *= (1 - 1 / p ** s)
    return product

# Example usage:
if __name__ == "__main__":
    s = 2
    logging.info(f"Sum of PMF for s={s}: {validate_pmf(s)}")
    k = 3
    logging.info(f"Probability that x is divisible by {k} for s={s}: {probability_divisible_by_k(k, s)}")
    logging.info(f"Probability that x is divisible by both 2 and 3 for s={s}: {probability_intersection_e2_e3(s)}")
    logging.info(f"Probability of intersection over first 100 primes for s={s}: {probability_intersection_all_primes(s)}")
