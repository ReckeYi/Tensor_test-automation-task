# pages/locators/sbis_download_page_locators.py
from selenium.webdriver.common.by import By


class SbisDownloadPageLocators:
    DOWNLOAD_LINK = (By.LINK_TEXT, "Скачать локальные версии")
    PLUGIN_ELEMENT = (By.XPATH, '(//div[contains(text(), "СБИС Плагин")])[1]')
    WINDOWS_BUTTON = (By.XPATH, '//span[contains(text(), "Windows")]')
    WINDOWS_ELEMENT = (
        By.XPATH, '//span[@class="sbis_ru-DownloadNew-innerTabs__title sbis_ru-DownloadNew-innerTabs__title--default"]')
