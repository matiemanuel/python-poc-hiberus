from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class TopBar(BasePage):
    BANNER_LINKS_INDEX = ["KNOW_US", "MARKETS", "CLIENTS", "JOB_OPPORTUNITIES", "BLOG", "CONTACT"]
    MAIN_MENU_LINKS = (By.CSS_SELECTOR, "#block-mainmenu li > a")

    def __init__(self, driver):
        super().__init__(driver)

    def go_to_markets_page(self):
        self.__click_link("MARKETS")

    def go_to_job_opportunities(self):
        self.__click_link("JOB_OPPORTUNITIES")

    def __click_link(self, option):
        links = self.driver.find_elements(*self.MAIN_MENU_LINKS)
        self.click_element(links[self.BANNER_LINKS_INDEX.index(option)])
