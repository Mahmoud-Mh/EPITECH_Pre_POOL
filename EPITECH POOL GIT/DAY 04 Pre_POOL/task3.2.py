# Function to handle Caesar Cipher encryption and decryption
# It shifts each letter by a certain key
def caesar_cipher(text, key):
    result = ""  # This will hold the final result after shifting

    # Loop through each character in the provided text
    for char in text:
        # Check if the character is a letter (we won't shift numbers or punctuation)
        if char.isalpha():
            # Shift the character's ASCII value by the key
            shifted = ord(char) + key
            
            # Handle lowercase letters separately from uppercase letters
            if char.islower():
                # Wrap around if the shift goes past 'z'
                result += chr((shifted - ord('a')) % 26 + ord('a'))
            else:
                # Wrap around if the shift goes past 'Z'
                result += chr((shifted - ord('A')) % 26 + ord('A'))
        else:
            # If it's not a letter (e.g., a space or punctuation), just keep it as is
            result += char
    
    return result

# Function to decipher an encrypted message using the Caesar Cipher
def caesar_decipher(ciphertext, key):
    # Decryption is just shifting by the negative of the encryption key
    return caesar_cipher(ciphertext, -key)

# Ask the user for the encrypted message
encrypted_message = input("Enter the encrypted message: ")

# Ask for the key (make sure it's an integer between 1 and 25)
key = int(input("Enter the decryption key (1-25): "))

# Use the caesar_decipher function to decrypt the message
decrypted_message = caesar_decipher(encrypted_message, key)

# Print the final decrypted message
print(f"Decrypted message: {decrypted_message}")
