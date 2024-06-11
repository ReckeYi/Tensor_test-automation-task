import requests
import tempfile

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.locators.sbis_download_page_locators import *
from tests.checkouts.check_sbis_download_page import *
from utilites.constants import *

logger = logging.getLogger(__name__)


class SBISDownloadPage(BasePage):

    @allure.step("Клик по элементу плагина")
    def click_plugin_element(self):
        logger.info("Клик по элементу плагина")
        plugin_element = self.driver.find_element(*SbisDownloadPageLocators.PLUGIN_ELEMENT)
        self.mouse_click(plugin_element)

    @allure.step("Скачивание файла")
    def download_file(self):
        logger.info("Скачивание файла по URL")
        response = requests.get(FILE_URL)
        check_server_response(response)

        temp_dir = tempfile.gettempdir()
        file_path = os.path.join(temp_dir, FILE_NAME)

        with open(file_path, 'wb') as f:
            f.write(response.content)

        check_file_downloaded(file_path)
        return file_path

    @allure.step("Проверка размера файла")
    def validate_file_size(self, file_path, expected_size):
        logger.info(f"Проверка размера файла: {file_path}")
        check_file_size(expected_size, file_path)

    @allure.step("Клик мышью по элементу")
    def mouse_click(self, element):
        logger.info("Выполнение клика мышью по элементу")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    @allure.step("Ожидание видимости элемента плагина")
    def wait_for_plugin_element(self):
        logger.info("Ожидание видимости элемента плагина")
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(SbisDownloadPageLocators.PLUGIN_ELEMENT)
        )
