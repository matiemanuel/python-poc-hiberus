from tests.features.hiberus.steps.conftest import config_browser


def before_scenario(context, scenario):
    context.driver = config_browser()


def after_scenario(context, scenario):
    context.driver.quit()
