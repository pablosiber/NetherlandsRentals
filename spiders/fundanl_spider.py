import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from tutorial.items import FundaWebsite
from scrapy.selector import HtmlXPathSelector
import ipdb


class DmozSpider(CrawlSpider):  
    name = "funda"
    name
    allowed_domains = ["funda.nl"]
    start_urls = ["http://www.funda.nl/huur/amsterdam/"]
    
    rules = [Rule(LinkExtractor(allow_domains=allowed_domains,
                                allow=('(funda.nl/huur/amsterdam).*(appartement).*'),
                                deny=('.*(print)')),
                                follow=True,callback='parse_apt')]
    
    #.*(/kenmerken/) ## complete features

    def parse_apt(self, response):
        
        hxs = HtmlXPathSelector(response) 
        item = FundaWebsite()

        
        #if response.url.find("kenmerken") == -1:
                # not useful URL
                #return item     

        #ipdb.set_trace()        
        dirtyPrice = hxs.select("//tr[@id='hula12']//td//span[@class='specs-val']//span[@class='price-wrapper']").extract()
        if not dirtyPrice:
            return
        
        item['price'] = dirtyPrice[0].replace("\n","").replace("\t","")
        
        #ipdb.set_trace()         
        
        dirtySpace = hxs.select("//tr[@id='twwo13']//td//span[@class='specs-val']").extract()
        item['space'] = dirtySpace[0].replace("\n","").replace("\t","")

        #ipdb.set_trace()    
        dirtyLocation = hxs.select("//span[@itemprop='title']").extract()
        if not dirtyLocation:
            return
        item['location'] = dirtyLocation[len(dirtyLocation)-1]

        dirtyFurnished = hxs.select("//tr[@id='twby12']//td//span[@class='specs-val']").extract()
        if not dirtyFurnished:
            return
        item['furnished'] = dirtyFurnished[0].replace("\n","").replace("\t","")


        #ipdb.set_trace()      

        return item






        

    #apartment-for-rent        
    #family-house-for-rent
    # SOLO INGLES!!!
        #deny OTRAS COMBINACIONES, CASA IN AFFITO, NO SOLO APT
    # data cleansing
        #replace or unfurnished"

    # NO DUPLICAR VALORES
    # navegacion completa, iterar paginas 1-30 (paginado)
    
    