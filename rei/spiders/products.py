# start with 'scrapy crawls products'
import scrapy
from scrapy.spiders import CrawlSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from ..items import ReiItem
from scrapy.loader import ItemLoader


class ProductsSpider(CrawlSpider):
    name = 'products'
    allowed_domains = ['rei.com'] # replace with destination domain
    start_urls = ['https://www.rei.com/c/camping-and-hiking'] # replace with page of product listing

    rules = (
        Rule(LinkExtractor(allow=(r"page=",))),
        Rule(LinkExtractor(allow=(r"product",)), callback="parse_item"),
    )

    def parse_item(self, response):
        l = ItemLoader(item=ReiItem(), response=response)
        l.add_css("title","h1#product-page-title") #css id name, under inspect elements do not need the text
        l.add_css("price","span#buy-box-product-price")
        l.add_css("item_no","span#product-item-number")
        l.add_css("rating","span.cdr-rating__number_13-5-3") #css class name, under inspect elements

        return l.load_item()

