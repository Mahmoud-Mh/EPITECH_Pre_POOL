# Task 4.2: Compute Pi using the second formula
pi_approx = 0
n = 1
while n <= 13:  # Adjust to reach desired precision
    pi_approx += 12 / ((6 * n) ** 2)
    n += 1
pi_approx = 3 + pi_approx
print(round(pi_approx, 6))
