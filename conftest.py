from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.firefox.service import Service as FireService
from selenium.webdriver.chrome.options import Options as ChromeOptions
# from selenium.webdriver.firefox.options import Options as FireOptions
import pytest


@pytest.fixture(scope="session", autouse=True)
def driver():
    options = ChromeOptions()
    # options.add_argument('--headless')
    options.add_argument('--window-size=1920,1080')
    options.add_argument("--disable-blink-features=AutomationContlolled")
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0")
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(options=options, service=service)
    yield driver
    driver.quit()


# def pytest_addoption(parser):
#     parser.addoption(
#         "--browser",
#         action="store",
#         default="chrome",
#         help="Choose browser: chrome or firefox"
#     )


# @pytest.fixture(scope='session', autouse=True)
# def driver(request):
#     DRIVER_NAME = request.config.getoption("--browser")
#     if DRIVER_NAME == 'Chrome':
#         options = ChromeOptions()
#         # options.add_argument('--headless')
#         options.add_argument('--windowsize=1920,1080')
#         service = ChromeService(executable_path=ChromeDriverManager.install())
#         driver = webdriver.Chrome(options=options, service=service)
#     else:
#         options = FireOptions()
#         # options.add_argument('--headless')
#         options.add_argument('--windowsize=1920,1080')
#         service = FireService(executable_path=GeckoDriverManager.install())
#         driver = webdriver.Firefox(options=options, service=service)
#     yield driver
#     driver.quit()
