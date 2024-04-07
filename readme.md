# Hate Speech Detection Model using Naive Bayes Classification

## Overview
This is a Python script for detecting hate speech using a Naive Bayes classifier. The model has been trained to distinguish between hate speech and non-hate speech text inputs.

## Installation
Before running the script, make sure you have the following dependencies installed:
- Python (version 3.x)
- NLTK (Natural Language Toolkit)
- Tkinter (for GUI)
  
You can install NLTK using pip:
```
pip install nltk
```
And Tkinter is usually included with Python installations.

## Usage
1. **Clone the Repository**: 
   Clone the repository containing the script and the trained model files.

2. **Preprocess Text**: 
   The script preprocesses the input text to remove special characters, convert to lowercase, remove stopwords, and perform stemming.

3. **Load Models**: 
   The script loads pre-trained models for classification. Ensure that the model files (`NB_classifier.pkl` and `count_vectorizer.pkl`) are placed in the same directory as the script.

4. **Run the Application**: 
   Run the script using Python. This will open a GUI window where you can input text for classification.

5. **Input Text**: 
   Enter the text you want to classify into the large textbox provided.

6. **Classify**: 
   Click the "Naive Bayes" button to classify the input text. The result will be displayed in the smaller textbox below.

## File Descriptions
- **hate_speech_detection.py**: 
  The main Python script containing the Naive Bayes classifier implementation and GUI interface using Tkinter.
  
- **NB_classifier.pkl**: 
  Pre-trained Naive Bayes classifier model file.

- **count_vectorizer.pkl**: 
  Pre-trained CountVectorizer for text vectorization.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Credits
This script was developed by [Your Name] and [Your Team/Organization], inspired by the need to combat hate speech online and promote a safer digital environment.
