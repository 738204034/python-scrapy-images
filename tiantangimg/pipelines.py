# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import io
import urllib
import random
import string
class TiantangimgPipeline(object):
    def process_item(self, item, spider):
        ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
        file_path = os.path.join("D:\\IMAGES", item['images_name'])
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        file_path = file_path + '\%s%s.jpg' % (item['images_name'],ran_str)
        urllib.urlretrieve(item['images_url'], file_path)
        print file_path
        return item
