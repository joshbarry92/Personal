import os

#Define Lists
powershell_files = []
text_files = []

path = 'C:\\Users\\jbarry2\\Desktop'
x = os.listdir(path)

for i in x:
    if '.ps1' in i:
        powershell_files.append(i)
    elif '.txt' in i:
        text_files.append(i)


print(powershell_files)
print(text_files)

    
