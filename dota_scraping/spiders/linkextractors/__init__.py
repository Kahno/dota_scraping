# -*- coding: utf-8 -*-
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor


class CSSLinkExtractor(LxmlLinkExtractor):
    """
    Custom Link extractor that automatically uses CSS selectors
    """

    def __init__(self, selector, *args, **kwargs):
        kwargs['restrict_css'] = selector
        super(CSSLinkExtractor, self).__init__(*args, **kwargs)
