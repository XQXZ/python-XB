#coding:utf-8
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

#请求URL并把结果用UTF-8编码
resp = urlopen("https://en.wikipedia.org/wiki/Main_Page").read().decode("utf-8")
#使用BeautifulSoup解析
soup =  BeautifulSoup(resp, "html.parser")
#获取所有以/wiki/开头的a标签的href属性
listUrls = soup.findAll("a", href = re.compile("^/wiki/"))
#输出所有词条对应的名称和URL
for url in listUrls:
    #过滤图片
    if not re.search("\.(jpg|JPG)$",url["href"]):
        #输出名字及对应的链接
        print(url.get_text(),"<---->","https://en.wikipedia.org"+url["href"])
