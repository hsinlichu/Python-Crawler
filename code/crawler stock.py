#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
import requests
import re
from bs4 import BeautifulSoup
header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
rs=requests.Session()          #會話對象讓你能夠跨請求保持某些參數。它也會在同一個Session實例發出的所有請求之間保持cookie
res=rs.get("https://www.stockdog.com.tw/stockdog/index.php?m=overview&sid=1101+%E5%8F%B0%E6%B3%A5",headers=header)
url=re.findall('document\.getElementById\(\'g\d+\'\).innerHTML=\'<iframe src=\"(.*?)\"',res.text)         #正則表示式

for i in url:
    print(i)
    urlcomplete="https://www.stockdog.com.tw/stockdog/"+i
    newres=rs.get(urlcomplete,headers=header)
    print(newres.text)
    print("---------------------------------------------")


print("---------------------------------------------")
soup=BeautifulSoup(res.text)
print("---------------------------------------------")
#print(soup.text)


