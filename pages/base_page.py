from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    def is_element_displayed(self, by, query):
        element = self.driver.find_element(by, query)
        return element.is_displayed()

    def click(self, by, query):
        element = self.wait.until(EC.element_to_be_clickable((by, query)))
        element.click()

    def click_element(self, web_element):
        element = self.wait.until(EC.element_to_be_clickable(web_element))
        element.click()

    def get_page_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url
