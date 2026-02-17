import pytest
import os
from playwright.sync_api import sync_playwright, Playwright


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            os.makedirs("..//screenshotsfolder/screenshots/", exist_ok=True)
            path = f"..//screenshotsfolder/screenshots/{item.name}.png"
            page.screenshot(path=path)


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="qa")
    parser.addoption("--headless", action="store_true", default=True)

@pytest.fixture(scope="session")
def playwright():
    playwright = sync_playwright().start()
    yield playwright
    playwright.stop()

@pytest.fixture(scope="session")
def browser_type(playwright: Playwright, browser_name):
    return getattr(playwright, browser_name)

@pytest.fixture(scope="session")
def browser(browser_type, request):
    headless = request.config.getoption("--headless")
    browser = browser_type.launch(headless=headless, args=["--start-maximized"])
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def browser_context(browser):
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture(scope="function")
def page(browser_context):
    page = browser_context.new_page()
    yield page
    page.close()

