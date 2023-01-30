# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 14:23:42 2023

@author: P102MNPH1
"""

"""
builds a page browser.
since all testing are from the same site, conftest is located at the main folder.

"""
from playwright.sync_api import Playwright, sync_playwright, expect
import pytest

@pytest.fixture
def ConfTest(page): #playwright: Playwright):
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)
    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    # page = context.new_page()
    # page.goto("https://symonstorozhenko.wixsite.com/website-1")
    # page.set_default_timeout(3000)
    yield page
    
    page.close()