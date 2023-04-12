import scrapy


class TjceSpider(scrapy.Spider):
    name = "tjce"
    allowed_domains = ["google.com"]
    start_urls = ["http://google.com/"]

    def parse(self, response):
        pass
