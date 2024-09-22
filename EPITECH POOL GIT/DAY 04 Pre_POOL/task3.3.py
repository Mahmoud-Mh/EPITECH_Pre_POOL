# Task 3.3: Vigenère Cipher encryption and decryption
def vigenere_cipher(text, key, decrypt=False):
    result = []
    key = key.lower()
    key_indices = [ord(char) - ord('a') for char in key]
    for i, char in enumerate(text):
        if char.isalpha():
            shift = key_indices[i % len(key)]
            if decrypt:
                shift = -shift
            if char.islower():
                result.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
            else:
                result.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
        else:
            result.append(char)
    return ''.join(result)

message = input("Enter the message to encrypt/decrypt: ")
key = input("Enter the key: ")
encrypt_or_decrypt = input("Type 'e' to encrypt or 'd' to decrypt: ")

if encrypt_or_decrypt == 'e':
    print(f"Encrypted message: {vigenere_cipher(message, key)}")
elif encrypt_or_decrypt == 'd':
    print(f"Decrypted message: {vigenere_cipher(message, key, decrypt=True)}")
