# -*- coding: utf-8 -*-
import scrapy
from .DataBase import firebase


class AppleSpider(scrapy.Spider):
    name = 'apple'
    start_urls = ['https://jobs.apple.com/en-us/search?search=new%20college%20graduate%20software%20engineering&sort=newest&team=machine-learning-and-ai-SFTWR-MCHLN+security-and-privacy-SFTWR-SEC+software-quality-automation-and-tools-SFTWR-SQAT+wireless-software-SFTWR-WSFT+apps-and-frameworks-SFTWR-AF+cloud-and-infrastructure-SFTWR-CLD+core-operating-systems-SFTWR-COS+devops-and-site-reliability-SFTWR-DSR+engineering-project-management-SFTWR-EPM+information-systems-and-technology-SFTWR-ISTECH+internships-STDNT-INTRN']

    def parse(self, response):
        links = response.css('a.table--advanced-search__title::attr(href)').extract()
        title = response.css('.table--advanced-search__title::text').extract()
        location = response.css('.table-col-2 span::text').extract()
        thisdb = firebase()
        thisdb.sendMessage("apple", "https://jobs.apple.com", links, title, location)

