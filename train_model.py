# 1. Import Libraries
import pandas as pd
import string
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
import joblib
import nltk

# 2. Download NLTK Resources
nltk.download('punkt')
nltk.download('stopwords')

# 3. Load the Dataset
df = pd.read_csv("spam.csv", encoding='latin-1')[['v1', 'v2']]
df.columns = ['label', 'message']
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# 4. Text Preprocessing Function
stop_words = set(stopwords.words('english'))

def preprocess(text):
    text = text.lower()
    text = ''.join([char for char in text if char not in string.punctuation])
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return ' '.join(words)

# 5. Apply Preprocessing
df['message_clean'] = df['message'].apply(preprocess)

# 6. Feature Extraction (TF-IDF)
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['message_clean'])
y = df['label']

# 7. Split the Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 8. Train the Model
model = MultinomialNB()
model.fit(X_train, y_train)

# 9. Evaluate the Model
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# 10. Save the Model and Vectorizer
joblib.dump(model, "spam_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")
