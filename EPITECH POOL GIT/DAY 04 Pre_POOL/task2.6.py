# Task 2.6: Display multiples of each integer from 2 to n/2 in descending order
n = int(input("Enter a number n: "))

for i in range(2, n//2 + 1):
    multiples = [x for x in range(i, n, i)][::-1]
    print(" ".join(map(str, multiples)))
