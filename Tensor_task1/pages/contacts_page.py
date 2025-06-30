from selenium.webdriver.common.by import By
from .base_page import BasePage

class ContactsPage(BasePage):
    TENSOR_LOGO = (By.XPATH, '//*[@id="contacts_clients"]/div[1]/div/div/div[2]/div/a/img')

    def click_tensor_logo(self):
        self.click(self.TENSOR_LOGO)

    def open_offices(self):
        offices = self.wait.until(self.visibility_of_element((By.XPATH,
                                                              '//*[@id="wasaby-content"]/div/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[2]/div/div[2]/a[2]/span')))
        offices.click()
