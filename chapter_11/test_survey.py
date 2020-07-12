# Let’s write a test that verifies one aspect of the way AnonymousSurvey behaves.
# We’ll write a test to verify that a single response to the survey question is
# stored properly. We’ll use the assertIn() method to verify that the response is
# in the list of responses after it’s been stored:

import unittest
from chapter_11.survey import AnonymousSurvey

# class TestAnonymousSurvey(unittest.TestCase):
#     """Tests for the class AnonymousSurvey"""
#
#     def test_store_single_response(self):
#         """Test that a single response is stored properly."""
#         question = "What language did you first learn to speak?"
#         my_survey = AnonymousSurvey(question)
#         my_survey.store_response("English")
#         self.assertIn("English",my_survey.responses)
#
# if __name__ == "__main__":
#     unittest.main()

# Let’s verify that three responses can be stored correctly. To do
# this, we add another method to TestAnonymousSurvey:

# class TestAnonymousSurvey(unittest.TestCase):
#     """Tests for the class AnonymousSurvey"""
#
#     def test_store_single_response(self):
#         """Test that a single response is stored properly."""
#         question = "What language did you first learn to speak?"
#         my_survey = AnonymousSurvey(question)
#         my_survey.store_response("English")
#         self.assertIn("English",my_survey.responses)
#
#     def test_store_three_responses(self):
#         """Test that 3 individual responses are stored properly"""
#         question = "What language did you first learn to speak?"
#         my_survey = AnonymousSurvey(question)
#         responses = ["English", "Spanish", "Mandarin"]
#         for response in responses:
#             my_survey.store_response(response)
#
#         for response in responses:
#             self.assertIn(response,my_survey.responses)
#
# if __name__ == "__main__":
#     unittest.main()

# The unittest.TestCase
# class has a setUp() method that allows you to create instances/objects once and
# then use them in each of your test methods. When you include a setUp()
# method in a TestCase class, Python runs the setUp() method before running
# each method starting with test_. Any objects created in the setUp() method are
# then available in each test method you write:

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""

    def setUp(self):
        """Create a survey + set of responses for use in all test methods"""
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']


    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses)

    def test_store_three_responses(self):
        """Test that 3 individual responses are stored properly"""
        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response,self.my_survey.responses)

if __name__ == "__main__":
    unittest.main()