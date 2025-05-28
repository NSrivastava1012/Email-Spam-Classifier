Email Spam Classifier
A web-based spam detection tool built with Flask, using Natural Language Processing and Machine Learning. It classifies emails as Spam or Not Spam, shows the spam probability, highlights suspicious keywords, and logs recent predictions.

Features

- Classifies email text as Spam or Not Spam
- Displays Spam Probability Score
- Highlights key spam-related keywords
- Maintains a prediction history with timestamps

Tech Stack

- Backend: Python, Flask
- ML Model: Multinomial Naive Bayes (MultinomialNB)
- NLP: NLTK (tokenization, stopword removal, stemming)
- Data Handling: pandas, scikit-learn
- Model Serialization: joblib

Installation

1. Clone the Repository
```bash
git clone https://github.com/yourusername/email-spam-classifier.git
cd email-spam-classifier
```

2. Install Dependencies
```bash
pip install -r requirements.txt
```

Run the App

```bash
python app.py
```

Open your browser and go to:  
`http://127.0.0.1:5000`

Dataset

- Source: [SMS Spam Collection Dataset](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)
- Format: CSV with two columns:
  - `label`: `ham` or `spam`
  - `text`: Message content

How It Works

1. Text Cleaning: Lowercase conversion, punctuation removal, stopword filtering, stemming.
2. Vectorization: TF-IDF vectorizer converts text to numerical format.
3. Model: Trained a `MultinomialNB` classifier for spam detection.
4. Prediction:
   - Outputs spam/ham
   - Calculates spam probability
   - Highlights top spam-indicative keywords
   - Logs prediction time and details

Sample Output

> Input: _"Congratulations! You have won a free iPhone. Click here to claim."_  
> Prediction: Spam  
> Spam Probability: 97.4%  
> Highlighted Keywords: congratulations, won, free, click, claim

Evaluation

- Model Used: Multinomial Naive Bayes
- Accuracy: ~96% on test data
- Evaluated using precision, recall, and F1-score

Requirements

```txt
Flask
pandas
scikit-learn
nltk
joblib
```

Install all using:
```bash
pip install -r requirements.txt
```

Future Improvements

- [ ] Deploy the app on Render / Vercel / Heroku
- [ ] Add email file (.eml) upload support
- [ ] Add real-time email scraping from Gmail API
- [ ] Add bar chart of most common spam keywords

License

This project is licensed under the **MIT License**.

Acknowledgements

- UCI Machine Learning Repository – SMS Spam Collection Dataset  
- scikit-learn & NLTK documentation  
- Flask web framework
