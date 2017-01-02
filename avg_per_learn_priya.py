# NLP Assignment 2 - Niranjana Kandavel - 15st October 2016

import os,random
import sys
import pickle
import time

dir_path = '/home/ninja/PycharmProjects/NlpAssign2_new/spamham/train'
start_time = time.time()
word_weight_dict = {
    "weights" : {},
    "words" : {}, # average weights
    "bias" : 0, # average bias
    "weights_bias" : 0
}

tokenized_file = []
y = 0
c = 1
# Goes through the files and folders in training data and calculates weight
def perceptron_train():
    global c
    for i in range(0,1):
        for root, subFolder, files in os.walk(dir_path):
            if len(files) != 0 and any(".txt" in s for s in files):
                #files = random.shuffle(files)

                for f in files:
                    if ".txt" in f:
                        if "ham" in f:
                            type = "ham"
                            y = -1
                        elif "spam" in f:
                            type = "spam"
                            y = 1
                        else:
                            continue
                        filename = open(os.path.join(root,f), "r", encoding="latin1")
                        contents = filename.read()
                        tokenized_file = contents.split()
                        filename.close()

                        # Collects word count
                        alpha = 0
                        for word in tokenized_file:
                            if word in word_weight_dict["words"].keys():
                                # get the current weight of the word
                                alpha = alpha + word_weight_dict["weights"][word]
                            else:
                                word_weight_dict["weights"][word] = 0
                                word_weight_dict["words"][word] = 0
                        alpha = alpha + word_weight_dict["weights_bias"]
                        if(y*alpha) <= 0:
                            # update all the weights
                            for word in tokenized_file:
                                word_weight_dict["weights"][word] += y
                                word_weight_dict["words"][word] += (y*c)
                            word_weight_dict["weights_bias"] += y
                            word_weight_dict["bias"] += (y*c)
                        c = c + 1

    for word in word_weight_dict["words"].keys():
        word_weight_dict["words"][word] = word_weight_dict["weights"][word] - ((1/c)*word_weight_dict["words"][word])
    word_weight_dict["bias"] = word_weight_dict["weights_bias"] - ((1/c)*word_weight_dict["bias"])

perceptron_train()

# Dump the dictionary into the pickle file
model_file = open( "per_model.txt", "wb" )
pickle.dump( word_weight_dict, model_file )
model_file.close()
print(word_weight_dict["weights_bias"])
print(word_weight_dict["bias"])
print("--- %s seconds ---" % (time.time() - start_time))
