import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def chrome():
    chrome_browser = webdriver.Chrome()
    chrome_browser.implicitly_wait(5)
    yield chrome_browser
    chrome_browser.quit()


def test_tensor_region(chrome):
    chrome.get("https://sbis.ru/contacts")

    region_element = chrome.find_element(By.XPATH,
                                         '//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span')
    assert region_element.is_displayed()

    partners_list_element = chrome.find_element(By.XPATH, '//*[@id="contacts_list"]/div/div[2]')
    assert partners_list_element

    partners_list_step1 = partners_list_element.text

    region_element.click()

    region_list = WebDriverWait(chrome, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'ul.sbis_ru-Region-Panel__list-l'))
    )

    kamchatka_region = WebDriverWait(chrome, 10).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '//*[@id="popup"]/div[2]/div/div/div/div/div[2]/div/ul/li/span/span[contains(text(), "Камчатский край")]'))
    )
    kamchatka_region.click()

    changed_region = WebDriverWait(chrome, 10).until(
        EC.visibility_of_element_located((By.XPATH,
                                          '//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span[contains(text(), "Камчатский край")]'))
    )
    assert changed_region.is_displayed()

    current_url = chrome.current_url
    assert "41-kamchatskij-kraj" in current_url

    expected_title = "СБИС Контакты — Камчатский край"
    actual_title = chrome.title
    assert expected_title in actual_title

    partners_list_element = chrome.find_element(By.XPATH, '//*[@id="contacts_list"]/div/div[2]')
    assert partners_list_element

    partners_list_step2 = partners_list_element.text
    assert partners_list_step1 != partners_list_step2
