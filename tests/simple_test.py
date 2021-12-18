from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestClass:
    def test_something(self):
        driver = webdriver.Chrome(executable_path='../../chromedriver.exe')
        driver.get("http://151.80.70.42:3000/")
        create_button = driver.find_element(By.CSS_SELECTOR, 'i.mdi-content-add')
        create_button.click()
        name = driver.find_element_by_css_selector('div.main-content input#icon_prefix')
        name.clear()
        name.send_keys('VASYAAAAA')
        phone = driver.find_element_by_css_selector('div.main-content input#icon_telephone')
        phone.clear()
        phone.send_keys('1234567899')
        driver.find_element_by_css_selector('div.main-content a.save-btn').click()
        driver.close()
