# Task 2.1
# Write a recursive function that tests if a string is a palindrome.
def is_palindrome(s):
    s = ''.join(c for c in s if c.isalnum()).lower()
    if len(s) <= 1:
        return True
    return s[0] == s[-1] and is_palindrome(s[1:-1])

# Example usage
print(is_palindrome("A man, a plan, a canal, Panama"))
