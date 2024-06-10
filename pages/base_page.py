import logging
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger(__name__)


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Поиск элемента")
    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    @allure.step("Поиск элементов")
    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    @allure.step("Ожидание появления элемента")
    def wait_for_element(self, *locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
