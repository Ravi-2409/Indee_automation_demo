''' 
project_page.py (Project Page Object)
This page handles actions related to navigating through projects, such as opening the project or switching tabs.
'''

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProjectPage(BasePage):
    def __init__(self, driver):
        """
        Initializes the ProjectPage object with WebDriver instance and locators for various elements.
        
        :param driver: Selenium WebDriver instance
        """
        super().__init__(driver)  # Initialize the parent class (BasePage)

        # Locators for various elements on the project page
        self.test_automation_title = (By.XPATH, "//div/h5[text()='Test automation project']")  # Locator for the "Test automation project" title

        self.details_tab = (By.ID, "detailsSection")  # Locator for the "Details" tab
        self.videos_tab = (By.ID, "videosSection")  # Locator for the "Videos" tab
        self.project_page = (By.XPATH, "//img[@alt='Test automation project']")

    def get_details_tab(self):
        return self.wait_for_element(*self.details_tab)
    
    def get_videos_tab(self):
        return self.wait_for_element(*self.videos_tab)

    def get_project_page(self):
        return self.wait_for_element(*self.project_page)
    
    def open_test_automation_project(self):
        """
        Open the 'Test Automation Project' page by scrolling to the element and clicking it.
        """
        # Scroll to the bottom of the page
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        # Find the 'Test automation project' title element on the page
        self.element = self.find_element(*self.test_automation_title)
        
        # Scroll the element into view
        self.driver.execute_script("arguments[0].scrollIntoView(true);", self.element)
        
        # Click on the 'Test automation project' title to open the project page
        self.click(*self.test_automation_title)

    def switch_to_details_tab(self):
        """
        Switch to the 'Details' tab by scrolling to the bottom of the page and clicking on the tab.
        """
        # Scroll to the bottom of the page
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        # Click on the 'Details' tab to switch to it
        self.click(*self.details_tab)

    def switch_to_videos_tab(self):
        """
        Switch to the 'Videos' tab by scrolling to the bottom of the page and clicking on the tab.
        """
        # Scroll to the bottom of the page
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        # Click on the 'Videos' tab to switch to it
        self.click(*self.videos_tab)
