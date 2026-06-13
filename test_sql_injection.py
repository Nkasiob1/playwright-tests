from playwright.sync_api import sync_playwright

def test_sql_injection():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.saucedemo.com")

        #enter SQL injection string in username field 
        page.fill("#user-name", "' OR '1'='1")
        page.fill("#password", "'OR '1'='1")

        #click the login button
        page.click("#login-button")

        #assert that login was rejected and error message appears
        error_message = page.locator("[data-test='error']").inner_text()
        assert "Epic sadface" in error_message
        print("TC-005 Passed: sql injection correctly rejected")
        
        browser.close()

test_sql_injection()        
