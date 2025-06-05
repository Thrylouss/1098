from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class AuthPage:
    def __init__(self, driver):
        self.driver = driver
        self.login = (By.CSS_SELECTOR, "#app > div > div > div > div.log-in__content > form > label > input")
        self.next_btn = (By.CSS_SELECTOR, "#app > div > div > div > div.log-in__content > form > button")
        self.password = (By.CSS_SELECTOR, "#app > div > div > div > div.log-in__content > form > div > label > input")
        self.dropdown = (By.CSS_SELECTOR, "#dialog > div > div > div > div.material-dialog__window-body.material-dialog__window-body_modify > div > div:nth-child(2) > div > div")
        self.finish_btn = (By.CSS_SELECTOR, "#dialog > div > div > div > div.material-dialog__window-body.material-dialog__window-body_modify > div > div:nth-child(2) > div.drop-down-component__content > div.sessions__item-content > button")

    def enter_phone_number(self, phone):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.login)).send_keys(phone)

    def enter_password(self, password):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.password)).send_keys(password)

    def click_next_btn(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.next_btn)).click()

    def click_dropdown(self):
        wait = WebDriverWait(self.driver, 3)
        wait.until(EC.element_to_be_clickable(self.dropdown)).click()

    def click_finish_btn(self):
        wait = WebDriverWait(self.driver, 3)
        wait.until(EC.element_to_be_clickable(self.finish_btn)).click()