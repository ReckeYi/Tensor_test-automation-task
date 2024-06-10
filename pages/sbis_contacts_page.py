from .base_page import BasePage
from .locators.sbis_contacts_page_locators import SbisContactsPageLocators


class SbisContactsPage(BasePage):
    def open(self):
        self.driver.get("https://sbis.ru/contacts")

    def click_tensor_banner(self):
        banner = self.wait_for_element(*SbisContactsPageLocators.TENSOR_BANNER)
        assert banner.is_displayed()
        banner.click()

    def verify_region_element(self):
        region_element = self.wait_for_element(*SbisContactsPageLocators.REGION_ELEMENT)
        assert region_element.is_displayed()
        return region_element

    def get_partners_list_text(self):
        partners_list_element = self.wait_for_element(*SbisContactsPageLocators.PARTNERS_LIST_ELEMENT)
        assert partners_list_element
        return partners_list_element.text

    def click_region_element(self, region_element):
        region_element.click()
        self.wait_for_element(*SbisContactsPageLocators.REGION_LIST)

    def select_kamchatka_region(self):
        kamchatka_region = self.wait_for_element(*SbisContactsPageLocators.KAMCHATKA_REGION)
        kamchatka_region.click()

    def verify_changed_region(self):
        changed_region = self.wait_for_element(*SbisContactsPageLocators.CHANGED_REGION)
        assert changed_region.is_displayed()
        return changed_region

    def verify_url_contains(self, text):
        current_url = self.driver.current_url
        assert text in current_url

    def verify_page_title(self, expected_title):
        actual_title = self.driver.title
        assert expected_title in actual_title
