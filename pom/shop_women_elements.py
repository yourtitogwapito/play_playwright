# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 14:25:45 2023

@author: P102MNPH1
"""

class ShopWomen:
    def __init__(self, page):
        self.celebrating_beauty_header = page.locator("text=Celebrating Beauty and Style")
        self.celebrating_beauty_body = page.locator("text=playwright-practice")
        self.profile_arrow = page.locator('._1hHt1')
        self.cart_icon = page.locator('.bQgup')
        self.my_orders = page.locator('text = page.locator(My Orders')