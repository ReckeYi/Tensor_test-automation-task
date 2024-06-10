from pages.base_page import BasePage
from pages.locators.sbis_main_page_locators import SbisMainPageLocators


class SbisMainPage(BasePage):
    def open(self):
        self.driver.get("https://sbis.ru")

    def click_download_link(self):
        download_link = self.wait_for_element(*SbisMainPageLocators.DOWNLOAD_LINK)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", download_link)
        download_link.click()
