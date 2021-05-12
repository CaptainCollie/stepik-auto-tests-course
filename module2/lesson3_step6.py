from selenium import webdriver as w
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = w.Chrome()
    browser.get(link)
 
    btn = browser.find_element_by_css_selector(".btn-primary")
    btn.click()

    browser.switch_to.window(browser.window_handles[1])

    x_el = browser.find_element_by_css_selector("#input_value")
    x = x_el.text
    y = calc(x)

    browser.find_element_by_css_selector("#answer").send_keys(y)

    browser.find_element_by_css_selector(".btn").click()

finally:
    time.sleep(7)
    browser.quit()
