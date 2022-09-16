import time
from .pages.login_page import LoginPage

link = "https://dev-tenant.liis.su/"


def test_login_page_is_present(browser):
    browser.get(link)
    page = LoginPage(browser, link)
    page.open()
    page.should_be_elements_on_login_page()


def test_success_login(browser):
    browser.get(link)
    page = LoginPage(browser, link)
    page.open()
    page.user_can_login()
    time.sleep(15)
