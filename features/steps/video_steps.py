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
import config

from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Retrieve the PIN from the environment variables
pin = os.getenv("MY_PIN")

if not pin:
    raise ValueError("PIN not found in .env file.")

print(f"The PIN is: {pin}")

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

    # Wait for the logo element to be visible on the screen to confirm we are on the correct page
    wait = WebDriverWait(context.driver, 10)  # Timeout after 10 seconds
    logo = wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@id='form-logo-image']")))

    print("Logo is visible on the screen")  # Log that the logo is visible

    # Optional: Keep browser open for verification (remove in production)
    time.sleep(5)  # Wait for 5 seconds to manually verify the page before proceeding.

# Step for logging in with a provided PIN
@when('I login with the provided PIN')
def step_impl(context):
    # Call the login method from the LoginPage class and pass the PIN
    context.login_page.login(str(pin))
    # Wait for the Home icon to become visible, indicating successful login
    wait = WebDriverWait(context.driver, 10) 
    HomeIcon = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@aria-label='Home']")))
    time.sleep(5)  # Wait for the login process to complete (e.g., redirection).

# Step for navigating to the Test Automation Project
@when('I navigate to the Test Automation Project')
def step_impl(context):
    # Initialize the ProjectPage class and open the Test Automation Project page
    context.project_page = ProjectPage(context.driver)
    context.project_page.open_test_automation_project()

# Step for switching to the 'Details' tab of the project
@when('I switch to the Details tab')
def step_impl(context):
    # Switch to the 'Details' tab
    context.project_page.switch_to_details_tab()
    time.sleep(5)  # Wait for the page to load after switching tabs.

# Step for returning to the 'Videos' tab of the project
@when('I return to the Videos tab')
def step_impl(context):
    # Switch to the 'Videos' tab
    context.project_page.switch_to_videos_tab()

# Step for playing the video
@when('I play the video')
def step_impl(context):
    # Initialize the VideoPage class and play the video
    context.video_page = VideoPage(context.driver)
    context.video_page.play_video()
    time.sleep(10)  # Wait for 10 seconds to allow the video to play for a brief period.

# Step for pausing the video
@when('I pause the video')
def step_impl(context):
    # Initialize the VideoPage class and pause the video
    context.video_page = VideoPage(context.driver)
    context.video_page.pause_video()

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
    time.sleep(2)  # Wait for 2 seconds before switching resolution again
    context.video_page.change_resolution('720p')

# Step for pausing the video and navigating back
@when('I pause the video and navigate back')
def step_impl(context):
    # Initialize the VideoPage class, pause the video, and navigate back to the previous page
    context.video_page = VideoPage(context.driver)
    context.video_page.pause_video()
    context.video_page.navigate_back()

# Step for logging out from the application
@when('I log out')
def step_impl(context):
    # Initialize the VideoPage class and call the logout method
    context.video_page = VideoPage(context.driver)
    context.video_page.logout()
    time.sleep(3)  # Wait for the logout process to complete.

# Step for verifying that the user is logged out successfully
@then('I should see the logout successful')
def step_impl(context):
    # Initialize the LogoutPage class and verify that the login page is visible again
    context.logout_page = LogoutPage(context.driver)
    context.logout_page.verify_login_page()
    # Close the browser after the verification is done
    context.driver.quit()
