from playwright.sync_api import sync_playwright


def init_page():
    print('rodou mesmo')
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        try:
            yield page
        finally:
            browser.close()
