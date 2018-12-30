# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import time
import re
from dygang.items import MovieItem

class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['dygang.net']
    start_urls = ['http://dygang.net/ys/']

    def parse(self, response):
        #/ html / body / table[6] / tbody / tr / td[1] / table
        # /html/body/table[6]/tbody/tr/td[1]/table/tbody/tr/td/table[2]/tbody/tr[1]/td[1]/table

        # /html/body/table[6]/tbody/tr/td[1]/table/tbody/tr/td/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[1]/table[1]/tbody/tr/td/a
        href_list =response.xpath("//table[@class='border1']//a/@href").extract()
        for href in href_list:
            yield Request(url=href,
                        callback=self.parse_detail,)

        for i in range(2,583):
            print('---------->',i)
            time.sleep(1)
            url = 'http://www.dygang.net/ys/index_{}.htm'.format(i)
            yield Request(url=url,callback=self.get_html)

    def get_html(self,response):
        href_list = response.xpath("//table[@class='border1']//a/@href").extract()
        for href in href_list:
            yield Request(url=href,
                          callback=self.parse_detail, )

    def parse_detail(self,response):
        img = response.xpath("//td[@id='dede_content']/p[1]/img/@src").extract()[0]
        # content = response.xpath("//td[@id='dede_content']/p[2]").extract()
        contents = response.xpath("//td[@id='dede_content']/p[2]").extract()
        for content in contents:
            text = content.encode('utf-8').decode('utf-8')
            # print("------------>",text)
            # try:
            name = re.search(r'片　　名　(.*?)<br>',text).group(1)
            age = re.search(r'年　　代　(.*?)<br>',text).group(1)
            location = re.search(r'产　　地　(.*?)<br>',text).group(1)
            director = re.search(r'导　　演　(.*?)<br>',text).group(1)
            yield MovieItem(name=name,age=age,location=location,director=director)
            # except:
            #     print('cccc')



