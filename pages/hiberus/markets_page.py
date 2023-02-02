from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MarketsPage(BasePage):
    RECEIVE_INFORMATION_FORM = (By.ID, "contact-message-new-form-form")

    def __init__(self, driver):
        super().__init__(driver)

    def is_receive_information_form_displayed(self):
        self.is_element_displayed(*self.RECEIVE_INFORMATION_FORM)
