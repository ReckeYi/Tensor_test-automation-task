import logging
import allure

logger = logging.getLogger(__name__)


@allure.step("Проверка, что элемент отображается")
def check_element_displayed(element, message="Element is not displayed"):
    logger.info("Проверка, что элемент отображается")
    assert element.is_displayed(), message

def checks_region_element_displayed(region_element):
    assert region_element.is_displayed(), "Region element is not displayed"

def checks_partners_list_element(partners_list_element):
    assert partners_list_element, "Partners list element is not found"

def checks_changed_region_displayed(changed_region):
    assert changed_region.is_displayed(), "Changed region element is not displayed"

def checks_current_url(current_url):
    assert "41-kamchatskij-kraj" in current_url, "Incorrect URL"

def checks_title(expected_title, actual_title):
    assert expected_title in actual_title, f"Expected title: '{expected_title}', Actual title: '{actual_title}'"

def checks_partners_list_updated(partners_list_step1, partners_list_step2):
    assert partners_list_step1 != partners_list_step2, "Partners list was not updated"