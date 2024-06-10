import allure
import logging

logger = logging.getLogger(__name__)

@allure.step("Проверка заголовка 'О нас'")
def check_tensor_about_page_work_header(tensor_about_page):
    logger.info("Проверка заголовка 'О нас' на странице")
    tensor_about_page.verify_work_header()
    logger.info("Заголовок 'О нас' успешно проверен")

@allure.step("Проверка изображений")
def check_tensor_about_page_images(tensor_about_page):
    logger.info("Проверка изображений на странице")
    tensor_about_page.verify_images()
    logger.info("Изображения успешно проверены")
