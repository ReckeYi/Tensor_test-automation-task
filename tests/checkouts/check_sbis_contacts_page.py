import logging
import allure

logger = logging.getLogger(__name__)


@allure.step("Проверка, что элемент отображается")
def check_element_displayed(element, message="Элемент не отображается"):
    logger.info("Проверка, что элемент отображается")
    assert element.is_displayed(), message


@allure.step("Проверка, что регион отображается")
def checks_region_element_displayed(region_element):
    logger.info("Проверка, что регион отображается")
    assert region_element.is_displayed(), "Элемент региона не отображается"


@allure.step("Проверка, что элемент списка партнеров отображается")
def checks_partners_list_element(partners_list_element):
    logger.info("Проверка, что элемент списка партнеров отображается")
    assert partners_list_element, "Элемент списка партнеров не найден"


@allure.step("Проверка, что измененный регион отображается")
def checks_changed_region_displayed(changed_region):
    logger.info("Проверка, что измененный регион отображается")
    assert changed_region.is_displayed(), "Измененный элемент региона не отображается"


@allure.step("Проверка текущего URL")
def checks_current_url(current_url):
    logger.info("Проверка текущего URL")
    assert "41-kamchatskij-kraj" in current_url, "Неправильный URL"


@allure.step("Проверка заголовка")
def checks_title(expected_title, actual_title):
    logger.info("Проверка заголовка")
    assert expected_title in actual_title, f"Ожидаемый заголовок: '{expected_title}', Фактический заголовок: '{actual_title}'"


@allure.step("Проверка обновления списка партнеров")
def checks_partners_list_updated(partners_list_step1, partners_list_step2):
    logger.info("Проверка обновления списка партнеров")
    assert partners_list_step1 != partners_list_step2, "Список партнеров не был обновлен"
