import urllib.parse
import urllib.request
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import time
import codecs
import os

url = 'http://www.hao123.com/'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
values = {'tn': '99621802_hao_pg'}
headers = {'User-Agent': user_agent}
data = urllib.parse.urlencode(values)
data = data.encode('ascii')
req = urllib.request.Request(url, data, headers)
try:
    response=urlopen(req)
    the_page = response.read().decode('utf-8')
except HTTPError as e:
    print('The server couldn\'t fulfill the request.')
    print('Error code: ', e.code)
except URLError as e:
    print('We failed to reach a server.')
    print(e.reason)
else:
    current_time=time.strftime("%Y%b%d%H%M%S",time.localtime())
    tempdir="C:/Users/509064/Desktop/Temp/"
    prefix="Temp"
    suffix=".html"

    with codecs.open(os.path.join(tempdir,prefix+"-"+current_time+suffix),"w",encoding='utf-8') as file1:
        file1.write(the_page)
