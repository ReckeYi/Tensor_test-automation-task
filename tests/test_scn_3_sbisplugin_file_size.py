import pytest
from selenium import webdriver
from pages.sbis_download_page import SBISDownloadPage

def test_download_page(chrome):
    download_page = SBISDownloadPage(chrome)
    download_page.open("https://sbis.ru")
    download_page.click_download_link()

def test_element(chrome):
    download_page = SBISDownloadPage(chrome)
    download_page.open("https://sbis.ru/download")

    download_page.click_plugin_element()
    download_page.click_windows_button()

    download_page.wait_for_windows_element()

    file_path = download_page.download_file()
    expected_file_size = 7555736
    download_page.validate_file_size(file_path, expected_file_size)
