#Taking raw tweets and converting them into a the training form
'''
Nathaniel Gottschalt, Reena Sharma, Garikapati Geethika
Data Mining 431 Project
'''
import json

data = []

with open('../Cluster/cluster-0.txt') as f:
	for line in f:
		data.append(json.loads(line))

superlist = []
result = []

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
 

f = open('cluster0PositiveLRAssociationFormat.txt', 'w')
for i in range(0, len(superlist)):
	f.write(json.dumps(superlist[i]) + ",\n")
f.close()