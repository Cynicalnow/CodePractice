import os

workDir=input("Please specify the working folder:\n")

while True:
    newFolder=input("Please specify the new folder name (input 0 to quit):\n")
    if(newFolder!="0"):
        os.mkdir(os.path.join(workDir,newFolder))
    else:
        break

print("Done!")
