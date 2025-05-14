"""Main file for the server"""
from flask import Flask, render_template
from EmotionDetection import emotion_detector
app = Flask(__name__)

@app.route("/", methods=["GET"])
def default():
    """
    The main webpage
    """
    return render_template("index.html")

@app.route("/<textToAnalyze>", methods=["GET"])
def detect_that_emotion(text_to_analyze):
    """
    Grabs the parimiters, and returns the emotion.

    Parimiters:
    text_to_analyze (string): the sentence to analyze

    Returns:
    String of the responce from the webpage
    """
    test = emotion_detector(text_to_analyze)

    if test["dominant_emotion"] is None:
        return "Invalid text! Please try again!"
    result = "For the given statement, the system response is "
    result_again:dict[str, float] = {}
    for emotion in test.keys():
        if emotion != "dominant_emotion":
            result_again[emotion] = test[emotion]

    result = result + str(result_again)[1:-1]
    result = result + ". The dominant emotion is " + str(test["dominant_emotion"])

    return result

if __name__ == "__main__":
    app.run(debug=True)
