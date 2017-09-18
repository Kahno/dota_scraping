# -*- coding: utf-8 -*-
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor


class CSSLinkExtractor(LxmlLinkExtractor):

    def __init__(self, selector, *args, **kwargs):
        kwargs['restrict_css'] = selector
        super(CSSLinkExtractor, self).__init__(*args, **kwargs)
