import os
import time

def chooseOperation():
    choice=input("Would you like to add prefix or suffix? (p for prefix, s fo\
r suffix)\n")
    return choice

def strfix():
    strfix=str(input("Please specify the string you want to use for prefix/su\
ffix?\n"))
    return strfix

def strextension():
    strext=str(input("Please specify the file extension that will be affected\
:")).lower()
    if(strext[0]!="."):
        strext="."+strext
    return strext

def addPrefix(prefix,extension):
    workDir=input("Please specify the folder in which files exists:\n").strip()
    fileLists=os.listdir(workDir)
    
    fileCount=0

    for files in fileLists:
        if(files[len(files)-len(str(extension)):].lower()==extension):
            newfiles=str(prefix)+files
            os.rename(os.path.join(workDir,files),
                      os.path.join(workDir,newfiles))
            fileCount=fileCount+1
    return fileCount

def addSuffix(suffix,extension):
    workDir=input("Please specify the folder in which files exists:\n").strip()
    fileLists=os.listdir(workDir)

    fileCount=0

    for files in fileLists:
        if(files[len(files)-len(str(extension)):].lower()==extension):
            newfiles=files[:len(files)-len(str(extension))-1]+str(suffix)+extension
            os.rename(os.path.join(workDir,files),
                      os.path.join(workDir,newfiles))
            fileCount=fileCount+1
    return fileCount

if __name__=="__main__":
    userchoice=chooseOperation()
    if (userchoice in ["p","P"]):
        strfix=strfix()
        strext=strextension()
        try:
            fileCount=addPrefix(strfix,strext)
            if fileCount!=0:
                print(str(fileCount)+" file(s) affected!")
                print("Done!")
            else:
                print("No file affected!")
        except:
            print("Wrong directory!")
    elif (userchoice in ["s","S"]):
        strfix=strfix()
        strext=strextension()
        fileCount=addSuffix(strfix,strext)
        if fileCount!=0:
            print(str(fileCount)+" file(s) affected!")
            print("Done!")
        else:
            print("No file affected!")
    else:
        print("Wrong choice, please run the program again!")
    time.sleep(1000)
