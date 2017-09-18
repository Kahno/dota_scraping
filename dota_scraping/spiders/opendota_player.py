# -*- coding: utf-8 -*-
import json

from dota_scraping.spiders.base import BaseSpider

from scrapy import Request

PLAYER_ID = 95636068


class OpendotaSpider(BaseSpider):
    """
    Simple spider for obtaining basic info about an individual player from Opendota.com
    """

    name = 'opendota_player'
    allowed_domains = ['opendota.com']

    start_urls = ['https://api.opendota.com/api/players/{}/matches'.format(PLAYER_ID)]

    def parse(self, response):
        json_matches = json.loads(response.body)
        match_url = 'https://api.opendota.com/api/matches/{}?'

        for match in json_matches:
            yield Request(match_url.format(match['match_id']), meta={'player_data': match},
                          callback=self.parse_item)

    def parse_item(self, response):
        response.meta['match_data'] = json.loads(response.body)
        return super(OpendotaSpider, self).parse_item(response)

    def parse_match_id(self, response):
        return response.meta['match_data']['match_id']

    def parse_player_kda(self, response):
        """
        Returns the player's KDA statistic as a list of three integers (kills, deaths, assists)
        """
        return [response.meta['player_data']['kills'],
                response.meta['player_data']['deaths'],
                response.meta['player_data']['assists']]

    def parse_result(self, response):
        """
        Returns True if player was victorious
        """
        for player in response.meta['match_data']['players']:
            if player['account_id'] == PLAYER_ID:
                return player['player_slot'] < 5 == response.meta['match_data']['radiant_win']
