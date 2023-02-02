from assertpy import assert_that
from behave import given, when, then

from conftest import config_browser, HOMEPAGE_URL
from pages.hiberus.home_page import HomePage
from pages.hiberus.markets_page import MarketsPage
from pages.hiberus.work_with_us_page import WorkWithUsPage


@given('launch a new browser')
def launch_browser(context):
    context.driver = config_browser()


@given('Hiberus homepage is displayed')
def open_hiberus_homepage(context):
    context.driver.get(HOMEPAGE_URL)
    home_page = HomePage(context.driver)
    assert_that(home_page.is_main_video_displayed()).is_true()
    context.home_page = home_page


@when('the user accepts page cookies')
def user_accepts_page_cookies(context):
    context.home_page.accept_cookies()


@when('the user clicks on "{link}" link from the top bar')
def user_clicks_on_job_opportunities_link(context, link):
    top_bar = context.home_page.get_top_bar()
    if link.lower() == "mercados":
        top_bar.go_to_markets_page()
    elif link.lower() == "trabaja en hiberus":
        top_bar.go_to_job_opportunities()
    else:
        raise Exception(f"Option {link} not implemented")


@then('the hiberus market page is displayed')
def job_opportunities_page_is_displayed(context):
    MarketsPage(context.driver).is_receive_information_form_displayed()
    assert_that(context.driver.title).contains_ignoring_case('Soluciones Tecnológicas para todos los sectores')
    assert_that(context.driver.current_url).contains("/soluciones-tecnologicas-por-mercados")


@then('the hiberus job opportunities page is displayed')
def job_opportunities_page_is_displayed(context):
    WorkWithUsPage(context.driver).is_join_formulary_displayed()
    assert_that(context.driver.title).contains_ignoring_case('Por qué trabajar en Hiberus')
    assert_that(context.driver.current_url).contains("/trabaja-con-nosotros")


@then('browser is closed')
def quit_browser(context):
    context.driver.quit()
