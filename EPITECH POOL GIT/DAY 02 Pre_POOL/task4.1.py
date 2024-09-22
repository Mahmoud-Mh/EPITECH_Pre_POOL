# Task 4.1: Compute Pi using the series
pi_approx = 0
for i in range(1000000):  # More iterations for better accuracy
    pi_approx += (-1)**i / (2 * i + 1)
pi_approx *= 4
print(round(pi_approx, 6))
