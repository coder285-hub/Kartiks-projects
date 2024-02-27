import unittest
from project import jumbled_words

class TestJumbledWords(unittest.TestCase):

    def test_basic_functionality(self):
        # Test that the GUI window opens without errors
        jumbled_words()  # Assuming jumbled_words() is imported or defined globally
        # Assert that GUI window is opened successfully
        self.assertTrue(Hindi is not None)  # Assuming Hindi is accessible globally

    def test_correct_answer(self):
        # Simulate user entering correct answer and clicking Answer button
        entry_answer.insert(0, word)
        answer()
        # Assert that answer is marked as correct and score increases
        self.assertEqual(count, 1)  # Assuming count is initialized to 0

    def test_incorrect_answer(self):
        # Simulate user entering incorrect answer and clicking Answer button
        entry_answer.insert(0, "incorrect_answer")
        answer()
        # Assert that answer is marked as incorrect and score remains unchanged
        self.assertEqual(count, 1)  # Assuming count is initialized to 0

    def test_pick_another_word_button(self):
        # Simulate user clicking Pick Another Word button
        my_buttin.invoke()
        # Assert that a new word is displayed
        self.assertNotEqual(my_label.cget("text"), "")

    def test_english_meaning_button(self):
        # Simulate user clicking English Meaning button
        meaning_btn.invoke()
        # Assert that English meaning of the current word is displayed
        self.assertNotEqual(meaning_label.cget("text"), "")

    def test_exit_button(self):
        # Simulate user clicking Exit button
        Exit_btn.invoke()
        # Assert that the program window closes
        self.assertTrue(Hindi is None)  # Assuming Hindi is accessible globally

    def test_hindi_alphabet_buttons(self):
        # Simulate user clicking on Hindi alphabet buttons
        for alphabet in hindi_alphabets:
            btn = Button()
            btn.config(text=alphabet)
            btn.invoke()
            # Assert that corresponding alphabet is appended to the answer entry field
            self.assertEqual(entry_answer.get(), alphabet)

    def test_boundary_condition(self):
        # Play the game until all words from the list are exhausted
        for _ in range(len(keyword_list)):
            my_buttin.invoke()
            entry_answer.insert(0, word)
            answer()
        # Assert that the game handles the end condition gracefully
        self.assertTrue("All words exhausted" in answer_label.cget("text"))  # Assuming appropriate message is shown when all words are exhausted

if __name__ == '__main__':
    unittest.main()
