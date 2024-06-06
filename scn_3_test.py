import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import requests
import tempfile


@pytest.fixture
def chrome():
    chrome_browser = webdriver.Chrome()
    chrome_browser.implicitly_wait(5)
    yield chrome_browser
    chrome_browser.quit()


def mouse_click(driver, element):
    actions = ActionChains(driver)
    actions.move_to_element(element).click().perform()


def test_download_page(chrome):
    chrome.get("https://sbis.ru")
    download_link = chrome.find_element(By.LINK_TEXT, "Скачать локальные версии")
    chrome.execute_script("arguments[0].scrollIntoView(true);", download_link)
    download_link.click()


def test_element(chrome):
    chrome.get("https://sbis.ru/download")
    plugin_element = chrome.find_element(By.XPATH, '//div[contains(text(), "СБИС Плагин")]')
    mouse_click(chrome, plugin_element)
    windows_but = chrome.find_element(By.XPATH, '//span[contains(text(), "Windows")]')
    mouse_click(chrome, windows_but)
    windows_element = WebDriverWait(chrome, 10).until(
        EC.visibility_of_element_located((By.XPATH,
                                          '//span[@class="sbis_ru-DownloadNew-innerTabs__title sbis_ru-DownloadNew-innerTabs__title--default"]'))
    )

    file_url = "https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe"
    file_name = "sbisplugin-setup-web.exe"
    response = requests.get(file_url)
    assert response.status_code == 200

    temp_dir = tempfile.gettempdir()
    file_path = os.path.join(temp_dir, file_name)

    with open(file_path, 'wb') as f:
        f.write(response.content)

    assert os.path.exists(file_path)

    expected_file_size = 7555736
    actual_file_size = os.path.getsize(file_path)
    assert actual_file_size == expected_file_size
