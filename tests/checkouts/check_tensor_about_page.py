import allure
import logging

logger = logging.getLogger(__name__)


@allure.step("Проверка заголовка 'О нас'")
def check_tensor_about_page_work_header(tensor_about_page):
    logger.info("Проверка заголовка 'О нас' на странице")
    header_text = tensor_about_page.get_work_header()
    assert header_text == "Работаем", f"Ожидалось 'Работаем', но получено {header_text}"
    logger.info("Заголовок 'О нас' успешно проверен")


@allure.step("Проверка изображений")
def check_tensor_about_page_images(tensor_about_page):
    logger.info("Проверка изображений на странице")
    images = tensor_about_page.get_images()
    assert len(images) == 4, f"Ожидалось 4 изображения, но найдено {len(images)}"
    width = images[0].get_attribute("width")
    height = images[0].get_attribute("height")
    for image in images[1:]:
        assert image.get_attribute(
            "width") == width, f"Ширина изображения не совпадает: {image.get_attribute('width')} != {width}"
        assert image.get_attribute(
            "height") == height, f"Высота изображения не совпадает: {image.get_attribute('height')} != {height}"
    logger.info("Изображения успешно проверены")
