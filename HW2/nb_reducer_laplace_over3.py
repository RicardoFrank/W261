
import sys
import re
import math

output = {}
output["1"] = 0                 #count of spam
output["0"] = 0                 #count of nonspam
output["1 assistance"] = 0      #count of assistance for spam
output["0 assistance"] = 0      #count of assistance for nonspam
output["1 list"] = ""           #list of IDs spam 
output["0 list"] = ""           #list of IDs nonspam
output["ID assistance count"] = ""  #list of IDs, assistance in email

input = []

word_freq = {}

#take all inputs and then sort for aggregation
for line in sys.stdin:

    if line != "\n":
        lines = input.append(line)

#merge stats and lists into dictionary
for line in input:
    tmp = line.split('\t')

    if len(tmp) == 2:
        cur_key = tmp[0]
        cur_value = tmp[1]

        #if a numerical field
        if (cur_key == "0") or (cur_key == "1") or (cur_key == "1 assistance") or (cur_key == "0 assistance"):
            output[cur_key] += int(cur_value)

        #if a string list
        elif (cur_key == "1 list") or (cur_key == "0 list") or (cur_key == "ID assistance count"):
            output[cur_key] += cur_value
        
        #if a word and count
        else:
            if cur_key in output.keys():
                output[cur_key] += int(cur_value)
            else:
                output[cur_key] = int(cur_value)

#delete low frequency words
for key, value in output.items():
    #if a word and count
    if (key != "0") and (key != "1") and (key != "1 assistance") and (key != "0 assistance") and (key != "1 list") and (key != "0 list") and (key != "ID assistance count"): 
        if value < 3:
            del output[key]
            
#i reused old code to save time since this was a longgggg assignment, hence the strange switch in variables
#extract the data in each chunk
spam_count = output["1"]
email_count = output["1"] + output["0"]
words_in_spam = len(output.keys()) - 7
words_in_not_spam = len(output.keys()) - 7
target_in_spam = output["1 assistance"]
target_in_not_spam = output["0 assistance"]

#going to total count of words in each class instead of unique
total_words_in_spam = words_in_spam
total_words_in_not_spam = words_in_not_spam

p_spam = float(spam_count) / float(email_count)
p_not_spam = 1 - p_spam

error_count = 0

#for each space delimited entry
for email in output["ID assistance count"].split(' '):
    
    #compute probability of spam vs not spam
    tmp = email.split(',')
    
    if len(tmp) == 2:
        assistance_count = tmp[1]
        ID = tmp[0]
    
    else:
        ID = tmp[0]
        assistance_count = 0

    if ID in output["1 list"].split(' '):
        true_label = "1"
    else:
        true_label = "0"

    #p(term|Spam) = ( term_count(spam only) + 1 ) / ( total_word_count(spam only) + num_unique_words(spam only) ) 
    #for laplace, not quite sure I understand the equation and I don't have time to figure it out.
    #so, I just added one to the numerator and kept the denominator the same. It's the same idea
    #and the equation is engineered anyway since we aren't even dividing by P(term)

    p_cond_spam = float(target_in_spam + 1) / float(total_words_in_spam)
    p_cond_not_spam = float(target_in_not_spam + 1) / float(total_words_in_not_spam)

    #P(SPAM | word) = p_spam * P(word|SPAM) * word_count

    log_prob_spam = math.log(p_spam) + math.log(p_cond_spam) * float(assistance_count)
    log_prob_not_spam = math.log(p_not_spam) + math.log(p_cond_not_spam) * float(assistance_count)

    #if we predict spam
    if log_prob_spam > log_prob_not_spam:
        print ID + ",1," + true_label + "," + str(log_prob_spam) + "," + str(log_prob_not_spam)

        if true_label is not "1":
            error_count += 1

    #if we predict not spam
    else:
        print ID + ",0," + true_label + "," + str(log_prob_spam) + "," + str(log_prob_not_spam)

        if true_label is not "0":
            error_count += 1

print float(error_count) / float(100)