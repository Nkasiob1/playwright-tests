from playwright.sync_api import sync_playwright

def test_empty_password():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto("https://www.saucedemo.com")
        
        # enter a valid username and leave password empty
        page.fill("#user-name", "standard_user")
        page.fill("#password", "")
        
        page.click("#login-button")
        
        # assert that the error message is displayed
        error_message = page.locator("[data-test='error']").inner_text()
        assert "Password is required" in error_message
        print("TC-004 Passed: Empty password correctly rejected")
        
        browser.close()

test_empty_password()
