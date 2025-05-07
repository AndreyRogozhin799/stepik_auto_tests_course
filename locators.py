#from selenium.webdriver.common.by import By


#   LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

# Файл: tests/pages/locators.py

from selenium.webdriver.common.by import By

class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")
    PRICE_IN_CART = (By.CSS_SELECTOR, "#messages strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
