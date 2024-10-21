import nltk

# Downloading necessary NLTK resources
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')

from nltk.tokenize import word_tokenize
import pandas as pd
import numpy as np
import random
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

# Loading datasets with correct encoding
gr = pd.read_csv('Greeting Dataset.csv', engine='python', encoding='ISO-8859-1')
gd = gr.iloc[:, 0].values  # Use iloc to safely get the values

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
    words = word_tokenize(text)  # Ensure 'punkt' is used for tokenization
    filtered = [i for i in words if i.lower() not in stopw]
    return filtered

def stemming(text):
    ps = PorterStemmer()
    return [ps.stem(w) for w in text]

def getName(text):
    filtered = stopWords(text)
    stemmed = stemming(filtered)
    tag = nltk.pos_tag(stemmed)
    noun = [word for word, pos in tag if (pos in ['NN', 'NNP']) and word.lower() != 'name']
    return noun

def safe_random(array):
    if len(array) == 0:
        return None
    return array[random.randint(0, len(array) - 1)]

def greet():
    print(safe_random(gd))

def askName():
    print(safe_random(nd))
    inp = input()
    return inp

def askAge():
    print(safe_random(ad))
    inp = input()
    return inp

def getAge(text):
    filtered = stopWords(text)
    for i in filtered:
        try:
            return int(i)
        except ValueError:
            continue
    return None  # Return None if no valid age is found

def askGender():
    print('Are you a Male or a Female?')
    inp = input()
    return inp

def getGender(text):
    filtered = stopWords(text)
    for word in filtered:
        if word.lower() in ['male', 'female']:
            return word.capitalize()
    return None

def sorry():
    print('I\'m sorry I could not understand that. Let\'s try again.')

def getEmail():
    inp = input("Please enter your email: ")
    return inp

def smokeAndAlc():
    print('Do you smoke? (yes/no)')
    inp1 = input()
    res1 = 1 if 'yes' in inp1.lower() else 0
    print('Do you consume Alcohol? (yes/no)')
    inp2 = input()
    res2 = 1 if 'yes' in inp2.lower() else 0
    return (res1 * 10) + res2

def getZip():
    inp = input("Please enter your Zip Code: ")
    code = ''.join([i for i in inp if i.isdigit()])
    return int(code) if code else None

def extDisease():
    print('Before we ask you your symptoms, we would like to know your health status.')
    print('If you have any existing Medical Conditions or Problems, please provide them here. Reply with \'no\' if none.')
    inp = input()
    if 'no' in inp.lower():
        return 'Nothing Severe'
    return inp

def getSymptoms():
    inp = input("Please describe your symptoms: ")
    filtered = stopWords(inp)
    stemmed = stemming(filtered)
    return stemmed

# Starting the conversation
greet()
print('I\'m MedBot, your personal health assistant.')
print("I can help you find out what's going on with a simple symptom assessment.")

ufName = askName()
name = getName(ufName)
ufAge = askAge()
age = getAge(ufAge)
ufGender = askGender()
gender = getGender(ufGender)

while not gender:
    sorry()
    ufGender = askGender()
    gender = getGender(ufGender)

print('To help you keep a record of your symptoms and enable us to provide you with better assistance, we would like you to provide us with your email. This is mandatory.')
email = getEmail()

print('Your ZipCode would enable us to provide personalized suggestions for hospitals. This is mandatory.')
zip_code = getZip()

sa = smokeAndAlc()
existingDiseases = extDisease()

# Default to 'User' if name is not found
print('Okay, {}.'.format(name[0] if name else 'User'))
print('Can you please describe your symptoms?')
symptoms = getSymptoms()

# Outputs for debug
print(f"Name: {name}, Age: {age}, Gender: {gender}, Email: {email}, Zip: {zip_code}, Smoke/Alcohol: {sa}, Existing Diseases: {existingDiseases}")
print(f"Symptoms: {symptoms}")
