import logging
import requests
import tempfile
import os

from pages.sbis_download_page import SbisDownloadPage
from pages.sbis_main_page import SbisMainPage

logger = logging.getLogger(__name__)


def test_download_page(chrome):
    sbis_main_page = SbisMainPage(chrome)
    sbis_main_page.open()
    logger.info("Открыта страница https://sbis.ru/")

    sbis_main_page.click_download_link()
    logger.info("Нажата ссылка для скачивания")


def test_element(chrome):
    sbis_download_page = SbisDownloadPage(chrome)
    sbis_download_page.open()
    logger.info("Открыта страница https://sbis.ru/download")

    sbis_download_page.click_plugin_element()
    logger.info("Клик по элементу 'СБИС Плагин'")

    sbis_download_page.click_windows_button()
    logger.info("Клик по кнопке 'Windows'")

    sbis_download_page.verify_windows_element()
    logger.info("Проверка элемента Windows")

    file_url = "https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe"
    file_name = "sbisplugin-setup-web.exe"
    response = requests.get(file_url)
    assert response.status_code == 200
    logger.info(f"Запрос к файлу {file_url} выполнен успешно")

    temp_dir = tempfile.gettempdir()
    file_path = os.path.join(temp_dir, file_name)

    with open(file_path, 'wb') as f:
        f.write(response.content)
    logger.info(f"Файл {file_name} успешно скачан и сохранен в {temp_dir}")

    assert os.path.exists(file_path)
    logger.info(f"Проверка существования файла {file_name}: успешно")
