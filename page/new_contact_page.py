from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class NewContactPage(BaseAction):

    name_edit_text = By.XPATH, "//*[@text='姓名']"
    phone_edit_text = By.XPATH, "//*[@text='电话']"

    def input_name(self, text):
        self.input(self.name_edit_text, text)

    def input_phone(self, text):
        self.input(self.phone_edit_text, text)

