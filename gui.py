import joblib
import tkinter as tk
from tkinter import ttk
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


# Loading models:
loaded_model1 = joblib.load('NB_classifier.pkl')
# loaded_model2 = joblib.load('xgb_classifier.pkl')
loaded_cv = joblib.load('count_vectorizer.pkl')




def preprocess_text(text):
    review = re.sub('[^a-zA-Z]', ' ', text)
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    all_stopwords = stopwords.words('english')
    all_stopwords.remove('not')
    review = [ps.stem(word) for word in review if not word in set(all_stopwords)]
    review = ' '.join(review)
    return review


def naive_bayes(text):
    # Preprocess the user input
    preprocessed_input = preprocess_text(text)

    # Vectorize the preprocessed input
    user_input_vectorized = loaded_cv.transform([preprocessed_input]).toarray()

    # Predict
    prediction = loaded_model1.predict(user_input_vectorized)

    if prediction == 0:
        return 'Not Hate Speech'
    else:
        return 'Hate Speech!!'


# def xg_boost(text):
#     # Preprocess the user input
#     preprocessed_input = preprocess_text(text)

#     # Vectorize the preprocessed input
#     user_input_vectorized = loaded_cv.transform([preprocessed_input]).toarray()

#     # Predict
#     prediction = loaded_model2.predict(user_input_vectorized)

#     if prediction == 0:
#         return 'Not Hate Speech'
#     else:
#         return 'Hate Speech!!'

def print_and_display_text():
    # geeting the text: from i/p
    input_text = input_textbox.get("1.0", tk.END)  # str

    # print(type(input_text))
    # exit(0)

    # Predictions:
    naive_bayes_prediction = naive_bayes(input_text)
    # xg_boost = xg_boost(input_text)

    output_text = f'''Naive-Bayes: {naive_bayes_prediction}\n'''
    # output_text = f'''Naive-Bayes: {naive_bayes}\nXG-Boost: {xg_boost}'''

    output_textbox.config(state=tk.NORMAL)
    output_textbox.delete("1.0", tk.END)
    # output_textbox.insert(tk.END, input_text) # ****
    output_textbox.insert(tk.END, output_text) # ****
    output_textbox.config(state=tk.DISABLED)

# Create the main window
window = tk.Tk()
window.title("Text Display App")
window.geometry('350x300')

# Create a large Textbox
input_textbox = tk.Text(window, height=5, width=40)
input_textbox.pack(pady=10)

# Naive Bayes: Button
button1 = tk.Button(window, 
                   text="Naive Bayes", 
                   command=print_and_display_text)
                #    command=lambda x: print_and_display_text(x))
button1.pack()

# XGBoost: Button
# button2 = tk.Button(window, 
#                    text="XGBoost", 
#                    command=print_and_display_text)
# button2.pack()

# Create a smaller Textbox
output_textbox = tk.Text(window, height=3, width=40, state=tk.DISABLED)
output_textbox.pack(pady=10)

# Run the application
window.mainloop()
