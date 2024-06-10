import logging
import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.locators.sbis_download_page_locators import SbisDownloadPageLocators

logger = logging.getLogger(__name__)


class SbisDownloadPage(BasePage):
    @allure.step("Клик по элементу 'СБИС Плагин'")
    def click_plugin_element(self):
        logger.info("Клик по элементу 'СБИС Плагин'")
        plugin_element = self.wait_for_element(*SbisDownloadPageLocators.PLUGIN_ELEMENT)
        self.mouse_click(plugin_element)

    @allure.step("Клик по кнопке 'Windows'")
    def click_windows_button(self):
        logger.info("Клик по кнопке 'Windows'")
        windows_button = self.wait_for_element(*SbisDownloadPageLocators.WINDOWS_BUTTON)
        self.mouse_click(windows_button)

    @allure.step("Проверка элемента Windows")
    def verify_windows_element(self):
        logger.info("Проверка элемента Windows")
        windows_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(SbisDownloadPageLocators.WINDOWS_ELEMENT)
        )
        assert windows_element.is_displayed()

    def mouse_click(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    def open(self):
        logger.info("Открытие страницы https://sbis.ru/download")
        self.driver.get("https://sbis.ru/download")
