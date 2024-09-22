# Task 3.5: Extract decimal part of a floating-point number
def decimal_part(number):
    return number - int(number)

print(decimal_part(12.24))
print(decimal_part(424242.8412))
