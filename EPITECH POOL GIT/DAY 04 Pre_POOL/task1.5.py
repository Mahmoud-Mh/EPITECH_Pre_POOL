# Task 1.5: Check various conditions for the input number
number = int(input("Enter an integer: "))
if number == 42 or number <= 21 or number % 2 == 0 or (number // 2) < 21:
    print("OK")
elif number % 2 != 0 and number >= 45:
    print("OK")
else:
    print("You got it wrong, my poor friend!")
