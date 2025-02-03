from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Retrieve the PIN from the environment variables
pin = os.getenv("MY_PIN")

if not pin:
    raise ValueError("PIN not found in .env file.")

print(f"The PIN is: {pin}")


class LoginPage(BasePage):
    def __init__(self, driver):
        """
        Initializes the LoginPage object with WebDriver instance and locators for elements on the login page.
        
        :param driver: Selenium WebDriver instance to interact with the browser.
        """
        super().__init__(driver)  # Initialize the parent class (BasePage)

        # Locator for the input field where users enter their PIN
        self.pin_input = (By.ID, "access-code")
        
        # Locator for the "Sign In" button on the login page
        self.login_button = (By.XPATH, "//div//span[text()='Sign In']")

    def login(self, pin):
        """
        Performs the login action by entering the PIN and clicking the login button.

        :param pin: The PIN to be entered into the PIN input field.
        """
        # Use the inherited send_keys method from BasePage to type the provided PIN into the PIN input field
        self.send_keys(*self.pin_input, pin)
        
        # Use the inherited click method from BasePage to click the "Sign In" button to complete login
        self.click(*self.login_button)
