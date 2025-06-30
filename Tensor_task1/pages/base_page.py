from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url):
        self.driver.get(url)

    def click(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.click()

    def wait_for_text(self, text):
        return self.wait.until(EC.visibility_of_element_located(("xpath", f"//*[contains(text(), '{text}')]")))

    def wait_for_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_elements(self, by, value):
        return self.driver.find_elements(by, value)

