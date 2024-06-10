import allure
import logging
from pages.sbis_contacts_page import SbisContactsPage
from pages.tensor_about_page import TensorAboutPage
from pages.tensor_main_page import TensorMainPage


logger = logging.getLogger(__name__)


@allure.feature("Размер изображений")
@allure.story("Сравнение размеров изображений")
def test_tensor_functionality(chrome):
    sbis_contacts_page = SbisContactsPage(chrome)
    sbis_contacts_page.open()
    sbis_contacts_page.click_tensor_banner()
    chrome.switch_to.window(chrome.window_handles[1])
    logger.info("Проверка адреса сайта")
    assert "tensor.ru" in chrome.current_url

    tensor_main_page = TensorMainPage(chrome)
    tensor_main_page.verify_slogan()
    tensor_main_page.click_detail_link()
    logger.info("Проверка ссылки на открытой странице")
    assert chrome.current_url == "https://tensor.ru/about"

    # Проверка страницы "О нас" на tensor.ru
    tensor_about_page = TensorAboutPage(chrome)
    tensor_about_page.verify_work_header()
    tensor_about_page.verify_images()

