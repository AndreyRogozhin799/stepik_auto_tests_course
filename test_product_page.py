# Файл: tests/test_product_page.py

import pytest
from .product_page import ProductPage



@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    product_name = page.get_product_name()
    product_price = page.get_product_price()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    page.check_success_message(product_name)
    page.check_price_matches(product_price)
