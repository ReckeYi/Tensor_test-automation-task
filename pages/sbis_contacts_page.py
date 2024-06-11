import logging
import allure

from pages.base_page import BasePage
from pages.locators.sbis_contacts_page_locators import SbisContactsPageLocators
from tests.checkouts.check_sbis_contacts_page import check_element_displayed
from utilites.constants import *

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger(__name__)


class SbisContactsPage(BasePage):
    def open(self):
        logger.info("Открытие страницы Сбис Контакты")
        self.open_page(SBIS_CONTACTS)

    @allure.step("Клик по баннеру 'Тензор'")
    def click_tensor_banner(self):
        logger.info("Клик по баннеру 'Тензор'")
        banner = self.wait_for_element(*SbisContactsPageLocators.TENSOR_BANNER)
        check_element_displayed(banner, "Баннер 'Тензор' не отображается")
        banner.click()
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step("Получение элемента региона")
    def get_region_element(self):
        logger.debug("Получение элемента региона")
        return self.driver.find_element(*SbisContactsPageLocators.REGION_ELEMENT)

    @allure.step("Получение элемента списка партнеров")
    def get_partners_list_element(self):
        logger.debug("Получение элемента списка партнеров")
        return self.driver.find_element(*SbisContactsPageLocators.PARTNERS_LIST_ELEMENT)

    @allure.step("Клик по элементу региона")
    def click_region_element(self):
        logger.info("Клик по элементу региона")
        self.get_region_element().click()

    @allure.step("Выбор региона: {region_name}")
    def select_region(self, region_name):
        logger.info(f"Выбор региона: {region_name}")
        region_list = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(SbisContactsPageLocators.REGION_LIST)
        )

        region = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        f'{SbisContactsPageLocators.REGION}, "{region_name}")]'))
        )
        region.click()

    @allure.step("Получение измененного элемента региона")
    def get_changed_region_element(self):
        logger.debug("Получение измененного элемента региона")
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(SbisContactsPageLocators.REGION_ELEMENT)
        )

    @allure.step("Получение текущего URL")
    def get_current_url(self):
        logger.debug("Получение текущего URL")
        return self.driver.current_url

    @allure.step("Получение заголовка страницы")
    def get_title(self):
        logger.debug("Получение заголовка страницы")
        return self.driver.title

    @allure.step("Ожидание изменения списка партнеров")
    def wait_for_partners_list_to_change(self, partners_list_step1):
        logger.debug("Ожидание изменения списка партнеров")
        WebDriverWait(self.driver, 10).until(
            lambda driver: self.get_partners_list_element().text != partners_list_step1
        )

    @allure.step("Клик по ссылке 'Подробнее'")
    def click_detail_link(self):
        logger.info("Клик по ссылке 'Подробнее'")
        link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(SbisContactsPageLocators.DETAILS)
        )
        link.click()
