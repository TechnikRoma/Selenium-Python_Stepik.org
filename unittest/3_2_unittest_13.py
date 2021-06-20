import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class HomeWorkTeam(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\chromedriver/chromedriver.exe')


    def test_team_search(self):
        driver = self.driver
        driver.get("http://suninjuly.github.io/registration2.html")
        teamelem = driver.find_element_by_css_selector(".first_block .form-control.first")
        teamelem.send_keys("Ivan")
        input2 = driver.find_element_by_css_selector(".first_block .form-control.second")
        input2.send_keys("Petrov")
        input3 = driver.find_element_by_css_selector(".first_block .form-control.third")
        input3.send_keys("Smolensk")  
        button = driver.find_element_by_xpath('//button[text()="Submit"]')
        button.click()        
        #assert "No results found" not in driver.page_source
        time.sleep(1)
        welcome_text_elt = driver.find_element_by_tag_name('h1')
        welcome_text = welcome_text_elt.text
        print(welcome_text)
        self.assertEqual('Congratulations! You have successfully registered!',welcome_text)
        
        
    def test_abs2(self):
        driver = self.driver
        driver.get("http://suninjuly.github.io/registration1.html")
        teamelem = driver.find_element_by_css_selector(".first_block .form-control.first")
        teamelem.send_keys("Ivan")
        input2 = driver.find_element_by_css_selector(".first_block .form-control.second")
        input2.send_keys("Petrov")
        input3 = driver.find_element_by_css_selector(".first_block .form-control.third")
        input3.send_keys("Smolensk")  
        button = driver.find_element_by_xpath('//button[text()="Submit"]')
        button.click()        
        #assert "No results found" not in driver.page_source
        time.sleep(1)
        welcome_text_elt = driver.find_element_by_tag_name('h1')
        welcome_text = welcome_text_elt.text
        print(welcome_text)
        self.assertEqual('Congratulations! You have successfully registered!', welcome_text)
        time.sleep(10)
        

@classmethod
def tearDownClass(cls):
    cls.driver.close()
    cls.driver.quit()
    print('Test completed')

    if __name__ == '__main__':
        unittest.main()