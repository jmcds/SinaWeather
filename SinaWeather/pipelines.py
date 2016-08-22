# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SinaweatherPipeline(object):
    def __init__(self):
        pass

    def process_item(self, item, spider):
        with open('weather.txt', 'w+') as file:
            city = item['city'][0].encode('utf-8')
            file.write('city:{0}\n\n'.format(str(city)))

            date = item['date']

            description = item['description']
            dayDescription = description[1::2]
            nightDescription = description[0::2]

            temperature = item['temperature']

            weatherItem = zip(date, dayDescription, nightDescription, temperature)
            # item[0]: date, item[1]: dayDescription,
            # item[2]: nightDescription, item[3]: temperature

            for i in xrange(len(weatherItem)):
                item = weatherItem[i]
                ta = item[3].split('/')
                text = 'date:{0}\t\t day:{1}({2})\t\tnight:{3}({4})\n\n'.format(
                    item[0],
                    item[1].encode('utf-8'),
                    ta[0].encode('utf-8'),
                    item[2].encode('utf-8'),
                    ta[1].encode('utf-8')
                )
                file.write(text)

        return item
