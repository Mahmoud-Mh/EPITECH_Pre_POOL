import random

# List of possible words to guess
words = ["hangman", "python", "challenge", "programming", "development"]

# Function to pick a random word from the list
def get_random_word():
    return random.choice(words)

# Function to display the current state of the guessed word
def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

# Function to play the hangman game
def play_hangman():
    word = get_random_word().upper()  # Randomly select a word and convert to uppercase
    guessed_letters = set()  # Keep track of guessed letters
    penalties = 0  # Initialize penalties

    print(f"Guess the word: {display_word(word, guessed_letters)} / {penalties} penalties")

    while penalties < 22:  # Maximum penalties before losing
        guess = input("Enter a letter or word: ").strip().upper()
        
        if len(guess) == 1:  # If the guess is a letter
            if guess in word:
                occurrences = word.count(guess)
                guessed_letters.add(guess)
                penalties += 1
                print(f"Found {occurrences} '{guess}'")
            else:  # If the letter is not in the word
                penalties += 3
                print(f"No '{guess}' found")
        elif len(guess) == len(word):  # If the guess is a word
            if guess == word:
                print(f"{guess}: correct guess - {penalties} penalties")
                break
            else:
                penalties += 5
                print(f"{guess}: incorrect guess")
        else:
            print("Invalid input. Please enter a single letter or the full word.")

        # Display the current state of the word and penalties
        print(f"{display_word(word, guessed_letters)} / {penalties} penalties")
    
    if penalties >= 22:
        print("Game Over! The word was:", word)

# Start the game
if __name__ == "__main__":
    play_hangman()
