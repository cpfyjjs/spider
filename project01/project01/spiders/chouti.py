# -*- coding: utf-8 -*-
import scrapy


class ChoutiSpider(scrapy.Spider):
    name = 'chouti'
    allowed_domains = ['chouti.com']
    start_urls = ['http://chouti.com/']

    def parse(self, response):
        from scrapy.http.response.html import HtmlResponse

        print(response.text)
        response.xpath('//')
        response.css()




