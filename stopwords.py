import nltk
import spacy
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
from scipy import spatial

#nlp = spacy.load('en_core_web_md')
nlp = spacy.load('/usr/local/lib/python3.6/dist-packages/en_core_web_md/en_core_web_md-2.0.0')
#nlp = spacy.load('{en_core_web_md}')
def removestop_words(string):
	example_sent = string
  
	stop_words = set(stopwords.words('english')) 
  
	word_tokens = word_tokenize(example_sent) 
  
	filtered_sentence = [w for w in word_tokens if not w in stop_words] 
  
	filtered_sentence = [] 
  
	for w in word_tokens: 
		if w not in stop_words: 
			filtered_sentence.append(w)
	print(example_sent)
	print(word_tokens) 
	print(filtered_sentence) 
	return 
def get_cosine_similarity(str1,str2):
	wordlist1 = list(str1.split(" ")) 
	wordlist2 = list(str2.split(" "))
	vector1 = []
	vector2 = [] 
	for word in wordlist1:
		vector1 = vector1 + (list(nlp(word).vector))
	for word in wordlist2:
		vector2 = vector2 + list(nlp(word).vector)
    

	
	result = 1 - spatial.distance.cosine(vector1, vector2)
	print ("Similarity", result)

	return result
string = "this is python"
removestop_words(string)
str1 = "welcome to ma world"
str2 = "welcome to ma world"
#removestop_words()
get_cosine_similarity(str1,str2)