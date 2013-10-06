#Compare Files and remove Duplicates
import os

with open('file1.txt', 'r') as f:
    data3 = f.readlines()
print(len(data3))

with open('file2.txt', 'r') as f:
    data2 = f.readlines()


for i in range(0,len(data2)):
    str1 = data2[i]
    for z in range(0, len(data3)):
        str2 = data3[z]
        if (str1 == str2):
            q = 1
            break
        else:
            q = 0

    if q==0:
        data3.append(str1)
        
            


file2 = open('MasterList.txt','w')
for item in data3:
  file2.write("%s" % item)
