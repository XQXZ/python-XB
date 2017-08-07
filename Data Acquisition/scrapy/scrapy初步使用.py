#coding:utf-8
import scrapy
from pip._vendor.requests.packages.urllib3 import response

class FincrisisSpider(scrapy.Spider):
    name = "fincrisis"
    start_urls = ["https://www.zaobao.com/special/report/politic/fincrisis"]
    
    #解析并产生下一步需要处理的URL
    def parse(self, response):
        for href in response.css('#l_title .l_title a::attr(href)'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_news)
    
    #抓取最终内容
    def parse_news(self, response):
        yield{
            'title':response.css('#a_title h1::text').extract(default = 'not found')[0],
            'dt':response.css('#a_credit .time::text').extract(default = 'not found')[0],
            'body':response.css('#article_content').extract()[0],
            'link':response.url
        }
        
            