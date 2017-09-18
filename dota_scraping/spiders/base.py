# -*- coding: utf-8 -*-
from pyquery import PyQuery

from scrapy.contrib.spiders import CrawlSpider

from dota_scraping.items import DotaScrapingItem


class BaseSpider(CrawlSpider):

    def parse_item(self, response):
        self.pq = PyQuery(response.body)
        item = DotaScrapingItem()

        item['match_id'] = self.parse_match_id(response)
        item['player_kda'] = self.parse_player_kda(response)
        item['result'] = self.parse_result(response)

        return item
