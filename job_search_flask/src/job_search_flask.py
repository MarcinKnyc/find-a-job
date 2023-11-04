from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/job_search',methods = ['POST'])
def sentimentCheck():
	if request.method == 'POST':
		text = request.json['text']
		return f'The best job offer we found for you is: {text}'


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 15000))
    app.run(debug=True,host='0.0.0.0',port=port)



# #SETUP - NEEDS CHECKING WHAT IS RELEVANT. PROBABLY NOTHING, JUST METHODOLOGY
# import re
# import nltk
# from nltk.stem import WordNetLemmatizer
# from nltk.corpus import stopwords
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('omw-1.4')
# nltk.download('stopwords')
# stopwords_fetched = stopwords.words('english')

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