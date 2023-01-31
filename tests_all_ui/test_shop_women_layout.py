# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 11:33:52 2023

@author: P102MNPH1
"""

from playwright.sync_api import Playwright, sync_playwright, expect
from pom.shop_women_elements import ShopWomen
import pytest, time

@pytest.mark.shopwomenpage
def test_shop_women(ConfTest) -> None:
    page = ConfTest
    shop_women = ShopWomen(page)
    time.sleep(3)
    page.get_by_role("link", name="Shop Women").click()
    assert shop_women.shoes.is_visible()
    
    
#@pytest.mark.xfail(reason="need timesleep")
@pytest.mark.shopwomenpage
def test_shop_wome2n(ConfTest) -> None:
    page = ConfTest
    shop_women = ShopWomen(page)
    page.get_by_role("link", name="Shop Women").click()
    time.sleep(3)
    assert shop_women.backpack.is_visible()
    
    
    
