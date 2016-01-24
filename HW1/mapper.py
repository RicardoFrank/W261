#!/usr/bin/python

##The following mapper reducer pair does organization in the mapper.
##The output is a list with entries being (ID, target_word_count), and the last entry being a list of words in spam
##The reducer takes the list of all words in all spam, creates a total list
##Using the total list size and target_word_count, we compute the probability of spam

import sys
import re

## collect user input

filename = sys.argv[1]
findword = sys.argv[2]  #ok for this example since we only have 1 arg
 
lines = open(filename).read().splitlines()

#no need to check lines for correct number of fields.  All have 4

set_of_words_spam = ""
set_of_words_not_spam = ""
output_set = []
spam_count = 0
email_count = 0
target_in_spam_count = 0
target_in_not_spam_count = 0
words_in_spam_count = 0
words_in_not_spam_count = 0

#append ID and target word count to output
#get set of words in spam
#get [spam email, email] count
for line in lines:
    if len(line.split('\t')) == 4:
        tmp = line.split('\t')
        all_text = tmp[2] + " " + tmp[3]
        true_label = tmp[1]
        
        #append the tuple (ID, target word count)
        target_word_count = len(re.findall(findword,all_text))
        output_set.append(str(tmp[0] + "," + str(target_word_count)) + "," + true_label)
            
        #if spam
        if tmp[1] == "1":
            #check to see if we've seen the word before in spam
            for word in all_text.split(' '):
                if word not in set_of_words_spam:
                    set_of_words_spam = set_of_words_spam + word + " "
            
            #increment number of times seen in spam and total spam words
            target_in_spam_count += len(re.findall(findword,all_text))
            words_in_spam_count += len(all_text.split(' '))
            spam_count += 1
        
        #not spam
        else:
            #check to see if the word is in the total corpus
            for word in all_text.split(' '):
                if word not in set_of_words_not_spam:
                    set_of_words_not_spam = set_of_words_not_spam + word + " "
            
            #increment number of times seen in not_spam
            target_in_not_spam_count += len(re.findall(findword,all_text))
            words_in_not_spam_count += len(all_text.split(' '))
            
        email_count += 1

#append email stats
output_set.append(str(spam_count)+","+str(email_count))

#append word stats
output_set.append(str(target_in_spam_count)+","+str(target_in_not_spam_count))

#append target stats
output_set.append(str(words_in_spam_count)+","+str(words_in_not_spam_count))

#append spam words
output_set.append(set_of_words_spam)

#append total corpus
output_set.append(set_of_words_not_spam)


#print list of info
for element in output_set:
    print element