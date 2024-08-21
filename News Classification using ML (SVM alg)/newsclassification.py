import pandas as pd
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
import tkinter as tk

def load_data():
    file_path = 'BBC News Train - BBC News Train.csv.csv'
    data = pd.read_csv(file_path)
    return data

def train_model(data):
    vectorizer = TfidfVectorizer(stop_words='english')
    inp = vectorizer.fit_transform(data['Text'].values.astype('U'))
    out = data['Category']
    classifier = svm.SVC(kernel='linear')
    classifier.fit(inp, out)
    return vectorizer, classifier

def predict_category(vectorizer, classifier):
    root = tk.Tk()
    root.title('News Classifier')
    root.geometry('500x209')

    tk.Label(root, text='Enter News Text:', font=("MS Gothic", 10, " bold")).pack()

    extra1 = tk.Label(root, text=" ")
    extra1.pack()
    text_entry = tk.Text(root, height=5, bg="light blue")
    text_entry.pack()

    def classify_news():
        text = text_entry.get('1.0', 'end-1c')
        inp = vectorizer.transform([text])
        prediction = classifier.predict(inp)
        category_label.config(text=f'Predicted Category: {prediction[0]}')

    extra1 = tk.Label(root, text=" ")
    extra1.pack()
    classify_button = tk.Button(root, text='Classify',font=("MS Gothic", 10, " bold"), command=classify_news, bg="blue", fg="white")
    classify_button.pack()

    extra1=tk.Label(root,text=" ")
    extra1.pack()

    category_label = tk.Label(root, text='Predicted Category:',font=("MS Gothic", 10, " bold") )
    category_label.pack()
    extra1 = tk.Label(root, text=" ")
    extra1.pack()
    root.mainloop()

data = load_data()

vectorizer, classifier = train_model(data)

predict_category(vectorizer, classifier)
