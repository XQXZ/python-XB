#coding:utf-8

from pdfminer.pdfdevice import PDFDevice
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.layout import LAParams 
from pdfminer.converter import PDFPageAggregator
#从网页上读取PDF
#from urllib.request import urlopen
#获取文档对象
fp = open("naacl06-shinyama.pdf", "rb")#以二进制读模式打开
#fp = urlopen("url") 
#创建一个与文档关联的解释器
parser = PDFParser(fp)

#创建PDF文档对象
doc = PDFDocument()

#链接解释器和文档对象
parser.set_document(doc)
doc.set_parser(parser)

#初始化文档
doc.initialize("")

#创建PDF资源管理器
resource = PDFResourceManager()

#参数分析器
laparam = LAParams()

#PDF聚合器
device = PDFPageAggregator(resource, laparams = laparam)

#创建PDF页面解释器
interpreter = PDFPageInterpreter(resource, device)

#使用文档对象得到页面的集合
for page in doc.get_pages():
    #使用页面解释器读取
    interpreter.process_page(page)
    
    #使用聚合器来获得内容
    layout = device.get_result()
    
    for out in layout:
        if hasattr(out, "get_text"):
            print(out.get_text())




