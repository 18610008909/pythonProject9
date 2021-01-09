from time import sleep

import allure
import pytest


from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page



class TestContact:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        sleep(3)
        self.driver.quit()


    @pytest.mark.parametrize("args", analyze_file('test_contact'))
    def test_contact(self, args):
        name = args['name']
        phone = args['phone']
        # print(name, phone)
        self.page.contact_list_page.click_add_contact_button()
        allure.attach("姓名", name)
        self.page.new_contact_page.input_name(name)
        allure.attach("截图", self.driver.get_screenshot_as_png(), allure.attach_type.PNG)
        self.page.new_contact_page.input_phone(phone)
        self.page.new_contact_page.press_back()
        assert name == self.page.saved_contact_page.get_contact_title_text()