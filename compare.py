#Compare Files and remove Duplicates
import os

#Open Old File
with open('file3.txt', 'r') as f:
    data3 = f.readlines()

#Open New File
with open('file2.txt', 'r') as f:
    data2 = f.readlines()

data = []

for i in range(0,len(data2)):
    str1 = data2[i]
    str1 = str1.strip('\n')
    for z in range(0, len(data3)):
        #print(z)
        str2 = data3[z]
        str2 = str2.strip('\n')
        if (str1 != str2):
            q = 0
        else:
            q=1
            break

    if q==0:
        data.append(str1)
        
            

file2 = open('file_diff.txt','w')
for item in data:
  file2.write("%s\n" % item)
file2.close()
