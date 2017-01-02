# NLP Assignment 2 - Niranjana Kandavel - 15th October 2016


import os
import pickle
from collections import defaultdict
import sys

# get input file path

#file_path = '/home/ninja/PycharmProjects/NlpAssign2_new/SpamHam/dev'
file_path = sys.argv[1]
output_file = sys.argv[2]
fout = open(output_file,'w', encoding="latin1")
#fout = open('per_output.txt','w')

# defining dictionary
main_dict = pickle.load(open("per_model.txt", "rb"))
words = main_dict["word_weights"]
bias = main_dict["bias"]



cal_spam_count = 0
cal_ham_count = 0
act_spam_count = 0
act_ham_count = 0
match = 0
mismatch = 0
ham_match = 0
spam_match = 0



#scan the files recursively and check if a file is ham  or spam
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



