from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
    button.click()

    
    
    
    input1 = browser.find_element_by_tag_name('input')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name('last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name('city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id('country')
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector('button.btn')
    button.click()
finally:
    alert = browser.switch_to.alert
    alert_text = alert.text
    # validate the alert text
    alert.accept()

    print(alert_text.split()[-1])
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
