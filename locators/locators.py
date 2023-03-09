from selenium.webdriver.common.by import By

class MainPageLocators:
    INPUT_STREET = (By.CSS_SELECTOR, 'input[class="app141 app148 app147 app143 app160 app142"]')
    INPUT_HOME = (By.CSS_SELECTOR, 'input[class="app141 app148 app147 app143 app160"]')
    CHOOSE_APARTMENT = (By.CSS_SELECTOR, '.app183 > div:nth-child(1) > ul:nth-child(1) > li:nth-child(1)')
    CHOOSE_HOUSE = (By.CSS_SELECTOR, '#forSelectField > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(3)')
    CHOOSE_OFFICE = (By.CSS_SELECTOR, '.app183 > div:nth-child(1) > ul:nth-child(1) > li:nth-child(2)')
    FIND_TO_HOME_BUTTON = (By.CSS_SELECTOR, 'div[class="app205 app237 app233 app228 app217 app234"]')

class PopUp1Locators:
    CLOSE_POP_UP_BUTTON = (By.CSS_SELECTOR, 'div[datatest="close_popup1_from_quiz_input_tel"]')

class TariffPageLocators:
    CONNECT_TARIFF_BUTTON = (By.CSS_SELECTOR, 'div[datatest="providers_form_inspect_connect_tariff_button"]')

class OrderFormLocators:
    INPUT_NAME = (By.CSS_SELECTOR, 'input[datatest="providers_provider_order_input_name"]')
    INPUT_PHONE = (By.CSS_SELECTOR, 'input[datatest="providers_provider_order_input_tel"]')
    INPUT_CONNECT_BUTTON = (By.CSS_SELECTOR, 'div[data-test="order_form_input_connect_button"]')

