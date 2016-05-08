
# coding: utf-8

# In[1]:

import Orange


raw_data = ["cold, flu",
"cold, flu",
"Sneezing, day, flu",
"good, cold, flu",
"cold, flu",
"flu, fever, night",
"flu, fever",
"flu",
"good, day, night, cold, flu",
"day, flu",
"flu, cold",
"flu",
"flu",
"cold, flu",
"cold, flu",
"day, flu",
"flu, fever",
"flu",
"Cold, cold, flu",
"flu",
"flu",
"cold, flu",
"flu, love",
"cold, flu",
"fever, flu",
"love, cold, flu",
"flu, cold",
"cold, flu",
"flu",
"diarrhea, fever, flu",
"flu",
"Good, flu",
"Flu, flu, day",
"day, flu",
"flu, fever",
"cold, flu",
"day, flu",
"day, flu",
"flu, day",
"flu",
"flu",
"flu, day",
"flu",
"fever, flu",
"flu, cold",
"flu",
"night, flu, fever",
"flu",
"cold, flu",
"flu, day",
"cold, flu",
"flu",
"flu",
"flu, fever",
"flu",
"flu",
"flu",
"flu, fever",
"flu",
"flu, day",
"fever, flu",
"love, flu",
"flu, cold",
"night, flu, fever",
"cold, flu",
"flu, day",
"cold, flu",
"flu, cold, fever",
"flu",
"cold, flu",
"flu, day, love",
"cold, flu",
"flu, cold",
"cold, flu",
"cold, flu",
"flu, fever, day",
"flu",
"cold, flu",
"flu",
"cold, flu",
"cold, flu",
"flu, cold",
"Cold, cold, flu",
"flu, day",
"flu, cold",
"fever, flu",
"love, cold, flu",
"cold, flu",
"flu",
"flu",
"flu",
"flu",
"flu",
"flu",
"day, flu",
"cold, flu",
"flu",
"flu, fever",
"flu, day",
"flu",
"love, flu",
"flu",
"flu, fever",
"day, flu",
"flu",
"fever, flu",
"flu",
"fever, flu",
"flu",
"cold, flu",
"flu",
"flu",
"flu, day",
"flu",
"flu, day",
"cold, flu"]


# write data to the text file: data.basket
f = open('data.basket', 'w')
for item in raw_data:
    f.write(item + '\n')
f.close()

# Load data from the text file: data.basket
data = Orange.data.Table("data.basket")


# Identify association rules with supports at least 0.3
rules = Orange.associate.AssociationRulesSparseInducer(data, support = 0.3)


# print out rules
print "%4s %4s  %s" % ("Supp", "Conf", "Rule")
for r in rules[:]:
    print "%4.1f %4.1f  %s" % (r.support, r.confidence, r)

rule = rules[0]
for idx, d in enumerate(data):
    print '\nUser {0}: {1}'.format(idx, raw_data[idx])
    for r in rules:
        if r.applies_left(d) and not r.applies_right(d):
            print "%4.1f %4.1f  %s" % (r.support, r.confidence, r)

