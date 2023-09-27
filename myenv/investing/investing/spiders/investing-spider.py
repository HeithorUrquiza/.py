import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.exporters import CsvItemExporter
from utils.analyzer import Analyzer
from utils.translator import Translator

class InvestingSpider(scrapy.Spider):
    name = "investing"
    start_urls = ["https://br.investing.com/news/commodities-news"]

    def parse(self, response):
        #for article in response.css("#leftColumn .textDiv"):
            #news = article.css(".title ::attr(href)").get()  
            #if news is not None:
            yield response.follow(url="https://br.investing.com/news/economy/emenda-incluida-em-projeto-na-camara-pode-aumentar-preco-de-combustiveis-diz-associacao-1153343", callback=self.collect)
        
    """     next_pag = response.xpath('//*[@id="paginationWrap"]/div[3]/a').attrib['href']
        if next_pag != '/news/commodities-news/5':
            yield response.follow(url=next_pag, callback=self.parse) """
                

    def collect(self, response):
        res = response.css(".articlePage p::text").getall()
    
        if res is not None:
            article = ' '.join(res)
            article = article.replace("Posição adicionada com êxito a:  \n ", "")
            yield {"text": f"{article}"}
        


if __name__ == "__main__":
    path = "myenv/utils/data/dados.csv"
    trans_path = "myenv/utils/data/translateData.csv"
    analy_path = "myenv/utils/data/analysisData.csv"
    
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
    
    translator = Translator(trans_path)
    translator.translate(path=path)
    
    analyzer = Analyzer(analy_path)
    analyzer.analyze(trans_path)
    
    
    # Pesquisar a respeito da analise do sentimento do Orange.