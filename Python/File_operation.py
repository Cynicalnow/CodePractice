try:
    with open(r"File.txt","a") as f:
        f.write("Hello!\n")
        f.write("World!\n")
except:
    print("An Error Occurred!")
