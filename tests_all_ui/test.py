from playwright.sync_api import Playwright, sync_playwright, expect
import pytest
#from playwright.async_api import Playwright, async_playwright


def test_run(playwright) -> None:
    # Assess
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)
    page.wait_for_load_state("networkidle")
    
    # Act
    page.get_by_role("button", name="Log In").click()
    page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_test_id("siteMembersDialogLayout").get_by_test_id("buttonElement").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").fill("symon.storozhenko@gmail.com")
    page.get_by_test_id("emailAuth").get_by_label("Email").press("Tab")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("test123")
    page.get_by_label("Password").press("Enter")
    page.click('[data-testid=\"submit"\"] [data-testid=\"buttonElement\"]')
    page.get_by_role("button", name="symon.storozhenko account menu").click()
    
    # Assertion
    assert page.is_visible("text = My Orders")

    # ---------------------
    context.close()
    browser.close()


#@pytest.mark.skip
