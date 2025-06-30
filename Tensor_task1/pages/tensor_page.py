from selenium.webdriver.common.by import By
from .base_page import BasePage

class TensorPage(BasePage):
    MORE_LINK = (By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a')
    IMAGE_CARDS_CLASS = "tensor_ru-About__block3-image-wrapper"

    def verify_slogan_visible(self):
        self.wait_for_text("Сила в людях")

    def click_more(self):
        self.click(self.MORE_LINK)

    def all_cards_same_size(self):
        cards = self.wait_for_element((By.CLASS_NAME, self.IMAGE_CARDS_CLASS))
        cards = self.find_elements(By.CLASS_NAME, self.IMAGE_CARDS_CLASS)
        if not cards:
            return False, []

        w0, h0 = cards[0].size['width'], cards[0].size['height']
        sizes = [(c.size['width'], c.size['height']) for c in cards]
        all_equal = all(w == w0 and h == h0 for w, h in sizes)

        return all_equal, sizes
