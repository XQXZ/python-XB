# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from scrapy.http import Request
from scrapy.selector import Selector
from doubanmoive.items import DoubanmoiveItem

class MoivespiderSpider(Spider):
    name = 'MoiveSpider'
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        
        selector = Selector(response)
        movies = selector.xpath('//div[@class="info"]')
        for moive in movies:
            item = DoubanmoiveItem()
            title = moive.xpath('div[@class="hd"]/a/span/text()').extract()
            complete_title = ''
            for each in title:
                complete_title += each
            minfo = movie.xpath('div[@class="bd"]/p/text()').extract()
            star = moive.xpath('div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]
            quote = moive.xpath('div[@class="bd"]/p/span/text()').extract()[0]
            if not quote:
                quote = ''
            item['title'] = complete_title;
            item['info'] = ' '.join(minfo).replace(' ', '').replace('\n', '')
            item['star'] = star[0]
            item['quote'] = quote[0]
            yield item
        nextPage = response.xpath('//span[@class="next"]/link/@href').extract()
        if nextPage:
            nextPage = nextPage[0]  
            yield Request(self.url + str(nextPage), callback=self.parse)
        
        
            
                