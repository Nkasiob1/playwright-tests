from playwright.sync_api import sync_playwright

def test_invalid_password():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto("https://www.saucedemo.com")
        
        page.fill("#user-name", "standard_user")
        page.fill("#password", "wrong_password")
        
        page.click("#login-button")
        
        error_message = page.locator("[data-test='error']").inner_text()
        assert "Epic sadface" in error_message
        print("TC-002 PASSED: Invalid password correctly rejected")
        
        browser.close()

test_invalid_password()
