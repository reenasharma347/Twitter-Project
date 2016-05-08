#Taking raw tweets and converting them into a the training form
'''
Nathaniel Gottschalt, Reena Sharma, Garikapati Geethika
Data Mining 431 Project
'''
import json

data = []

with open('../Cluster/cluster-1.txt') as f:
	for line in f:
		data.append(json.loads(line))

superlist = []
result = []

#stopwords = ["make", "got", "time", "feel", "makes", "dont", "like", "make", "having", "want", "just", "people", "prince", "que", "ive", "baby", "a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"]

#Most common words from LR
include = ["fever", "love", "diarrhea", "sneezing", "flu", "dehydrated", "good", "vomit", "night", "cold", "day"]

querywords = data[0][1].split()

#remove duplicates words
output = []
seen = set()
for value in data:
	output.append(value[1])

stopWordsListEdit = []

#include words
for value in output:
	querywords = value.split()
	resultwords = [word for word in querywords if word.lower() in include]
	stopWordsListEdit.append(' '.join(resultwords))

finalListNoDups = []
 
for value in stopWordsListEdit:
	l = value.split()
 	ulist = []
 	[ulist.append(x) for x in l if x not in ulist]
 	finalListNoDups.append(' '.join(ulist))


for i in range(0, len(finalListNoDups)):
	superlist.append(finalListNoDups[i].replace(' ', ', '))
 

f = open('cluster1PositiveLRAsociationFormat.txt', 'w')
for i in range(0, len(superlist)):
	f.write(json.dumps(superlist[i]) + ",\n")
#f.close()