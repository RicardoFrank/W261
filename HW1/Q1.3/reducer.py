#!/usr/bin/python

import sys
import re
import math

total_set_of_spam = ""
total_set_of_not_spam = ""
words_in_spam = 0
words_in_not_spam = 0
target_in_spam = 0
target_in_not_spam = 0
spam_count = 0
email_count = 0

#get set_of_spam words from each file and combine
for filename in sys.argv[1:]:
    
    lines = open(filename).read().splitlines()
    
    #extract the data in each chunk
    spam_count += int(lines[-5].split(',')[0])
    email_count += int(lines[-5].split(',')[1])
    words_in_spam += int(lines[-4].split(',')[0])
    words_in_not_spam += int(lines[-4].split(',')[1])
    target_in_spam = int(lines[-3].split(',')[0])
    target_in_not_spam = int(lines[-3].split(',')[1])
    set_of_spam = lines[-2]
    set_of_not_spam = lines[-1]
    
    for word in set_of_spam.split(' '):
        if word not in total_set_of_spam:
            total_set_of_spam = total_set_of_spam + word + " "
            
    for word in set_of_not_spam.split(' '):
        if word not in total_set_of_not_spam:
            total_set_of_not_spam = total_set_of_not_spam + word + " "

#going to total count of words in each class instead of unique
total_words_in_spam = len(total_set_of_spam.split(' '))
total_words_int_not_spam = len(total_set_of_not_spam.split(' '))

p_spam = float(spam_count) / float(email_count)
p_not_spam = 1 - p_spam


#compute probability of spam vs not spam
for filename in sys.argv[1:]:
    lines = open(filename).read().splitlines()
    
    #remove the email stats, spam word set, and total vocab set
    lines = lines[0:-5]
    
    for line in lines:
        ID = line.split(',')[0]
        target_count = line.split(',')[1]
        #p_word = float(target_count) / float(total_words_unique) 
        p_cond_spam = float(target_in_spam) / float(total_words_in_spam)
        p_cond_not_spam = float(target_in_not_spam) / float(total_words_int_not_spam)
        
        #P(SPAM | word) = [P(word | SPAM) * P(SPAM)] / P(word)
        #why is the equation above wrong?
        #log(P) = log(P(word|SPAM)) + log(P(SPAM)) - log(P(word))
        
        #log_prob_spam = math.log(p_cond_spam) + math.log(p_spam) - math.log(p_word)
        #log_prob_not_spam = math.log(p_cond_not_spam) + math.log(p_not_spam) - math.log(p_word)

        #P(SPAM | word) = p_spam * P(word|SPAM) * word_count
        
        log_prob_spam = math.log(p_spam) + math.log(p_cond_spam) * float(target_count)
        log_prob_not_spam = math.log(p_not_spam) + math.log(p_cond_not_spam) * float(target_count)
        
        if log_prob_spam > log_prob_not_spam:
            print ID + ",1," + str(log_prob_spam) + "," + str(log_prob_not_spam)
        else:
            print ID + ",0," + str(log_prob_spam) + "," + str(log_prob_not_spam)
        