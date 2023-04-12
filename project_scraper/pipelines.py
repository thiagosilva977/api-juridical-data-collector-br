# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import time

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ProjectScraperPipeline:
    def process_item(self, item, spider):

        print(item)
        time.sleep(2112)
        return item
