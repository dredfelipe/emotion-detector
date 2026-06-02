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
