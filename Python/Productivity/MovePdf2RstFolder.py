import os
import time
import shutil

timestamp=timestamp=str(time.localtime(time.time())[3])+\
           '-'+str(time.localtime(time.time())[4])+\
           '-'+str(time.localtime(time.time())[5])
srcDir =input("Please provide the Source File Folder:\n").strip()
dstDir=os.path.join(srcDir,"Result"+"_"+timestamp)
os.mkdir(os.path.join(srcDir,"Result"+"_"+timestamp))
extension=".PDF"
ListFile=os.path.join(srcDir,"ToMove.txt")

#Read "ToMove.txt" from source Folder!
def readList(ListFile):
   with open(ListFile) as f:
      fileNames=f.readlines()
   fileList=[item.strip("\n") for item in fileNames]
   return fileList

def MovePdf2RstFolder(fileList,srcDir,dstDir):
   for item in fileList:
      shutil.copy(srcDir+ os.path.sep + item,dstDir+ os.path.sep + item)

fileList=readList(ListFile)
fileList=(item+extension for item in fileList)
MovePdf2RstFolder(fileList,srcDir,dstDir)

print("Done!")




