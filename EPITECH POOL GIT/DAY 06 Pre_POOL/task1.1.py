def f(x):
    return 2 * x + 1  # This function doubles x and adds 1

def g():
    return 7  # This function simply returns 7

# Calculate y using function f with an input of 2
y = f(2)
print(y)  # Output: 5

# Calculate y using function f with an input of 5 and add the result of g()
y = f(5) + g()
print(y)  # Output: 17 (11 from f(5) + 7 from g())
