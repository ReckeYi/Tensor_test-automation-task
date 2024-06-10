import logging

import requests
import tempfile
import os
import allure
from pages.sbis_main_page import SbisMainPage
from pages.sbis_download_page import SbisDownloadPage


logger = logging.getLogger(__name__)


@allure.feature("Скачивание файлов")
@allure.story("Загрузка плагина и проверка его размера")
def test_download_and_verify(chrome):
    sbis_main_page = SbisMainPage(chrome)
    sbis_main_page.open()
    sbis_main_page.click_download_link()

    sbis_download_page = SbisDownloadPage(chrome)
    sbis_download_page.open()
    sbis_download_page.click_plugin_element()
    sbis_download_page.click_windows_button()
    sbis_download_page.verify_windows_element()

    file_url = "https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe"
    file_name = "sbisplugin-setup-web.exe"
    response = requests.get(file_url)
    logger.info("Проверка ответа сервера")
    assert response.status_code == 200

    temp_dir = tempfile.gettempdir()
    file_path = os.path.join(temp_dir, file_name)

    with open(file_path, 'wb') as f:
        f.write(response.content)

    logger.info("Проверка существования скачанного файла")
    assert os.path.exists(file_path), "Скачанный файл не найден"

    expected_file_size = 7.219871520996094
    actual_file_size = os.path.getsize(file_path) / (1024 * 1024)
    logger.info("Проверка размера файла")
    assert actual_file_size == expected_file_size
