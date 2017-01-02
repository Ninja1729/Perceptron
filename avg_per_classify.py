# NLP Assignment 1 - Niranjana Kandavel - 21st September 2016


import os
import pickle
from collections import defaultdict
import sys

# get input file path
#file_path = '/home/ninja/PycharmProjects/NlpAssign1/tenpercent_ravi'
file_path = '/home/ninja/PycharmProjects/NlpAssign2_new/spamham/dev'
#file_path = sys.argv[1]
#fout = sys.avg[1]
fout = open('avg_per_output.txt','w')

# defining dictionary for all words, spam words, ham words and count of ham files, spam files
main_dict = pickle.load(open("per_model.txt", "rb"))
words = main_dict["word_avg_weights"]
bias = main_dict["avg_bias"]


# recursively going through each file and calculate all the counts
cal_spam_count = 0
cal_ham_count = 0
act_spam_count = 0
act_ham_count = 0
match = 0
mismatch = 0
ham_match = 0
spam_match = 0



#scan the files recursively and caculate the probablity of spam and ham files
for root, dirs, files in os.walk(file_path):
    for file in files:
        if file.endswith('.txt'):
            fullfilename = os.path.join(root, file)
            tokens = open(fullfilename, "r", encoding="latin1").read().split()
            alpha = 0
            for w in tokens:
                if w in words:
                    alpha += words[w]
            alpha += bias
            isham = 0
            if (alpha > 0):
                fout.write("SPAM" + " " + fullfilename + "\n")
                cal_spam_count += 1
            else:
                fout.write("HAM" + " " + fullfilename + "\n")
                cal_ham_count += 1
                isham += 1
        if file.endswith('ham.txt'):
            act_ham_count += 1
            if (isham == 1):
                match += 1
                ham_match += 1
            else:
                mismatch += 1
        if file.endswith('spam.txt'):
            act_spam_count += 1
            if (isham == 1):
                mismatch += 1
            else:
                match += 1
                spam_match += 1

print ("Calculated Spam Files : "+str(cal_spam_count))
print ("Calculated Ham Files : "+str(cal_ham_count))
print ("Actual Spam Files : "+str(act_spam_count))
print ("Actual Ham Files : "+str(act_ham_count))
print ("Match : "+str(match))
print ("Mismatch : "+str(mismatch))


pre_ham = ham_match*100/cal_ham_count
print("Ham Precision : "+str(pre_ham))
recall_ham = ham_match*100/act_ham_count
print("Ham Recall : "+str(recall_ham))
f1_ham = (2 * pre_ham * recall_ham) / (pre_ham + recall_ham)
print("Ham F1 score : "+str(f1_ham))

pre_spam = spam_match*100/cal_spam_count
print("Spam Precision : "+str(pre_spam))
recall_spam = spam_match*100/act_spam_count
print("Spam Recall : "+str(recall_spam))
f1_spam = (2 * pre_spam * recall_spam) / (pre_spam + recall_spam)
print("Spam F1 Score : "+str(f1_spam))

#few other calculation(not part of assignmnet)
accuracy = match*100/(act_ham_count+act_spam_count)
print("Accuracy : "+str(accuracy))