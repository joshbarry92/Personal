file = open('file1.txt','r')
#Read in the file as a string
data = file.read()
#Close the file
file.close()
#Set strNew with shipping code and replace in XML file
data = data.replace("'",'')

data = data.strip('\t\n\r')
data = data.replace('\n','')
data = data.replace(' ', '')
data = data.replace('J','\nJ')
#UNCOMMENT FOR DEBUGGING
print(data)

file2 = open('file2.txt','w')
#file2 = open('K:\\Documents\\Result.txt', 'w' )

file2.write(data)
file2.close()
