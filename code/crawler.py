#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
import requests
import sys
from bs4 import BeautifulSoup

res=requests.get("https://tw.bid.yahoo.com/tw/%E5%A5%B3%E5%8C%85%E7%B2%BE%E5%93%81%E8%88%87%E5%A5%B3%E9%9E%8B-2092101501-category.html")
#print(res.text.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding))           #用預設編碼(big5)編碼再解碼
                                                                                            #byte解碼變成string

#u.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding)
#u.replace("\t",'').replace('\n','').replace(' ','').replace('?','')
                                                                                                                                                                                        
#u=u.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding)
#u=u.replace("\t",'').replace('\n','').replace(' ','').replace('?','')

soup=BeautifulSoup(res.text)
print("---------------------------------------------")
u=soup.select("a")
print(u)                               #更改過debugI/O use "utf-8"
                                                                                            
                                                                                            

                                                                                            

