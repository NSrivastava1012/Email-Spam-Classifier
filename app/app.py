from flask import Flask, render_template, request, session
import joblib
import re
from collections import deque
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Needed for session

# Load model and vectorizer
base_dir = os.path.dirname(os.path.dirname(__file__))
model = joblib.load('C:\\Users\\naven\\OneDrive\\Desktop\\Email Spam Classifier\\models\\spam_model.pkl')
vectorizer = joblib.load('C:\\Users\\naven\\OneDrive\\Desktop\\Email Spam Classifier\\models\\vectorizer.pkl')

# Define suspicious keywords
SUSPICIOUS_WORDS = {# Financial scams & prizes
    "lottery", "winner", "won", "prize", "reward", "bonus", "free", "cash", "million", "billion", "crore", "jackpot", "rich", "earn", "income", "profit", "investment",

    # Urgency and fear tactics
    "urgent", "immediately", "now", "act fast", "last chance", "final notice", "expires soon", "warning", "alert", "limited time", "time-sensitive",

    # Account & phishing threats
    "account", "verify", "verification", "password", "login", "credentials", "security alert", "unauthorized", "access", "update", "reactivate", "suspended", "confirm",

    # Payments, billing & fake orders
    "invoice", "billing", "payment", "overdue", "transaction", "receipt", "refund", "order", "pending", "balance", "credit card", "debit", "charged",

    # Delivery scams
    "package", "shipment", "courier", "tracking", "on hold", "address update", "delivery failed", "dispatch", "shipping fee",

    # Job scams
    "job", "career", "hiring", "recruitment", "work from home", "part-time", "freelancer", "salary", "daily payout", "no experience",

    # Tech support & malware
    "virus", "malware", "spyware", "infected", "scan", "system failure", "repair", "firewall", "threat detected", "clean now",

    # Suspicious links and files
    "click here", "open attachment", "download", "link", "access now", "http", "https", "bit.ly", "tinyurl", "verify here", "login here",

    # Impersonation (brands/officials)
    "Microsoft", "Google", "Amazon", "Apple", "PayPal", "Netflix", "Facebook", "Income Tax", "government", "admin", "support team", "official",

    # Personal data requests
    "ID proof", "Aadhar", "PAN", "bank details", "OTP", "credit card number", "security question", "CVV", "SSN", "date of birth"}

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

@app.route('/')
def home():
    return "Hello from Flask on Render!"




def highlight_keywords(text):
    # Sort to match longer phrases first
    sorted_keywords = sorted(SUSPICIOUS_WORDS, key=lambda x: -len(x))
    pattern = r'(' + '|'.join(re.escape(word) for word in sorted_keywords) + r')'
    regex = re.compile(pattern, flags=re.IGNORECASE)

    matches = regex.findall(text)
    print("Matched keywords:", matches)

    return regex.sub(lambda m: f"<mark>{m.group(0)}</mark>", text)


if __name__ == '__main__':

    import os
from your_app_file import app  # or from app import app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # use Render’s PORT if set
    app.run(host="0.0.0.0", port=port)
