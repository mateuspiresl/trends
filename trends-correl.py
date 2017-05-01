import json
from scipy.stats.stats import pearsonr    
import os
 
l1 = list()
l2 = list()
 
file1 = raw_input()
file2 = raw_input()
 
os.system("node ./trends/index.js " + file1)
os.system("node ./trends/index.js " + file2)
 
with open(file1+'.json') as data_file:    
    data = json.load(data_file)
 
for i in data["default"]["timelineData"]:
    l1.append(i["value"][0])
 
with open(file2+'.json') as data_file:    
    data = json.load(data_file)
 
for i in data["default"]["timelineData"]:
    l2.append(i["value"][0])
   
print pearsonr(l1, l2)[0]