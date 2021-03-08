# -*- coding: utf-8 -*-
import scrapy


import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://www.mercadolivre.com.br']

    def parse(self, response):
        for title in response.css('.sinonimo'):
            yield {'title': title.css('::text').get()}  
