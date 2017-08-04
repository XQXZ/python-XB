1. Beautiful Soup的简介
   Beautiful Soup是python的一个库，最主要的功能是从网页抓取数据。
   中文文档：https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/

2. 创建 Beautiful Soup 对象
   (1) 导入 bs4 库
       from bs4 import BeautifulSoup
   (2) 请求URL并把结果用UTF-8编码
       resp = urlopen("URL").read().decode("utf-8")
   (3) 使用BeautifulSoup解析
       soup =  BeautifulSoup(resp, "html.parser")
3. 搜索
   soup.find_all(re.compile("正则表达式"))
   获取文字内容可用string 或 get_text:string 仅获取一个， get_text可获取标签下的所有文字内容
   具体用法参考中文文档