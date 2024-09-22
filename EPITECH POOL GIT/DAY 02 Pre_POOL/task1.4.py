# Task 1.4: Check the behavior when dividing by 0
try:
    print(84 / (8 + (-3) + (-7) + 2))  # Division by zero?
except ZeroDivisionError:
    print("Division by zero error!")
