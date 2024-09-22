import sys
import random

def load_words(filename):
    """Load words from a specified file and return a list of words."""
    try:
        with open(filename, 'r') as file:
            words = [line.strip() for line in file if line.strip()]
        return words
    except FileNotFoundError:
        print("Error: The file does not exist.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def get_random_word(words):
    """Return a random word from the list of words."""
    return random.choice(words)

def update_best_score(word, attempts):
    """Update the best score if the current score is better."""
    try:
        with open('best_scores.txt', 'a') as score_file:
            score_file.write(f"{word} - {attempts} attempts\n")
        print(f'Best ever!!! You\'ve guessed "{word}" in {attempts} attempts.')
    except Exception as e:
        print(f"Error: {e}")

def end_game(word, attempts, best_attempts):
    """Handle the end of the game and score tracking."""
    if attempts < best_attempts:
        update_best_score(word, attempts)
    else:
        print(f'You\'ve guessed "{word}" in {attempts} attempts. The record is {best_attempts} attempts.')

def main():
    if len(sys.argv) != 2:
        print("Error: missing argument. Please provide a filename.")
        sys.exit(1)

    filename = sys.argv[1]
    words = load_words(filename)
    word_to_guess = get_random_word(words)

    print(f"Word to guess: {word_to_guess}")  # For testing, display the word

    # Additional game logic goes here (e.g., gameplay loop, user input, etc.)
    # Example: simulate attempts
    attempts = 0  # Replace with actual logic
    best_attempts = 10  # Example best score; replace with actual logic
    end_game(word_to_guess, attempts, best_attempts)

if __name__ == "__main__":
    main()
