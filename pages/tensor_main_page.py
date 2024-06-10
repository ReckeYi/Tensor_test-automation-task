from .base_page import BasePage
from .locators.tensor_main_page_locators import TensorMainPageLocators


class TensorMainPage(BasePage):
    def open(self):
        self.driver.get("https://tensor.ru/")

    def verify_slogan(self):
        element = self.wait_for_element(*TensorMainPageLocators.SLOGAN_ELEMENT)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        assert element.is_displayed()
        assert element.text == "Сила в людях"

    def click_detail_link(self):
        link = self.wait_for_element(*TensorMainPageLocators.DETAIL_LINK)
        assert link.is_displayed()
        link.click()
