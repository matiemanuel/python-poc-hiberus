from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.hiberus.top_bar_component import TopBar


class HomePage(BasePage):
    ALLOW_COOKIES_BUTTON = (By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll')
    MAIN_VIDEO = (By.ID, 'video-cabecera')

    def __init__(self, driver):
        super().__init__(driver)
        self.top_bar = TopBar(driver)

    def accept_cookies(self):
        self.click(*self.ALLOW_COOKIES_BUTTON)

    def is_main_video_displayed(self):
        return self.is_element_displayed(*self.MAIN_VIDEO)

    def get_top_bar(self):
        return self.top_bar
