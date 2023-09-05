import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.exporters import CsvItemExporter

class InvestingSpider(scrapy.Spider):
    name = "investing"
    start_urls = ["https://br.investing.com/news/commodities-news"]

    def parse(self, response):
        for article in response.css("#leftColumn .textDiv"):
            news = article.css(".title ::attr(href)").get()  
            if news is not None:
                yield response.follow(url=news, callback=self.collect)
        
        next_pag = response.xpath('//*[@id="paginationWrap"]/div[3]/a').attrib['href']
        if next_pag != '/news/commodities-news/5':
            yield response.follow(url=next_pag, callback=self.parse)
                

    def collect(self, response):
        res = response.css(".articlePage p::text").getall()
    
        if res is not None:
            article = ' '.join(res)
            article = article.replace("Posição adicionada com êxito a:  \n ", "")
            yield {"text": f"{article[0:1385]}"}
        else:
            yield {"text": "Not relevant news"}
            
        home = "https://br.investing.com/news/commodities-news"
        yield response.follow(url=home, callback=self.parse)
            


if __name__ == "__main__":
    path = "myenv\investing\investing\spiders\data\dados.csv"
    
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        'FEED_FORMAT': 'csv',  # CSV output format
        'FEED_URI': path,  # CSV output name file
    })

    # Configure the exporter to use CSV format
    exporter = CsvItemExporter(open(path, 'wb'))
    exporter.start_exporting()

    process.crawl(InvestingSpider)
    process.start()

    # Stop the exporter after the scraping
    exporter.finish_exporting()