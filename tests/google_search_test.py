from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from time import sleep


class TestGoogle:
    def test_simple_search(self):
        driver = webdriver.Chrome(executable_path='../../chromedriver.exe')
        search_word = 'cats'
        pages = 5
        driver.get('http://google.com.ua/')
        driver.find_element(By.CSS_SELECTOR, 'input[name="q"]').send_keys(search_word)
        driver.find_element(By.CSS_SELECTOR, 'input[name="q"]').send_keys(Keys.ENTER)
        results = self.collect_search_results(pages, driver)
        for i in range(len(results)):
            assert search_word.lower() in results[i].lower()
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
        driver.quit()

    def collect_search_results(self, pages, driver):
        res = []
        for i in range(1, pages + 1):
            r = driver.find_elements(By.XPATH, '//div[@class="g"]')
            for j in range(len(r)):
                res.append(r[i].text)
            if i is pages:
                continue
            driver.find_element(By.CSS_SELECTOR, "a[aria-label='Page {}']".format(str(i + 1))).click()
            sleep(5)
        return res
