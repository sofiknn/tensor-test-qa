from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 15)

    def open(self):
        self.browser.get('https://saby.ru/')

    def open_contacts_offices(self):
        contacts = self.wait.until(EC.visibility_of_element_located((By.XPATH,
            '//*[@id="wasaby-content"]/div/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[2]/div/div[1]')))
        contacts.click()

        offices = self.wait.until(EC.visibility_of_element_located((By.XPATH,
            '//*[@id="wasaby-content"]/div/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[2]/div/div[2]/a[2]/span')))
        offices.click()
