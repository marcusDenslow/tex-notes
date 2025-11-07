import numpy as np

def f(x):
    """Funksjonen f(x) = sqrt(1 - x^2)"""
    return np.sqrt(1 - x**2)

def riemann_sum(a, b, n):
    """
    Beregner Riemann-sum for f(x) på intervallet [a, b] med n rektangler.
    Bruker høyre endepunkt (right Riemann sum).
    """
    delta_x = (b - a) / n
    total = 0

    for i in range(1, n + 1):
        x_i = a + i * delta_x
        total += f(x_i) * delta_x

    return total

# Beregn tilnærming med ulike verdier av n
a, b = -1, 1
n_values = [10, 100, 1000, 10000]

print("Tilnærming av arealet under f(x) = sqrt(1-x^2):")
print("=" * 50)
for n in n_values:
    areal = riemann_sum(a, b, n)
    print(f"n = {n:5d}: Areal ≈ {areal:.8f}")
