import os
import shutil


dir_src = ("/home/ninja/PycharmProjects/NlpAssign2_new/SpamHam/train")
dir_dst_ham = ("/home/ninja/PycharmProjects/NlpAssign2_new/tenper/ham")
dir_dst_spam = ("/home/ninja/PycharmProjects/NlpAssign2_new/tenper/spam")

tot_spam = 0
tot_ham = 0
for root, dirs, files in os.walk(dir_src):
    for file in files:
        if file.endswith('.txt'):
            if "spam" in file:
                tot_spam += 1
            if "ham" in file:
                tot_ham += 1

print("Total Ham : "+str(tot_ham))
print("Total Spam : "+str(tot_spam))
spam_count = (tot_spam*10)/100
ham_count = (tot_ham*10)/100
print("Ten Per Ham : "+str(ham_count))
print("Ten Per Spam : "+str(spam_count))
copy_ham = 0
copy_spam = 0

for root, dirs, files in os.walk(dir_src):
    for file in files:
        if file.endswith('.txt'):
            if copy_spam < spam_count:
                if "spam" in file:
                    fullfilename = os.path.join(root, file)
                    shutil.copy(fullfilename, dir_dst_spam)
                    copy_spam += 1
            if copy_ham < ham_count:
                if "ham" in file:
                    fullfilename = os.path.join(root, file)
                    shutil.copy(fullfilename, dir_dst_ham)
                    copy_ham += 1