"""Math236 Honors Option Project Part 3.

Author: Spencer Wilford
Version: 05/02/2025
"""

import math


def compute_f_coefs(f0, num_coefs, exponent):
    """Computes the coefficients for the solution of f'(x) = f(x)^exponent.

    Args:
        f0 (float or int): The initial value f(0).
        num_coefs (int): The total number of coefficients to compute (including f(0)).
        exponent (int): The power m in the differential equation f'(x) = f(x)^m.

    Returns:
        list: List of coefficients for f(x).
    """
    f = [f0]  # Start with the constant term f(0)
    pows = {1: f}  # Creates a dict, keys corresponding to each power and assigns empty lists

    for e in range(2, exponent + 1):
        # Sets each constant term
        pows[e] = [f0 ** e]

    f.append(pows[exponent][0])  # Adds the a1 term

    for k in range(1, num_coefs - 1):
        # Build the k degree term of each power
        for e in range(2, exponent + 1):
            coef = 0
            for j in range(k + 1):
                coef += pows[e - 1][j] * f[k - j]
            pows[e].append(coef)

        # Calculates the next coefficient
        f.append(pows[exponent][k] / (k + 1))

    return f


def evaluate(coefs, x):
    """Evaluates a polynomial at a given x using Horner's method.

    The polynomial is assumed to be in the form:
       f(x) = f0 + f1*x + f2*x^2 + ... + fn*x^n.

    Args:
        coefs (list): List of coefficients [f0, f1, f2, ..., fn].
        x (float or int): The point where the polynomial is evaluated.

    Returns:
        float or int: The value of the polynomial f(x).
    """
    result = 0
    for coef in reversed(coefs):
        result = result * x + coef
    return result


def expected_solution(f0, x, exponent):
    """Closed form solution y = f0 / (1 - f0 * x).

    Args:
        f0 (float or int): The initial value f(0).
        x (float or int): The point where the solution is evaluated.
        exponent (int): The power.

    Returns:
        float or int: The solution.
    """
    if exponent == 1:
        return f0 * math.exp(x)
    return (f0**(1-exponent) + (1-exponent)*x) ** (1/(1-exponent))


if __name__ == "__main__":
    f0 = float(input("Enter f(0): "))
    n = int(input("How many coefficients? "))
    while (n < 1):
        print("The number of coefficients must be 1 or above.")
        n = int(input("How many coefficients? "))
    exponent = int(input("To what power? "))
    while (exponent < 2):
        print("The exponent must be 2 or above")
        exponent = int(input("To what power? "))

    coefs = compute_f_coefs(f0, n, exponent)

    print("\nCoefficients:")
    for i, a in enumerate(coefs):
        print(f"  a{i} = {a}")

    x = float(input("\nEnter a test value for x: "))
    evaluated_solution = evaluate(coefs, x)
    test_solution = expected_solution(f0, x, exponent)
    error = abs(evaluated_solution - test_solution)

    print(f"\nf({x}) at (n={n}): {evaluated_solution}")
    print(f"f({x}) test solution: {test_solution}")
    print(f"Error: {error}")
