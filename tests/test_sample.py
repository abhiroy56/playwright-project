"""
Test Sample Module
"""
from playwright.sync_api import Page

class TestDemo:
    """
    Demo class
    """

    def test_demo(self, page: Page):
        """
        sample test case
        """
        assert True