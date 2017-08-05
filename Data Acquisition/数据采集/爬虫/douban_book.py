#coding:UTF-8
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pymysql.cursors
import time    #设置延时时间，防止爬取过于频繁被封IP号
import random 
from douban_tag import *
import requests

def douban_main(url):
    #请求URL并把结果用UTF-8编码
    resp =  requests.get(url)
    #使用BeautifulSoup解析
    soup =  BeautifulSoup(resp.text.encode("utf-8"), "html.parser")
    #获取书名
    titles = soup.select("#subject_list > ul > li > div.info > h2 > a")
    #出版信息
    details = soup.select("#subject_list > ul > li > div.info > div.pub")
    #评分信息
    scores = soup.select("#subject_list > ul > li > div.info > div.star.clearfix > span.rating_nums") 
    #评价人数  
    persons = soup.select("#subject_list > ul > li > div.info > div.star.clearfix > span.pl") 
    #提取标签信息 
    tag=url.split("?")[0].split("/")[-1]   
    #便利获取的信息，并组成一条
    for title, detail, score, person in zip(titles, details, scores, persons):
        #正则分解detail中每一项
        
        l = []
        try:  
            author=detail.get_text().split("/")[0] 
            yizhe= detail.get_text().split("/")[1]            
            publish=detail.get_text().split("/")[2]           
            date=detail.get_text().split("/")[-2]
            price=detail.get_text().split("/")[-1]
            score=score.get_text() if True else ""     
            person=person.get_text()
            title=title.get_text().split()[0] 
            if(len(detail.get_text().split("/"))<=4):
                publish=detail.get_text().split("/")[1]      
        except IndexError:      
            try:               
                author=detail.get_text().split("/")[0]               
                yizhe=""          
                publish=detail.get_text().split("/")[1]                
                date=detail.get_text().split("/")[-2]                
                price=detail.get_text().split("/")[-1]              
                score=score.get_text() if True else ""                
                person=person.get_text()               
                title=title.get_text().split()[0]       
            except (IndexError,TypeError):          
                continue   

        except TypeError:      
            continue
        #信息存入列表
        if "-" not in publish:
            l.append([title,author,publish, date, score, person,price, tag])
        #信息存入数据库
        sql = "INSERT INTO books values(%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.executemany(sql, l)
        conn.commit()
        
#连接数据库
conn = pymysql.connect(
                            host = 'localhost',
                            user = 'root',
                            passwd = '123456',
                            db = 'douban_books',
                            charset = 'utf8mb4')
cursor = conn.cursor()
#如果数据库中有books的数据库则删除
cursor.execute('DROP TABLE IF EXISTS books')  
#创建book表 
sql = """CREATE TABLE books(      
        title CHAR(255) NOT NULL,         
        author CHAR(255), 
        publish CHAR(255), 
        date CHAR(255),
        score CHAR(255), 
        person CHAR(255),          
        price CHAR(255),          
        tag CHAR(255)       
 )"""
#执行sql语句
cursor.execute(sql)
#设置时钟
start = time.clock() 
for url1 in urls.split():
    #提取url信息，并组装成每一页的链接
    url2=[url1+"?start={}&type=T".format(str(i)) for i in range(20,980,20)]   
    for url in url2:
        douban_main(url)       #执行主函数，开始爬取
        print(url)        #输出要爬取的链接
        #设置一个随机数时间，每爬一个网页可以随机的停一段时间，防止IP被封
        time.sleep(int(format(random.randint(0,9))))   
end = time.clock()
#爬取结束，输出爬取时间
print('Time Usage:', end - start)    
#输出爬取的总数目条数
count = cursor.execute('select * from books')
print('has %s record' % count)       

# 释放数据连接
if cursor:   
    cursor.close()
if conn:   
    conn.close()   

