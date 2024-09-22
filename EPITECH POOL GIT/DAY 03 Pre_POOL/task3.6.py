# Task 3.6: Count letter frequency and infer language
from collections import Counter

text = "This is an example text where we count letters and frequencies."
text = text.lower().replace(" ", "")  # Convert to lowercase and remove spaces
letter_counts = Counter(text)

print(letter_counts)  # Prints frequency of each letter
