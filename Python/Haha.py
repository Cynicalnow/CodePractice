print("What's your name?")
name_=input()
print("What's your age?")
age_= int(input())
if age_ <= 18:
    print("Hello, teenager!%s")
else:
    print("Hello, %s!"%name_)
