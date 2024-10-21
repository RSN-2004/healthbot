from flask import Flask, render_template, request, redirect, url_for
import nltk
import pandas as pd
import random
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

# Downloading necessary NLTK resources
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

app = Flask(__name__)

# Load datasets
gr = pd.read_csv('Greeting Dataset.csv', engine='python', encoding='ISO-8859-1')
gd = gr.iloc[:, 0].values

tu = pd.read_csv('ThankYou.csv', engine='python', encoding='ISO-8859-1')
td = tu.iloc[:, 0].values

wc = pd.read_csv('Welcome Dataset.csv', engine='python', encoding='ISO-8859-1')
wd = wc.iloc[:, 0].values

ag = pd.read_csv('AGE Dataset.csv', engine='python', encoding='ISO-8859-1')
ad = ag.iloc[:, 0].values

by = pd.read_csv('BYE Dataset.csv', engine='python', encoding='ISO-8859-1')
bd = by.iloc[:, 0].values

nm = pd.read_csv('Name Dataset.csv', engine='python', encoding='ISO-8859-1')
nd = nm.iloc[:, 0].values

# Helper functions
def stopWords(text):
    stopw = set(stopwords.words('english'))
    words = word_tokenize(text)
    filtered = [i for i in words if i.lower() not in stopw]
    return filtered

def stemming(text):
    ps = PorterStemmer()
    return [ps.stem(w) for w in text]

def safe_random(array):
    if len(array) == 0:
        return None
    return array[random.randint(0, len(array) - 1)]

@app.route('/')
def home():
    greeting = safe_random(gd)
    return render_template('index.html', greeting=greeting)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    age = request.form.get('age')
    gender = request.form.get('gender')
    email = request.form.get('email')
    zip_code = request.form.get('zip_code')
    symptoms = request.form.get('symptoms')

    # Process and display the collected information (for demonstration)
    return render_template('response.html', name=name, age=age, gender=gender, email=email, zip_code=zip_code, symptoms=symptoms)

if __name__ == '__main__':
    app.run(debug=True)