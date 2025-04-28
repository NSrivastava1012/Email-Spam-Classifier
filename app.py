from flask import Flask, request, render_template
import joblib

app = Flask(__name__)
model = joblib.load("models/spam_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        message = request.form["message"]
        msg_vector = vectorizer.transform([message])
        prediction = model.predict(msg_vector)[0]
        result = "Spam" if prediction == 1 else "Not Spam"
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)