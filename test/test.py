from pages.test_pages import TestPage


class OneTest:
    class MainTest:
        def test_main(self, driver):
            test_main = TestPage(driver, 'https://piter-online.net')
            test_main.open()
            street, home = test_main.fill_adress_fields()
            test_main.clouse_pop_up()
            output_adress_text = test_main.check_filled_adress()
            assert street in output_adress_text
            assert home in output_adress_text
            #test.push_tarif_button()
            #test.fill_adress_fields()



