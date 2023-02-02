from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class WorkWithUsPage(BasePage):
    JOIN_FORM = (By.ID, "contact-message-new-form-talento-form")

    def __init__(self, driver):
        super().__init__(driver)

    def is_join_formulary_displayed(self):
        self.is_element_displayed(*self.JOIN_FORM)
