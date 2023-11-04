import streamlit as st


st.header("Find the most appropriate job offers for your resume!")
sent=st.text_area("Enter your CV in plain-text format. Max ", height=400)
# transformed_sent1=cleanInput(sent)
# vector_sent1=vectorizer.transform([transformed_sent1])
# prediction1=model.predict(vector_sent1)[0]

if st.button("Predict"):
	st.success(f"The most appropriate job offer is: {sent}!")



# #OLD SETUP - STAYS HERE SO WE CAN USE THE METHODOLOGY. PROBABLY NO SINGLE LINE OF CODE WILL REMAIN.
# import re
# import nltk
# from nltk.stem import WordNetLemmatizer
# from nltk.corpus import stopwords
# from joblib import load
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('omw-1.4')
# nltk.download('stopwords')
# stopwords_fetched = stopwords.words('english')

# model = load('model/best-model.joblib')
# vectorizer = load('model/vectorizer.pkl')

# def contractions(s):
# 	s = re.sub(r"won't", "will not",s)
# 	s = re.sub(r"would't", "would not",s)
# 	s = re.sub(r"could't", "could not",s)
# 	s = re.sub(r"\'d", " would",s)
# 	s = re.sub(r"can\'t", "can not",s)
# 	s = re.sub(r"n\'t", " not", s)
# 	s= re.sub(r"\'re", " are", s)
# 	s = re.sub(r"\'s", " is", s)
# 	s = re.sub(r"\'ll", " will", s)
# 	s = re.sub(r"\'t", " not", s)
# 	s = re.sub(r"\'ve", " have", s)
# 	s = re.sub(r"\'m", " am", s)
# 	return s

# def cleanInput(text):
# 	# lower-case
# 	text = " ".join(word.lower() for word in str(text).split())

# 	# unwrap contractions	
# 	text=contractions(text)

# 	# remove non-alphanumeric characters	
# 	text = " ".join([re.sub('[^A-Za-z]+','', x) for x in nltk.word_tokenize(text)])

# 	# lemmatize		
# 	lemmatizer = WordNetLemmatizer()
# 	text=" ".join([lemmatizer.lemmatize(w) for w in nltk.word_tokenize(text)])

# 	# remove stopwords, normalize whitespace	
# 	text = " ".join([word for word in text.split() if word not in stopwords_fetched])
# 	return text