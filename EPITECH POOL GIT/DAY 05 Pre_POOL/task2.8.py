# Explain filtering with lambda
numbers = [42, 3, 4, 18, 3, 10]
filtered = list(filter(lambda x: x > 10, numbers))
print("Numbers greater than 10:", filtered)
