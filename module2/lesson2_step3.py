from selenium import webdriver as w
from selenium.webdriver.support.ui import Select
import time
import math


link = "http://suninjuly.github.io/selects1.html"

try:
    browser = w.Chrome()
    browser.get(link)
    
    num1 = browser.find_element_by_css_selector('#num1').text
    num2 = browser.find_element_by_css_selector('#num2').text
    res = int(num1) + int(num2)

    sel = Select(browser.find_element_by_css_selector('#dropdown'))
    sel.select_by_value(str(res))

    button = browser.find_element_by_css_selector('.btn')
    button.click()

    time.sleep(1)


finally:
    time.sleep(7)
    browser.quit()

