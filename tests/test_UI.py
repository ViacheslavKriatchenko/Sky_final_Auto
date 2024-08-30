from pages.main_page import MainPage
from time import sleep


def test_1(driver):
    main = MainPage(driver)

    main.open()
    # main.is_opened()
    sleep(5)
    main.click_login_button()
