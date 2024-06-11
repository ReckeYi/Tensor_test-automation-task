import logging
import allure

from pages.base_page import BasePage
from pages.locators.sbis_main_page_locators import SbisMainPageLocators
from utilites.constants import SBIS

logger = logging.getLogger(__name__)


class SbisMainPage(BasePage):
    def open(self):
        logger.info("Открытие главной страницы Сбис")
        self.open_page(SBIS)

    @allure.step("Клик по ссылке 'Скачать локальные версии'")
    def click_download_link(self):
        logger.info("Клик по ссылке 'Скачать локальные версии'")
        download_link = self.wait_for_element(*SbisMainPageLocators.DOWNLOAD_LINK)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", download_link)
        download_link.click()
