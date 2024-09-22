# Task 3.3: Calculate the sum of the digits of a number
def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

print(sum_of_digits(123434565))
print(sum_of_digits(345567426))
print(sum_of_digits(44490320097))
