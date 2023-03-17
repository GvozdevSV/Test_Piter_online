import time
import requests
import pyautogui
from selenium.webdriver import Keys

from locators.locators import MainPageLocators
from pages.base_page import BasePage

class TestPage(BasePage):
    locators = MainPageLocators()


    def fill_adress_fields(self):
        street = 'Тестовая'
        home = '1'
        input_street = self.element_is_visible(self.locators.INPUT_STREET)
        input_street.send_keys(street)
        time.sleep(1)
        input_street.send_keys(Keys.RETURN)
        input_home = self.element_is_visible(self.locators.INPUT_HOME)
        input_home.send_keys(home)
        time.sleep(1)
        input_home.send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.CHOOSE_APARTMENT).click()
        self.element_is_visible(self.locators.FIND_TO_HOME_BUTTON).click()
        return str(street).lower()

    def clouse_pop_up(self):
        self.element_is_visible(self.locators.CLOSE_POP_UP_BUTTON).click()

    def check_filled_adress(self):
        output_address_text = self.elements_are_present(self.locators.CHECK_ADRESS_TEXT)
        data = []
        for item in output_address_text:
            self.go_to_element(item)
            data.append(item.text)
        return str(data).lower()

    def push_tarif_button(self):
        self.elements_are_visible(self.locators.CONNECT_TARIFF_BUTTON).click()

    def field_order_forn(self):
        name = 'Автотест'
        phone = '1111111111'
        self.element_is_visible(self.locators.INPUT_NAME).send_keys(name)
        self.element_is_visible(self.locators.INPUT_PHONE).send_keys(phone)
        self.elements_are_visible(self.locators.INPUT_CONNECT_BUTTON).click()






