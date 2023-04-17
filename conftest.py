import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser_setup(get_browser_flag):
        driver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            desired_capabilities={'browserName': get_browser_flag}
        )
        yield driver
        driver.quit()
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")

@pytest.fixture(scope="session")
def get_browser_flag(request):
    browser = request.config.getoption("browser")
    return browser


