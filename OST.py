import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://ost.dell.com/OST/UI/Home.aspx")
    page.locator("#ctl00_topHeaderControl_tbContrHeader_tbpnlPgSetting_txtbxRCSearch").click()
    page.locator("#ctl00_topHeaderControl_tbContrHeader_tbpnlPgSetting_txtbxRCSearch").fill("RC1277374")
    page.locator("#ctl00_topHeaderControl_tbContrHeader_tbpnlPgSetting_txtbxRCSearch").press("Enter")
    page.get_by_role("button", name="Page Preview").click()
    with page.expect_popup() as page1_info:
        page.get_by_role("button", name="Preview", exact=True).click()
    # page1 = page1_info.value
    page.get_by_role("menuitem", name="Monitors & Monitor Accessories").click()

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)