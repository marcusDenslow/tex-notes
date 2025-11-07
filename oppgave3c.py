import numpy as np

def f(x):
    """Funksjonen f(x) = sqrt(1 - x^2)"""
    return np.sqrt(1 - x**2)

def riemann_sum(a, b, n):
    """Beregner Riemann-sum med n rektangler"""
    delta_x = (b - a) / n
    total = 0
    for i in range(1, n + 1):
        x_i = a + i * delta_x
        total += f(x_i) * delta_x
    return total

# Finn b slik at integral fra -1 til b er 1
target_value = 1.0
n = 10000  # Bruk mange rektangler for god presisjon

# Binaer sok
left, right = -1, 1
tolerance = 1e-6

print(f"Sokker etter b slik at integral fra -1 til b = {target_value}")
print("=" * 60)

iterations = 0
while right - left > tolerance:
    iterations += 1
    b_mid = (left + right) / 2
    integral = riemann_sum(-1, b_mid, n)

    print(f"Iterasjon {iterations}: b = {b_mid:.8f}, integral = {integral:.8f}")

    if integral < target_value:
        left = b_mid
    else:
        right = b_mid

b_final = (left + right) / 2
integral_final = riemann_sum(-1, b_final, n)

print("\n" + "=" * 60)
print(f"Resultat: b ≈ {b_final:.8f}")
print(f"Integral fra -1 til {b_final:.8f} = {integral_final:.8f}")
