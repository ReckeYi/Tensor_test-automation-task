import logging
from pages.sbis_contacts_page import SbisContactsPage

logger = logging.getLogger(__name__)


def test_tensor_region(chrome):
    sbis_contacts_page = SbisContactsPage(chrome)
    sbis_contacts_page.open()
    logger.info("Открыта страница https://sbis.ru/contacts")

    region_element = sbis_contacts_page.verify_region_element()
    logger.info("Проверка наличия элемента региона")

    partners_list_step1 = sbis_contacts_page.get_partners_list_text()
    logger.info("Получение текста списка партнеров")

    sbis_contacts_page.click_region_element(region_element)
    logger.info("Клик по элементу региона")

    sbis_contacts_page.select_kamchatka_region()
    logger.info("Выбор региона 'Камчатский край'")

    sbis_contacts_page.verify_changed_region()
    logger.info("Проверка измененного региона")

    sbis_contacts_page.verify_url_contains("41-kamchatskij-kraj")
    logger.info("Проверка URL страницы")

    sbis_contacts_page.verify_page_title("СБИС Контакты — Камчатский край")
    logger.info("Проверка заголовка страницы")

    partners_list_step2 = sbis_contacts_page.get_partners_list_text()
    assert partners_list_step1 != partners_list_step2
    logger.info("Сравнение текста списка партнеров до и после выбора региона")
