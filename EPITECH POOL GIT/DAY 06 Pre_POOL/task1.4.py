# Task 1.4
# Write a function that takes the number of sandwiches to prepare as a parameter and displays as many sandwiches as requested.
def bread():
    print("<////////// >")

def lettuce():
    print("~~~~~~~~~~~~")

def tomato():
    print("O O O O O O")

def ham():
    print("=============")

def prepare_sandwiches(num_sandwiches):
    if num_sandwiches <= 0:
        print("I can’t do this")
        return
    for _ in range(num_sandwiches):
        bread()
        lettuce()
        tomato()
        ham()
        ham()
        bread()

# Example usage
prepare_sandwiches(5)
