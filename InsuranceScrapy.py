#!/usr/bin/env python
# coding: utf-8

# In[4]:


import scrapy
import urllib.parse as urlparse

class InsuranceSpider(scrapy.Spider):
    name = 'insurance_spider'

    #handle_httpstatus_list = [500, 502]

    start_urls = ['https://val.aakenya.co.ke/rptwithhdr/insurance.aspx?id=1']

    def parse(self, response):
        base_url='https://val.aakenya.co.ke/rptwithhdr/insurance.aspx?id='
        parsed = urlparse.urlparse(response.url)
        last_id = urlparse.parse_qs(parsed.query)['id']
        next_id = int(last_id[0])+1
        next_page = base_url+str(next_id)
        
        
        print(last_id)        
        
        if response.status == 500:
            if(next_id<558999):
                yield response.follow(next_page, self.parse)
        elif response.status == 502:
            if(next_id<558999):
                yield response.follow(next_page, self.parse)
        else:
            self.logger.info('A response from %s just arived!', response.url)
            SET_SELECTOR = '.protected'
            '''
                Yield a json dictionary and yield a response
            '''

            for brickset in response.css(SET_SELECTOR):
                item = {}
                META_SELECTOR = 'td ::text'
                SERIAL_SELECTOR = './/table/tr/td/table/tr[2]/td[2]/text()'
                OFFICE_SELECTOR = './/tr[td/text() = "ISSUING OFFICE: "]/td[2]/b/text()'
                RECEIPT_SELECTOR = './/tr[td/text() = "ISSUING OFFICE: "]/td[4]/b/text()'
                INSURED_SELECTOR = './/tr[td/text() = "INSURED: "]/td[2]/b/text()'
                POLICY_SELECTOR = './/tr[td/text() = "INSURED: "]/td[4]/b/text()'
                TEL_SELECTOR = './/tr[td/text() = "INSURED TEL: "]/td[2]/b/text()'
                EMAIL_SELECTOR = './/tr[td/text() = "INSURED TEL: "]/td[4]/b/text()'
                INSURER_SELECTOR = './/tr[td/text() = "INSURER: "]/td[2]/b/text()'
                AGENT_SELECTOR = './/tr[td/text() = "INSURER: "]/td[4]/b/text()'
                REG_SELECTOR = './/tr[td/text() = "Reg. No: "]/td[2]/b/text()'
                MAKE_SELECTOR = './/tr[td/text() = "Reg. No: "]/td[4]/b/text()'
                TYPE_SELECTOR = './/tr[td/text() = "Reg. No: "]/td[6]/b/text()'
                ODO_SELECTOR = './/tr[td/text() = "Odo. Reading: "]/td[2]/b/text()'
                COLOR_SELECTOR = './/tr[td/text() = "Odo. Reading: "]/td[4]/b/text()'
                YEAR_SELECTOR = './/tr[td/text() = "Odo. Reading: "]/td[6]/b/text()'
                FIRST_REG_SELECTOR = './/tr[td/text() = "Date of First Reg: "]/td[2]/b/text()'
                CHASSIS_SELECTOR = './/tr[td/text() = "Date of First Reg: "]/td[4]/b/text()'
                ENGINE_SELECTOR = './/tr[td/text() = "Date of First Reg: "]/td[6]/b/text()'
                BODY_SELECTOR = './/tr[td/text() = "Body Condition: "]/td/b/text()'
                GENERAL_SELECTOR = './/tr[td/text() = "General Condition: "]/td/b/text()'
                ELECTRICALS_SELECTOR = './/tr[td/text() = "Electricals: "]/td/b/text()'
                ENGINE_AREA_SELECTOR = './/tr[td/text() = "Engine Area: "]/td/b/text()'
                TRANSMISSION_SELECTOR = './/tr[td/text() = "Transmission System: "]/td/b/text()'
                STEERING_SELECTOR = './/tr[td/text() = "Steering System: "]/td/b/text()'
                SUSPENSION_SELECTOR = './/tr[td/text() = "Suspension System: "]/td/b/text()'
                TYRE1_SELECTOR = './/tr[td/text() = "Tyres Condition & Depth in mm:"]/td[2]/text()'
                TYRE2_SELECTOR = './/tr/td[b/text() = "FL : "]/text()'
                BRAKING_SELECTOR = './/tr[td/text() = "Braking System: "]/td/b/text()'
                EXTRAS_SELECTOR = './/tr[td/text() = "Extras: "]/td/b/text()'
                REMARKS_SELECTOR = './/tr[td/text() = "Remarks: "]/td/b/text()'
                WINDSCREEN_SELECTOR = './/tr[td/text() = "Windscreen: "]/td[2]/b/text()'
                ANTITHEFT_SELECTOR = './/tr[td/text() = "Windscreen: "]/td[4]/b/text()'
                PLAYER_SELECTOR = './/tr[td/text() = "Windscreen: "]/td[6]/b/text()'
                TOTAL_INSURABLES_SELECTOR = './/tr[td/text() = "Examiner\'s Opinion: Kshs"]/td[2]/b/text()'

                IMAGE_SELECTOR = 'img ::attr(src)'

                item['Serial'] = brickset.xpath(SERIAL_SELECTOR).extract_first()
                item['Issuing_Office'] = brickset.xpath(OFFICE_SELECTOR).extract()
                item['Receipt_Number'] = brickset.xpath(RECEIPT_SELECTOR).extract()
                item['Insured'] = brickset.xpath(INSURED_SELECTOR).extract()
                item['Policy_Number'] = brickset.xpath(POLICY_SELECTOR).extract()
                item['Insured_Tel'] = brickset.xpath(TEL_SELECTOR).extract()
                item['Email'] = brickset.xpath(EMAIL_SELECTOR).extract()
                item['Insurer'] = brickset.xpath(INSURER_SELECTOR).extract()
                item['Broker_Agent'] = brickset.xpath(AGENT_SELECTOR).extract()
                item['Reg_No'] = brickset.xpath(REG_SELECTOR).extract()
                item['Make'] = brickset.xpath(MAKE_SELECTOR).extract()
                item['Type_No'] = brickset.xpath(TYPE_SELECTOR).extract()
                item['Odo_Reading'] = brickset.xpath(ODO_SELECTOR).extract()
                item['Color'] = brickset.xpath(COLOR_SELECTOR).extract()
                item['Year_Manufacture'] = brickset.xpath(YEAR_SELECTOR).extract()
                item['First_Reg_Date'] = brickset.xpath(FIRST_REG_SELECTOR).extract()
                item['Chassis_No'] = brickset.xpath(CHASSIS_SELECTOR).extract()
                item['Engine_No'] = brickset.xpath(ENGINE_SELECTOR).extract()
                item['Body_Condition'] = brickset.xpath(BODY_SELECTOR).extract()
                item['General_Condition'] = brickset.xpath(GENERAL_SELECTOR).extract()
                item['Electricals'] = brickset.xpath(ELECTRICALS_SELECTOR).extract()
                item['Engine_Area'] = brickset.xpath(ENGINE_AREA_SELECTOR).extract()
                item['Transmission_System'] = brickset.xpath(TRANSMISSION_SELECTOR).extract()
                item['Steering_System'] = brickset.xpath(STEERING_SELECTOR).extract()
                item['Suspension_System'] = brickset.xpath(SUSPENSION_SELECTOR).extract()
                item['Tyre_condition(FR, RR, SPARE)'] = brickset.xpath(TYRE1_SELECTOR).extract()
                item['Tyre_condition(FL, RL, OTHERS)'] = brickset.xpath(TYRE2_SELECTOR).extract()
                item['Braking_System'] = brickset.xpath(BRAKING_SELECTOR).extract()
                item['Extras'] = brickset.xpath(EXTRAS_SELECTOR).extract()
                item['Remarks'] = brickset.xpath(REMARKS_SELECTOR).extract()
                item['Windscreen_Price_Est']  = brickset.xpath(WINDSCREEN_SELECTOR).extract()
                item['Anti_Theft_Price_Est'] = brickset.xpath(ANTITHEFT_SELECTOR).extract()
                item['Player_Price_Est'] = brickset.xpath(PLAYER_SELECTOR).extract()
                item['Total_Insurable'] = brickset.xpath(TOTAL_INSURABLES_SELECTOR).extract()
                item['images'] = brickset.css(IMAGE_SELECTOR).extract()
                yield item

            '''
                Yield the next request as long as the index of the url is not reached
            '''
            if(next_id<558999):
                yield response.follow(next_page, self.parse)

# run spider
process = CrawlerProcess()
process.crawl(InsuranceSpider)
process.start()
