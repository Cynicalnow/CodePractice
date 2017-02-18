##This script is used to unpack files in subfolders into designated folder!

import os

WorkDir=(input("Please specify the working directory/Folder:\n")).strip()
SubFolderList=os.listdir(WorkDir)

SubDirList=[]
SubItemsReplaceTo=WorkDir

for item in SubFolderList:
   if (os.path.isdir(os.path.join(WorkDir,item))):
      item=os.path.join(WorkDir,item)
      SubDirList.append(item)

for item in SubDirList:
   subItemList=os.listdir(item)
   for item2 in subItemList:
      os.rename(os.path.join(item,item2),os.path.join(WorkDir,item2))
      
print("Done!")

exitInfo=input("Press any key to exit!")

if exitInfo:
   exit()
