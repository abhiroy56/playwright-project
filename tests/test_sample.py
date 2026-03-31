"""
Test Sample Module
"""
from playwright.sync_api import Page

class Test_Demo:

    def test_demo(self, page: Page):
        page.go