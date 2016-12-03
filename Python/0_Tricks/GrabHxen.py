from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

import re
import os
import urllib.request

def split_by_n(string, n ):
    """A generator to divide a sequence into chunks of n units."""
    while seq:
        yield string[:n]
        string = string[n:]

#------retrieve content
url=input("Please provide the url you want to grab:\n")
data = urllib.request.urlopen(url).read()
data = data.decode("gb2312").replace("&quot;",'"')
m = re.search('<p>', data)
n=re.search("</p><",data)
start = m.end()
end = n.start()-1
urlContent = data[start:end].replace("<p>","")
urlContentList=urlContent.split('</p>')

for item in urlContentList:
    print(item)

###------retrieve title
##m2=re.search('<title>', data)
##n2=re.search("</title>",data)
##tStart=m2.end()
##tEnd=n2.start()
##urlTitle=data[tStart:tEnd].replace("|","").replace(":","")
##
##
##dstDir="C:/Users/509064/Desktop/Temp"
##
##c=canvas.Canvas(filename=os.path.join(dstDir,urlTitle+".pdf"))
##
###------text start position (bottom left is x=0,y=0)
##x=50
##y=800
##
##
##    
##c.save()
