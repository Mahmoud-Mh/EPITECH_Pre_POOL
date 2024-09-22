# Zip first and last names
first_name = ["Jackie", "Bruce", "Arnold", "Sylvester"]
last_name = ["Stallone", "Schwarzenegger", "Willis", "Chan"]
magic = list(zip(first_name, last_name[::-1]))  # Zips first names with reversed last names
print("Zipped names:", magic)
print("First magic pair:", magic[0])
print("Last magic pair:", magic[3])
print("First name of second pair:", magic[1][0])
print("Last name of first pair:", magic[0][1])
print("Third magic pair:", magic[2])
