#Taking raw tweets and clean
import json
import HTMLParser
import string

data = []

with open('test.txt') as f:
	for line in f:
		data.append(json.loads(line))

superlist = []
result = []

stopwords = ["rt"] 

querywords = data[0][1].split()

resultwords = [word for word in querywords if word.lower() not in stopwords]
result = ' '.join(resultwords)


#remove duplicates
output = []
seen = set()
for value in data:
	if value[1] not in seen:
		output.append(value[1])
		seen.add(value[1])

stopWordsListEdit = []

#stop words
for value in output:
	querywords = value.split()
	resultwords = [word for word in querywords if word.lower() not in stopwords]
	stopWordsListEdit.append(' '.join(resultwords))

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
	
'''
#remove usernames
for words in stopWordsListEdit:
	words.encode('ascii', errors='ignore')
	toBeMoved = []
	splitWords = words.split()
	for i in range(0, len(splitWords)):
		if splitWords[i][0] != "@":
			if website not in splitWords[i]:
				if not (splitWords[i].isdigit()):
					if len(splitWords[i]) > 1:
						if(splitWords[i][0] == '#'):
							toBeMoved.append(splitWords[i][1:])
						else:
							toBeMoved.append(splitWords[i])
	userNameRemoved.append(' '.join(toBeMoved))

for i in range(0, len(userNameRemoved)):
	superlist.append(userNameRemoved[i].replace(' ', ' '))
'''


f = open('queryTweetsCleanedNoDups.txt', 'w')
for i in range(0, len(userNameRemoved)):
	f.write(json.dumps([i + 1, 0, userNameRemoved[i]]) + "\n")
#f.close()