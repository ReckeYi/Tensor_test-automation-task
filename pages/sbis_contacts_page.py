import logging
import allure
from selenium.webdriver.support.wait import WebDriverWait

from .base_page import BasePage
from .checkout_pages.check_sbis_contacts_page import *
from .locators.sbis_contacts_page_locators import SbisContactsPageLocators

logger = logging.getLogger(__name__)


class SbisContactsPage(BasePage):
    @allure.step("Открытие страницы https://sbis.ru/contacts")
    def open(self):
        logger.info("Открытие страницы https://sbis.ru/contacts")
        self.driver.get("https://sbis.ru/contacts")

    @allure.step("Клик по баннеру 'Тензор'")
    def click_tensor_banner(self):
        logger.info("Клик по баннеру 'Тензор'")
        banner = self.wait_for_element(*SbisContactsPageLocators.TENSOR_BANNER)
        check_element_displayed(banner, "Tensor banner is not displayed")
        banner.click()

    @allure.step("Проверка наличия элемента региона")
    def verify_region_element(self):
        logger.info("Проверка наличия элемента региона")
        region_element = self.wait_for_element(*SbisContactsPageLocators.REGION_ELEMENT)
        check_element_displayed(region_element, "Region element is not displayed")
        return region_element

    @allure.step("Получение текста списка партнеров")
    def get_partners_list_text(self):
        logger.info("Получение текста списка партнеров")
        partners_list_element = self.wait_for_element(*SbisContactsPageLocators.PARTNERS_LIST_ELEMENT)
        check_element_displayed(partners_list_element, "Partners list element is not displayed")
        return partners_list_element.text

    @allure.step("Клик по элементу региона")
    def click_region_element(self, region_element):
        logger.info("Клик по элементу региона")
        region_element.click()
        self.wait_for_element(*SbisContactsPageLocators.REGION_LIST)

    @allure.step("Выбор региона 'Камчатский край'")
    def select_kamchatka_region(self):
        logger.info("Выбор региона 'Камчатский край'")
        kamchatka_region = self.wait_for_element(*SbisContactsPageLocators.KAMCHATKA_REGION)
        kamchatka_region.click()

    @allure.step("Ожидание изменения текста списка партнеров")
    def wait_for_partners_list_to_change(self, initial_text):
        WebDriverWait(self.driver, 10).until(
            lambda driver: self.get_partners_list_text() != initial_text
        )

    @allure.step("Проверка измененного региона")
    def verify_changed_region(self):
        logger.info("Проверка измененного региона")
        changed_region = self.wait_for_element(*SbisContactsPageLocators.CHANGED_REGION)
        check_element_displayed(changed_region, "Changed region element is not displayed")
        return changed_region

    @allure.step("Проверка, что URL страницы содержит текст")
    def verify_url_contains(self, text):
        logger.info(f"Проверка, что URL страницы содержит текст: {text}")
        check_url_contains(self.driver, text, f"Expected '{text}' to be in URL")

    @allure.step("Проверка заголовка страницы")
    def verify_page_title(self, expected_title):
        logger.info(f"Проверка заголовка страницы: ожидаемый заголовок {expected_title}")
        check_page_title(self.driver, expected_title, f"Expected page title to be '{expected_title}'")
