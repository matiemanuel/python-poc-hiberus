import json

import selenium.webdriver

# Constants

HOMEPAGE_URL = 'https://www.hiberus.com'


# Util methods

def config_browser():
    with open('config.json') as config_file:
        config = json.load(config_file)

    browser = config['browser']
    headless = config['headless']
    implicit_time = config['implicit_wait']

    if browser == 'Firefox':
        firefox_options = selenium.webdriver.FirefoxOptions()
        firefox_options.add_argument('--private')
        if headless:
            firefox_options.add_argument('--headless')
        b = selenium.webdriver.Firefox(options=firefox_options)

    elif browser == 'Chrome':
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument('incognito')
        if headless:
            opts.add_argument('headless')
        b = selenium.webdriver.Chrome(options=opts)
    else:
        raise Exception(f"Browser {browser} is not supported")
    b.implicitly_wait(implicit_time)
    b.maximize_window()
    return b
