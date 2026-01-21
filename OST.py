from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://ost.dell.com/OST/UI/Home.aspx")
        field = page.wait_for_selector('[id="ctl00_topHeaderControl_tbContrHeader_tbpnlPgSetting_txtbxRCSearch"]')
        field.fill("RC1277374")
        go_button = page.query_selector('[id="ctl00_topHeaderControl_tbContrHeader_tbpnlPgSetting_imgbtnGo"]')
        go_button.click()
        prev_button = page.wait_for_selector('[id="ctl00_topHeaderControl_tbContrHeader_tbpnlPgSetting_imgbtnPgPrvw"]')
        prev_button.click()
        page.query_selector('[id="ctl00_topHeaderControl_tbContrHeader_tbpnlPgSetting_imgbtnPgPrevw"]').click()
        print("Press Enter to exit....")
        input()
        context.close()
        browser.close()

if __name__ == "__main__":
    main()