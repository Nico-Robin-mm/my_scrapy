# -*- coding: utf-8 -*-
import scrapy

from scrapy_imagetest.items import BookItem


class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        books = response.css("li.col-xs-6")
        for book in books:
            item = BookItem()
            title = book.css("h3 a::attr(title)").get()
            image_urls = book.css("div a img::attr(src)").get()
            item["title"] = title
            item["image_urls"] = response.urljoin(image_urls)
            yield item
