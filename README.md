# SinaWeather

This is a scrapy project to crawl the data from http://weather.sina.com.cn/.

### Directory Structure

![icon](http://obw22u9v2.bkt.clouddn.com/figure1.png)

### File Contents

* *scrapy.cfg*: 项目的配置文件
* *SinaWeather/*: 该项目的python模块
* *SinaWeather/items.py*: 项目item文件
* *SinaWeather/pipelines.py*: 项目pipelines文件
* *SinaWeather/settings.py*: 项目的设置文件
* *SinaWeather/spiders/*: 放置spiders的目录

### Operating method

```
scrapy crawl SinaWeather
```

Then the crawl result will be shown in wea.txt.

### Reference

* [实验楼](https://www.shiyanlou.com/courses/142/labs/433/document)
* [Scrapy Documents](http://scrapy-chs.readthedocs.io/zh_CN/latest/topics/spiders.html)
