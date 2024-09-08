from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FireService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FireOptions
import pytest
import allure
from userdata.DataProvider import DataProvider
from config.ConfigProvider import ConfigProvider


@pytest.fixture()
@allure.title('Подготовка к тесту, выбор браузера')
def driver():
    DRIVER_NAME = ConfigProvider().get(section='common', prop='BROWSER')
    if DRIVER_NAME == 'Chrome':
        options = ChromeOptions()
        # options.add_argument('--headless')
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument(
            "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0"
        )
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(options=options, service=service)
    elif DRIVER_NAME == 'Firefox':
        options = FireOptions()
        # options.add_argument('--headless')
        options.add_argument('--windowsize=1920,1080')
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument(
            "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0"
        )
        service = FireService(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(options=options, service=service)
    yield driver
    driver.quit()


@pytest.fixture()
@allure.title('Подготовка к тесту, запрос токена')
def get_token():
    TOKEN = DataProvider().getAPI('TOKEN')
    return TOKEN


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
