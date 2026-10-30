''' Executing this program initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("__name__")

@app.route("/emotionDetector", methods=['GET', 'POST'])
def emo_detector():
    '''This code receives the text from the HTML interface and
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the emotions, the scores
        and the dominat emotion for the provided text.
    '''

    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        formatted_result = "Invalid text! Please try again!."
    else:
        formatted_result = (
            f"For the given statement, the system response is "
            f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
            f"'fear': {response['fear']}, 'joy': {response['joy']} and "
            f"'sadness': {response['sadness']}. The dominant emotion is "
            f"<b>{response['dominant_emotion']}</b>."
)

    return formatted_result

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
