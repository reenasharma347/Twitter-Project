'''
Nathaniel Gottschalt, Reena Sharma, Garikapati Geethika
Data Mining 431 Project
'''

#Taking raw tweets and clean
import json
import HTMLParser
import string

data = []

with open('queryTweetsRaw.txt') as f:
	for line in f:
		data.append(json.loads(line))

superlist = []
result = []

#stop words
stopwords = ["rt"] 
stopWordsListEdit = []
for value in data:
	querywords = value.split()
	resultwords = [word for word in querywords if word.lower() not in stopwords]
	stopWordsListEdit.append(' '.join(resultwords))


#main cleaning
cleanedWords = []
toBeMoved = []
website = "https"
userNameRemoved = []
APPOSTOPHES = {"'s" : "is", "'re" : "are", "I'm": "I am", "'ll" : "will", "'t" : "not", "'ve " : "have"}
html_parser = HTMLParser.HTMLParser()
for words in stopWordsListEdit:
	toBeMoved = []
	tweet = html_parser.unescape(words)
	tweet = tweet.encode('ascii', 'ignore').decode('ascii')
	words = tweet.split() 
	for word in words:
		if word[0:1] != '@':
			flag = 0
			word = str(word)
			for c in string.punctuation:
				word = word.replace(c,"")
			if website not in word:
				for key, value in APPOSTOPHES.iteritems():
					if key in word:
						if (key == "'t"):
							if(word[0:word.find(key)].lower() == "can"):
								toBeMoved.append(word[0:word.find(key)])
								toBeMoved.append(value)
							else:
								toBeMoved.append(word[0:word.find(key) - 1])
								toBeMoved.append(value)
						else:
							toBeMoved.append(word[0:word.find(key)])
							toBeMoved.append(value)
						flag = 1
				if(flag == 0):
					toBeMoved.append(word)
	if(len(toBeMoved) != 0):
		userNameRemoved.append(' '.join(toBeMoved))


#remove duplicates
output = []
seen = set()
for value in userNameRemoved:
	if value not in seen:
		output.append(value)
		seen.add(value)

f = open('queryTweetsCleaned.txt', 'w')
for i in range(0, len(output)):
	f.write(json.dumps([i + 1, output[i]]) + "\n")
f.close()