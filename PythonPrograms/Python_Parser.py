# Python program to read
# json file


import json
import sys

# Opening JSON file
print(sys.argv)
print(sys.argv[1])
f = open(sys.argv[1])

# returns JSON object as
# a dictionary
data = json.load(f)

f2=open("log.txt","r")
all_of_it=f2.read()

# Iterating through the json
# list

for i in data:
    if data[i] in all_of_it:
        print(data[i],"Yes Present")
    else:
        print(data[i],"Not Present")


# Closing file
f.close()
f2.close()
