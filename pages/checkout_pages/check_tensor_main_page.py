import allure
import logging

logger = logging.getLogger(__name__)

@allure.step("Проверка слогана")
def check_tensor_main_page_slogan(tensor_main_page):
    logger.info("Проверка слогана на главной странице")
    tensor_main_page.verify_slogan()
    logger.info("Слоган проверен успешно")

@allure.step("Проверка ссылки на открытой странице")
def check_tensor_main_page_link(chrome):
    expected_url = "https://tensor.ru/about"
    current_url = chrome.current_url
    logger.info(f"Проверка ссылки на открытой странице. Ожидаемый URL: {expected_url}, Текущий URL: {current_url}")
    assert current_url == expected_url, f"Ссылка не соответствует ожидаемому. Текущий URL: {current_url}"
    logger.info("Ссылка на открытой странице проверена успешно")
