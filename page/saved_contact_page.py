from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class SavedContactPage(BaseAction):

    contact_title_feature = By.ID, "com.android.contacts:id/large_title"

    def get_contact_title_text(self):
        return self.find_element(self.contact_title_feature).text

