# -*- coding: utf-8 -*-
import pytest
from gilded_rose import Item, GildedRose



def test_generic_item_sell_in():
    name = "foo"
    sell_in = 10
    quality = 5
    items = [Item(name, sell_in, quality)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == sell_in - 1
    assert items[0].quality == quality - 1

def test_generic_item_past_date():
    name = "foo"
    sell_in = -1
    quality = 5
    items = [Item(name, sell_in, quality)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == sell_in - 1
    assert items[0].quality == quality - 2

def test_generic_item_zero_quality():
    name = "foo"
    sell_in = -1
    quality = 0
    items = [Item(name, sell_in, quality)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == sell_in - 1
    assert items[0].quality == quality


def test_aged_brie_quality_increases():
    name = "Aged Brie"
    sell_in = 1
    quality = 5
    items = [Item(name, sell_in, quality)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == sell_in - 1
    assert items[0].quality == quality + 1

def test_aged_brie_50_quality():
    name = "Aged Brie"
    sell_in = 1
    quality = 50
    items = [Item(name, sell_in, quality)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == sell_in - 1
    assert items[0].quality == quality

def test_aged_brie_past_sell_in():
    name = "Aged Brie"
    sell_in = -1
    quality = 5
    items = [Item(name, sell_in, quality)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == sell_in - 1
    assert items[0].quality == quality + 2

def test_sulfuras_quality():
    name = "Sulfuras, Hand of Ragnaros"
    sell_in = 10
    quality = 80
    items = [Item(name, sell_in, quality)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == sell_in
    assert items[0].quality == quality

def test_sulfuras_past_sell_in():
    name = "Sulfuras, Hand of Ragnaros"
    sell_in = -1
    quality = 80
    items = [Item(name, sell_in, quality)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == sell_in
    assert items[0].quality == quality

def test_backstage_passes_far_out():
    name = "Backstage passes to a TAFKAL80ETC concert"
    sell_in = 11
    quality = 10
    items = [Item(name, sell_in, quality)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == sell_in - 1
    assert items[0].quality == quality + 1

def test_backstage_passes_inside_10_days():
    name = "Backstage passes to a TAFKAL80ETC concert"
    sell_in = 10
    quality = 10
    items = [Item(name, sell_in, quality)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == sell_in - 1
    assert items[0].quality == quality + 2

def test_backstage_passes_inside_5_days():
    name = "Backstage passes to a TAFKAL80ETC concert"
    sell_in = 5
    quality = 10
    items = [Item(name, sell_in, quality)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == sell_in - 1
    assert items[0].quality == quality + 3

def test_backstage_passes_past_concert():
    name = "Backstage passes to a TAFKAL80ETC concert"
    sell_in = -1
    quality = 50
    items = [Item(name, sell_in, quality)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == sell_in - 1
    assert items[0].quality == 0
