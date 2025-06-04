import random
import math
import argparse


def get_random_positions(amount: int, side_length: int) -> list[tuple[float, float]]:
    """Generate random positions within a square with side length `site_length`."""
    return [(random.uniform(0, side_length), random.uniform(0, side_length)) for _ in range(amount)]


def estimate_pi(positions: list[tuple[float, float]], radius: float) -> float:
    """Estimate the value of π using the Monte Carlo method based on a list of random positions."""
    if not positions:
        raise ValueError("The list of positions cannot be empty.")
    hits_inside_circle = sum(1 for x, y in positions if (x - radius) ** 2 + (y - radius) ** 2 <= radius ** 2)
    return 4 * hits_inside_circle / len(positions)


def main():
    parser = argparse.ArgumentParser(description="Estimate the value of Pi using the Monte Carlo method.")
    parser.add_argument("--amount", default=1000, type=int, help="Number of random positions to generate with in a square")
    parser.add_argument("--side_length", default=1.0, type=float, help="Length of the sides of the square (equals the radius of the circle)")
    args = parser.parse_args()
    
    positions = get_random_positions(args.amount, args.side_length)
    # we assume a quarter circle inscribed in a square, so the radius is equal to the side length
    pi_estimate = estimate_pi(positions, args.side_length)
    
    print(f"Estimated value of Pi: {pi_estimate} with {args.amount} random positions in a square of side length {args.side_length}")


if __name__ == "__main__":
    main()

