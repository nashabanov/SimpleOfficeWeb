from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#root > div > main > div > div.sc-ZyCDH.JmWfZ > div.sc-jOhDuK.kmTltQ > div:nth-child(1) > input")
    PASSWORD_FORM = (By.CSS_SELECTOR, "#root > div > main > div > div.sc-ZyCDH.JmWfZ > div.sc-jOhDuK.kmTltQ > div:nth-child(2) > input")
    ENG_LANG_BUTTON = (By.CSS_SELECTOR, "#root > div > main > div > div.sc-eFWqGp.fSVOLz > div.sc-csvncw.cVUNWq")
    RU_LANG_BUTTON = (By.CSS_SELECTOR, "#root > div > main > div > div.sc-eFWqGp.fSVOLz > div.sc-csvncw.gHqxHF")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "#root > div > main > div > div.sc-ZyCDH.JmWfZ > div.sc-jOhDuK.kmTltQ > button.sc-fvNpTx.fmUvfb")
    FORGOT_PASSWORD = (By.CSS_SELECTOR, "#root > div > main > div > div.sc-ZyCDH.JmWfZ > div.sc-jOhDuK.kmTltQ > button.sc-brCFrO.jsjsNz")
