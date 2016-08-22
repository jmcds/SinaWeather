# -*- coding:utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from ..items import SinaweatherItem

__author__ = 'patrick_psq'

class SinaWeatherSpider(scrapy.Spider):
    name = 'SinaWeather'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://weather.sina.com.cn/']

    def parse(self, response):
        # Parsed by xpath
        # item = SinaweatherItem()
        # item['city'] = response.xpath('//*[@id="slider_ct_name"]/text()').extract()
        # tenDays = response.xpath('//*[@id="blk_fc_c0_scroll"]')
        # item['date'] = tenDays.css('p.wt_fc_c0_i_date::text').extract()
        # item['description'] = tenDays.css('img.icons0_wt::attr(title)').extract()
        # item['temperature'] = tenDays.css('p.wt_fc_c0_i_temp::text').extract()

        # Parsed by BeautifulSoup
        html_doc = response.body
        soup = BeautifulSoup(html_doc)
        itemTemp = {}
        itemTemp['city'] = soup.find(id='slider_ct_name')
        tenDays = soup.find(id='blk_fc_c0_scroll')
        itemTemp['date'] = tenDays.findAll('p', {'class': 'wt_fc_c0_i_date'})
        itemTemp['description'] = tenDays.findAll('img', {'class': 'icons0_wt'})
        itemTemp['temperature'] = tenDays.findAll('p', {'class': 'wt_fc_c0_i_temp'})
        item = SinaweatherItem()

        for att in itemTemp:
            item[att] = []
            if att == 'city':
                item[att] = itemTemp.get(att).text
                continue
            for obj in itemTemp.get(att):
                if att == 'description':
                    item[att].append(obj['title'])
                else:
                    item[att].append(obj.text)

        return item
