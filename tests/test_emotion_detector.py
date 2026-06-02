"""
Unit tests for the Emotion Detection application
"""
import unittest
from emotion_detection.emotion_detector import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test cases for emotion_detector function"""

    def test_emotion_detector_joy(self):
        """
        Test emotion detector with a joyful text
        """
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_emotion_detector_fear(self):
        """
        Test emotion detector with a fearful text
        """
        result = emotion_detector("I am really afraid of this")
        self.assertEqual(result['dominant_emotion'], 'fear')

    def test_emotion_detector_sadness(self):
        """
        Test emotion detector with a sad text
        """
        result = emotion_detector("I am so sad")
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_emotion_detector_disgust(self):
        """
        Test emotion detector with a disgust text
        """
        result = emotion_detector("This is disgusting")
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_emotion_detector_anger(self):
        """
        Test emotion detector with an angry text
        """
        result = emotion_detector("I am so angry")
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_emotion_detector_blank_input(self):
        """
        Test emotion detector with blank input
        """
        result = emotion_detector("")
        self.assertIsNone(result['dominant_emotion'])

    def test_emotion_detector_none_input(self):
        """
        Test emotion detector with None input
        """
        result = emotion_detector(None)
        self.assertIsNone(result['dominant_emotion'])


if __name__ == '__main__':
    unittest.main()
