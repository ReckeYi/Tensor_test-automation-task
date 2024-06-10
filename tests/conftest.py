import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def chrome():
    chrome_browser = webdriver.Chrome()
    chrome_browser.implicitly_wait(5)
    yield chrome_browser
    chrome_browser.quit()


# @pytest.fixture
# def chrome():
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")  # Включение headless режима
#     chrome_options.add_argument("--disable-gpu")  # Опция рекомендуется для Windows
#     chrome_options.add_argument("--window-size=1920,1080")  # Установка размера окна
#
#     logger.info("Инициализация браузера Chrome")
#     chrome_browser = webdriver.Chrome(options=chrome_options)
#     chrome_browser.implicitly_wait(5)
#
#     yield chrome_browser
#
#     logger.info("Очистка кеша браузера")
#     chrome_browser.delete_all_cookies()
#     chrome_browser.execute_script("localStorage.clear();")
#
#     logger.info("Завершение сессии браузера")
#     chrome_browser.quit()


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)