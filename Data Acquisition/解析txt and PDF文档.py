txt文档
	from urllib.request import urlopen

	html = urlopen("https://wikipedia.org/robots.txt")

	print(html.read().decode("utf-8")) 
PDF文档
下载pdfminer3k：https://pypi.python.org/pypi/pdfminer3k/
找到存取路径，终端切换到该路径，并输入python setup.py install

初始化：
分析器PDFParser
文档对象PDFDocument
初始化 initialize()
读取：
资源管理器PDFResourceManager
      |
聚合器PDFPageAggregator         -->   解释器 PDFPageInterpreter
	  |
参数分析器LAParams