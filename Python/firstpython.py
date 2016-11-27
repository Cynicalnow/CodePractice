import os
tempdir=os.listdir("C:\\")
i=len(tempdir)
for item in tempdir:
	print(item)
print("There are "+str(i)+" items in current directory!")
