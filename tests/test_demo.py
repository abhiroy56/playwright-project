"""
Test Demo Module
"""
from playwright.sync_api import Page


class TestDemo:
    """
    Test Demo Class
    """

    def test_pass(self, page: Page):
        """
        test method to with PASS
        :return:
        """
        page.goto("https://www.letcode.in/")
        assert True

    def test_fail(self, page: Page):
        """
        test method to with Fail
        :return:
        """
        page.goto("https://www.letcode.in/")
        assert False
    def test_fail2(self, page: Page):
        """
        test method to with Fail
        :return:
        """
        page.goto("https://www.letcode.in/")
        assert False
