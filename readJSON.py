import json

data = []

with open('streamedTweets.txt') as f:
	for line in f:
		data.append(json.loads(line))

superlist = []

for i in range(0, 500):
	superlist.append(data[i].get("text").encode("utf-8"))

f = open('unique.txt', 'w')
for i in range(0, 500):
	f.write(json.dumps([i+1, 0, superlist[i]]) + "\n")
f.close()



