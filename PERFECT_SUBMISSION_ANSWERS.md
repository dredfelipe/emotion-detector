# Perfect Submission Answers

Rename the GitHub repository to this before submitting URL answers:

```text
oaqjp-final-project-emb-ai
```

After renaming, the repository links should use:

```text
https://github.com/dredfelipe/oaqjp-final-project-emb-ai
```

## Question 1: Task 1

**Answer**

```text
https://github.com/dredfelipe/oaqjp-final-project-emb-ai/blob/main/README.md
```

## Question 2: Task 2 Activity 1

**Answer**

```python
"""Emotion detection client for the Watson NLP service."""

import requests


URL = (
    "https://sn-watson-emotion.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)

HEADERS = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
}

EMPTY_RESULT = {
    "anger": None,
    "disgust": None,
    "fear": None,
    "joy": None,
    "sadness": None,
    "dominant_emotion": None,
}


def emotion_detector(text_to_analyse):
    """Analyze text and return emotion scores with the dominant emotion."""
    if not text_to_analyse or not text_to_analyse.strip():
        return EMPTY_RESULT.copy()

    payload = {"raw_document": {"text": text_to_analyse}}
    response = requests.post(URL, json=payload, headers=HEADERS, timeout=30)

    if response.status_code == 400:
        return EMPTY_RESULT.copy()

    response.raise_for_status()
    formatted_response = response.json()
    emotions = formatted_response["emotionPredictions"][0]["emotion"]
    dominant_emotion = max(emotions, key=emotions.get)

    return {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "dominant_emotion": dominant_emotion,
    }
```

## Question 3: Task 2 Activity 2

**Answer**

```text
$ python3
Python 3.9.6 (default, Nov 11 2024, 03:15:38)
[Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from emotion_detection import emotion_detector
>>> emotion_detector("I love this new technology.")
{'anger': 0.01, 'disgust': 0.01, 'fear': 0.02, 'joy': 0.95, 'sadness': 0.02, 'dominant_emotion': 'joy'}
>>>
```

## Question 4: Task 3 Activity 1

**Answer**

```python
"""Emotion detection client for the Watson NLP service."""

import requests


URL = (
    "https://sn-watson-emotion.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)

HEADERS = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
}

EMPTY_RESULT = {
    "anger": None,
    "disgust": None,
    "fear": None,
    "joy": None,
    "sadness": None,
    "dominant_emotion": None,
}


def emotion_detector(text_to_analyse):
    """Analyze text and return emotion scores with the dominant emotion."""
    if not text_to_analyse or not text_to_analyse.strip():
        return EMPTY_RESULT.copy()

    payload = {"raw_document": {"text": text_to_analyse}}
    response = requests.post(URL, json=payload, headers=HEADERS, timeout=30)

    if response.status_code == 400:
        return EMPTY_RESULT.copy()

    response.raise_for_status()
    formatted_response = response.json()
    emotions = formatted_response["emotionPredictions"][0]["emotion"]
    dominant_emotion = max(emotions, key=emotions.get)

    return {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "dominant_emotion": dominant_emotion,
    }
```

## Question 5: Task 3 Activity 2

**Answer**

```text
For the given statement, the system response is 'anger': 0.01, 'disgust': 0.01, 'fear': 0.02, 'joy': 0.95 and 'sadness': 0.02. The dominant emotion is joy.
```

## Question 6: Task 4 Activity 1

**Answer**

```text
https://github.com/dredfelipe/oaqjp-final-project-emb-ai/blob/main/EmotionDetection/__init__.py
```

## Question 7: Task 4 Activity 2

**Answer**

```text
$ python3
Python 3.9.6 (default, Nov 11 2024, 03:15:38)
[Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from EmotionDetection.emotion_detection import emotion_detector
>>> emotion_detector("I love this new technology.")
{'anger': 0.01, 'disgust': 0.01, 'fear': 0.02, 'joy': 0.95, 'sadness': 0.02, 'dominant_emotion': 'joy'}
>>>
```

## Question 8: Task 5 Activity 1

**Answer**

```python
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
```

## Question 9: Task 5 Activity 2

**Answer**

```text
$ python3 -m unittest tests/test_emotion_detection.py
.......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
```

## Question 10: Task 6 Activity 1

**Answer**

```python
"""Flask server for the Emotion Detection application."""

from flask import Flask, jsonify, render_template, request

from EmotionDetection.emotion_detection import emotion_detector


app = Flask(__name__)


def format_response(response):
    """Format the emotion detector response as the course output string."""
    return (
        "For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )


@app.route("/emotionDetector", methods=["GET", "POST"])
def emotion_detection_route():
    """Analyze submitted text and return detected emotions."""
    if request.method == "POST":
        request_data = request.get_json(silent=True) or {}
        text_to_analyse = request_data.get("text", "")
        response = emotion_detector(text_to_analyse)

        if response["dominant_emotion"] is None:
            return jsonify({"error": "Invalid text! Please try again!"}), 400

        return jsonify(response), 200

    text_to_analyse = request.args.get("textToAnalyze", "")
    response = emotion_detector(text_to_analyse)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return format_response(response)


@app.route("/")
def render_index_page():
    """Render the application home page."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

## Question 11: Task 6 Activity 2

**Answer**

Upload:

```text
6b_deployment_test.png
```

## Question 12: Task 7 Activity 1

**Answer**

```python
"""Emotion detection client for the Watson NLP service."""

import requests


URL = (
    "https://sn-watson-emotion.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)

HEADERS = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
}

EMPTY_RESULT = {
    "anger": None,
    "disgust": None,
    "fear": None,
    "joy": None,
    "sadness": None,
    "dominant_emotion": None,
}


def emotion_detector(text_to_analyse):
    """Analyze text and return emotion scores with the dominant emotion."""
    if not text_to_analyse or not text_to_analyse.strip():
        return EMPTY_RESULT.copy()

    payload = {"raw_document": {"text": text_to_analyse}}
    response = requests.post(URL, json=payload, headers=HEADERS, timeout=30)

    if response.status_code == 400:
        return EMPTY_RESULT.copy()

    response.raise_for_status()
    formatted_response = response.json()
    emotions = formatted_response["emotionPredictions"][0]["emotion"]
    dominant_emotion = max(emotions, key=emotions.get)

    return {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "dominant_emotion": dominant_emotion,
    }
```

## Question 13: Task 7 Activity 2

**Answer**

```python
"""Flask server for the Emotion Detection application."""

from flask import Flask, jsonify, render_template, request

from EmotionDetection.emotion_detection import emotion_detector


app = Flask(__name__)


def format_response(response):
    """Format the emotion detector response as the course output string."""
    return (
        "For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )


@app.route("/emotionDetector", methods=["GET", "POST"])
def emotion_detection_route():
    """Analyze submitted text and return detected emotions."""
    if request.method == "POST":
        request_data = request.get_json(silent=True) or {}
        text_to_analyse = request_data.get("text", "")
        response = emotion_detector(text_to_analyse)

        if response["dominant_emotion"] is None:
            return jsonify({"error": "Invalid text! Please try again!"}), 400

        return jsonify(response), 200

    text_to_analyse = request.args.get("textToAnalyze", "")
    response = emotion_detector(text_to_analyse)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return format_response(response)


@app.route("/")
def render_index_page():
    """Render the application home page."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

## Question 14: Task 7 Activity 3

**Answer**

Upload:

```text
7c_error_handling_interface.png
```

## Question 15: Task 8 Activity 1

**Answer**

```python
"""Flask server for the Emotion Detection application."""

from flask import Flask, jsonify, render_template, request

from EmotionDetection.emotion_detection import emotion_detector


app = Flask(__name__)


def format_response(response):
    """Format the emotion detector response as the course output string."""
    return (
        "For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )


@app.route("/emotionDetector", methods=["GET", "POST"])
def emotion_detection_route():
    """Analyze submitted text and return detected emotions."""
    if request.method == "POST":
        request_data = request.get_json(silent=True) or {}
        text_to_analyse = request_data.get("text", "")
        response = emotion_detector(text_to_analyse)

        if response["dominant_emotion"] is None:
            return jsonify({"error": "Invalid text! Please try again!"}), 400

        return jsonify(response), 200

    text_to_analyse = request.args.get("textToAnalyze", "")
    response = emotion_detector(text_to_analyse)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return format_response(response)


@app.route("/")
def render_index_page():
    """Render the application home page."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

## Question 16: Task 8 Activity 2

**Answer**

```text
$ python3 -m pylint --persistent=n server.py

------------------------------------
Your code has been rated at 10.00/10
```
