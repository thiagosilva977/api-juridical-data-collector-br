import time

import scrapy
from bs4 import BeautifulSoup
import requests
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose
from project_scraper.items import ProjectScraperItem


class MySpiderSpider(scrapy.Spider):
    name = "my_spider"
    start_urls = ['http://pstrial-2019-12-16.toscrape.com/browse/insunsh']

    def start_requests(self):
        for item_url in self.start_urls:
            response = requests.get(item_url)

            soup = BeautifulSoup(response.text, parser='html.parser')
            print(soup)

            subcats_a_list = soup.find('div', {'id': 'subcats'}).find_next('div').find_all_next('a')
            for item in subcats_a_list:
                full_url = str(f"http://pstrial-2019-12-16.toscrape.com{item['href']}")
                yield scrapy.Request(full_url, callback=self.parse)

    def parse(self, response, **kwargs):

        loader = ItemLoader(item=ProjectScraperItem(), response=response)
        loader.default_input_processor = MapCompose(str.strip)
        loader.default_output_processor = TakeFirst()

        loader.add_css('title', 'h2.artist::text')
        loader.add_css('description', '.description > p:nth-child(1)')
        loader.add_value('url', 'sometexxt')

        yield loader.load_item()
