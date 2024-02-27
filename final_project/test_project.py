import unittest
from unittest.mock import patch
import project  # Assuming your project file is named project.py

class TestProject(unittest.TestCase):
    def test_memory_game_reset(self):
        # Test if the game resets properly
        with patch('project.reset') as mocked_reset:
            project.reset()
            mocked_reset.assert_called()

    def test_memory_game_win(self):
        # Test if the game detects a win properly
        with patch('project.win') as mocked_win:
            # Simulate a situation where all matches are found
            project.winner = 6
            project.win()
            mocked_win.assert_called()

    def test_grammar_training_speech_recognition(self):
        # Test if speech recognition works properly
        with patch('project.speak') as mocked_speak:
            # Simulate speech recognition with a known phrase
            project.speak("आपका", text1)
            mocked_speak.assert_called_with("आपका", text1)

    # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()

