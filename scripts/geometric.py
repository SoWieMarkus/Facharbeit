import math
import argparse


def estimate_pi_with_polygon(iterations: int) -> float:
    """
    Estimate the value of π using a geometric approach based on inscribed polygons.
    The method starts with a square inscribed in a circle and iteratively refines the estimate
    by doubling the number of sides of the polygon.
    The formula used is:
    π ≈ (number of sides * side length) / 2
    where side length is calculated based on the previous iteration's side length.
    """
    current_amount_sides = 4
    current_side_length = math.sqrt(2)
    current_pi_estimate = current_amount_sides * current_side_length / 2

    for _ in range(1, iterations):
        current_amount_sides *= 2
        current_side_length = math.sqrt(2 - math.sqrt(4 - current_side_length ** 2))
        current_pi_estimate = current_amount_sides * current_side_length / 2

    return current_pi_estimate


def main():
    parser = argparse.ArgumentParser(description="Estimate the value of Pi using a geometric approach method.")
    parser.add_argument("--iterations", default=10, type=int, help="Number of iterations to refine the estimate")
    args = parser.parse_args()

    pi_estimate = estimate_pi_with_polygon(args.iterations)
    print(f"Estimated value of Pi: {pi_estimate} with {args.iterations} iterations")


if __name__ == "__main__":
    main()



