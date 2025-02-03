from behave import *  # Importing the Behave module for BDD (Behavior-Driven Development).
from selenium import webdriver  # Importing Selenium WebDriver for browser automation.
from pages.login_page import LoginPage  # Importing the LoginPage class from the 'pages' module.
from pages.project_page import ProjectPage  # Importing the ProjectPage class from the 'pages' module.
from pages.video_page import VideoPage  # Importing the VideoPage class from the 'pages' module.
from pages.logout_page import LogoutPage  # Importing the LogoutPage class from the 'pages' module.
import time  # Importing the time module to introduce delays between actions.
from selenium.webdriver.common.by import By  # Importing 'By' to locate elements.
from selenium.webdriver.support.ui import WebDriverWait  # Importing WebDriverWait to wait for elements.
from selenium.webdriver.support import expected_conditions as EC  # Importing expected conditions for element visibility.
import config  # Importing the config file for base URL and other configurations.
from pages.base_page import BasePage  # Importing the BasePage class to create reusable methods for page actions.

from dotenv import load_dotenv  # Importing dotenv to load environment variables from .env file.
import os  # Importing os module for environment variable handling.

# Load environment variables from the .env file
load_dotenv()

# Retrieve the PIN from the environment variables
pin = os.getenv("MY_PIN")

# Raise an error if the PIN is not found in the environment variables
if not pin:
    raise ValueError("PIN not found in .env file.")

# Step for navigating to the login page
@given('I am on the login page')
def step_impl(context):
    # Initialize the WebDriver (Chrome in this case)
    context.driver = webdriver.Chrome()  # Ensure chromedriver is set in PATH
    context.driver.get(config.BASE_URL)  # Open the login page URL.
    
    # Maximize the browser window for a consistent testing environment
    context.driver.maximize_window()

    # Initialize the LoginPage class for interaction with the login page
    context.login_page = LoginPage(context.driver)
    # Assert that the logo element is displayed to ensure the page is loaded properly
    assert context.login_page.get_logo_element().is_displayed()

# Step for logging in with a provided PIN
@when('I login with the provided PIN')
def step_impl(context):
    # Reinitialize the LoginPage class for the login action
    context.login_page = LoginPage(context.driver)
    # Call the login method from the LoginPage class and pass the PIN
    context.login_page.login(str(pin))
    # Initialize the ProjectPage class to interact with the project page after login
    context.project_page = ProjectPage(context.driver)
    # Assert that the project page is displayed after successful login
    assert context.project_page.get_project_page().is_displayed()

# Step for navigating to the Test Automation Project
@when('I navigate to the Test Automation Project')
def step_impl(context):
    # Reinitialize the ProjectPage class for navigation
    context.project_page = ProjectPage(context.driver)
    # Assert that the project page is displayed
    assert context.project_page.get_project_page().is_displayed()
    # Open the Test Automation Project from the ProjectPage
    context.project_page.open_test_automation_project()

# Step for switching to the 'Details' tab of the project
@when('I switch to the Details tab')
def step_impl(context):
    # Reinitialize the ProjectPage class for interacting with the project
    context.project_page = ProjectPage(context.driver)
    # Assert that the Details tab is displayed
    assert context.project_page.get_details_tab().is_displayed()
    # Switch to the Details tab
    context.project_page.switch_to_details_tab()
    # Wait for the page to load after switching tabs
    time.sleep(5)

# Step for returning to the 'Videos' tab of the project
@when('I return to the Videos tab')
def step_impl(context):
    # Reinitialize the ProjectPage class for interacting with the project
    context.project_page = ProjectPage(context.driver)
    # Assert that the Videos tab is displayed
    assert context.project_page.get_videos_tab().is_displayed()
    # Switch to the Videos tab
    context.project_page.switch_to_videos_tab()

# Step for playing the video
@when('I play the video')
def step_impl(context):
    # Initialize the VideoPage class to interact with the video player
    context.video_page = VideoPage(context.driver)
    # Call the play_video method from the VideoPage class to start the video
    context.video_page.play_video()
    # Wait for 10 seconds to allow the video to play for a brief period
    time.sleep(10)

# Step for pausing the video
@when('I pause the video')
def step_impl(context):
    # Initialize the VideoPage class and pause the video
    context.video_page = VideoPage(context.driver)
    context.video_page.pause_video()
    # Wait for 2 seconds before performing the next action
    time.sleep(2)

# Step for continuing the video from the pause state
@when('I continue watching the video')
def step_impl(context):
    # Initialize the VideoPage class and continue watching the video
    context.video_page = VideoPage(context.driver)
    context.video_page.continue_watching()

# Step for adjusting the volume to 50%
@when('I adjust the volume to 50%')
def step_impl(context):
    # Initialize the VideoPage class and adjust the volume
    context.video_page = VideoPage(context.driver)
    context.video_page.adjust_volume()

# Step for changing video resolution to 480p, then back to 720p
@when('I change the resolution to 480p and back to 720p')
def step_impl(context):
    # Initialize the VideoPage class and change the resolution
    context.video_page = VideoPage(context.driver)
    context.video_page.change_resolution('480p')
    # Wait for 2 seconds before switching resolution again
    time.sleep(2)
    # Change the resolution back to 720p
    context.video_page.change_resolution('720p')

# Step for pausing the video and navigating back
@when('I pause the video and navigate back')
def step_impl(context):
    # Initialize the VideoPage class, pause the video, and navigate back to the previous page
    context.video_page = VideoPage(context.driver)
    context.video_page.pause_video()
    context.video_page.navigate_back()
    # Assert that the project page is displayed after navigating back
    assert context.project_page.get_project_page().is_displayed()

# Step for logging out from the application
@when('I log out')
def step_impl(context):
    # Initialize the VideoPage class and call the logout method
    context.video_page = VideoPage(context.driver)
    context.video_page.logout()

# Step for verifying that the user is logged out successfully
@then('I should see the logout successful')
def step_impl(context):
    # Initialize the LogoutPage class and verify that the login page is visible again
    context.logout_page = LogoutPage(context.driver)
    context.logout_page.verify_login_page()
    # Close the browser after the verification is done
    context.logout_page.close_browser()
