from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.locators.sbis_download_page_locators import SbisDownloadPageLocators


class SbisDownloadPage(BasePage):
    def mouse_click(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    def open(self):
        self.driver.get("https://sbis.ru/download")

    def click_plugin_element(self):
        plugin_element = self.wait_for_element(*SbisDownloadPageLocators.PLUGIN_ELEMENT)
        self.mouse_click(plugin_element)

    def click_windows_button(self):
        windows_button = self.wait_for_element(*SbisDownloadPageLocators.WINDOWS_BUTTON)
        self.mouse_click(windows_button)

    def verify_windows_element(self):
        windows_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(SbisDownloadPageLocators.WINDOWS_ELEMENT)
        )
        assert windows_element.is_displayed()
