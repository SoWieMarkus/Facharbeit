import argparse
import random


def are_numbers_coprime(a: int, b: int) -> bool:
    """Check if two numbers are coprime (i.e., their greatest common divisor is 1)."""
    while b:
        a, b = b, a % b
    return a == 1


def generate_random_number_pairs(amount: int, max_value: int) -> list[tuple[int, int]]:
    """Generate a list of random pairs of integers."""
    return [(random.randint(1, max_value), random.randint(1, max_value)) for _ in range(amount)]


def estimate_pi(pairs: list[tuple[int, int]]) -> float:
    """
    Estimate the value of π using the probaility that two random integers are coprime.

    The probaility that two random integers are coprime is 6 / π^2.
    By generating random pairs of integers and checking how many of them are coprime,
    we can estimate π using the formula:
    π ≈ (6 / (number of coprime pairs / total pairs)) ** 0.5
    """
    if not pairs:
        raise ValueError("The list of pairs cannot be empty.")
    
    coprime_count = sum(1 for a, b in pairs if are_numbers_coprime(a, b))
    ratio = coprime_count / len(pairs)
    if ratio == 0:
        raise ValueError("No coprime pairs found, cannot estimate Pi.")
    return (6 / ratio) ** 0.5


def main():
    parser = argparse.ArgumentParser(description="Estimate the value of Pi using the coprime method.")
    parser.add_argument("--amount", default=1000, type=int, help="Number of random pairs of integers to generate")
    parser.add_argument("--max_value", default=1000, type=int, help="Maximum value for the random integers")
    args = parser.parse_args()
    
    pairs = generate_random_number_pairs(args.amount, args.max_value)
    pi_estimate = estimate_pi(pairs)
    
    print(f"Estimated value of Pi: {pi_estimate} with {args.amount} random pairs of integers up to {args.max_value}")

if __name__ == "__main__":
    main()