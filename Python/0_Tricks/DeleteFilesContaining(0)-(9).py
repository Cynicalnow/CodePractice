import os,re

path=input("Please specify the folder in which the files exist:\n")

fileList=os.listdir(path)

for file in fileList:
    if re.search('('+'[0-9]'+')',file):
        os.remove(os.path.join(path,file))

