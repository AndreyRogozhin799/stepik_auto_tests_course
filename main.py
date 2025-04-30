from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ждем, когда цена уменьшится до $100
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # Нажимаем на кнопку "Book"
    button = browser.find_element(By.ID, "book")
    button.click()

    # Находим значение для переменной x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text

    # Вычисляем значение функции
    y = calc(x)

    # Вводим ответ в текстовое поле
    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(y)

    # Нажимаем на кнопку Submit
    button = browser.find_element(By.ID, "solve")
    button.click()

finally:
    # Ждем 30 секунд, чтобы успеть увидеть результат
    time.sleep(30)
    # Закрываем браузер
    browser.quit()
