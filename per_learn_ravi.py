import os
import sys
import pickle
import time

learning_data = {"weights":{}, "bias":0}
start_time = time.time()
for iterate in range(0, 20):
	for path, dirs, files in os.walk(str(sys.argv[1])):
		for filename in files:
			#print(path);
			if "spam.txt" in filename:
                        	label = 1
			elif "ham.txt" in filename:
                        	label = -1
			else:
				continue;

			fullpath = os.path.join(path, filename)
			fd = open(fullpath, "r", encoding="latin1")
			string = fd.read()
			fd.close()
			tokens = string.split();
			alpha = 0;
			for token in tokens:
				if token in learning_data["weights"].keys():
					alpha += learning_data["weights"][token];
				else:
					learning_data["weights"][token] = 0;
			alpha += learning_data["bias"];

			if ((label*alpha) <= 0):
				for token in tokens:
					learning_data["weights"][token] += label;
				learning_data["bias"] += label;

print (learning_data["weights"])
print (learning_data["bias"])
print("--- %s seconds ---" % (time.time() - start_time))
