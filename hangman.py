"""
Hangman Game
A beginner-friendly text-based word guessing game developed in Python.
Suitable for Python internship project submission.
"""

import random

# Predefined list of 5 words required for the game
WORDS = ["PYTHON", "COMPUTER", "PROGRAM", "STUDENT", "SOFTWARE"]

# Maximum allowed incorrect attempts
MAX_INCORRECT_ATTEMPTS = 6

# ASCII art stages representing the hangman for each incorrect attempt (0 to 6)
HANGMAN_STAGES = [
    """
       ------
       |    |
       |
       |
       |
       |
    =========
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    =========
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    =========
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    =========
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    =========
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    =========
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    =========
    """
]


def select_random_word(word_list):
    """Selects and returns a random word from the provided list."""
    return random.choice(word_list)


def get_masked_word(secret_word, guessed_letters):
    """
    Builds a string showing guessed letters and hiding unguessed letters with underscores.
    Example: 'P _ T H _ N'
    """
    display = []
    for letter in secret_word:
        if letter in guessed_letters:
            display.append(letter)
        else:
            display.append("_")
    return " ".join(display)


def is_word_guessed(secret_word, guessed_letters):
    """Checks if all letters of the secret word have been guessed."""
    for letter in secret_word:
        if letter not in guessed_letters:
            return False
    return True


def play_hangman_round():
    """Executes a single round of the Hangman game."""
    secret_word = select_random_word(WORDS)
    guessed_letters = []
    incorrect_attempts = 0

    print("\n" + "=" * 45)
    print("      A NEW HANGMAN GAME HAS STARTED!      ")
    print("=" * 45)
    print("I have chosen a secret word. Can you guess it?")
    print(f"You have {MAX_INCORRECT_ATTEMPTS} incorrect attempts allowed.")

    # Game loop continues until player guesses the word or runs out of attempts
    while incorrect_attempts < MAX_INCORRECT_ATTEMPTS:
        # Display the visual hangman stage
        print(HANGMAN_STAGES[incorrect_attempts])

        # Display current word status
        current_display = get_masked_word(secret_word, guessed_letters)
        print(f"Word: {current_display}")

        # Display guessed letters so far
        if guessed_letters:
            print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        else:
            print("Guessed letters: None")

        remaining_attempts = MAX_INCORRECT_ATTEMPTS - incorrect_attempts
        print(f"Remaining attempts: {remaining_attempts}")

        # Prompt player for input
        user_input = input("\nEnter your guess (a single letter): ").strip().upper()

        # Input validation: check if input is a single character
        if len(user_input) != 1:
            print("[!] Please enter only one letter at a time.")
            continue

        # Input validation: check if input is an alphabet letter
        if not user_input.isalpha():
            print("[!] Invalid input. Please enter an alphabetical character (A-Z).")
            continue

        # Check for repeated guesses (does not penalize attempts)
        if user_input in guessed_letters:
            print(f"[i] You already guessed '{user_input}'. Try another letter! No attempt lost.")
            continue

        # Record new guess
        guessed_letters.append(user_input)

        # Check if the guess is in the secret word
        if user_input in secret_word:
            print(f"[+] Great guess! '{user_input}' is in the secret word.")

            # Check for winning condition
            if is_word_guessed(secret_word, guessed_letters):
                print("\n" + "*" * 45)
                print("   CONGRATULATIONS! YOU WON THE GAME!   ")
                print("*" * 45)
                print(f"You successfully guessed the word: {secret_word}")
                return
        else:
            incorrect_attempts += 1
            remaining_attempts = MAX_INCORRECT_ATTEMPTS - incorrect_attempts
            print(f"[-] Sorry, '{user_input}' is NOT in the secret word.")
            print(f"Incorrect attempts used: {incorrect_attempts}/{MAX_INCORRECT_ATTEMPTS}")

    # Player ran out of attempts (Loss condition)
    print(HANGMAN_STAGES[MAX_INCORRECT_ATTEMPTS])
    print("\n" + "x" * 45)
    print("              GAME OVER! YOU LOST!           ")
    print("x" * 45)
    print(f"You ran out of attempts. The correct word was: {secret_word}")


def main():
    """Main function that handles the game lifecycle and play-again logic."""
    print("=============================================")
    print("        WELCOME TO THE HANGMAN GAME!         ")
    print("=============================================")

    while True:
        play_hangman_round()

        # Prompt the user to play again
        while True:
            choice = input("\nDo you want to play again? (yes/no): ").strip().lower()
            if choice in ["yes", "y"]:
                break
            elif choice in ["no", "n"]:
                print("\nThank you for playing Hangman! Goodbye!")
                return
            else:
                print("Please enter 'yes' or 'no'.")


if __name__ == "__main__":
    main()
