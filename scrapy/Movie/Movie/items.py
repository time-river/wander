# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class MovieInformation(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = Field()
    year = Field()
    movie = Field()
    director = Field()
    writer = Field()
    actor = Field()
    type = Field()
    official_site = Field()
    area = Field()
    language = Field()
    release_data = Field()
    season = Field()
    episodes = Field()
    single_runtime = Field()
    runtime = Field()
    alias = Field()
    imdb = Field()
    synopsis = Field()
    awards = Field()
    
class MovieComment(Item):
    _from = Field()
    id = Field()
    author = Field()
    rating = Field()
    time = Field()
    content = Field()
    vote = Field()

class MovieReview(Item):
    _from = Field()
    id = Field()
    author = Field()
    rating = Field()
    time = Field()
    title = Field()
    content = Field()
    useful = Field()
    useless = Field()
    comments =Field()

class MovieReviewComments(Item):
    _from = Field()
    comments = Field()    
        
class MovieReviewComment(Item):
    id = Field()
    author = Field()
    time = Field()
    quote_author = Field()
    content = Field()
