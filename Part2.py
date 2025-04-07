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


if __name__ == "__main__":
    f0_input = float(input("Enter the value for f(0): "))
    n = int(input("Enter the number of coefficients to compute: "))
    coefficients = compute_f_coefs(f0_input, n)
    print("The coefficients for f(x) are:")
    for i, coef in enumerate(coefficients):
        print(f"f({i}) = {coef}")
