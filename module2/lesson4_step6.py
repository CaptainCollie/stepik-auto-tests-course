from selenium import webdriver as w
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/cats.html"

try:
    browser = w.Chrome()
    browser.get(link)

    browser.find_element_by_id("button").click()

finally:
    time.sleep(7)
    browser.quit()
