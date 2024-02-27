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
        # Test if speech recognition works properly for each question
        with patch('project.speak') as mocked_speak:
            # Simulate speech recognition for each question
            # Question 1
            project.ques_1()
            mocked_speak.assert_called_with("आपका स्वास्थ्य कैसा है?", "MockedTextWidget1")
            # Question 2
            project.ques_2()
            mocked_speak.assert_called_with("आपका नाम क्या है?", "MockedTextWidget2")
            # Question 3
            project.ques_3()
            mocked_speak.assert_called_with("क्या मैं आपकी मदद कर सकता हुँ?", "MockedTextWidget3")
            # Question 4
            project.ques_4()
            mocked_speak.assert_called_with("मानव शरीर में कितनी आखें होती है?", "MockedTextWidget4")
            # Question 5
            project.ques_5()
            mocked_speak.assert_called_with("आम का रंग कौनसा होता है?", "MockedTextWidget5")
            # Question 6
            project.ques_6()
            mocked_speak.assert_called_with("बच्चों को विद्यालय क्यों जाना चाहिए?", "MockedTextWidget6")

if __name__ == '__main__':
    unittest.main()



