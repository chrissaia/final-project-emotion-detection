"""
Emotion Detection Server

This script defines a Flask-based server for performing emotion detection
on user-provided text.

Author: Christopher Saia
"""

from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

# Main function
def run_emotion_detection():
    """
    Main function to run the Emotion Detection application on localhost.
    """
    app.run(debug=True, host="0.0.0.0", port=5001)

@app.route("/emotionDetector", methods=['GET', 'POST'])
# Analyzing the user text
def sent_detector():
    """
    Analyze the user-provided text for emotions and return the result.
    
    Returns:
        JSON response with the emotions detected or an error message.
    """
    if request.method == 'POST':
        text_to_detect = request.json.get('textToAnalyze')  # For POST request, expecting JSON body
    else:
        text_to_detect = request.args.get('textToAnalyze')  # For GET request

    # Call emotion detection function
    response = emotion_detector(text_to_detect)

    # If no dominant emotion found, return invalid text message
    if 'dominant_emotion' not in response or response['dominant_emotion'] is None:
        return jsonify({"error": "Invalid text! Please try again."}), 400

    # Format the response text using the correct variable 'response'
    return (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

# Initiates rendering of the main application page over Flask channel
@app.route("/")
def render_index_page():
    """
    Render the main application page (index.html).
    
    Returns:
        HTML response for the main page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    run_emotion_detection()
