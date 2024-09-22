# Task 2.1: Compute 1 + 11 + 111 + ... + 111111111
num_str = ''
total = 0
for i in range(1, 10):
    num_str += '1'
    total += int(num_str)
print(total)

# Compute powers of the result
for power in range(2, 8):
    print(f"Power {power}: {total ** power}")
