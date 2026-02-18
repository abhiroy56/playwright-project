"""
Test Demo Module
"""
import logging
import os

import pytest
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
        print("Login with username", os.environ.get("test_username"))
        print("Login with password", os.environ.get("test_password"))
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

    @pytest.mark.prod_only
    def test_fail3(self, page: Page):
        """
        test method to with Fail
        :return:
        """
        page.goto("https://www.letcode.in/")
        assert True