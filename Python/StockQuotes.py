import re
import urllib.request

url = "http://www.nasdaq.com/symbol/"
stock = input("Enter your stock: ")
furl = url + stock.lower()
fp= urllib.request.urlopen(furl)
data=fp.read()
data= data.decode("utf-8")
fp.close()
m = re.search('qwidget-dollar', data)
start = m.start()
end = start + 30
newString = data[start:end]
#print(newString)
m=re.search("</div>",newString)
n=re.search(">",newString)
start=n.start()+1
end=m.start()
final = newString[start:end]
print("The stock price of " + stock.upper() + " is " + final)
