# -*- coding: utf-8 -*-
import scrapy


class AmazonpiderSpider(scrapy.Spider):
    name = "amazonspider"
    allowed_domains = ["amazon.com"]
#    links = ["https://www.amazon.com/Amazon-Echo-Bluetooth-Speaker-with-WiFi-Alexa/product-reviews/B00X4WHP5E/ref=cm_cr_arp_d_viewpnt_lft?ie=UTF8&reviewerType=avp_only_reviews&showViewpoints=1&sortBy=helpful&filterByStar=positive&pageNumber={}".format(i) for i in range (1,4)]
    links = ["https://www.amazon.com/Amazon-Echo-Bluetooth-Speaker-with-WiFi-Alexa/product-reviews/B00X4WHP5E/ref=cm_cr_arp_d_viewpnt_lft?ie=UTF8&reviewerType=avp_only_reviews&showViewpoints=1&sortBy=helpful&filterByStar=positive&pageNumber={}".format(i) for i in range (1,2744)]
    start_urls = links

    def parse(self, response):
    	review_author = response.xpath('//a[contains(@data-hook,"review-author")]/text()').extract()
    	review_title = response.xpath('//a[contains(@data-hook,"review-title")]/text()').extract()
    	review_date = response.xpath('//span[contains(@data-hook,"review-date")]/text()').extract()
    	helpful_vote = response.xpath('//span[contains(@data-hook,"helpful-vote-statement")]/text()').extract()
    	star_rating = response.xpath('//i[contains(@data-hook,"review-star-rating")]/span[contains(@class,"a-icon-alt")]/text()').extract()

    	yield {
    		'review_author': review_author,
    		'review_title': review_title,
    		'review_date': review_date,
    		'helpful_vote': helpful_vote,
    		'star_rating': star_rating
    	}