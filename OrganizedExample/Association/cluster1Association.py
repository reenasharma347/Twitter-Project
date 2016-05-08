
# coding: utf-8

# In[1]:

import Orange


raw_data = ["love, sneezing",
"sneezing, day",
"love, sneezing",
"sneezing, love",
"love, sneezing",
"night, sneezing",
"sneezing, day",
"cold, fever",
"sneezing, day",
"sneezing, day",
"day, sneezing",
"sneezing, night, fever",
"sneezing",
"day, sneezing",
"cold, sneezing",
"sneezing, night, cold",
"cold, sneezing",
"sneezing, night",
"cold, sneezing",
"fever, cold, day",
"love, sneezing",
"sneezing, day",
"day, sneezing",
"day, sneezing",
"sneezing, cold",
"Good, day, sneezing",
"day, sneezing",
"cold, sneezing",
"day, sneezing, flu",
"fever, day",
"fever",
"fever",
"day, sneezing",
"sneezing, cold",
"day, sneezing",
"flu, sneezing",
"fever, sneezing",
"sneezing, day",
"love, sneezing",
"day, sneezing",
"love, cold, dehydrated",
"sneezing",
"love, sneezing",
"sneezing, cold",
"day, sneezing",
"cold, sneezing",
"love, sneezing",
"cold, sneezing",
"sneezing, cold, good",
"sneezing",
"fever",
"love, sneezing",
"sneezing, day",
"love, sneezing",
"love, sneezing",
"sneezing, day",
"fever, cold",
"cold, sneezing",
"love, sneezing",
"sneezing"]


# write data to the text file: data.basket
f = open('data.basket', 'w')
for item in raw_data:
    f.write(item + '\n')
f.close()

# Load data from the text file: data.basket
data = Orange.data.Table("data.basket")


# Identify association rules with supports at least 0.3
rules = Orange.associate.AssociationRulesSparseInducer(data, support = 0.2)


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

