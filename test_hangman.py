"""
Automated Test Suite for Hangman Game
-------------------------------------
Unit tests verifying winning conditions, losing conditions,
repeated guess handling, and input validation.
"""

import io
import sys
import unittest
from unittest.mock import patch
import hangman


class TestHangmanGame(unittest.TestCase):

    def test_predefined_words(self):
        """Verify the predefined list of 5 required words."""
        expected_words = ["PYTHON", "COMPUTER", "PROGRAM", "STUDENT", "SOFTWARE"]
        self.assertEqual(hangman.WORDS, expected_words)

    def test_masked_word_display(self):
        """Verify underscores and revealed letters."""
        word = "PYTHON"
        self.assertEqual(hangman.get_masked_word(word, []), "_ _ _ _ _ _")
        self.assertEqual(hangman.get_masked_word(word, ["P", "O"]), "P _ _ _ O _")
        self.assertEqual(hangman.get_masked_word(word, ["P", "Y", "T", "H", "O", "N"]), "P Y T H O N")

    def test_word_guessed_condition(self):
        """Verify the complete word guessed checker."""
        word = "STUDENT"
        self.assertFalse(hangman.is_word_guessed(word, ["S", "T", "U"]))
        self.assertTrue(hangman.is_word_guessed(word, ["S", "T", "U", "D", "E", "N"]))

    @patch("random.choice", return_value="PYTHON")
    @patch("builtins.input", side_effect=["P", "Y", "T", "H", "O", "N"])
    def test_winning_scenario(self, mock_input, mock_choice):
        """Test winning scenario when player guesses all letters correctly."""
        captured_output = io.StringIO()
        sys.stdout = captured_output

        hangman.play_hangman_round()

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("CONGRATULATIONS! YOU WON THE GAME!", output)
        self.assertIn("PYTHON", output)
        self.assertNotIn("GAME OVER! YOU LOST!", output)

    @patch("random.choice", return_value="PYTHON")
    @patch("builtins.input", side_effect=["A", "B", "C", "D", "E", "F"])
    def test_losing_scenario(self, mock_input, mock_choice):
        """Test losing scenario when player exhausts 6 incorrect attempts."""
        captured_output = io.StringIO()
        sys.stdout = captured_output

        hangman.play_hangman_round()

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("GAME OVER! YOU LOST!", output)
        self.assertIn("The correct word was: PYTHON", output)
        self.assertNotIn("CONGRATULATIONS! YOU WON THE GAME!", output)

    @patch("random.choice", return_value="PROGRAM")
    @patch("builtins.input", side_effect=["1", "AB", "P", "P", "R", "O", "G", "A", "M"])
    def test_input_validation_and_repeated_guesses(self, mock_input, mock_choice):
        """Test that invalid input and repeated guesses do not consume attempts."""
        captured_output = io.StringIO()
        sys.stdout = captured_output

        hangman.play_hangman_round()

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("Please enter only one letter at a time.", output)
        self.assertIn("Invalid input. Please enter an alphabetical character (A-Z).", output)
        self.assertIn("You already guessed 'P'", output)
        self.assertIn("CONGRATULATIONS! YOU WON THE GAME!", output)


if __name__ == "__main__":
    unittest.main()
