# Task 4: Count occurrences of specific words in both directions
import re

def count_occurrences(text, words):
    text = text.lower()
    count = 0
    for word in words:
        # Count occurrences of word and its reverse
        count += len(re.findall(word.lower(), text))
        count += len(re.findall(word[::-1].lower(), text))
    return count

text = "thE Cat’s tactic wAS tO surpRISE thE mIce iN tHE gArdeN"
words = ["Cat", "Garden", "Mice"]
print(count_occurrences(text, words))  # Output: 4
