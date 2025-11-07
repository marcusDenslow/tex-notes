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


# Eksakt areal: halvsirkel med radius 1
eksakt_areal = np.pi / 2  # FIKSET: var π/3, skulle være π/2
print(f"Eksakt areal: {eksakt_areal:.10f}")
print(f"Dette er π/2 ≈ {eksakt_areal:.8f}\n")

# Finn minste n for 8 riktige siffer med increment av +1
target_accuracy = 0.5e-8

# Start fra et fornuftig sted (vet at det er rundt 300k-500k)
n_start = 300000

print(f"Soker fra n = {n_start:,} med inkrement av +1")
print("Dette kan ta litt tid...")
print("=" * 60)

n_final = None
for n in range(n_start, 1000000):
    approx = riemann_sum(-1, 1, n)
    error = abs(eksakt_areal - approx)

    # Print progress hver 10000
    if n % 10000 == 0:
        print(f"n = {n:7d}: Feil = {error:.2e}")

    if error < target_accuracy:
        n_final = n
        print(f"\nFUNNET! n = {n:,}")
        print(f"Feil = {error:.2e}")
        break

if n_final is None:
    print("\nFant ikke n innenfor sokeomradet!")
    n_final = 1000000

# Verifiser
approx_final = riemann_sum(-1, 1, n_final)
error_final = abs(eksakt_areal - approx_final)


print("\n" + "=" * 60)
print(f"\nEKSAKT minste n: {n_final:,}")
print(f"Tilnaerming: {approx_final:.10f}")
print(f"Feil: {error_final:.2e}")
print(f"\nDette gir 8 riktige siffer: {error_final < target_accuracy}")
print(f"\n(Rundet til naermeste 1000: {((n_final + 999) // 1000) * 1000:,})")
