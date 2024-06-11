import allure
from pages.sbis_download_page import SBISDownloadPage
from pages.sbis_main_page import SbisMainPage
from utilites.constants import EXPECTED_FILE_SIZE, SBIS


@allure.feature("Загрузка файла на странице загрузки")
@allure.story("Проверка размера скачанного файла")
def test_download_page(chrome):
    main_page = SbisMainPage(chrome)
    main_page.open()
    main_page.click_download_link()

    download_page = SBISDownloadPage(chrome)
    download_page.wait_for_plugin_element()
    download_page.click_plugin_element()
    file_path = download_page.download_file()
    download_page.validate_file_size(file_path, EXPECTED_FILE_SIZE)
