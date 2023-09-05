import scrapy


class InvestingSpider(scrapy.Spider):
    name = "investing"
    allowed_domains = ["investing.com"]
    start_urls = ["https://investing.com"]

    def parse(self, response):
        pass
