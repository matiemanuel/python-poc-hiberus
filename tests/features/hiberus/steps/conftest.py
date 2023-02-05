import json
import os

import selenium.webdriver

# Constants

HOMEPAGE_URL = 'https://www.hiberus.com'
ROOT_DIR = os.path.dirname(os.path.abspath('.gitignore'))
CONFIG_FILEPATH = os.path.join(ROOT_DIR, 'config.json')


# Util methods

def config_browser():
    with open(CONFIG_FILEPATH) as config_file:
        config = json.load(config_file)

    browser = config['browser']
    headless = config['headless']
    implicit_time = config['implicit_wait']
    run_remotely = config['run_remotely']
    command_executor = config['command_executor']

    if browser.lower() == 'firefox':
        firefox_options = selenium.webdriver.FirefoxOptions()
        firefox_options.add_argument('--private')
        if headless:
            firefox_options.add_argument('--headless')
        if run_remotely:
            b = selenium.webdriver.Remote(command_executor=command_executor, options=firefox_options)
        else:
            b = selenium.webdriver.Firefox(options=firefox_options)

    elif browser.lower() == 'chrome':
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument('incognito')
        opts.add_argument('no-sandbox')
        opts.add_argument('disable-dev-shm-usage')
        opts.add_argument('disable-gpu')
        opts.add_argument('window-size=1920,1080')
        if headless:
            opts.add_argument('headless')
        if run_remotely:
            b = selenium.webdriver.Remote(command_executor=command_executor, options=opts)
        else:
            b = selenium.webdriver.Chrome(options=opts)
    else:
        raise Exception(f"Browser {browser} is not supported")
    b.implicitly_wait(implicit_time)
    b.maximize_window()
    return b
