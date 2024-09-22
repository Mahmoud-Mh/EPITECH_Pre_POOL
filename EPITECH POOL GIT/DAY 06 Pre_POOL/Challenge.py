# CHALLENGE
# Write a little program that computes the power function as fast as possible.
import time

def power_function(base, exponent):
    if exponent == 0:
        return 1
    return base * power_function(base, exponent - 1)

# Measure time for 4284
start_time = time.time()
result_4284 = power_function(4, 284)
print("Result for 4^284:", result_4284)
print("Time taken:", time.time() - start_time)

# Measure time for 42168
start_time = time.time()
result_42168 = power_function(4, 2168)
print("Result for 4^2168:", result_42168)
print("Time taken:", time.time() - start_time)
