# base_page.py (Base class for shared logic)
# This is the base page class that all page objects will inherit.
# It includes common functionality like waiting for elements, finding elements, and clicking actions.

from selenium.webdriver.common.by import By  # Importing 'By' to locate elements using different strategies.
from selenium.webdriver.support.ui import WebDriverWait  # Importing WebDriverWait to wait for elements to appear.
from selenium.webdriver.support import expected_conditions as EC  # Importing expected conditions for element interaction.
from selenium.webdriver.common.keys import Keys  # Importing Keys for keyboard interactions.
from selenium.webdriver.common.action_chains import ActionChains  # Importing ActionChains for complex user interactions.

class BasePage:
    def __init__(self, driver):
        """
        Initializes the BasePage object, which is inherited by other page objects.
        
        :param driver: The Selenium WebDriver instance used to interact with the browser.
        """
        self.driver = driver  # Store the driver reference to interact with the page elements.

    def wait_for_element(self, by, value, timeout=15):
        """
        Waits for an element to be clickable, which means it is both visible and enabled.

        :param by: The method to locate the element (e.g., By.ID, By.XPATH).
        :param value: The value to use with the 'by' locator (e.g., element ID or XPath).
        :param timeout: Time (in seconds) to wait for the element to become clickable (default is 10 seconds).
        :return: The WebElement that becomes clickable.
        """
        # Wait until the element is clickable using WebDriverWait
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((by, value))  # Check if the element is clickable.
        )

    def find_element(self, by, value):
        """
        Finds and returns a web element on the page.

        :param by: The method to locate the element (e.g., By.ID, By.XPATH).
        :param value: The value to use with the 'by' locator (e.g., element ID or XPath).
        :return: The WebElement object that matches the locator.
        """
        return self.driver.find_element(by, value)  # Return the WebElement matching the provided locator.

    def click(self, by, value):
        """
        Finds an element and clicks it.

        :param by: The method to locate the element (e.g., By.ID, By.XPATH).
        :param value: The value to use with the 'by' locator (e.g., element ID or XPath).
        """
        # Wait for the element to become clickable and then click on it
        self.wait_for_element(by, value).click()  # Click the element once it is clickable.

    def send_keys(self, by, value, keys):
        """
        Finds an element, clears it (if needed), and sends the specified keys to it.

        :param by: The method to locate the element (e.g., By.ID, By.XPATH).
        :param value: The value to use with the 'by' locator (e.g., element ID or XPath).
        :param keys: The keys or text to be sent to the element.
        """
        # Locate the element using the provided 'by' and 'value'
        element = self.find_element(by, value)
        element.clear()  # Clear the text input field before sending keys (if it is a text field)
        element.send_keys(keys)  # Send the provided keys or text to the element.
