import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def chrome():
    chrome_browser = webdriver.Chrome()
    chrome_browser.implicitly_wait(5)
    yield chrome_browser
    chrome_browser.quit()


def test_tensor_transition(chrome):
    chrome.get("https://sbis.ru/contacts")
    tensor_banner = chrome.find_element(By.XPATH, "//a[@href='https://tensor.ru/']")
    assert tensor_banner.is_displayed()
    tensor_banner.click()
    chrome.switch_to.window(chrome.window_handles[1])
    assert "tensor.ru" in chrome.current_url


def test_tensor_block(chrome):
    chrome.get("https://tensor.ru/")
    element = chrome.find_element(By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[1]')
    chrome.execute_script("arguments[0].scrollIntoView();", element)
    assert element.is_displayed()
    assert element.text == "Сила в людях"
    detail_link = chrome.find_element(By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a[text()="Подробнее"]')
    assert detail_link.is_displayed()
    detail_link.click()
    assert chrome.current_url == "https://tensor.ru/about"


def test_about_page(chrome):
    chrome.get("https://tensor.ru/about")
    work_header = chrome.find_element(By.XPATH, '//*[@id="container"]/div[1]/div/div[4]/div[1]/h2')
    assert work_header.text == "Работаем"
    images = chrome.find_elements(By.XPATH,
                                  '//div[@class="s-Grid-col s-Grid-col--3 tensor_ru-About--col-md6 tensor_ru-About__block3--col-sm12"]//img')
    assert len(images) == 4
    width = images[0].get_attribute("width")
    height = images[0].get_attribute("height")
    for image in images[1:]:
        assert image.get_attribute("width") == width
        assert image.get_attribute("height") == height
