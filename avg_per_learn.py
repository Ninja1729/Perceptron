# NLP Assignment 2 - Niranjana Kandavel - 15st October 2016


import os
import timeit
import pickle

import sys
import random

# get input file path
#file_path = '/home/ninja/PycharmProjects/NlpAssign2_new/tenper'
file_path = sys.argv[1]

# defining dictionary
words = defaultdict(int)
avg_words = defaultdict(int)
main_dict = defaultdict(int)
file_names_dict = defaultdict()


# recursively get the file names and its contents
for root, dirs, files in os.walk(file_path):
    for file in files:
        if file.endswith(".txt"):
            fullfilename = os.path.join(root, file)
            file_names_dict[fullfilename] = open(fullfilename, "r", encoding="latin1").read().split()


# recursively going through each file and calculate all the weight of words
count = 1
b = 0
a_b = 0
items = list(file_names_dict.keys())
for iterate in range(0, 30):
    random.shuffle(items)
    for file in items:
        if "spam" in file:
            y = 1
        elif "ham" in file:
            y = -1
        else:
            continue
        alpha = 0
        tokens = file_names_dict[file]
        for w in tokens:
            alpha += words[w]
        alpha += b
        if ((y * alpha) <= 0):
            for w in tokens:
                words[w] += y
                avg_words[w] += (y*count)
            b += y
            a_b += (y*count)
        count += 1
items = list(words.keys())
for w in items:
    avg_words[w] = words[w] - ((1/count)*avg_words[w])
a_b = b - ((1/count)*a_b)

# nested dictionary
main_dict["word_weights"] = avg_words
main_dict["bias"] = a_b

# store it in a file
pickle.dump(main_dict, open("per_model.txt","wb"))

