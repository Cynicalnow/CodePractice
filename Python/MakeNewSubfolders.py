import os

print("Please specify the working folder:")
workDir=input()

while True:
    print("Please specify the new folder name (input 0 to quit):")
    newFolder=input()
    if(newFolder!="0"):
        os.mkdir(os.path.join(workDir,newFolder))
    else:
        break

print("Done!")
