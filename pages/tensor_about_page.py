from .base_page import BasePage
from .locators.tensor_about_page_locators import TensorAboutPageLocators


class TensorAboutPage(BasePage):
    def open(self):
        self.driver.get("https://tensor.ru/about")

    def verify_work_header(self):
        header = self.wait_for_element(*TensorAboutPageLocators.WORK_HEADER)
        assert header.text == "Работаем"

    def verify_images(self):
        images = self.find_elements(*TensorAboutPageLocators.IMAGES)
        assert len(images) == 4
        width = images[0].get_attribute("width")
        height = images[0].get_attribute("height")
        for image in images[1:]:
            assert image.get_attribute("width") == width
            assert image.get_attribute("height") == height
