"""Math236 Honors Option Project Part 1.

Author: Spencer Wilford
Version: 03/24/25
"""


def get_coef_c(coef_a, coef_b, degree):
    """Get the list of coefficient in the polynomial c.

    Returns a list of the coefficients of the polynomial c that
    is resultant from multiplying polynomial a and polynomial b
    up to the the degree specified.

    Args:
        coef_a (list): the list of coefficients in polynomial a
        coef_b (list): the list of coefficients in polynomial b
        degree (int): the degree of the polynomial

    Returns:
        list: List of the coefficients of the polynomial c

    Raises:
        ValueError: If the polynomials provided are different degrees.
        ValueError: If the degree of polynomial a does not match the provided degree
        ValueError: If the degree of polynomial b does not match the provided degree
    """
    if (len(coef_a) != len(coef_b)):
        raise ValueError("Polynomials must be of the same degree")
    if (len(coef_a) - 1 != degree):
        raise ValueError("The degree of polynomial a does not match the provided degree.")
    if (len(coef_b) - 1 != degree):
        raise ValueError("The degree of polynomial b does not match the provided degree.")

    coef_c = [0] * (degree + 1)

    for i in range(degree + 1):  # Covers each coefficient from c0 to c degree
        for j in range(i + 1):  # Sums each value of aj + b(i-1)
            if j < len(coef_a) and (i - j) < len(coef_b):
                coef_c[i] += coef_a[j] * coef_b[i - j]

    return coef_c


if __name__ == "__main__":
    a = []
    b = []

    degree = int(input("Enter the degree of the polynomials: "))
    print()

    for i in range(degree + 1):
        a.append(int(input("Enter a" + str(i) + ": ")))

    print()

    for i in range(degree + 1):
        b.append(int(input("Enter b" + str(i) + ": ")))

    print()
    print("Coefficients of polynomial c: " + str(get_coef_c(a, b, degree)))
