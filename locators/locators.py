from selenium.webdriver.common.by import By

class MainPageLocators:
    INPUT_STREET = (By.CSS_SELECTOR, 'input[datatest="main_input_street_home_new"]')
    INPUT_HOME = (By.CSS_SELECTOR, 'input[class="app141 app148 app147 app143 app160"]')
    CHOOSE_APARTMENT = (By.CSS_SELECTOR, '.app183 > div:nth-child(1) > ul:nth-child(1) > li:nth-child(1)')
    CHOOSE_HOUSE = (By.CSS_SELECTOR, '#forSelectField > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(3)')
    CHOOSE_OFFICE = (By.CSS_SELECTOR, '.app183 > div:nth-child(1) > ul:nth-child(1) > li:nth-child(2)')
    FIND_TO_HOME_BUTTON = (By.CSS_SELECTOR, 'div[class="app205 app237 app233 app228 app217 app234"]')
    CLOSE_POP_UP_BUTTON = (By.CSS_SELECTOR, 'div[datatest="close_popup1_from_quiz_input_tel"]')
    CHECK_TEXT_POP_UP = (By.CSS_SELECTOR, 'div[class="app570"]')
    CONNECT_TARIFF_BUTTON = (By.CSS_SELECTOR, 'div[datatest="providers_form_inspect_connect_tariff_button"]')
    CHECK_ADRESS_TEXT = (By.CSS_SELECTOR, 'span[itemprop="name"]')
    INPUT_NAME = (By.CSS_SELECTOR, 'input[datatest="providers_provider_order_input_name"]')
    INPUT_PHONE = (By.CSS_SELECTOR, 'input[datatest="providers_provider_order_input_tel"]')
    INPUT_CONNECT_BUTTON = (By.CSS_SELECTOR, 'div[data-test="order_form_input_connect_button"]')
    CHECK_TEXT_ORDER_POP_UP = (By.CSS_SELECTOR, 'div[class="col-md-9 col-lg-8"]')


