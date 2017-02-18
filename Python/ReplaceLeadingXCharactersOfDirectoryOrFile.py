import os
print("Please specify the directory you want to perform action:")
sourceDir = input()
print(sourceDir+"\n")
dir=os.listdir(sourceDir)
print(dir)
print("How many leading characters you would like to replace?")
x=int(input())
print("What string will be the replacement?")
replaceString=input()
dir2 = [replaceString+dir0[x:] for dir0 in dir]
print(dir2)
for directory in dir:
    os.rename(sourceDir+"\\"+directory,sourceDir+"\\"+replaceString+directory[x:])
print("Successfully renamed files/directory!")
