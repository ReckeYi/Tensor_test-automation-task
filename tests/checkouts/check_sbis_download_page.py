import logging
import os
import allure

logger = logging.getLogger(__name__)


@allure.step("Проверка ответа сервера")
def check_server_response(response):
    logger.info("Проверка ответа сервера")
    assert response.status_code == 200, f"Ошибка: {response.status_code}"


@allure.step("Проверка скачивания файла")
def check_file_downloaded(file_path):
    logger.info("Проверка скачивания файла")
    assert os.path.exists(file_path), "Скачанный файл не найден"


@allure.step("Проверка размера файла")
def check_file_size(expected_file_size, file_path):
    logger.info("Проверка размера файла")
    actual_file_size = os.path.getsize(file_path)
    assert actual_file_size == expected_file_size, f"Ожидаемый размер: {expected_file_size}, текущий размер: {actual_file_size}"
