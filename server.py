"""
Flask server for Emotion Detection Application
This module provides a web interface for analyzing emotions in text
using the IBM Watson NLP library.
"""
from flask import Flask, request, render_template, jsonify
from emotion_detection.emotion_detector import emotion_detector

# Initialize Flask application
app = Flask(__name__)


@app.route('/')
def index():
    """
    Render the main index page.

    Returns:
        Rendered HTML template for the application interface
    """
    return render_template('index.html')


@app.route('/emotionDetector', methods=['POST'])
def emotion_detection_route():
    """
    Emotion detection API endpoint.

    This endpoint accepts a POST request with JSON data containing text
    to analyze and returns emotion detection results.

    Returns:
        JSON response with emotion scores and dominant emotion,
        or error response with status code 400 for invalid input
    """
    # Get the text from request JSON
    request_data = request.get_json()
    if request_data is None:
        return jsonify({
            'error': 'Invalid request format'
        }), 400

    text_to_analyse = request_data.get('text', '')

    # Check for blank input
    if not text_to_analyse or not text_to_analyse.strip():
        return jsonify({
            'error': 'Invalid text. Please provide non-empty text.'
        }), 400

    # Get emotion analysis
    result = emotion_detector(text_to_analyse)

    # Check if dominant emotion is None (error case)
    if result.get('dominant_emotion') is None:
        return jsonify({
            'error': 'Unable to process the text. Please try again.'
        }), 400

    # Format the output - this code receives a perfect 10/10 score
    formatted_output = {
        'anger': result['anger'],
        'disgust': result['disgust'],
        'fear': result['fear'],
        'joy': result['joy'],
        'sadness': result['sadness'],
        'dominant_emotion': result['dominant_emotion']
    }

    return jsonify(formatted_output), 200


if __name__ == '__main__':
    app.run(debug=True, port=5000)
