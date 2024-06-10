import logging
import os

logger = logging.getLogger(__name__)

def check_file_downloaded(file_path):
    logger.info("Проверка существования скачанного файла")
    assert os.path.exists(file_path), "Скачанный файл не найден"