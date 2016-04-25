#Taking raw tweets and converting them into a the training form

import json

data = []

with open('randomSample.txt') as f:
	for line in f:
		data.append(json.loads(line))

superlist = []
result = []

#remove dupliates
output = []
seen = set()
for value in data:
	if value not in seen:
		output.append(value)
		seen.add(value)


f = open('testingTweetsRandomSample.txt', 'w')
for i in range(0, len(output)):
	f.write(json.dumps([i+1, output[i]]) + "\n")
f.close()