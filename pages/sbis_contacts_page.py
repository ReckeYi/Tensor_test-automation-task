import logging
import allure
from selenium.webdriver.support.wait import WebDriverWait

from .base_page import BasePage
from .checkout_pages.check_sbis_contacts_page import *
from .locators.sbis_contacts_page_locators import SbisContactsPageLocators


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger(__name__)


class SbisContactsPage(BasePage):
    @allure.step("Открытие страницы https://sbis.ru/contacts")
    def open(self):
        logger.info("Открытие страницы https://sbis.ru/contacts")
        self.driver.get("https://sbis.ru/contacts")

    def click_tensor_banner(self):
        logger.info("Клик по баннеру 'Тензор'")
        banner = self.wait_for_element(*SbisContactsPageLocators.TENSOR_BANNER)
        check_element_displayed(banner, "Tensor banner is not displayed")
        banner.click()
        # Ждем, пока появится новая вкладка
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        # Переключаемся на новую вкладку
        self.driver.switch_to.window(self.driver.window_handles[1])

    def get_region_element(self):
        return self.driver.find_element(By.XPATH,
                                        '//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span')

    def get_partners_list_element(self):
        return self.driver.find_element(By.XPATH, '//*[@id="contacts_list"]/div/div[2]')

    def click_region_element(self):
        self.get_region_element().click()

    def select_region(self, region_name):
        region_list = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'ul.sbis_ru-Region-Panel__list-l'))
        )

        region = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        f'{SbisContactsPageLocators.REGION}, "{region_name}")]'))
        )
        region.click()

    def get_changed_region_element(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
                                              '//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span'))
        )

    def get_current_url(self):
        return self.driver.current_url

    def get_title(self):
        return self.driver.title

    def wait_for_partners_list_to_change(self, partners_list_step1):
        WebDriverWait(self.driver, 10).until(
            lambda driver: self.get_partners_list_element().text != partners_list_step1
        )

    @allure.step("Клик по ссылке 'Подробнее'")
    def click_detail_link(self):
        logger.info("Клик по ссылке 'Подробнее'")
        link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[text()="Подробнее"]'))
        )
        link.click()