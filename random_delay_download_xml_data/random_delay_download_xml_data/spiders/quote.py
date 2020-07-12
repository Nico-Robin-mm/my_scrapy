# -*- coding: utf-8 -*-
import scrapy
import json

from random_delay_download_xml_data.items import QuoteItem


class QuoteSpider(scrapy.Spider):
    name = 'quote'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/api/quotes?page=1']

    custom_settings = {
        "RANDOM_DELAY": 5,
        'DEFAULT_REQUEST_HEADERS': {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
        },
        'DOWNLOADER_MIDDLEWARES': {
           'random_delay_download_xml_data.middlewares.RandomDelayMiddleware': 543,
        },
        'ITEM_PIPELINES': {
           'random_delay_download_xml_data.pipelines.RandomDelayDownloadXmlDataPipeline': 300,
        }
    }

    page = 1

    def parse(self, response):
        data = json.loads(response.text)
        for quote in data['quotes']:
            item = QuoteItem()
            for field in item.fields:
                if field in quote.keys():
                    item[field] = quote.get(field)
            yield item

        if data['has_next']:
            self.page += 1
            next_url = 'http://quotes.toscrape.com/api/quotes?page={page}'.format(page=self.page)
            yield scrapy.Request(url=next_url, callback=self.parse)

