import allure
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
    assert "tensor.ru" in chrome.current_url

    tensor_main_page = TensorMainPage(chrome)
    tensor_main_page.verify_slogan()
    tensor_main_page.click_detail_link()
    assert chrome.current_url == "https://tensor.ru/about"

    # Проверка страницы "О нас" на tensor.ru
    tensor_about_page = TensorAboutPage(chrome)
    tensor_about_page.verify_work_header()
    tensor_about_page.verify_images()

