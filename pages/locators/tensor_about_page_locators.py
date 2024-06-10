# pages/locators/tensor_about_page_locators.py
from selenium.webdriver.common.by import By

class TensorAboutPageLocators:
    WORK_HEADER = (By.XPATH, '//*[@id="container"]/div[1]/div/div[4]/div[1]/h2')
    IMAGES = (By.XPATH, '//div[@class="s-Grid-col s-Grid-col--3 tensor_ru-About--col-md6 tensor_ru-About__block3--col-sm12"]//img')
