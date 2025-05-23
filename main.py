from .base import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators

class MainPage(BasePage): 
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, *MainPageLocators.LOGIN_LINK)
        login_link.click()
    def should_be_login_link(self):
        assert self.is_element_present(By.CSS_SELECTOR, *MainPageLocators.LOGIN_LINK), "Login link is not presented"
