from selenium.webdriver.common.by import By


class SbisContactsPageLocators:
    TENSOR_BANNER = (By.XPATH, "//a[@href='https://tensor.ru/']")
    REGION_ELEMENT = (By.XPATH, '//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span')
    PARTNERS_LIST_ELEMENT = (By.XPATH, '//*[@id="contacts_list"]/div/div[2]')
    REGION_LIST = (By.CSS_SELECTOR, 'ul.sbis_ru-Region-Panel__list-l')
    REGION = '//*[@id="popup"]/div[2]/div/div/div/div/div[2]/div/ul/li/span/span[contains(text()'
    DETAILS = (By.XPATH, '//a[text()="Подробнее"]')
