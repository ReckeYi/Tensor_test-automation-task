from selenium.webdriver.common.by import By


class TensorMainPageLocators:
    SLOGAN_ELEMENT = (By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[1]')
    DETAIL_LINK = (By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a[text()="Подробнее"]')
