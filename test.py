# -*- coding: gbk -*-
import json
import urllib2
from city import city

cityname=raw_input('which city do you wanna search?\n')
citycode=city.get(cityname)
if citycode:
    try:
        url='http://www.weather.com.cn/data/cityinfo/%s.html'%citycode
        content=urllib2.urlopen(url).read()
        data=json.loads(content)
        result=data['weatherinfo']
        str_temp=('%s\n%s~%s')%(
                result['weather'],
                result['temp1'],
                result['temp2']
        )
        print str_temp
    except:
        print 'failed search'
else:
    print 'cannot find the city'

