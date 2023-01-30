# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 14:25:45 2023

@author: P102MNPH1
"""

class ShopWomen:
    def __init__(self, page):
        self.shoes = page.get_by_role("link", name = "Shoes Shoes") #shoes is already a page object
        self.backpack = page.get_by_role("link", name = "Backpack Backpack")
        # self.profile_arrow = page.locator('._1hHt1')
        # self.cart_icon = page.locator('.bQgup')
        # self.my_orders = page.locator('text = page.locator(My Orders')