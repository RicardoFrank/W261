
#the mapper is changed to keep count of all words seen in the dictionary
#so the reducer can filter and compute

import sys
import re

## collect user input

input = []

for line in sys.stdin:
    input.append(line)

output = {}
output["1"] = 0                 #count of spam
output["0"] = 0                 #count of nonspam
output["1 assistance"] = 0      #count of assistance for spam
output["0 assistance"] = 0      #count of assistance for nonspam
output["1 list"] = ""           #list of IDs spam 
output["0 list"] = ""           #list of IDs nonspam
output["ID assistance count"] = ""  #list of IDs, assistance in email

skip_email = False

#go through line-by-line and count assistance
#note any new words in spam / not spam
#and count spam emails

for line in input:

    skip_email = False

    if len(line.split('\t')) == 4:
        tmp = line.split('\t')
        all_text = tmp[2] + " " + tmp[3]
        true_label = tmp[1]

    #empty subject
    elif len(line.split('\t')) == 3:
        tmp = line.split('\t')
        all_text = tmp[-1]
        true_label = tmp[1]

    else:
        skip_email = True

    clean_line = re.split("[, \.\n]+", all_text)

    if skip_email is False:
        #count number of times assistance is present
        #output["assistance"] += len(re.findall("assistance",clean_line))

        #append ID,assistance_count
        id = tmp[0]
        if output["ID assistance count"] == "":
                output["ID assistance count"] = id+","+str(len(re.findall(r'\bassistance\b',all_text)))+" "
        else:
            output["ID assistance count"] += id+","+str(len(re.findall(r'\bassistance\b',all_text)))+" "
        
        #add words seen and increment keys
        tokens = re.split("[, \.\n]+", all_text)
        for word in tokens:
            if word in output.keys():
                output[word] += 1
            else:
                output[word] = 1
        
        #if spam
        if tmp[1] == "1":
            #add id to spam list
            output["1 list"] += id + " "

            #increment spam count, assistance in spam count, and words in spam
            matches = re.findall(r'\bassistance\b',all_text)

            output["1 assistance"] += len(matches)
            output["1"] += 1

                #if len(matches) > 0:
                #       print line
        #not spam
        else:
            #add id to not spam list
            output["0 list"] += id + " "

            #increment not spam count, assistance in not spam count, and words
            #not in spam
            matches = re.findall(r'\bassistance\b',all_text)
            output["0 assistance"] += len(matches)
            output["0"] += 1

#print all info
for key, value in output.items():
    print key + "\t" + str(value)