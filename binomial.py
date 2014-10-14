import math

# Reimplemented because we couldn't get scipy to install on the lab machine

def _choose(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

def probability_mass(k, n, p):
    return _choose(n, k) * p ** k * (1 - p) ** (n - k)
