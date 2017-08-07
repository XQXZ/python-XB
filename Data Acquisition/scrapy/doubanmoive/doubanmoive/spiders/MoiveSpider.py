# -*- coding: utf-8 -*-
import scrapy
from doubanmoive.items import DoubanmoiveItem

class MoivespiderSpider(scrapy.Spider):
    name = 'MoiveSpider'
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        item = DoubanmoiveItem()
        for moive in response.xpath('//div[@class="info"]'):
            title = moive.xpath('div[@class="hd"]/a/span/text()').extract()
            complete_title = ''
            for each in title:
                complete_title += each
            info = movie.xpath('div[@class="bd"]/p/text()').extract()
            star = moive.xpath('div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]
            quote = moive.xpath('div[@class="bd"]/p/span/text()').extract()[0]
            if not quote:
                quote = ''
            item['title'] = complete_title;
            item['info'] = ' '.join(info).replace(' ', '').replace('\n', '')
            item['star'] = star[0]
            item['quote'] = quote[0]
            yield item
        nextPage = response.xpath('//span[@class="next"]/link/@href').extract()
        if nextPage:
            nextPage = nextPage[0]  
            yield scrapy.Request(self.url + str(nextPage), callback=self.parse)
            
                