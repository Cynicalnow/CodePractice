import os,shutil
def MoveFiles2Directory():
    print("Please specify the directory in which the files exist you would like \
to move:")
    src=input()
    if os.path.exists(src):
        srcFiles = os.listdir(src)

        if (not srcFiles == []):
            string = src + "\\"
            srcFiles = [string + x for x in srcFiles]
            print(srcFiles)

            print("Please input the destination folder:")
            dst = input()

            try:
                for src in srcFiles:
                    shutil.move(src,dst)
            except:
                print("Destnation not found!")
        else:
            print("The specified folder is empty!")
    else:
        print("site:pan.baidu.com")
    print("\nDone!")

if __name__ == "__main__":
    MoveFiles2Directory()
