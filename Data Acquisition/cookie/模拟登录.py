#coding:utf-8
import urllib
import urllib.request
import urllib.parse
import http.cookiejar
import re


from pip._vendor.requests.api import request

class SDUT:
    def __init__(self, id):
        self.loginUrl = 'http://xkzx.sdut.edu.cn/cjcx/zcjcx_list.php'
        self.cookies = http.cookiejar.CookieJar()
        self.postdata = urllib.parse.urlencode({
            'post_xuehao':id
        }).encode(encoding='UTF8')
        self.opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.cookies))
        #学分
        self.credit = []
        #成绩
        self.grades = []
        
    def getPage(self):
        request = urllib.request.Request(
            url = self.loginUrl,
            data = self.postdata    
        )
        result = self.opener.open(request)
        #打印
        return result.read().decode('utf-8')
    
    def getGrades(self):
        page = self.getPage()
        myItems = re.findall('<tr>.*?<td.*?<td.*?<td.*?<td.*?<td.*?<td.*?<td.*?<td.*?>(.*?)</td>.*?<td.*?<td.*?<td.*?>(.*?)</td>.*?</tr>', page, re.S)
        index = 0
        for item in myItems:   
            index+=1;
            if index>=3 and item[1].replace('&nbsp;','').isdigit():
                self.credit.append(item[0].replace('&nbsp;','').encode('gbk'))
                self.grades.append(item[1].replace('&nbsp;','').encode('gbk'))
        self.getGrade()
    
    def getGrade(self):
        sum = 0.0
        weight = 0.0
        for i in range(len(self.credit)):
            if(self.grades[i].isdigit()):
                sum += float(self.credit[i])*float(self.grades[i])  #string.atof转化为float
                weight += float(self.credit[i])
        print(u"该学生绩点为：", sum/weight)

id = input("请输入您的学号:")
sdut = SDUT(id)
sdut.getGrades()
        
