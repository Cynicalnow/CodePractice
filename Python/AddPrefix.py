import os

print("Please specify the folder in which files exists:")
workDir=input()

print("Please input the prefix:")
prefix=input()
fileLists=os.listdir(workDir)

for files in fileLists:
    newfiles=prefix+files
    os.rename(os.path.join(workDir,files),os.path.join(workDir,newfiles))

print("Done!")
