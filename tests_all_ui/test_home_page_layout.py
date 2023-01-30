# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 13:42:06 2023

@author: P102MNPH1
"""

from playwright.sync_api import Playwright, sync_playwright, expect
from pom.home_page_elements import HomePage
import pytest

@pytest.mark.homepagebody
def test_about_us_section_verbiage(ConfTest):
    # browser = playwright.chromium.launch(headless=True,slow_mo=(3000))
    # context = browser.new_context()
    # page = context.new_page()
    # page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page = ConfTest
    home_page = HomePage(page)
    
    
    assert page.is_visible(home_page.celebrate_body)
# with sync_playwright() as playwright:
#     about_us_section_verbiage(playwright)
