#coding:UTF-8
from urllib.request import urlopen

html = urlopen("https://wikipedia.org/robots.txt")

print(html.read().decode("utf-8")) 