import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://contentstudio.dell.com/itemv2/details?collectionid=b8b3e4b8-feb9-43b4-ac8b-4d2c82caf0a7&id=abda6eb4-a5ef-4b0a-93de-6cd413314919&collectionname=uberhomeglobalherobanneritem",timeout=500000000)
    page.get_by_role("button", name="More Options").click()
    page.get_by_role("listitem", name="My Stuff").click()
    page.get_by_role("listitem", name="Clipboard").click()
    page.get_by_role("link", name="My Stuff").click()
    page.wait_for_timeout(30000)
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)