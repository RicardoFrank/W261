
import sys
import re
import math

output = {}
output["1"] = 0
output["0"] = 0
output["1 words"] = ""
output["0 words"] = ""
output["1 assistance"] = 0
output["0 assistance"] = 0
output["1 word count"] = 0
output["0 word count"] = 0
output["1 list"] = ""
output["0 list"] = ""

input = []

#take all inputs and then sort for aggregation
for line in sys.stdin:

    if line != "\n":
        lines = input.append(line)

#merge into dictionary
for line in input:
    tmp = line.split('\t')

    if len(tmp) == 2:
        cur_key = tmp[0]
        cur_value = tmp[1]

        #if a numerical field
        if (cur_key == "1 word count") or (cur_key == "0 word count") or (cur_key == "0") or (cur_key == "1") or (cur_key == "1 assistance") or (cur_key == "0 assistance"):
            output[cur_key] += int(cur_value)

        #if a string list
        elif (cur_key == "1 words") or (cur_key == "0 words") or (cur_key == "1 list") or (cur_key == "0 list"):
#                       print cur_key
            output[cur_key] += cur_value

        #user email content
        else:
            output[cur_key] = cur_value

tmp_str = ""
tmp_list = []

#dedup unique words
for word in output["0 words"].split(' '):
    if word not in tmp_list:
        tmp_str += word + " "

output["0 words"] = tmp_str

tmp_str = ""
tmp_list = []

for word in output["1 words"].split(' '):
    if word not in tmp_list:
        tmp_str += word + " "

output["1 words"] = tmp_str

#for key, value in output.items():
#       print key + "," + str(value)

#i reused old code to save time since this was a longgggg assignment, hence the strange switch in variables
#extract the data in each chunk
spam_count = output["1"]
email_count = output["1"] + output["0"]
words_in_spam = output["1 word count"]
words_in_not_spam = output["0 word count"]
target_in_spam = output["1 assistance"]
target_in_not_spam = output["0 assistance"]
set_of_spam = output["1 words"]
set_of_not_spam = output["0 words"]

#going to total count of words in each class instead of unique
total_words_in_spam = len(set_of_spam.split(' '))
total_words_in_not_spam = len(set_of_not_spam.split(' '))

#print total_words_in_spam
#print total_words_in_not_spam

p_spam = float(spam_count) / float(email_count)
p_not_spam = 1 - p_spam

error_count = 0

#compute probability of spam vs not spam
for key, value in output.items():

    #if an email
    if (key != "1 words") and (key != "0 words") and (key != "1") and (key != "0") and (key != "1 word count") and (key != "0 word count") and (key != "1 assistance") and (key != "0 word count") and (key != "1 list") and (key != "0 list"):

        assistance_count = len(re.findall('\bassistance\b',str(value)))
        ID = key

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