import streamlit as st
import pandas as pd
import pickle
import requests
import numpy as np
import re
import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
#from nltk.corpus import stopwords
#import contractions
nltk.download('wordnet')
nltk.download('punkt')
nltk.download("stopwords")


model = "LogisticRegression_model.pkl"
vocab = "tfidf.pkl"


# --------------------------------------------------
# Cleaning text

def text_preprocess(text):
  lemmatizer = WordNetLemmatizer()
  filter_Sentence = ''

  sentence = text.lower()
  #sentence = expand_contractions(sentence)
  #sentence = spell_check(sentence)
  sentence = re.sub(r'[^\w\s]',' ',sentence)
  sentence = re.sub(r"\d", " ", sentence)#removing digits
  sentence = re.sub(r"\s+[a-zA-Z]\s+", " ", sentence)#removing single characters
  sentence = re.sub(r"\s+", " ", sentence, flags=re.I)  # removing extra space
  sentence = re.sub(r"[,@\'?\.$%_]", "", sentence, flags=re.I)#removing multiple characters

  words = nltk.word_tokenize(sentence)

  #words = [w for w in words if not w in stop_words]

  for word in words:
      #filter_Sentence = filter_Sentence + ' ' + str(word)
      filter_Sentence = filter_Sentence + ' ' + str(lemmatizer.lemmatize(word))

  return [filter_Sentence]

# ------------------------------------------------------
# Vectorize clean text

def vectorize(vocab, text):
    vec = pickle.load(open(vocab, "rb"))
    tf_new_1 = TfidfVectorizer(vocabulary = vec.vocabulary_)
    return tf_new_1.fit_transform(text)


# -------------------------------------------------------
# Predict on word vector

def predict(text, model):
    Lg = pickle.load(open(model, "rb"))
    return Lg.predict(text)

#---------------------------------------------------------------------
#'''Fetching internet to get news data'''

def retriev_news(secret, url, category, top_news):
  parameters = {
    'q': category, # query phrase
    'pageSize': top_news,  # maximum is 100
    'apiKey': secret # your own API key
  }

  # Make the request
  response = requests.get(url, params=parameters)

  # Convert the response to JSON format and pretty print it
  response_json = response.json()
  df = pd.DataFrame(response_json['articles'])
  for i in range(len(df)):
      st.title(df['title'][i])
      st.image(df['urlToImage'][i], width=750)
      st.subheader(df['description'][i])
      st.write(df['content'][i])
      #st.text(df['url'][i])
      link = df['url'][i] + "/"
      st.subheader("Watch full Story at:")
      st.markdown(link)


# -------------------------------------------------------------
# main function that calls all the function

def main():
    st.title("News Classifier and Online News Fetcher")

    st.image("https://raw.githubusercontent.com/AbhigyanSingh97/NewsClassifier_And_Online_news_fetcher/main/GIF/newspaper-clipart-black-and-white-8.jpg", width = 150, use_column_width=True, clamp = True)

    secret = '62d1569d3f804f20a13960a7a5e51a6b'
    url = 'https://newsapi.org/v2/everything?'


    category = []


    options = ['Only Predict', 'Predict and Search the Internet', 'Use Manual Input']
    us_ip = st.radio("Check News online by", options)
    if us_ip == 'Only Predict':
        text = st.text_area("Enter your news here")
        if text != "":
            clean_text = text_preprocess(text)
            pred = predict(vectorize(vocab, clean_text), model)
            st.success(pred[0])


    if us_ip == 'Predict and Search the Internet':
        text = st.text_area("Enter your news here")
        if text != "":
            clean_text = text_preprocess(text)
            pred = predict(vectorize(vocab, clean_text), model)
            st.success(pred[0])
            st.write("More online news for the", pred[0])
            top_news = st.slider("Select Number of News to be Displayed", 1, 20, 1)
            retriev_news(secret, url, pred[0], top_news=top_news)

    if us_ip == 'Use Manual Input':
        user_ip = st.text_input("Enter the category you wanna see.")
        if user_ip != "":
            top_news = st.slider("Select Number of News to be Displayed", 1, 20, 1)
            retriev_news(secret, url, user_ip, top_news=top_news)



if __name__ == '__main__':
    main()