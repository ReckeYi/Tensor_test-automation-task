import allure
import logging

from pages.checkout_pages.check_sbis_contacts_page import check_partners_list_changed
from pages.sbis_contacts_page import SbisContactsPage

logger = logging.getLogger(__name__)


@allure.feature("Регионы")
@allure.story("Проверка региона")
def test_tensor_region(chrome):
    sbis_contacts_page = SbisContactsPage(chrome)
    sbis_contacts_page.open()

    region_element = sbis_contacts_page.verify_region_element()
    partners_list_step1 = sbis_contacts_page.get_partners_list_text()

    sbis_contacts_page.click_region_element(region_element)
    sbis_contacts_page.select_kamchatka_region()
    sbis_contacts_page.verify_changed_region()
    sbis_contacts_page.verify_url_contains("41-kamchatskij-kraj")
    sbis_contacts_page.verify_page_title("СБИС Контакты — Камчатский край")

    sbis_contacts_page.wait_for_partners_list_to_change(partners_list_step1)
    partners_list_step2 = sbis_contacts_page.get_partners_list_text()

    check_partners_list_changed(partners_list_step1, partners_list_step2)
