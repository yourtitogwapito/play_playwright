# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 11:33:52 2023

@author: P102MNPH1
"""

from playwright.sync_api import Playwright, sync_playwright, expect
from pom.shop_women_elements import ShopWomen

def test_shop_women(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True, slow_mo=(3000))
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1/")
    page.get_by_role("link", name="Shop Women").click()
    shop_women = ShopWomen(page)
    # ---------------------
    page.is_visible(shop_women.shoes)

