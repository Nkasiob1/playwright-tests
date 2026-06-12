from playwright.sync_api import sync_playwright 

def test_empty_username():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page =browser.new_page()

        #navigate to login page 
        page.goto("https://www.saucedemo.com")

        # leave user name field empty and enter vaild password 
        page.fill("#user-name", "")
        page.fill("#password","secret_sauce")

        #click the login button 
        page.click("#login-button")

        #assert that the error message displayed 
        error_message = page.locator("[data-test='error']").inner_text()
        assert "Username is required" in error_message 
        print("TC-003 Passed: Empty username correctly rejected")


        browser.close()

test_empty_username()


                  
            
