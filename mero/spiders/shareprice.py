import scrapy
import json
import sys
from flaskapi import*
from pydispatch import dispatcher
from scrapy import signals
from scrapy.exceptions import CloseSpider





data=[]

i=0



from scrapy.crawler import CrawlerProcess
class shareprice (scrapy.Spider):
    def __init__(self):
        dispatcher.connect(self.spider_closed, signals.spider_closed)
    
    name='shareprice'
    allowed_domains=['merolagani.com']
    start_urls=['https://merolagani.com/latestmarket.aspx']
    
    def parse(self,response):
        title=response.xpath("//*[@id='live-trading']/div/h4/span/text()").get()
        print(title)
        
        pricesrow=response.xpath("//table[@class='table table-hover live-trading sortable']//tr")
        
        for pricerow in pricesrow:
            
            symbol=pricerow.xpath('.//td[1]/a/text()').get()
            ltp=pricerow.xpath('.//td[2]/text()').get()
            ltv=pricerow.xpath('.//td[3]/text()').get()
            Change=pricerow.xpath('.//td[4]/text()').get()
            high=pricerow.xpath('.//td[5]/text()').get()
            low=pricerow.xpath('.//td[6]/text()').get()
            open=pricerow.xpath('.//td[7]/text()').get()
            qty=pricerow.xpath('.//td[8]/text()').get()
            link=response.urljoin(pricerow.xpath('./td[1]/a/@href').get())
            # data.append({
            #     'symbol':symbol,
            #     'ltp':ltp,
            #     'ltv':ltv,
            #     'change':Change,
            #     'high':high,
            #     'low':low,
            #     'open':open,
            #     'qty':qty
            # })


            
    
      

            
            yield response.follow(url=link,callback=self.parse_detail)
    def parse_detail(self,response):
        global i
        
        i=i+1
        
        print(i)
    
        company_name=response.xpath('.//*[@id="ctl00_ContentPlaceHolder1_CompanyDetail1_companyName"]/text()').get()
        sector=str(response.xpath(".//*[@id='accordion']/tbody[1]/tr/td/text()").get()).strip()
        last_traded=str(response.xpath('.//*[@id="accordion"]/tbody[5]/tr/td/text()').get()).strip()
        week_lh=str(response.xpath('.//*[@id="accordion"]/tbody[6]/tr/td/text()').get()).strip()
        onetwenty_day_average=str(response.xpath('.//*[@id="accordion"]/tbody[8]/tr/td/text()').get()).strip()
        one_year_yield=str(response.xpath('.//*[@id="ctl00_ContentPlaceHolder1_CompanyDetail1_lblYearYeild"]/text()').get()).strip()
        eps=str(response.xpath('.//*[@id="accordion"]/tbody[10]/tr/td/text()').get()) .strip()
        eps_year=str(response.xpath('.//*[@id="accordion"]/tbody[10]/tr/td/span/text()').get()).strip()
        pe_ratio=str(response.xpath('.//*[@id="accordion"]/tbody[11]/tr/td/text()').get()).strip()
        book_value=str(response.xpath('.//*[@id="accordion"]/tbody[12]/tr/td/text()').get()).strip()
        pbv_ratio=str(response.xpath('.//*[@id="accordion"]/tbody[13]/tr/td/text()').get()).strip()
        dividend=str(response.xpath('.//*[@id="accordion"]/tbody[14]/tr[1]/td/text()').get()).strip() 
        dividend_year=str(response.xpath('.//*[@id="accordion"]/tbody[14]/tr[1]/td/span/text()').get()).strip()
        bonus_percentage=str(response.xpath('.//*[@id="accordion"]/tbody[15]/tr[1]/td/text()').get()).strip()
        bonus_year=str(response.xpath('.//*[@id="accordion"]/tbody[15]/tr[1]/td/span/text()').get()).strip()
        right_share=str(response.xpath('.//*[@id="accordion"]/tbody[16]/tr[1]/td/text()').get()).strip()
        right_share_year=str(response.xpath('.//*[@id="accordion"]/tbody[16]/tr[1]/td/span/text()').get()).strip()
        market_capital=str(response.xpath('.//*[@id="accordion"]/tbody[18]/tr/td/text()').get()).strip()
        



        yield{    
            'sector':sector,
            'company_name':company_name,
            'last_traded':last_traded,
            'week_lh':week_lh,
            'onetwenty_day_average':onetwenty_day_average,
            'one_year_yield':one_year_yield,
            'eps':eps,
            'eps_year':eps_year,
            'pe_ratio':pe_ratio,
            'book_value':book_value,
            'pbv_ratio':pbv_ratio,
            'dividend':dividend,
            'dividend_year':dividend_year,
            'bonus_percentage':bonus_percentage,
            'bonus_year':bonus_year,
            'right_share':right_share,
            'right_share_year':right_share_year,
            'market_capital':market_capital,

            
            
        }
        global data
        

        
        data.append({    
            'sector':sector,
            'company_name':company_name,
            'last_traded':last_traded,
            'week_lh':week_lh,
            'onetwenty_day_average':onetwenty_day_average,
            'one_year_yield':one_year_yield,
            'eps':eps,
            'eps_year':eps_year,
            'pe_ratio':pe_ratio,
            'book_value':book_value,
            'pbv_ratio':pbv_ratio,
            'dividend':dividend,
            'dividend_year':dividend_year,
            'bonus_percentage':bonus_percentage,
            'bonus_year':bonus_year,
            'right_share':right_share,
            'right_share_year':right_share_year,
            'market_capital':market_capital,
            
            
        })
    def spider_closed(self, spider):
        data.pop(1)
        a_file = open("data.json", "w")
        json.dump(data, a_file)
        a_file.close()
            
        
        
        

        


       



           
    
     
        
            

            
      
     
    
     

     
if __name__ == '__main__':
    settings = dict()
    settings['USER_AGENT'] = 'my agent'
    settings['DOWNLOAD_DELAY'] = 0.5
    settings['FEED_URI'] = 'sharedetailall.json'
    settings['CONCURRENT_REQUESTS'] = 100
process = CrawlerProcess(settings=settings)
process.crawl(shareprice)
process.start()
#spider for scrapy