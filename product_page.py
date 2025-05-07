from .pages.base import BasePage
from .pages.locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_cart(self):
        """Метод добавляет товар в корзину"""
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        button.click()

    def solve_quiz_and_get_code(self):
        """Метод решает задачу из всплывающего окна и получает код"""
        from selenium.common.exceptions import NoAlertPresentException
        import time
        import math
        try:
            alert = self.browser.switch_to.alert
            x = alert.text.split(" ")[2]
            answer = str(math.log(abs((12 * math.sin(float(x))))))
            alert.send_keys(answer)
            alert.accept()

            try:
                alert = self.browser.switch_to.alert
                alert_text = alert.text
                print(f"Your code: {alert_text}")
                alert.accept()
            except NoAlertPresentException:
                pass
        finally:
            time.sleep(1)

    def check_success_message(self, expected_product_name):
        """Проверяет, что название товара в сообщении совпадает с именем товара"""
        success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE)
        actual_product_name = success_message.text.split()[0].strip()
        assert expected_product_name == actual_product_name, \
               f"Expected product '{expected_product_name}' but got '{actual_product_name}'"

    def check_price_matches(self, expected_price):
        """Проверяет, что цена товара в корзине равна указанной цене товара"""
        price_in_cart = self.browser.find_element(*ProductPageLocators.PRICE_IN_CART).text.strip()
        assert expected_price == price_in_cart, \
               f"Price mismatch: Expected '{expected_price}', Got '{price_in_cart}'"

    def get_product_name(self):
        """Возвращает название текущего товара"""
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text.strip()

    def get_product_price(self):
        """Возвращает цену текущего товара"""
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text.strip()
