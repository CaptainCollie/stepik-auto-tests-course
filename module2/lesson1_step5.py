from selenium import webdriver as w
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"

try:
    browser = w.Chrome()
    browser.get(link)
    
    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)
    
    input = browser.find_element_by_css_selector("#answer")
    input.send_keys(y)
    btn_chkbx = browser.find_element_by_css_selector('[type="checkbox"]')
    btn_chkbx.click()
    btn_radio = browser.find_element_by_css_selector('[for="robotsRule"]')
    btn_radio.click()
    button = browser.find_element_by_css_selector('.btn')
    button.click()

    time.sleep(1)


finally:
    time.sleep(7)
    browser.quit()

