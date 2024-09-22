# Task 3.1
# Write 5 functions to check string conditions.
def funA(s, n):
    return sum(1 for c in s if c.islower()) >= n

def funB(s, n):
    return sum(1 for c in s if c.isupper()) >= n

def funC(s, n):
    return len(s) >= n

def funD(s, n):
    special_chars = "!@#$%^&*()_+-=[]{}|;:',.<>?/`~"
    return sum(1 for c in s if c in special_chars) >= n

def funE(s, n):
    return sum(1 for c in s if c.isdigit()) >= n
