import logging
import allure

from pages.base_page import BasePage
from pages.locators.tensor_about_page_locators import TensorAboutPageLocators

logger = logging.getLogger(__name__)


class TensorAboutPage(BasePage):

    @allure.step("Получение заголовка 'Работаем'")
    def get_work_header(self):
        logger.info("Получение заголовка 'Работаем'")
        header = self.wait_for_element(*TensorAboutPageLocators.WORK_HEADER)
        return header.text

    @allure.step("Получение изображений")
    def get_images(self):
        logger.info("Получение изображений")
        images = self.find_elements(*TensorAboutPageLocators.IMAGES)
        return images
