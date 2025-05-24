from playwright.sync_api import sync_playwright

def test_wiki_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.wikipedia.org/")
        page.pause()

        search_button = page.locator('xpath=//*[@id="search-form"]/fieldset/button')
        search_button.wait_for()
        page.pause()

        native_language_button = page.locator('xpath=//*[@id="js-lang-list-button"]')
        native_language_button.wait_for()
        page.pause()

        footer_google_play_button = page.locator('xpath=//*[@id="www-wikipedia-org"]/footer/div[2]/div/div/ul/li[1]/a/span')
        footer_google_play_button.wait_for()
        page.pause()

        search_input = page.locator('xpath=//*[@id="searchInput"]')
        search_input.wait_for()
        page.pause()

        browser.close()
