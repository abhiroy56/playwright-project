"""
Test Demo Module
"""
from playwright.sync_api import Page


class TestDemo:
    """
    Test Demo Class
    """

    def test_pass(self, page: Page, get_url):
        """
        test method to with PASS
        :return:
        """
        page.goto(get_url)
        print(page.title())
        assert True

    def test_fail(self, page: Page, get_url):
        """
        test method to with Fail
        :return:
        """
        page.goto(get_url)
        print(page.title())
        assert True

    def test_fail2(self, page: Page, get_url):
        """
        test method to with Fail
        :return:
        """
        page.goto(get_url)
        print(page.title())
        assert False
