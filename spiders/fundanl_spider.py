import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from tutorial.items import FundaWebsite
from scrapy.selector import HtmlXPathSelector
import ipdb


class DmozSpider(CrawlSpider):  
    name = "funda"
    
    allowed_domains = ["funda.nl"]
    start_urls = ["http://www.funda.nl/huur/amsterdam/+2km/0-2000/"]
    
    rules = [Rule(LinkExtractor(allow=('(funda.nl).*(appartement).*')),follow=True,callback='parse_apt')]
    
    #.*(/kenmerken/) ## complete features

    def parse_apt(self, response):
        
        hxs = HtmlXPathSelector(response) 
        item = FundaWebsite()

        ipdb.set_trace()
        item['price'] = hxs.select(".//dd[@class='price']//text()").extract()
        item['space'] = hxs.select("//tr[@id='twwo13']//td//span[@class='specs-val']").extract()
        #item['interior'] = hxs.select(".//dl[@class='details-product']/dd[4]//text()").extract()
        #item['bedrooms'] = hxs.select(".//dl[@class='details-product']/dd[5]//text()").extract()
        #item['price_inc'] = hxs.select(".//ul[@class='attribList']/li[8]//text()").extract()
        #item['zip_code'] = hxs.select(".//div[@class='description']/address//text()").extract()
        #item['neighborhood'] = hxs.select("//li//div[@class='trail']//span[1]").extract()

        #specific/fur  "//tr[@id='twby12']//td//span[@class='specs-val']"

        return item


##precio>> hula12



        

    #apartment-for-rent        
    #family-house-for-rent
    # SOLO INGLES!!!
        #deny OTRAS COMBINACIONES, CASA IN AFFITO, NO SOLO APT
    # data cleansing
        #replace or unfurnished"

    # NO DUPLICAR VALORES
    # navegacion completa, iterar paginas 1-30 (paginado)
    
    