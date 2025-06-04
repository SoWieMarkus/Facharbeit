from decimal import Decimal, getcontext
import math

# Set precision: a few digits more to avoid rounding errors
getcontext().prec = 1050


def estimate_pi(digits: int) -> Decimal:
    """ 
    Estimate the value of π using the Chudnovsky algorithm.
    This algorithm converges very quickly and is suitable for calculating π to a large number of digits.
    """
    C = 426880 * Decimal(10005).sqrt()
    M = 1
    L = 13591409
    X = 1
    K = 6
    S = L

    for i in range(1, digits):
        M = (M * (K**3 - 16*K)) // (i**3)
        L += 545140134
        X *= -262537412640768000
        S += Decimal(M * L) / X
        K += 12

    pi = C / S
    return pi


def main():
    # Compute π to 1000 digits
    pi_1000 = estimate_pi(1000)

    # Print first 1000 digits
    pi_str = str(pi_1000)[:1001]  # includes "3."
    print(pi_str)

    
if __name__ == "__main__":
    main()

