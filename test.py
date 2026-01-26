from playwright.sync_api import sync_playwright

URL = "https://www.dell.com/en-us/shop/dell-laptops/scr/laptops"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Load page
    page.goto(URL, timeout=60000)

    # Wait until product cards are loaded
    page.wait_for_selector("[data-stock-status]", timeout=80000)

    # Get all elements having data-stock-status
    elements = page.locator("[data-stock-status]")

    count = elements.count()
    print(f"Found {count} stock status entries:\n")

    for i in range(count):
        status = elements.nth(i).get_attribute("data-stock-status")
        print(status)

    browser.close()


