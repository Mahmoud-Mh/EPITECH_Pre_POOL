# Task 2.2: Repeat each character of the string twice
string = input("Enter a string: ")
output = "".join([char * 2 for char in string])
print(output)
