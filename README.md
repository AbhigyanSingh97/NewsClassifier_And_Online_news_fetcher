# **NewsClassifier_And_Online_news_fetcher**


News Classifier aims to classify news depending on the several categories of news present around the world.

</br>
<img alt="GIF" src="GIF/newspaper-clipart-black-and-white-8.jpg" width="340" height="250" />
</br>

# **Data**
News data obtained from Kaggle. [link](https://www.kaggle.com/rmisra/news-category-dataset)
</br>


# **Objective**
- Objective of this project is to help apps automatically classify news.
- People can see news depending on their choice/Interests.
- Preventing fake news from spread by predicting the fake news and not letting it go to the customers.


# **Dependencies**
- re
- sys
- pandas
- numpy
- matplotlib
- seaborn
- nltk
- contractions
- autocorrect
- sklearn
- zeugma

# **Models**
- Logistic Regression
- MultinomialNB
- SVM

# **Metrics**
- accuracy_score
- matthews_corrcoef

# **Performance**
- *Logistic Regression* 
  - `accuracy_score` -----> **0.65**
  - `matthews_corrcoef` --> **0.63**
- *MultinomialNB*
  - `accuracy_score` -----> **0.44**
  - `matthews_corrcoef` --> **0.39**
- *SVM*
  - `accuracy_score` -----> ** **
  - `matthews_corrcoef` --> ** **
  
# **Result**
1. *Predict Only*</br>
    <img alt="GIF" src="GIF/Onlypredict.gif"/>
2. *Predict and fetch news online*</br>
    <img alt="GIF" src="GIF/predictandfetch.gif" />
3. *Manual Search online*</br>
    <img alt="GIF" src="GIF/manual.gif" />
