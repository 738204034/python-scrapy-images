# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from tiantangimg.items import TiantangimgItem


class TtimgSpider(scrapy.Spider):
    name = 'ttimg'
    allowed_domains = ['ivsky.com']
    start_urls = ['http://www.ivsky.com/tupian/ziranfengguang/']
    def parse(self, response):
        images_urls = response.xpath('/html/body/div[3]/div[2]/div[1]/ul/li/a/@href').extract()
        for images_url in images_urls:
            images_url = 'http://www.ivsky.com' + images_url
            if images_url != 'http://www.ivsky.com/tupian/':
                yield Request(images_url, callback=self.classification)

    def classification(self, response):
        images_urls = response.xpath('/html/body/div[3]/div[2]/ul/li/div/a/@href').extract()
        next_page = response.xpath('/html/body/div[3]/div[2]/div[5]/a[11]/@href').extract()
        next_page='http://www.ivsky.com' + next_page[0]
        for images_url in images_urls:
            images_url = 'http://www.ivsky.com' + images_url
            yield Request(images_url, callback=self.imagesList)
        if next_page:
            yield Request(next_page, callback=self.classification)

    def imagesList(self,response):
        images_lists=response.xpath('/html/body/div[3]/div[4]/ul/li/div/a/@href').extract()
        for images_url in images_lists:
            images_url = 'http://www.ivsky.com' + images_url
            yield Request(images_url, callback=self.imagesInfo)

    def imagesInfo(self,response):
        images_info_url = response.xpath('//*[@id="imgis"]/@src').extract()
        name=response.xpath('/html/body/div[3]/div[1]/a[4]/text()').extract()
        item =TiantangimgItem()
        item['images_name']=name[0]
        item['images_url']=images_info_url[0]
        return item

