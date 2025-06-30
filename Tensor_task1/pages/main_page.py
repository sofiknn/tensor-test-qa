from selenium.webdriver.common.by import By
from .base_page import BasePage

class MainPage(BasePage):
    CONTACTS_MENU = (By.XPATH, '//*[@id="wasaby-content"]/div/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[2]/div/div[1]')
    OFFICES_LINK = (By.XPATH, '//*[@id="wasaby-content"]/div/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[2]/div/div[2]/a[2]/span')

    def go_to_offices(self):
        self.click(self.CONTACTS_MENU)
        self.click(self.OFFICES_LINK)

