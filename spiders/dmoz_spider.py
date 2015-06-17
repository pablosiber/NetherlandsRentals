import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from tutorial.items import Website
from scrapy.selector import HtmlXPathSelector

class DmozSpider(CrawlSpider):
    name = "dmoz"
    
    allowed_domains = ["pararius.com"]
    start_urls = [
        "http://www.pararius.com/apartments/amsterdam",
        "http://www.pararius.com/apartments/haarlem"
    ]
    
    rules = [Rule(LinkExtractor(allow=('http://www.pararius.com/'),deny=('page')),follow=True,callback='parse_apt')]
    
    '''
    def parse(self, response):

        items = []
        for sel in response.xpath("//div[@id='searchResultContainer']/ul[@id='resultset']"):
            
            item = Website()
            item['title'] =  sel.xpath(".//div[@class='addressTitle']//text()").extract()
            item['link'] = sel.xpath(".//div[@class='addressTitle']//@href").extract()
            #desc = sel.xpath(".//p[@class='description']//text()").extract()
            items.append(item)
            #print title,link,desc
        return items
    '''     

    def parse_apt(self, response):
        
        hxs = HtmlXPathSelector(response) 
        item = Website()

        item['price'] = hxs.select(".//dd[@class='price']//text()").extract()
        item['space'] = hxs.select(".//dl[@class='details-product']/dd[3]//text()").extract()
        item['interior'] = hxs.select(".//dl[@class='details-product']/dd[4]//text()").extract()
        item['bedrooms'] = hxs.select(".//dl[@class='details-product']/dd[5]//text()").extract()
        item['price_inc'] = hxs.select(".//ul[@class='attribList']/li[8]//text()").extract()
        item['zip_code'] = hxs.select(".//div[@class='description']/address//text()").extract()

        return item
    
    # idioma siempre ingles
    # persistir a archivo
    # navegacion completa, iterar paginas 1-30 (paginado)
    
    