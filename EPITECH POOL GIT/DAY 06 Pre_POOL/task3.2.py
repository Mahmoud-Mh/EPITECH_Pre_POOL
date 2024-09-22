# Task 3.2

def funA(s, n):
    return sum(1 for c in s if c.islower()) >= n
# Write a generic function that checks if a password is valid.
def check_password(condition_function, n, password):
    if condition_function(password, n):
        return True
    return False

# Example usage
print(check_password(funA, 4, "mysecretpassword"))
