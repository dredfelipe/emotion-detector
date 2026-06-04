"""Unit tests for the emotion detector function."""

import unittest
from unittest.mock import patch

from emotion_detection.emotion_detector import emotion_detector


class MockResponse:
    """Small response object that behaves like requests.Response."""

    def __init__(self, emotion, status_code=200):
        self.emotion = emotion
        self.status_code = status_code

    def json(self):
        """Return a Watson-like response payload."""
        return {"emotionPredictions": [{"emotion": self.emotion}]}

    def raise_for_status(self):
        """Match the requests.Response method used by the detector."""


class TestEmotionDetector(unittest.TestCase):
    """Test cases for emotion_detector."""

    def mock_post(self, url, json, headers, timeout):
        """Return an emotion payload for each required test sentence."""
        del url, headers, timeout
        text = json["raw_document"]["text"]
        responses = {
            "I am glad this happened": {
                "anger": 0.01,
                "disgust": 0.01,
                "fear": 0.02,
                "joy": 0.95,
                "sadness": 0.02,
            },
            "I am really afraid of this": {
                "anger": 0.02,
                "disgust": 0.01,
                "fear": 0.92,
                "joy": 0.01,
                "sadness": 0.04,
            },
            "I am so sad": {
                "anger": 0.01,
                "disgust": 0.01,
                "fear": 0.04,
                "joy": 0.01,
                "sadness": 0.93,
            },
            "This is disgusting": {
                "anger": 0.02,
                "disgust": 0.91,
                "fear": 0.02,
                "joy": 0.01,
                "sadness": 0.04,
            },
            "I am so angry": {
                "anger": 0.94,
                "disgust": 0.02,
                "fear": 0.02,
                "joy": 0.0,
                "sadness": 0.02,
            },
        }
        return MockResponse(responses[text])

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_emotion_detector_joy(self, mock_requests_post):
        """Test emotion detector with a joyful text."""
        mock_requests_post.side_effect = self.mock_post
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result["dominant_emotion"], "joy")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_emotion_detector_fear(self, mock_requests_post):
        """Test emotion detector with a fearful text."""
        mock_requests_post.side_effect = self.mock_post
        result = emotion_detector("I am really afraid of this")
        self.assertEqual(result["dominant_emotion"], "fear")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_emotion_detector_sadness(self, mock_requests_post):
        """Test emotion detector with a sad text."""
        mock_requests_post.side_effect = self.mock_post
        result = emotion_detector("I am so sad")
        self.assertEqual(result["dominant_emotion"], "sadness")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_emotion_detector_disgust(self, mock_requests_post):
        """Test emotion detector with a disgust text."""
        mock_requests_post.side_effect = self.mock_post
        result = emotion_detector("This is disgusting")
        self.assertEqual(result["dominant_emotion"], "disgust")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_emotion_detector_anger(self, mock_requests_post):
        """Test emotion detector with an angry text."""
        mock_requests_post.side_effect = self.mock_post
        result = emotion_detector("I am so angry")
        self.assertEqual(result["dominant_emotion"], "anger")

    def test_emotion_detector_blank_input(self):
        """Test emotion detector with blank input."""
        result = emotion_detector("")
        self.assertIsNone(result["dominant_emotion"])

    def test_emotion_detector_none_input(self):
        """Test emotion detector with None input."""
        result = emotion_detector(None)
        self.assertIsNone(result["dominant_emotion"])


if __name__ == "__main__":
    unittest.main()
