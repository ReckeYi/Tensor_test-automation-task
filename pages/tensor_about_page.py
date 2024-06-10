import logging
import allure
from .base_page import BasePage
from .locators.tensor_about_page_locators import TensorAboutPageLocators

logger = logging.getLogger(__name__)


class TensorAboutPage(BasePage):
    # @allure.step("Открытие страницы 'О нас' на сайте https://tensor.ru")
    # def open(self):
    #     logger.info("Открытие страницы 'О нас' на сайте https://tensor.ru")
    #     self.driver.get("https://tensor.ru/about")

    @allure.step("Проверка заголовка 'Работаем'")
    def verify_work_header(self):
        logger.info("Проверка заголовка 'Работаем'")
        header = self.wait_for_element(*TensorAboutPageLocators.WORK_HEADER)
        assert header.text == "Работаем"

    @allure.step("Проверка размера изображений")
    def verify_images(self):
        logger.info("Проверка размера изображений")
        images = self.find_elements(*TensorAboutPageLocators.IMAGES)
        assert len(images) == 4
        width = images[0].get_attribute("width")
        height = images[0].get_attribute("height")
        for image in images[1:]:
            assert image.get_attribute("width") == width
            assert image.get_attribute("height") == height
