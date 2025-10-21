# -*- coding: utf-8 -*-

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def check_item(self, item):
        return item.sell_in < 0

    def is_sulfuras(self, item):
        return item.name == "Sulfuras, Hand of Ragnaros"

    def increase_quality(self, item):
        if item.quality < 50:
            item.quality = min(50, item.quality + 1)

    def decrease_quality(self, item):
        if item.quality > 0:
            item.quality = max(0, item.quality - 1)

    def is_item(self, item):
        return self.is_brie(item) or self.is_backstage(item)

    def is_backstage(self, item): 
        return item.name == "Backstage passes to a TAFKAL80ETC concert"

    def is_brie(self, item):
        return item.name == "Aged Brie"

    def update_quality(self):
        for item in self.items:
            if not self.is_item(item):
                if item.quality > 0:
                    if not self.is_sulfuras(item):
                        self.decrease_quality(item)
            else:
                self.increase_quality(item)
                if self.is_backstage(item):
                    if item.sell_in < 11:
                        self.increase_quality(item)
                    if item.sell_in < 6:
                        self.increase_quality(item)

            if not self.is_sulfuras(item):
                item.sell_in -= 1

            if self.check_item(item):
                if not self.is_brie(item):
                    if not self.is_backstage(item):
                        if item.quality > 0:
                            if not self.is_sulfuras(item):
                                self.decrease_quality(item)
                    else:
                        item.quality = item.quality - item.quality
                else:
                    self.increase_quality(item)

