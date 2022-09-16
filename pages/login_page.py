from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .users import Users


class LoginPage(BasePage):
    def should_be_elements_on_login_page(self):
        #WebDriverWait(self.browser, 15).until(EC.visibility_of_element_located(*LoginPageLocators.LOGIN_FORM))
        self.should_be_login_form()
        self.should_be_password_form()
        self.should_be_en_language_button()
        self.should_be_ru_language_button()
        self.should_be_forgot_password_button()
        self.should_be_submit_button()

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "login form is not present"

    def should_be_password_form(self):
        assert self.is_element_present(*LoginPageLocators.PASSWORD_FORM), "password form is not present"

    def should_be_ru_language_button(self):
        assert self.is_element_present(*LoginPageLocators.RU_LANG_BUTTON), "ru lang button is not present"

    def should_be_en_language_button(self):
        assert self.is_element_present(*LoginPageLocators.ENG_LANG_BUTTON), "eng lang button is not present"

    def should_be_forgot_password_button(self):
        assert self.is_element_present(*LoginPageLocators.FORGOT_PASSWORD), "forgot password button is not present"

    def should_be_submit_button(self):
        assert self.is_element_present(*LoginPageLocators.SUBMIT_BUTTON), "submit button is not present"

    def user_can_login(self):
        login = self.browser.find_element(*LoginPageLocators.LOGIN_FORM)
        login.send_keys(*Users.ADMIN_LOGIN)
        password = self.browser.find_element(*LoginPageLocators.PASSWORD_FORM)
        password.send_keys(*Users.ADMIN_PASSWORD)
        button = self.browser.find_element(*LoginPageLocators.SUBMIT_BUTTON)
        button.click()
