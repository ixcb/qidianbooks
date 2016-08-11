# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from qidian.items import QidianItem

class QidianSpiderSpider(CrawlSpider):
    name = 'qidian_spider'
    allowed_domains = ['qidian.com']
    start_urls = ['http://r.qidian.com/']

    rules = (
        Rule(LinkExtractor(allow=r'/[^/]+style=1$')),
        Rule(LinkExtractor(allow=r'/Book/\d+\.aspx$'), callback='parse_item', follow=False)
    )

    def parse_item(self, response):
        item = QidianItem()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        item['title'] = response.xpath('//*[@id="divBookInfo"]/div[1]/h1/text()').extract()[0].strip()
        item['name'] = response.xpath('//*[@id="divBookInfo"]/div[1]/span/a/span/text()').extract()[0].strip()
        item['week_click'] = response.xpath('//*[@id="contentdiv"]/div/div[1]/table/tr/td[2]/text()').extract()[1].strip()
        return item
