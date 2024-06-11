import allure
import logging

logger = logging.getLogger(__name__)


@allure.step("Проверка адреса сайта")
def check_tensor_site_address(chrome):
    logger.info("Проверка адреса сайта")
    assert "tensor.ru" in chrome.current_url


@allure.step("Проверка слогана")
def check_tensor_main_page_slogan(tensor_main_page):
    logger.info("Проверка слогана на главной странице")
    slogan_text = tensor_main_page.get_slogan()
    assert slogan_text == "Сила в людях", f"Ожидалось 'Сила в людях', но получено '{slogan_text}'"
    logger.info("Слоган проверен успешно")


@allure.step("Проверка ссылки 'Подробнее'")
def check_tensor_main_page_detail_link(tensor_main_page):
    logger.info("Проверка ссылки 'Подробнее' на главной странице")
    link = tensor_main_page.get_detail_link()
    assert link.is_displayed(), "Ссылка 'Подробнее' не отображается"
    logger.info("Ссылка 'Подробнее' проверена успешно")


@allure.step("Проверка ссылки на открытой странице")
def check_tensor_main_page_link(chrome):
    logger.info("Проверка ссылки на открытой странице")
    expected_url = "https://tensor.ru/about"
    current_url = chrome.current_url
    assert current_url == expected_url, f"Ссылка не соответствует ожидаемому. Текущий URL: {current_url}"
    logger.info("Ссылка на открытой странице проверена успешно")
