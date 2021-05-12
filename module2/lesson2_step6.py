from selenium import webdriver as w
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://SunInJuly.github.io/execute_script.html"

try:
    browser = w.Chrome()
    browser.get(link)
    
    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)
    
    input = browser.find_element_by_css_selector("#answer")
    browser.execute_script("return arguments[0].scrollIntoView(true)", input)
    input.send_keys(y)

    btn_chkbx = browser.find_element_by_css_selector('[type="checkbox"]')
    browser.execute_script("return arguments[0].scrollIntoView(true)", btn_chkbx)
    btn_chkbx.click()

    btn_radio = browser.find_element_by_css_selector('[for="robotsRule"]')
    browser.execute_script("return arguments[0].scrollIntoView(true)", btn_radio)
    btn_radio.click()

    button = browser.find_element_by_css_selector('.btn')
    browser.execute_script("return arguments[0].scrollIntoView(true)", button)
    button.click()

    time.sleep(1)


finally:
    time.sleep(7)
    browser.quit()

