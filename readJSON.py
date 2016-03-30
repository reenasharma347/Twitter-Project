import json

with open("users1.txt") as json_file:
	json_data = json.load(json_file)

with open("users2.txt") as json_file1:
	json_data1 = json.load(json_file1)

with open("users3.txt") as json_file2:
	json_data2 = json.load(json_file2)

flag = 0

i = 0;

print len(json_data)
print len(json_data1)

masterlist = json_data
print len(masterlist)

for item in json_data1:
	for item1 in json_data:
		if(item['id'] == item1['id']):
			flag = 1

	if(flag == 0):
		masterlist.append(item)
	flag = 0

print len(masterlist)

superMasterList = masterlist

flag = 0
for item in json_data2:
	for item1 in masterlist:
		if(item['id'] == item1['id']):
			flag = 1

	if(flag == 0):
		superMasterList.append(item)
	flag = 0

print len(superMasterList)

with open('unique.txt', 'w') as outfile:
	json.dump(superMasterList, outfile, indent = 4)







