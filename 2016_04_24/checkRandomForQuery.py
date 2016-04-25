#Taking raw tweets and converting them into a the training form

import json

data = []

with open('randomSample.txt') as f:
	for line in f:
		data.append(json.loads(line))

terms = [' sneezing ', ' vomit ', ' Fever ', ' heahache ', ' fever ', ' diarrhea ', ' dehydrated ', ' flu ']

superlist = []

#remove dupliates
output = []
seen = set()
for value in data:
	if value not in seen:
		output.append(value)
		seen.add(value)

for item in output:
	for keyword in terms:
		if keyword in item:
			superlist.append(item)

f = open('queryMatchInRandomSample.txt', 'w')
for i in range(0, len(superlist)):
	f.write(json.dumps([i+1, superlist[i]]) + "\n")
#f.close()