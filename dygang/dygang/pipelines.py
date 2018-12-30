# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from dygang.items import MovieItem
class DygangPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item,MovieItem):
            txt = json.dumps(dict(item))
            with open('./movie.txt','a',encoding='utf-8') as f:
                f.write(txt)
                f.write('\r\n')
        return item
