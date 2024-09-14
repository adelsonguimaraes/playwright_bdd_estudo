import pytest
from playwright.sync_api import Page, sync_playwright


@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Define headless=False para ver o navegador
        page = browser.new_page()
        try:
            yield page
        finally:
            browser.close()


def test_google_search(page: Page):
    # Acessa a página do Google
    page.goto('https://www.google.com.br')

    # Realiza a busca
    page.fill('textarea[name="q"]', 'siena 2007')
    page.press('textarea[name="q"]', 'Enter')

    # Verifica se o texto "Imagens" está visível na página
    page.wait_for_timeout(2000)
    is_visible = page.is_visible('text=Imagens')
    assert is_visible, 'Texto "Imagens" não está visível na página.'
