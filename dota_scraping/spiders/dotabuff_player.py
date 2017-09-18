# -*- coding: utf-8 -*-
import re

from scrapy.contrib.spiders import Rule

from dota_scraping.spiders.linkextractors import CSSLinkExtractor
from dota_scraping.spiders.base import BaseSpider

PLAYER_ID = 95636068


class DotabuffPlayerSpider(BaseSpider):
    """
    Simple spider for obtaining basic info about an individual player from Dotabuff.com
    """

    name = 'dotabuff_player'
    allowed_domains = ['dotabuff.com']

    start_urls = ['https://www.dotabuff.com/players/{}/matches'.format(PLAYER_ID)]

    download_delay = 0.5

    rules = [
        Rule(CSSLinkExtractor('.won'), callback='parse_item'),
        Rule(CSSLinkExtractor('.lost'), callback='parse_item'),

        # Pagination
        Rule(CSSLinkExtractor('.next'))
    ]

    def parse_match_id(self, response):
        return re.search('Match (\d+)', self.pq('.header-content-title').text()).group(1)

    def parse_player_kda(self, response):
        """
        Returns the player's KDA statistic as a list of three integers (kills, deaths, assists)
        """
        return [self.pq('.player-{} .tf-r'.format(PLAYER_ID)).eq(0).text(),
                self.pq('.player-{} .tf-r'.format(PLAYER_ID)).eq(1).text(),
                self.pq('.player-{} .tf-r'.format(PLAYER_ID)).eq(2).text()]

    def parse_result(self, response):
        """
        Returns True if player was victorious
        """
        player_text = self.pq('.player-{}'.format(PLAYER_ID)).attr('class').lower()
        victor_text = self.pq('.match-result').text().lower()

        return any((side in player_text and side in victor_text) for side in ['radiant', 'dire'])
