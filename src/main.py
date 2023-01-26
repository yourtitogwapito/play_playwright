# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 10:55:05 2023

@author: P102MNPH1
"""

from playwright.sync_api import Playwright, sync_playwright, expect
from tests_ui.test_home_page_layout import test_about_us_section_verbiage

with sync_playwright() as playwright:
    test_about_us_section_verbiage(playwright)
