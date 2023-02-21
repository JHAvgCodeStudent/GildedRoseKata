# -*- coding: utf-8 -*-



class GildedRose(object):

    def __init__(self, items):
        self.items = items
        self.item_types = {
            "Aged Brie":Aged_Brie,
            "Backstage passes to a TAFKAL80ETC concert":Backstage_Pass,
            "Sulfuras, Hand of Ragnaros":Base_Item,
            "Conjured":Conjured_Item
        }

    def update_quality(self):
        for item in self.items:
            item_class = self.item_types.get(item.name, Generic_Item)
            item_class(item).update()
            

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class Base_Item:
    def __init__(self, item):
        self.item = item
    
    def update(self):
        return

class Aged_Brie(Base_Item):
    def update(self):
        self.item.quality += 1
        self.item.sell_in -= 1

        if(self.item.sell_in < 0):
            self.item.quality += 1

        if(self.item.quality > 50):
            self.item.quality = 50

class Backstage_Pass(Base_Item):
    def update(self):
        self.item.sell_in -= 1
        self.item.quality += 1

        if(self.item.sell_in < 10):
            self.item.quality += 1
        
        if(self.item.sell_in < 5):
            self.item.quality += 1
        
        if(self.item.sell_in < 0):
            self.item.quality = 0
        return

class Generic_Item(Base_Item):
    def update(self):
        self.item.sell_in -= 1
        self.item.quality -= 1

        if(self.item.sell_in < 0):
            self.item.quality -= 1

        if(self.item.quality < 0):
            self.item.quality = 0
        return

class Conjured_Item(Base_Item):
    def update(self):
        self.item.sell_in -= 1
        self.item.quality -= 2

        if(self.item.sell_in < 0):
            self.item.quality -= 2

        if(self.item.quality < 0):
            self.item.quality = 0
        return