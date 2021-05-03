from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # находим и копируем значение х из формулы
    x_element = browser.find_element_by_id("input_value")
    # рассчитываем формулу
    x = x_element.text
    y = calc(x)
    # находим поле ввода и вставляем ответ 
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    # отмечаем чекбокс I'm the robot
    option1 = browser.find_element_by_id('robotCheckbox')
    option1.click()
    # выбираем radiobutton Robots rule
    option2 = browser.find_element_by_id('robotsRule')
    option2.click()
    button = browser.find_element_by_class_name('btn')
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

