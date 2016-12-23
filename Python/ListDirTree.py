import os

rootDir=input("Please specify the root directory/folder which you would like to execute:")



if(os.listdir(rootDir)):
    Level1=os.listdir(rootDir)
    for item in Level1:
        print(item)
    Level1Dir=[os.path.join(rootDir,item) for item in Level1]
else:
    print ("No subdirectory exists or folder is empty!")

for item in Level1Dir:
    if(os.listdir(item)):
        Level2=os.listdir(item)
        Level2Dir=[os.path.join(Level1Dir,item) for item in Level2]





