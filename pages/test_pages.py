import time
import requests
import pyautogui
from locators.locators import MainPageLocators, PopUp1Locators, TariffPageLocators, OrderFormLocators
from pages.base_page import BasePage

class TestPage(BasePage):
    locators = MainPageLocators()
    locators = PopUp1Locators()
    locators = TariffPageLocators()
    locators = OrderFormLocators()

    def fill_adress_fields(self):
        street = 'Тестовая линия'
        home = '1'
        self.element_is_visible(self.locators.INPUT_STREET).send_keys(street)
        pyautogui.press("Enter")
        self.element_is_visible(self.locators.INPUT_HOME).send_keys(home)
        self.element_is_visible(self.locators.CHOOSE_APARTMENT).click()
        self.element_is_visible(self.locators.FIND_TO_HOME_BUTTON).click()
        return street, home

    def clouse_pop_up(self):
        self.element_is_visible(self.locators.CLOSE_POP_UP_BUTTON).click()

    def check_filled_adress(self):
        output_adress_text = self.element_is_visible(self.locators.CHECK_ADRESS_TEXT).text
        return output_adress_text

    def push_tarif_button(self):
        self.elements_are_visible(self.locators.CONNECT_TARIFF_BUTTON).click()


    def field_order_forn(self):
        name = 'Автотест'
        phone = '1111111111'
        self.element_is_visible(self.locators.INPUT_NAME).send_keys(name)
        self.element_is_visible(self.locators.INPUT_PHONE).send_keys(phone)
        self.elements_are_visible(self.locators.INPUT_CONNECT_BUTTON).click()






