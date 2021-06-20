import unittest
from selenium import webdriver
import time

class test_class_name(unittest.TestCase):
    def test_1(self):
        link =("http://suninjuly.github.io/registration2.html")
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_css_selector(".first_block .form-control.first")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector(".first_block .form-control.second")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector(".first_block .form-control.third")
        input3.send_keys("mail")  
        button = browser.find_element_by_xpath('//button[text()="Submit"]')
        button.click()        
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name('h1')
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Can't open the window with welcome text")
        
        
    def test_2(self):
        link =("http://suninjuly.github.io/registration1.html")
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_css_selector(".first_block .form-control.first")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector(".first_block .form-control.second")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector(".first_block .form-control.third")
        input3.send_keys("mail")  
        button = browser.find_element_by_xpath('//button[text()="Submit"]')
        button.click()        
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name('h1')
        welcome_text = welcome_text_elt.text
        print(welcome_text)
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Can't open the window with welcome text")
        time.sleep(10)
        

@classmethod
def tearDownClass(cls):
    cls.driver.close()
    cls.driver.quit()
    print('Test completed')

    if __name__ == '__main__':
        unittest.main()
