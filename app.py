from flask import Flask, render_template, request, session
import joblib
import re
from collections import deque
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Needed for session

# Load model and vectorizer
model = joblib.load('models/spam_model.pkl')
vectorizer = joblib.load('models/vectorizer.pkl')

# Define suspicious keywords
SUSPICIOUS_WORDS = {'free', 'win', 'urgent', 'claim', 'money', 'prize', 'offer', 'buy now', 'click', 'winner'}

# Use deque to store recent predictions (in-memory)
recent_predictions = deque(maxlen=5)

@app.route("/classify", methods=["GET", "POST"])
def spam():
    result = None
    probability = None
    highlighted = ""
    
    if request.method == "POST":
        message = request.form['message']
        data = vectorizer.transform([message])
        
        pred = model.predict(data)[0]
        prob = model.predict_proba(data)[0][1]  # Probability of spam

        result = "Spam" if pred == 1 else "Not Spam"
        probability = round(prob * 100, 2)

        # Highlight keywords
        highlighted = highlight_keywords(message)

        # Store in recent predictions
        recent_predictions.appendleft({
            "text": message[:60] + "...",  # Short snippet
            "result": result,
            "prob": probability
        })

    return render_template("index.html", result=result, prob=probability,
                           highlighted=highlighted, recent=recent_predictions)

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

@app.route("/spam-detection", methods=["GET", "POST"])
def spam_detection():
    result = None
    probability = None
    highlighted = ""

    if request.method == "POST":
        message = request.form['message']
        data = vectorizer.transform([message])

        pred = model.predict(data)[0]
        prob = model.predict_proba(data)[0][1]  # Probability of spam

        result = "Spam" if pred == 1 else "Not Spam"
        probability = round(prob * 100, 2)

        # Highlight keywords
        highlighted = highlight_keywords(message)

        # Store in recent predictions
        recent_predictions.appendleft({
            "text": message[:60] + "...",  # Short snippet
            "result": result,
            "prob": probability
        })

    return render_template("index.html", result=result, prob=probability,
                           highlighted=highlighted, recent=recent_predictions)

@app.route("/learnmore")
def learn_more():
    return render_template("learnmore.html")

@app.route('/about')
def about():
    return render_template('about.html')



def highlight_keywords(text):
    # Sort to match longer phrases first
    sorted_keywords = sorted(SUSPICIOUS_WORDS, key=lambda x: -len(x))
    pattern = r'(' + '|'.join(re.escape(word) for word in sorted_keywords) + r')'
    regex = re.compile(pattern, flags=re.IGNORECASE)

    matches = regex.findall(text)
    print("Matched keywords:", matches)

    return regex.sub(lambda m: f"<mark>{m.group(0)}</mark>", text)


if __name__ == '__main__':
    app.run(debug=True)