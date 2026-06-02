# Emotion Detection Application

This is a web-based emotion detection application that uses IBM Watson NLP library to analyze emotions in text.

## Features

- Real-time emotion analysis of text input
- Modern, responsive web interface
- RESTful API endpoint for integration
- Comprehensive error handling
- Unit tests for validation

## Project Structure

```
emotion-detector/
├── emotion_detection/
│   ├── __init__.py
│   └── emotion_detector.py
├── templates/
│   └── index.html
├── tests/
│   ├── __init__.py
│   └── test_emotion_detector.py
├── server.py
├── setup.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Before running the application, you need to set up IBM Watson credentials:

1. Get an IBM Cloud API key
2. Update `emotion_detector.py` with your API key and service URL

## Running the Application

```bash
python server.py
```

The application will be available at `http://localhost:5000`

## API Endpoint

### POST /emotionDetector

Analyzes emotions in the provided text.

**Request:**

```json
{
  "text": "I am so happy"
}
```

**Response (Success):**

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

**Response (Error - Status 400):**

```json
{
  "error": "Invalid text. Please provide non-empty text."
}
```

## Running Tests

```bash
python -m unittest discover -s tests -p "test_*.py"
```

## Emotions Detected

- **Anger**: Expresses strong displeasure or hostility
- **Disgust**: Expresses distaste or aversion
- **Fear**: Expresses concern or anxiety
- **Joy**: Expresses happiness or contentment
- **Sadness**: Expresses sorrow or melancholy

## Error Handling

The application includes comprehensive error handling:

- Validates non-empty text input
- Returns status code 400 for invalid requests
- Handles API errors gracefully
- Provides meaningful error messages to users

## Technology Stack

- **Backend**: Python, Flask
- **NLP**: IBM Watson NaturalLanguageUnderstanding
- **Frontend**: HTML5, CSS3, JavaScript
- **Testing**: Python unittest
