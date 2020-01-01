import sys
sys.path.append("..")
import scrapy
from ..items import InternshipBotItem
from .DataBase import firebase


class QuoteSpider(scrapy.Spider):
    name = 'facebook'
    start_urls = [
        'https://www.facebook.com/careers/jobs?teams[0]=University%20Grad%20-%20Engineering%2C%20Tech%20%26%20Design&teams[1]=Internship%20-%20Engineering%2C%20Tech%20%26%20Design&page=1'
    ]
    i = 1
    numberOfPages = 7
    def parse(self, response):
        thisdb = firebase()
        items = InternshipBotItem()
        links = response.css('a._8sef::attr(href)').extract()
        title = response.css("._8sel::text").extract()
        location = response.css('._8sen span::text').extract()

        items['title'] = title
        items['link'] = links
        items['location'] = location
        thisdb.sendMessage("facebook", "https://www.facebook.com", links, title, location)

        if(self.i ==1):
            pages = response.css('._8se1::text').get()
            numbers = pages.split('of ')
            numberOfPages = int(numbers[1])
            self.numberOfPages = numberOfPages//25+1

        next_page = 'https://www.facebook.com/careers/jobs?teams[0]=University%20Grad%20-%20Engineering%2C%20Tech%20%26%20Design&teams[1]=Internship%20-%20Engineering%2C%20Tech%20%26%20Design&page='+str(self.i)
        if next_page is not None and self.i <= self.numberOfPages:
            yield response.follow(next_page, callback=self.parse)
            self.i += 1



