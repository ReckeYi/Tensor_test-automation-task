import logging
import allure

logger = logging.getLogger(__name__)


@allure.step("Проверка, что элемент отображается")
def check_element_displayed(element, message="Element is not displayed"):
    logger.info("Проверка, что элемент отображается")
    assert element.is_displayed(), message


@allure.step("Проверка, что URL страницы содержит текст")
def check_url_contains(driver, text, message="URL does not contain expected text"):
    current_url = driver.current_url
    logger.info(f"Проверка, что URL страницы содержит текст: {text}. Текущий URL: {current_url}")
    assert text in current_url, f"{message}. Current URL: {current_url}"
    logger.info("URL страницы содержит ожидаемый текст")


@allure.step("Проверка заголовка страницы")
def check_page_title(driver, expected_title, message="Page title does not match"):
    actual_title = driver.title
    logger.info(
        f"Проверка заголовка страницы. Ожидаемый заголовок: {expected_title}, фактический заголовок: {actual_title}")
    assert expected_title in actual_title, f"{message}. Actual title: {actual_title}"
    logger.info("Заголовок страницы соответствует ожидаемому")


@allure.step("Проверка, что текст элемента изменился")
def check_text_changed(element, initial_text, message="Element text did not change"):
    current_text = element.text
    logger.info(
        f"Проверка, что текст элемента изменился. Начальный текст: {initial_text}, текущий текст: {current_text}")
    assert current_text != initial_text, f"{message}. Current text: {current_text}"
    logger.info("Текст элемента изменился корректно")


@allure.step("Проверка изменения списка партнеров")
def check_partners_list_changed(partners_list_step1, partners_list_step2):
    logger.info("Сравнение списка партнеров после изменения региона")
    assert partners_list_step1 != partners_list_step2, "Список партнеров не изменился после выбора региона"
    logger.info("Список партнеров успешно изменился после выбора региона")
