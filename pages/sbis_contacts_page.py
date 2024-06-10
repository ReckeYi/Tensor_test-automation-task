import logging
import allure
from selenium.webdriver.support.wait import WebDriverWait

from .base_page import BasePage
from .locators.sbis_contacts_page_locators import SbisContactsPageLocators

logger = logging.getLogger(__name__)

class SbisContactsPage(BasePage):
    @allure.step("Открытие страницы https://sbis.ru/contacts")
    def open(self):
        logger.info("Открытие страницы https://sbis.ru/contacts")
        self.driver.get("https://sbis.ru/contacts")

    @allure.step("Клик по баннеру 'Tensor'")
    def click_tensor_banner(self):
        logger.info("Клик по баннеру 'Tensor'")
        banner = self.wait_for_element(*SbisContactsPageLocators.TENSOR_BANNER)
        assert banner.is_displayed()
        banner.click()

    @allure.step("Проверка наличия элемента региона")
    def verify_region_element(self):
        logger.info("Проверка наличия элемента региона")
        region_element = self.wait_for_element(*SbisContactsPageLocators.REGION_ELEMENT)
        assert region_element.is_displayed()
        return region_element

    @allure.step("Получение текста списка партнеров")
    def get_partners_list_text(self):
        logger.info("Получение текста списка партнеров")
        partners_list_element = self.wait_for_element(*SbisContactsPageLocators.PARTNERS_LIST_ELEMENT)
        assert partners_list_element
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

    def wait_for_partners_list_to_change(self, initial_text):
        WebDriverWait(self.driver, 10).until(
            lambda driver: self.get_partners_list_text() != initial_text
        )

    @allure.step("Проверка измененного региона")
    def verify_changed_region(self):
        logger.info("Проверка измененного региона")
        changed_region = self.wait_for_element(*SbisContactsPageLocators.CHANGED_REGION)
        assert changed_region.is_displayed()
        return changed_region

    @allure.step("Проверка, что URL страницы содержит текст")
    def verify_url_contains(self, text):
        logger.info(f"Проверка, что URL страницы содержит текст: {text}")
        current_url = self.driver.current_url
        assert text in current_url

    @allure.step("Проверка заголовка страницы")
    def verify_page_title(self, expected_title):
        logger.info(f"Проверка заголовка страницы: ожидаемый заголовок {expected_title}")
        actual_title = self.driver.title
        assert expected_title in actual_title
