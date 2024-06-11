import logging
import time

import allure
from .base_page import BasePage
from .locators.tensor_main_page_locators import TensorMainPageLocators

logger = logging.getLogger(__name__)


class TensorMainPage(BasePage):
    # @allure.step("Открытие главной страницы https://tensor.ru/")
    # def open(self):
    #     logger.info("Открытие главной страницы https://tensor.ru/")
    #     self.driver.get("https://tensor.ru/")

    @allure.step("Проверка слогана 'Сила в людях'")
    def verify_slogan(self):
        logger.info("Проверка слогана 'Сила в людях'")
        element = self.wait_for_element(*TensorMainPageLocators.SLOGAN_ELEMENT)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        assert element.is_displayed()
        assert element.text == "Сила в людях"

    @allure.step("Клик по ссылке 'Подробнее'")
    def click_detail_link(self):
        logger.info("Клик по ссылке 'Подробнее'")
        link = self.wait_for_element(*TensorMainPageLocators.DETAIL_LINK)
        assert link.is_displayed()
        link.click()

    def wait_content(self):
        time.sleep(1)
