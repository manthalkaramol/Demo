# Python program to read
# json file


import json
import sys
import re

f2=open("log.txt","r")
lines=f2.readlines()


pattern = r"((20)\d\d-\d\d-\d\d \d\d:\d\d:\d\d)"
result=""

# Iterating through the json
# list
job_name=""
for line in lines:
    if "Building remotely on Windows in" in line:
        job_name=line.split("\\")[-1]
        break
for line in lines:
    result = re.match(pattern, line)
    if result:
        print(result.group())
        break
print(job_name)
f2.close()
