# Task 3.5: Extract first word from each sentence and join them
text = "This is a test. Is it possible to fly? Good things come to those who never give up."
sentences = text.split(". ")
first_words = [sentence.split()[0].capitalize() for sentence in sentences if sentence]
result = " ".join(first_words)
print(result)  # Output: "This Is Good"
