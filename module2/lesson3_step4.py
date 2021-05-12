from selenium import webdriver as w
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = w.Chrome()
    browser.get(link)

    btn = browser.find_element_by_css_selector(".btn-primary")
    btn.click()

    prompt = browser.switch_to.alert
    prompt.accept()

    time.sleep(1)
    
    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)
    
    input = browser.find_element_by_css_selector("#answer")
    browser.execute_script("return arguments[0].scrollIntoView(true)", input)
    input.send_keys(y)

    button = browser.find_element_by_css_selector('.btn')
    browser.execute_script("return arguments[0].scrollIntoView(true)", button)
    button.click()

finally:
    time.sleep(7)
    browser.quit()

