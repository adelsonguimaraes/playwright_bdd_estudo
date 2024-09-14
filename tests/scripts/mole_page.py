from playwright.sync_api import Page
from helpers.urls import URLS


class MolePage:
    def __init__(self, page: Page, expeted_poins=40):
        self.expeted_points = expeted_poins
        self.page = page

    def goto_page(self):
        self.page.goto(URLS['WHAC_MOLE'])

    def check_score(self):
        score = self.page.locator('h1.score > span')
        return int(score.inner_text()) == self.expeted_points

    def whac_at_target_score(self):
        while self.check_score() is not True:
            self.page.wait_for_timeout(1000)
            mole = self.page.locator('div > img.mole')
            if mole:
                mole.click()

    def assert_score(self):
        self.page.wait_for_timeout(1000)
        assert self.check_score(), 'not score valid'
