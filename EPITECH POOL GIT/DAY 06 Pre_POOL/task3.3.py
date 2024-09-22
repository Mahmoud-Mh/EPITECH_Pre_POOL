# Task 3.3
# Add an error management system to your previous function.
def check_password(condition_function, n, password):
    try:
        if condition_function(password, n):
            return True
        return False
    except Exception as e:
        print("An error occurred:", e)
        return False
