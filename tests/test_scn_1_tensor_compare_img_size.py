import allure
from pages.sbis_contacts_page import SbisContactsPage
from pages.tensor_about_page import TensorAboutPage
from pages.tensor_main_page import TensorMainPage
from tests.checkouts.check_tensor_about_page import *
from tests.checkouts.check_tensor_main_page import *


@allure.feature("Проверка соответствия размера изображений")
@allure.story("Сравнение размеров изображений")
def test_tensor_functionality(chrome):
    sbis_contacts_page = SbisContactsPage(chrome)
    sbis_contacts_page.open()
    sbis_contacts_page.click_tensor_banner()
    chrome.switch_to.window(chrome.window_handles[1])

    check_tensor_site_address(chrome)
    tensor_main_page = TensorMainPage(chrome)
    tensor_main_page.wait_content()
    check_tensor_main_page_slogan(tensor_main_page)
    check_tensor_main_page_detail_link(tensor_main_page)
    tensor_main_page.click_detail_link()
    check_tensor_main_page_link(chrome)

    tensor_about_page = TensorAboutPage(chrome)
    check_tensor_about_page_work_header(tensor_about_page)
    check_tensor_about_page_images(tensor_about_page)
