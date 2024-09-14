import pytest
from pytest_bdd import scenarios, given, when, then
from playwright.sync_api import Page, sync_playwright

scenarios('../features/google_search.feature')


@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        try:
            yield page
        finally:
            browser.close()


@given('in the google page')
def in_the_google_page(page: Page):
    page.goto('https://www.google.com.br')


@when('search to "Siena 2007"')
def search_to_siena_2007(page: Page):
    page.fill('textarea[name="q"]', 'siena 2007')


@when('press enter')
def press_enter(page: Page):
    page.press('textarea[name="q"]', 'Enter')


@then('show the text "Imagens"')
def show_the_text_images(page: Page):
    page.wait_for_timeout(2000)
    is_visible = page.is_visible('text=Imagens')
    assert is_visible, 'Not locate text'
