# -*- coding: utf-8 -*-
import scrapy


class ZingSpider(scrapy.Spider):
    name = 'zing'

    #First Start URL
    def start_request(self):
	urls = [
		"https://mp3.zing.vn/the-loai-nghe-si/US-UK/IWZ9Z08O.html",
		#"https://mp3.zing.vn/the-loai-nghe-si/Viet-Nam/IWZ9Z08I.html",
		#"https://mp3.zing.vn/the-loai-nghe-si/Kpop/IWZ9Z08W.html",
		#"https://mp3.zing.vn/the-loai-nghe-si/Nhat-Ban/IWZ9Z08Z.html",
		#"https://mp3.zing.vn/the-loai-nghe-si/Hoa-Ngu/IWZ9Z08U.html",
		#"https://mp3.zing.vn/the-loai-nghe-si/Hoa-Tau/IWZ9Z086.html"
    ]

    	npages = 15

    	for url in urls:
    		for i in range(1, npages+2):
	    		yield scrapy.Request(url=url+"?&page="+str(i), callback=self.parse)

    def parse(self, response):
        for item_link in response.css('div.row div.description a.txt-primary::attr(href)').extract():
	    yield scrapy.Request("https://mp3.zing.vn"+item_link, callback=self.parse_single_item)

    def parse_single_item(self, response):
	filename = response.url.split("/")[-1] 
        with open(filename, 'wb') as f:
            f.write(response.body)
	
