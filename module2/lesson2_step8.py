from selenium import webdriver as w
import time
import math
import os


link = "http://suninjuly.github.io/file_input.html"
cur_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(cur_dir, 'upload_example.txt')


try:
    browser = w.Chrome()
    browser.get(link)
    
    browser.find_element_by_css_selector('[name="firstname"]').send_keys('Ivan')
    browser.find_element_by_css_selector('[name="lastname"]').send_keys('Ivanov')
    browser.find_element_by_css_selector('[name="email"]').send_keys('ivanov@mail.ru')

    file_upload = browser.find_element_by_css_selector('[type="file"]')
    file_upload.send_keys(file_path)

    button = browser.find_element_by_css_selector('.btn')
    button.click()

    time.sleep(1)


finally:
    time.sleep(7)
    browser.quit()

