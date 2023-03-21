import time
from pages.test_pages import TestPage

class TestField:
    class TestFirstPage:
        def test_search(self, driver):
            test_main = TestPage(driver, 'https://piter-online.net')
            test_main.open()
            street = test_main.fill_adress_fields()
            time.sleep(1)
            test_main.clouse_pop_up()
            output_address_text = test_main.check_filled_adress()
            assert street in output_address_text
            count = 5
            while count != 0:
                test_main.push_random_tariff_button()
                output_text = test_main.fill_order_form()
                driver.back()
                time.sleep(3)
                count -= 1
                assert 'Ваша заявка на подключение принята в работу' in output_text



