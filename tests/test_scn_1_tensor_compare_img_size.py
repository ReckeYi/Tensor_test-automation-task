import allure

from pages.checkout_pages.check_tensor_about_page import *
from pages.checkout_pages.check_tensor_main_page import *
from pages.sbis_contacts_page import SbisContactsPage
from pages.tensor_about_page import TensorAboutPage
from pages.tensor_main_page import TensorMainPage


@allure.feature("Размер изображений")
@allure.story("Сравнение размеров изображений")
def test_tensor_functionality(chrome):
    sbis_contacts_page = SbisContactsPage(chrome)
    sbis_contacts_page.open()
    sbis_contacts_page.click_tensor_banner()
    chrome.switch_to.window(chrome.window_handles[1])
    check_tensor_site_address(chrome)

    tensor_main_page = TensorMainPage(chrome)
    check_tensor_main_page_slogan(tensor_main_page)
    tensor_main_page.click_detail_link()
    check_tensor_main_page_link(chrome)

    tensor_about_page = TensorAboutPage(chrome)
    check_tensor_about_page_work_header(tensor_about_page)
    check_tensor_about_page_images(tensor_about_page)
