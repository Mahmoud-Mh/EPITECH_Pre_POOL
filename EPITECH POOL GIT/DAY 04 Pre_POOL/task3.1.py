# Task 3.1: Caesar Cipher encryption
def caesar_cipher(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            shift = ord(char) + key
            if char.islower():
                result += chr((shift - ord('a')) % 26 + ord('a'))
            else:
                result += chr((shift - ord('A')) % 26 + ord('A'))
        else:
            result += char
    return result

message = input("Enter the message to encrypt: ")
key = int(input("Enter the key (1-25): "))
encrypted_message = caesar_cipher(message, key)
print(f"Encrypted message: {encrypted_message}")
