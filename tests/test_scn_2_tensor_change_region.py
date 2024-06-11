from pages.sbis_contacts_page import SbisContactsPage
from tests.checkouts.check_sbis_contacts_page import *
from utilites.constants import *


@allure.feature("Проверка региона на странице контактов")
@allure.story("Сравнение региона и списка партнеров")
def test_tensor_region(chrome):
    sbis_contacts_page = SbisContactsPage(chrome)
    sbis_contacts_page.open()

    region_element = sbis_contacts_page.get_region_element()
    checks_region_element_displayed(region_element)

    partners_list_element = sbis_contacts_page.get_partners_list_element()
    checks_partners_list_element(partners_list_element)

    partners_list_step1 = partners_list_element.text

    sbis_contacts_page.click_region_element()
    sbis_contacts_page.select_region(KAMCHATKA)

    sbis_contacts_page.wait_for_partners_list_to_change(partners_list_step1)

    changed_region = sbis_contacts_page.get_changed_region_element()
    checks_changed_region_displayed(changed_region)

    current_url = sbis_contacts_page.get_current_url()
    checks_current_url(current_url)

    actual_title = sbis_contacts_page.get_title()
    checks_title(EXPECTED_TITLE, actual_title)

    partners_list_element = sbis_contacts_page.get_partners_list_element()
    checks_partners_list_element(partners_list_element)

    partners_list_step2 = partners_list_element.text
    checks_partners_list_updated(partners_list_step1, partners_list_step2)
