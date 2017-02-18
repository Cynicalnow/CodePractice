import winreg

key=winreg.OpenKey(winreg.HKEY_CURRENT_USER,\
                   r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer")
##try:
##    i=0
##    while True:
##        name, value, type=winreg.EnumValue(key, i)
##        print(repr(name))
##        i+=1
##except OSError:
##    print("Error")
##
##    #(value,type=winreg.QueryValueEx(key, "EnableAutoTray"))

#newKey=winreg.CreateKey(key,"NoDrives")
winreg.SetValueEx(key,"NoDrives",0,winreg.REG_DWORD,8)
