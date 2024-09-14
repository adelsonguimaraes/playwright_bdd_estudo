import pytest
from pytest_bdd import scenarios, given, when, then
from playwright.sync_api import Page
from helpers.utils import init_page
from scripts.mole_page import MolePage

scenarios('../features/whac_a_mole.feature')


@pytest.fixture
def page():
    yield from init_page()


# commom given
@given('in the Whac a mole page')
def in_the_whac_a_mole_page(page: Page):
    mole_page = MolePage(page)
    mole_page.goto_page()


# scenario 1
@when('hit in mole unitl 40 points')
def hit_in_mole_unitl_40_points(page: Page):
    mole_page = MolePage(page, 40)
    mole_page.whac_at_target_score()


@then('received 40 points')
def received_40_points(page: Page):
    mole_page = MolePage(page, 40)
    mole_page.assert_score()


# scenario 2
@when('hit in mole unitl 60 points')
def hit_in_mole_unitl_60_points(page: Page):
    mole_page = MolePage(page, 60)
    mole_page.whac_at_target_score()


@then('received 60 points')
def received_60_points(page: Page):
    mole_page = MolePage(page, 60)
    mole_page.assert_score()


# scenario 3
@when('hit in mole unitl 80 points')
def hit_in_mole_unitl_80_points(page: Page):
    mole_page = MolePage(page, 80)
    mole_page.whac_at_target_score()


@then('received 80 points')
def received_80_points(page: Page):
    mole_page = MolePage(page, 80)
    mole_page.assert_score()
