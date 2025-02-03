from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException

class LogoutPage(BasePage):
    def __init__(self, driver):
        """
        Initializes the LogoutPage object with WebDriver instance and locators for various elements.
        
        :param driver: Selenium WebDriver instance
        """
        super().__init__(driver)  # Initialize the parent class (BasePage)
        
        # Locator for the "Sign In" form element on the logout page
        self.login_form = (By.XPATH, "//div//span[text()='Sign In']")  # Locator for the sign-in form

    def verify_login_page(self):
        """
        Verifies that the login page (sign-in form) is visible in the DOM.
        
        This method waits for the sign-in form to appear and confirms its visibility.
        """
        try:
            # Use wait_for_element from BasePage to ensure the sign-in form is visible
            self.wait_for_element(By.ID, "sign-in-form")
            print("Sign-in form is visible in the DOM.")
        except TimeoutException:
            # If the sign-in form is not found within the time limit, print an error message
            print("Failed to find the sign-in form.")
            raise  # Re-raise the exception so it doesn't silently fail

        # Ensure the sign-in form is present in the DOM and assert the condition
        assert len(self.driver.find_elements(By.ID, "sign-in-form")) > 0, "Sign-in form is not present in the DOM."

    def close_browser(self):
        """
        Close the browser window explicitly when called.
        
        This method terminates the browser session by calling `quit()` on the WebDriver instance.
        """
        self.driver.quit()  # Close the browser completely
