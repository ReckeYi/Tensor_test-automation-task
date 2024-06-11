import time

from pages.sbis_download_page import SBISDownloadPage
from utilites.constants import EXPECTED_FILE_SIZE


def test_download_page(chrome):
    download_page = SBISDownloadPage(chrome)
    download_page.open("https://sbis.ru")
    download_page.click_download_link()
    download_page.wait_for_plugin_element()
    download_page.click_plugin_element()
    file_path = download_page.download_file()
    download_page.validate_file_size(file_path, EXPECTED_FILE_SIZE)
