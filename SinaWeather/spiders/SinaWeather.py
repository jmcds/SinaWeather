# -*- coding:utf-8 -*-
import scrapy
from ..items import SinaweatherItem

__author__ = 'patrick_psq'

class SinaWeatherSpider(scrapy.Spider):
    name = 'SinaWeather'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://weather.sina.com.cn/']

    def parse(self, response):
        item = SinaweatherItem()
        item['city'] = response.xpath('//*[@id="slider_ct_name"]/text()').extract()
        tenDays = response.xpath('//*[@id="blk_fc_c0_scroll"]')
        item['date'] = tenDays.css('p.wt_fc_c0_i_date::text').extract()
        item['description'] = tenDays.css('img.icons0_wt::attr(title)').extract()
        item['temperature'] = tenDays.css('p.wt_fc_c0_i_temp::text').extract()
        return item
