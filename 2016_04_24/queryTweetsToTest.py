#Taking raw tweets and converting them into a the training form

import json

data = []

with open('queryTweets.txt') as f:
	for line in f:
		data.append(json.loads(line))

superlist = []

#remove duplicates
output = []
seen = set()
for value in data:
	if value not in seen:
		output.append(value)
		seen.add(value)


f = open('testingTweetsQuery.txt', 'w')
for i in range(0, len(output)):
	f.write(json.dumps([i+1, output[i]]) + "\n")
f.close()