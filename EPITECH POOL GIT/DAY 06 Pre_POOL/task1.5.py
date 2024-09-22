# Task 1.5
# Add a new parameter to your previous function for vegetarian sandwiches.
def bread():
    print("<////////// >")

def lettuce():
    print("~~~~~~~~~~~~")

def tomato():
    print("O O O O O O")

def ham():
    print("=============")
    
def prepare_sandwiches(num_sandwiches, vegetarian=False):
    if num_sandwiches <= 0:
        print("I can’t do this")
        return
    for _ in range(num_sandwiches):
        bread()
        lettuce()
        tomato()
        if not vegetarian:
            ham()
            ham()
        bread()

# Example usage
prepare_sandwiches(3, vegetarian=True)
