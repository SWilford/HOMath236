"""Math236 Honors Option Project Part 2.

Author: Spencer Wilford
Version: 04/07/2025
"""


def cauchy_product_deg(coef_a, coef_b, degree):
    """Return the coefficient for x^degree.

    Args:
        coef_a (list): Coefficients for polynomial a.
        coef_b (list): Coefficients for polynomial b.
        degree (int): The degree for which to return the coefficient from the product.

    Returns:
        The coefficient corresponding to x^degree.
    """
    result = 0
    for j in range(degree + 1):
        if j < len(coef_a) and (degree - j) < len(coef_b):
            result += coef_a[j] * coef_b[degree - j]
    return result


def compute_f_coefs(f0, num_coefs):
    """Computes the coefficients for f(x).

    Calculates via  f(k+1) = cauchy_product_deg(f, f, k) / (k+1)

    Args:
        f0 (float or int): The initial value f(0).
        num_coefs (int): The total number of coefficients to compute (including f(0)).

    Returns:
        list: List of coefficients for f(x).
    """
    f = [f0]  # Start with the constant term f(0)
    for k in range(0, num_coefs - 1):
        next_coef = cauchy_product_deg(f, f, k) / (k + 1)
        f.append(next_coef)
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


def analytic_solution(f0, x):
    """Closed form solution y = f0 / (1 - f0 * x).

    Args:
        f0 (float or int): The initial value f(0).
        x (float or int): The point where the solution is evaluated.

    Returns:
        float or int: The solution.
    """
    return f0 / (1 - f0 * x)


if __name__ == "__main__":
    f0 = float(input("Enter f(0): "))
    n = int(input("How many coefficients? "))
    coefs = compute_f_coefs(f0, n)

    print("\nCoefficients:")
    for i, a in enumerate(coefs):
        print(f"  a{i} = {a}")

    x = float(input("\nEnter a test value for x: "))
    evaluated_solution = evaluate(coefs, x)
    test_solution = analytic_solution(f0, x)
    error = abs(evaluated_solution - test_solution)

    print(f"\nf({x}) at (n={n}): {evaluated_solution}")
    print(f"f({x}) test solution: {test_solution}")
    print(f"Error: {error}")
