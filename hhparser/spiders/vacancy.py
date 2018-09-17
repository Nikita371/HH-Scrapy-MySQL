# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from hhparser.items import HhparserItem 

class VacancySpider(CrawlSpider):
    name = 'vacancy'
    allowed_domains = ['hh.ru']
    start_urls = ['https://ekaterinburg.hh.ru/search/vacancy?enable_snippets=true&clusters=true&page=0',
                 'https://ekaterinburg.hh.ru/search/vacancy?enable_snippets=true&clusters=true&page=1',
                 'https://ekaterinburg.hh.ru/search/vacancy?enable_snippets=true&clusters=true&page=2',
                 'https://ekaterinburg.hh.ru/search/vacancy?enable_snippets=true&clusters=true&page=3',
                 'https://ekaterinburg.hh.ru/search/vacancy?enable_snippets=true&clusters=true&page=4',
                 'https://ekaterinburg.hh.ru/search/vacancy?enable_snippets=true&clusters=true&page=5'
                 'https://ekaterinburg.hh.ru/search/vacancy?enable_snippets=true&clusters=true&page=6']
    rules = (
              Rule(LinkExtractor(allow=('page=2',)), callback='parse'),
             )
    


    def parse(self, response):
            item = HhparserItem()
            posts = response.xpath('//div[@class="vacancy-serp-item__row"]')   
            for post in posts:
                item['NameVacancy'] = post.xpath('.//div[@class="vacancy-serp-item__info"]/div[@class="search-item-name"]/a[@class="bloko-link HH-LinkModifier"]/text()').extract()
                item['Employer'] = post.xpath('.//div[@class="vacancy-serp-item__info"]/div[@class="vacancy-serp-item__meta-info"]/a[@class="bloko-link bloko-link_secondary"]/text()').extract()
                item['Salary'] = post.xpath('.//div[@class="vacancy-serp-item__sidebar"]//div[@class="vacancy-serp-item__compensation"]/text()').extract()
                yield item
   
        
        