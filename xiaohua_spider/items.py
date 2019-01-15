# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XiaohuaSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    folder_name = scrapy.Field()   # 吉林大学珠海学院校花余文丽
    img_name = scrapy.Field()   # 20190110AdOgzcLVqR.jpg
    img_url = scrapy.Field()  # https://www.dxsabc.com/api/20190110AdOgzcLVqR.jpg
