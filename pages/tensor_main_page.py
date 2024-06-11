import logging
import time
import allure

from pages.base_page import BasePage
from pages.locators.tensor_main_page_locators import TensorMainPageLocators

logger = logging.getLogger(__name__)


class TensorMainPage(BasePage):

    @allure.step("Получение слогана 'Сила в людях'")
    def get_slogan(self):
        logger.info("Получение слогана 'Сила в людях'")
        element = self.wait_for_element(*TensorMainPageLocators.SLOGAN_ELEMENT)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element.text

    @allure.step("Получение ссылки 'Подробнее'")
    def get_detail_link(self):
        logger.info("Получение ссылки 'Подробнее'")
        link = self.wait_for_element(*TensorMainPageLocators.DETAIL_LINK)
        return link

    @allure.step("Клик по ссылке 'Подробнее'")
    def click_detail_link(self):
        logger.info("Клик по ссылке 'Подробнее'")
        link = self.get_detail_link()
        link.click()

    @allure.step("Ожидание загрузки контента")
    def wait_content(self):
        logger.info("Ожидание загрузки контента")
        time.sleep(1)
