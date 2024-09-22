#way to combine lists using unpacking
my_first_list = [7, 8, 9]
my_second_list = [4, 5, 6]
my_first_list = [*my_first_list, *my_second_list]  # Unpacking both lists
print("Combined list using unpacking:", my_first_list)
