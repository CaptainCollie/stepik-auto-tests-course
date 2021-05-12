from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver as w
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = w.Chrome()
    browser.get(link)

    WDW(browser, 13).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    browser.find_element_by_css_selector("#book").click()

    x_el = browser.find_element_by_css_selector("#input_value")
    x = x_el.text
    y = calc(x)

    browser.find_element_by_css_selector("#answer").send_keys(y)

    button = browser.find_element_by_css_selector('[type="submit"]')
    browser.execute_script("return arguments[0].scrollIntoView(true)", button)
    button.click()

finally:
    time.sleep(7)
    browser.quit()

