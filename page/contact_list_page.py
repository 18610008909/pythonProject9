import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class ContactListPage(BaseAction):

    add_contact_button = By.ID, "com.android.contacts:id/floating_action_button"

    @allure.step(title='点击按钮')
    def click_add_contact_button(self):
        self.click(self.add_contact_button)