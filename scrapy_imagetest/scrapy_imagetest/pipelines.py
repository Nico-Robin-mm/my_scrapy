# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from urllib.parse import urlparse

import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
import os


class ScrapyImagetestPipeline(object):
    def process_item(self, item, spider):
        return item


class BookPipeline(ImagesPipeline):

    # default: return full/<request URL hash>.<extension>
    def file_path(self, request, response=None, info=None):
        return "book_images/" + os.path.basename(urlparse(request.url).path)

    def get_media_requests(self, item, info):
        # for image_url in item["image_urls"]:
        #     yield scrapy.Request(image_url)
        image_url = item["image_urls"]
        yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x["path"] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item["image_paths"] = image_paths
        return item
