# Emotion Detection Application

Emotion Detection Application is a Flask web app and Python package that uses
the Watson NLP emotion prediction service to analyze emotions in text.

## Features

- Detects anger, disgust, fear, joy, and sadness
- Returns the dominant emotion
- Provides a Flask web endpoint and browser interface
- Handles blank or invalid input
- Includes unit tests for the detector function

## Project Structure

```text
emotion-detector/
|-- EmotionDetection/
|   |-- __init__.py
|   `-- emotion_detection.py
|-- emotion_detection/
|   |-- __init__.py
|   `-- emotion_detector.py
|-- templates/
|   `-- index.html
|-- tests/
|   |-- __init__.py
|   `-- test_emotion_detector.py
|-- server.py
|-- setup.py
|-- requirements.txt
`-- README.md
```

## Installation

```bash
pip install -r requirements.txt
```

## Running the Application

```bash
python server.py
```

The application runs at `http://localhost:5000`.

## API Endpoint

### GET /emotionDetector

```text
/emotionDetector?textToAnalyze=I am so happy
```

Example response:

```text
For the given statement, the system response is 'anger': 0.0, 'disgust': 0.0, 'fear': 0.0, 'joy': 1.0 and 'sadness': 0.0. The dominant emotion is joy.
```

### POST /emotionDetector

```json
{
  "text": "I am so happy"
}
```

Example response:

```json
{
  "anger": 0.0,
  "disgust": 0.0,
  "fear": 0.0,
  "joy": 1.0,
  "sadness": 0.0,
  "dominant_emotion": "joy"
}
```

Blank input returns:

```json
{
  "error": "Invalid text! Please try again!"
}
```

## Running Tests

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```
