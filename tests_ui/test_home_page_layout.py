# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 13:42:06 2023

@author: P102MNPH1
"""

from playwright.sync_api import Playwright, sync_playwright, expect
from ..home_page_elements import HomePage
from ..shop_women_elements import ShopWomen

def about_us_section_verbiage(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    home_page = HomePage(page)
    shop_women = ShopWomen(page)
    
    
    assert expect(home_page.celebrate_header).to_be_visible()
    assert expect(home_page.celebrate_body).to_be_visible()
    
    assert expect(shop_women.celebrate_header).to_be_visible()
    assert expect(shop_women.celebrating_beauty_body).to_be_visible()
    
    
    
with sync_playwright() as playwright:
    about_us_section_verbiage(playwright)