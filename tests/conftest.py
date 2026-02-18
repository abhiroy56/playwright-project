"""
Test Demo Module
"""
import os
import pytest
from playwright.sync_api import sync_playwright, Playwright



@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Pytest hook to capture screenshots on test failure.

    :param item: The test item being executed.
    :yield: The outcome of the test execution.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        pagepw = item.funcargs.get("page")
        if pagepw:
            os.makedirs("..//screenshotsfolder/screenshots/", exist_ok=True)
            path = f"..//screenshotsfolder/screenshots/{item.name}.png"
            pagepw.screenshot(path=path)


def pytest_addoption(parser):
    """
    Adds custom command-line options for pytest.

    :param parser: The pytest parser object.
    """
    parser.addoption("--env", action="store", default="qa",
                     help="Set the test environment (default: qa).")
    parser.addoption("--headless", action="store_true", default=False,
                     help="Run browser in headless mode (default: False).")


@pytest.fixture(scope="session")
def playwright():
    """
    Provides a Playwright instance for the test session.
    :yield: The Playwright instance.
    """
    playwright_pw = sync_playwright().start()
    yield playwright_pw
    playwright_pw.stop()

@pytest.fixture(scope="session")
def browser_type(playwright: Playwright, browser_name):
    """
    Provides the browser type (e.g., chromium, firefox, webkit).

    :param playwright: The Playwright instance.
    :param browser_name: The name of the browser to use.
    :return: The browser type object.
    """
    return getattr(playwright, browser_name)


@pytest.fixture(scope="session")
def browser(browser_type, request):
    """
    Provides a browser instance for the test session.

    :param browser_type: The browser type object.
    :param request: The pytest request object.
    :yield: The browser instance.
    """
    headless = request.config.getoption("--headless")
    browser_pw = browser_type.launch(headless=headless, args=["--start-maximized"])
    print("Starting browser...")
    yield browser_pw
    browser_pw.close()


@pytest.fixture(scope="function")
def browser_context(browser):
    """
    Provides a browser context for each test function.

    :param browser: The browser instance.
    :yield: The browser context.
    """
    context = browser.new_context(no_viewport=True)
    yield context
    context.close()


@pytest.fixture(scope="function")
def page(browser_context):
    """
    Provides a new page for each test function.
    :param browser_context: The browser context.
    :yield: The page instance.
    """
    pw_page = browser_context.new_page()
    yield pw_page
    pw_page.close()
