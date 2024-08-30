from pages.main_page import MainPage


def test_1():
    main = MainPage()

    main.open()
    main.is_opened()
    main.click_login_button()
