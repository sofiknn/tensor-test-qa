from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ContactsPage:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 15)

    def get_region(self):
        region = self.wait.until(EC.visibility_of_element_located((By.XPATH,
            '//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span')))
        return region.text.strip()

    def partners_contain(self, text):
        partners = self.wait.until(EC.visibility_of_element_located((By.XPATH,
            '//*[@id="contacts_list"]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]')))
        return text in partners.text

    def change_region_to_kamchatka(self):
        region = self.wait.until(EC.element_to_be_clickable((By.XPATH,
            '//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span')))
        region.click()

        kamchatka_option = self.wait.until(EC.element_to_be_clickable((By.XPATH,
            '//*[@id="popup"]/div[2]/div/div/div/div/div[2]/div/ul/li[43]/span/span')))
        kamchatka_option.click()
