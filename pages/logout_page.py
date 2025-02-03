from selenium.webdriver.common.by import By  # Importing By to locate elements in the DOM
from pages.base_page import BasePage  # Importing the BasePage class that contains common methods
from selenium.common.exceptions import TimeoutException  # Importing TimeoutException to handle timeout errors

class LogoutPage(BasePage):
    def __init__(self, driver):
        """
        Initializes the LogoutPage object with WebDriver instance and locators for various elements.
        
        :param driver: Selenium WebDriver instance used for interacting with the web browser
        """
        super().__init__(driver)  # Initialize the parent class (BasePage) to inherit its functionality
        
        # Locator for the "Sign In" form element on the logout page
        self.login_form = (By.XPATH, "//div//span[text()='Sign In']")  # XPath to locate the "Sign In" text
        self.login_page = (By.ID, "sign-in-form")  # ID of the sign-in form to verify its presence

    def verify_login_page(self):
        """
        Verifies that the login page (sign-in form) is visible in the DOM.
        
        This method waits for the sign-in form to appear and confirms its visibility.
        """
        try:
            # Call the `wait_for_element` method from the BasePage to ensure the sign-in form is visible
            self.wait_for_element(By.ID, "sign-in-form")
            print("Sign-in form is visible in the DOM.")  # Log a success message when the element is visible
        except TimeoutException:
            # If the sign-in form is not found within the expected time, handle the exception and log an error
            print("Failed to find the sign-in form.")
            raise  # Re-raise the exception to ensure the failure is not silently ignored
        
        # Ensure the sign-in form is visible and confirm the login page has been reached
        if self.wait_for_element(*self.login_page):  # Wait for the login form element by ID
            print("Welcome to login page")  # Log a success message
        else:
            print("Could not redirect to login page")  # Log a failure message if the element is not found

    def close_browser(self):
        """
        Close the browser window explicitly when called.
        
        This method terminates the browser session by calling `quit()` on the WebDriver instance.
        """
        self.driver.quit()  # Quit the browser session to end the test or automation session
