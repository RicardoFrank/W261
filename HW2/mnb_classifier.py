
import sys
import re
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.metrics import classification_report
from sklearn.feature_extraction.text import *
import numpy as np

data = []
label = []
for line in sys.stdin:
    tmp = line.split('\t')
    
    if len(tmp) == 4:
        data.append(re.split("[, \.\n]+", tmp[2]+tmp[3]))
    
    else:
        data.append(re.split("[, \.\n]+", tmp[-1]))
    
    label.append(tmp[1])
    
#print (data.shape)
tmp_str = ""
tmp = []

for entry in data:
    
    tmp_str = ""
    for token in entry:
        tmp_str = tmp_str + " " + token
    tmp.append(tmp_str)
    
#print(tmp)

countVec = CountVectorizer(analyzer=u'word')
DocMatrix= countVec.fit_transform(tmp)

MNB = MultinomialNB()
MNB.fit(DocMatrix,label)
train_pred_MNB = MNB.predict(DocMatrix)
print(classification_report(label, train_pred_MNB))
    