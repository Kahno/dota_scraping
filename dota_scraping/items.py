# -*- coding: utf-8 -*-
from scrapy.item import Item, Field


class DotaScrapingItem(Item):
    match_id = Field()
    player_kda = Field()
    result = Field()
