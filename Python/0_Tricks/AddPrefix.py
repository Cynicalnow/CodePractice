import os

workDir=input("Please specify the folder in which files exists:\n")
prefix=input("Please input the prefix:")

fileLists=os.listdir(workDir)

for files in fileLists:
    newfiles=prefix+files
    os.rename(os.path.join(workDir,files),os.path.join(workDir,newfiles))

print("Done!")
