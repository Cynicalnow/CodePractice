import os

srcDir = input("Please specify the directory you want to perform action:")
print("The files to be renamed are:")
dir=os.listdir(srcDir)
for item in dir:
    print(os.path.join(srcDir,item))
print()

inputDir=input("Please pecify the destination folder:(if stay the same \
please hit ENTER)")

if(inputDir==""):
    dstDir=srcDir
else:
    dstDir=inputDir
    
print("How many leading characters you would like to replace? (If adding prefix\
only please type \"0\")")

x=int(input())

print("What string will be the replacement?")
replaceString=input()
dir2 = [replaceString+dir0[x:] for dir0 in dir]
print("Here are the result files:")
for item in dir2:
    print(os.path.join(dstDir,item))
for directory in dir:
    os.rename(os.path.join(srcDir,directory),os.path.join(dstDir,(replaceString\
                                                                  +directory[x:\
                                                                             ])\
                                                          ))
print("Successfully renamed files/directory!")
