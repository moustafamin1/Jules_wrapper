from playwright.sync_api import sync_playwright

def verify_splash_screen():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Navigate to the local server
        page.goto("http://localhost:8080/index.html")

        # Check if the logo is present (splash screen)
        # The logo has class "logo"
        logo = page.locator(".logo")
        if logo.is_visible():
            print("Splash screen logo is visible.")
            # Take a screenshot of the splash screen
            page.screenshot(path="splash_screen.png")
        else:
            print("Splash screen logo NOT found.")

        # Check if the notification permission prompt is GONE
        # The old code had #notification-prompt
        prompt = page.locator("#notification-prompt")
        if not prompt.is_visible():
             print("Notification prompt is correctly removed.")
        else:
             print("Notification prompt is STILL VISIBLE (Error).")

        browser.close()

if __name__ == "__main__":
    verify_splash_screen()
