import logging
import allure
from pages.base_page import BasePage
from pages.locators.sbis_main_page_locators import SbisMainPageLocators

logger = logging.getLogger(__name__)


class SbisMainPage(BasePage):
    @allure.step("Открытие главной страницы https://sbis.ru")
    def open(self):
        logger.info("Открытие главной страницы https://sbis.ru")
        self.driver.get("https://sbis.ru")

    @allure.step("Клик по ссылке 'Скачать локальные версии'")
    def click_download_link(self):
        logger.info("Клик по ссылке 'Скачать локальные версии'")
        download_link = self.wait_for_element(*SbisMainPageLocators.DOWNLOAD_LINK)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", download_link)
        download_link.click()
