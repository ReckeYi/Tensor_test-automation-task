import logging
import os
import allure

logger = logging.getLogger(__name__)


@allure.step("Проверка существования скачанного файла")
def check_file_downloaded(file_path):
    logger.info("Проверка существования скачанного файла")
    assert os.path.exists(file_path), "Скачанный файл не найден"
