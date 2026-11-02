# Hangman Game (Python)

A beginner-friendly, text-based implementation of the classic **Hangman** word guessing game written in Python. This project was developed as a clean, modular, and well-documented project suitable for a Python internship submission.

---

## 📌 Project Description

Hangman is a classic guessing game where the player tries to decipher a hidden word by guessing one letter at a time. The game selects a secret word at random from a predefined list. For every incorrect guess, a part of the hangman figure is drawn. The player has a maximum of 6 incorrect attempts before the game is lost. If the player reveals all letters of the secret word before running out of attempts, they win!

---

## ✨ Features

- **Random Word Selection**: Randomly picks a secret word from a predefined list of 5 words (`PYTHON`, `COMPUTER`, `PROGRAM`, `STUDENT`, `SOFTWARE`) using Python's built-in `random` module.
- **Hidden Word Display**: Correctly guessed letters are shown in their proper positions, while unrevealed letters are represented by underscores (`_`).
- **Attempt Tracking**: Players are given up to **6 incorrect attempts**. The remaining attempts count updates dynamically after every turn.
- **Repeat Guess Protection**: Prevents duplicate guesses (whether previously correct or incorrect) from penalizing the player or consuming attempts.
- **Input Validation**: Ensures the user only enters valid single alphabetic characters (`A-Z`). Empty inputs, numbers, and multi-character strings are caught gracefully.
- **Visual Hangman Progression**: Dynamic ASCII art stages visually show the hangman being drawn as incorrect attempts increase (from Stage 0 to Stage 6).
- **Clear Outcome Messages**: 
  - Displays a victory banner if the word is fully solved.
  - Displays a game-over banner and reveals the secret word if the player exhausts all attempts.
- **Replayability**: Includes an interactive prompt at the end of every round allowing the player to play again or exit cleanly.

---

## 📋 Requirements

- **Operating System**: Cross-platform (Windows, macOS, Linux)
- **Python Version**: Python 3.x (No external libraries required; uses only standard library modules: `random`).

---

## 📁 Project Structure

```text
hangman_game/
│
├── hangman.py       # Main Python script containing all game logic & functions
└── README.md        # Documentation and running instructions
```

---

## 🚀 How to Run the Program

### 1. Open Terminal or Command Prompt
Navigate to the project directory:

```bash
cd "C:\Users\surya roshan\.gemini\antigravity\scratch\hangman_game"
```

### 2. Run the Game
Execute the script using Python:

**On Windows:**
```bash
python hangman.py
```
*(or `python3 hangman.py` / `py hangman.py` depending on your environment)*

**On macOS / Linux:**
```bash
python3 hangman.py
```

---

## 🎮 Sample Gameplay Preview

```text
=============================================
        WELCOME TO THE HANGMAN GAME!         
=============================================

=============================================
      A NEW HANGMAN GAME HAS STARTED!      
=============================================
I have chosen a secret word. Can you guess it?
You have 6 incorrect attempts allowed.

       ------
       |    |
       |
       |
       |
       |
    =========
    
Word: _ _ _ _ _ _
Guessed letters: None
Remaining attempts: 6

Enter your guess (a single letter): P
[+] Great guess! 'P' is in the secret word.

       ------
       |    |
       |
       |
       |
       |
    =========
    
Word: P _ _ _ _ _
Guessed letters: P
Remaining attempts: 6

Enter your guess (a single letter): Z
[-] Sorry, 'Z' is NOT in the secret word.
Incorrect attempts used: 1/6

       ------
       |    |
       |    O
       |
       |
       |
    =========
    
Word: P _ _ _ _ _
Guessed letters: P, Z
Remaining attempts: 5
```

---

## 💡 Code Architecture & Concepts Used

The code adheres to clean coding practices and demonstrates core fundamental Python programming concepts:

1. **Functions & Modularity**:
   - `select_random_word(word_list)`: Selects a word randomly using `random.choice`.
   - `get_masked_word(secret_word, guessed_letters)`: Generates the masked string representation.
   - `is_word_guessed(secret_word, guessed_letters)`: Evaluates if winning criteria are met.
   - `play_hangman_round()`: Orchestrates the game loop for a single round.
   - `main()`: Manages game startup and the replay loop.
2. **Data Types & Data Structures**:
   - **Strings**: Used for words, inputs, and masked display manipulation.
   - **Lists**: Used to store words (`WORDS`), ASCII art stages (`HANGMAN_STAGES`), and guessed letters (`guessed_letters`).
3. **Control Flow**:
   - **Loops**: `while` loops for game rounds and input validation; `for` loops for string inspection.
   - **Conditional Statements**: `if`, `elif`, and `else` blocks for checking guess correctness, repeated letters, and termination states.
