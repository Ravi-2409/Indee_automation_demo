from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from pages.project_page import ProjectPage
import time

class VideoPage(BasePage):
    def __init__(self, driver):
        """
        Initializes the VideoPage object with WebDriver instance and locators for various elements.
        
        :param driver: Selenium WebDriver instance
        """
        super().__init__(driver)  # Initialize the parent class (BasePage)
        
        # Locators for various video controls and elements on the page
        self.all_titles = (By.XPATH,"//p[text()=' All Titles ']")
        self.play_button = (By.XPATH, "//button[@aria-label='Play Video']")  # Locator for play button
        self.video_element = (By.XPATH, "//video[@class='jw-video jw-reset']")  # Locator for video element
        self.project_page = (By.XPATH, "//img[@alt='Test automation project']")
        self.continue_watching_button = (By.XPATH, "//button[@aria-label='Continue Watching']")  # Locator for 'Continue Watching' button
        self.volume_slider = (By.XPATH, "//div[@aria-label='Mute button'] | //div[@aria-label='Unmute button']")  # Locator for volume control (mute/unmute)
        self.settings_menu = (By.XPATH, "//div[@aria-label='Settings']")  # Locator for settings menu
        self.resolution_480p = (By.XPATH, "//button[@class='jw-reset-text jw-settings-content-item' and text()='480p']")  # Locator for 480p resolution option
        self.resolution_720p = (By.XPATH, "//button[@class='jw-reset-text jw-settings-content-item' and text()='720p']")  # Locator for 720p resolution option
        self.pause_button = (By.XPATH, "//div[@class='jw-icon jw-icon-inline jw-button-color jw-reset jw-icon-playback' and @aria-label='Play'] | //div[@class='jw-icon jw-icon-inline jw-button-color jw-reset jw-icon-playback' and @aria-label='Pause']")  # Locator for play/pause button
        self.back_button = (By.XPATH, "//div/button[@aria-label='Go Back and continue playing video']")  # Locator for back button
        self.logout_button = (By.ID, "signOutSideBar")  # Locator for logout button

    def get_logout_button(self):
        """
        Waits for the logout button to be visible on the page.
        """
        self.wait_for_element(*self.logout_button)  # Wait for the logout button element to be visible

    def play_video(self):
        """
        Click the play button to start video playback if the play button is visible.
        """
        self.wait_for_element(*self.play_button)  # Wait until play button is visible
        self.click(*self.play_button)  # Click the play button to start the video
        time.sleep(2)  # Sleep for 2 seconds after clicking the play button
    
    def navigate_to_all_titles(self):
        """
        Scrolls the 'All Titles' element into view.
        """
        # Wait for the 'All Titles' element to be present
        self.wait_for_element(*self.all_titles)
        
        # Scroll the 'All Titles' element into view
        self.driver.execute_script("arguments[0].scrollIntoView();", self.find_element(*self.all_titles))
        
        # Optionally, you can log or print that the element is now in view.
        print("'All Titles' element has been scrolled into view.")

    def switch_to_video_iframe(self):
        """
        Switch to the video iframe if the video player is inside an iframe.
        Handles iframe switching for video controls interaction.
        """
        try:
            # Wait for the iframe to be present in the DOM and switch to it
            self.wait_for_element(By.ID, "video_player")  # Wait for iframe to be present
            iframe = self.find_element(By.ID, "video_player")  # Find the iframe element
            self.driver.switch_to.frame(iframe)  # Switch to the iframe containing the video player
            print("Switched to video iframe successfully.")
        except Exception as e:
            print(f"Error switching to iframe: {e}")  # Log error if iframe switch fails

    def hover_over_video(self):
        """
        Hover over the video player to make video controls visible (like play/pause buttons, volume slider).
        """
        # Wait for video player container to be present before hovering
        video_player_container = self.wait_for_element(By.ID, "media-player")
        
        # Create ActionChains object to simulate mouse movements and hover over the video player
        actions = ActionChains(self.driver)
        
        # Hover over the video player container to trigger floating buttons and controls
        actions.move_to_element(video_player_container).perform()

    def pause_video(self):
        """
        Click the pause button to pause the video playback.
        """
        self.switch_to_video_iframe()  # Switch to the video iframe if not already inside
        self.hover_over_video()  # Hover over the video to reveal controls
        self.click(*self.pause_button)  # Click the play/pause button to toggle video pause/play

    def continue_watching(self):
        """
        Click the 'Continue Watching' button to continue playback after a break.
        """
        self.driver.switch_to.parent_frame()  # Switch back to the parent frame if inside an iframe
        self.click(*self.continue_watching_button)  # Click the continue watching button

    def adjust_volume(self):
        """
        Adjust the video volume to a desired level.
        This can simulate key presses to change the volume.
        """
        self.switch_to_video_iframe()  # Switch to the video iframe
        self.hover_over_video()  # Hover over the video player to make controls visible

        video_player_container = self.wait_for_element(By.ID, "media-player")  # Wait for video player container to be visible

        # Use ActionChains to hover over the volume slider element
        action = ActionChains(self.driver)
        action.move_to_element(video_player_container).perform()  # Hover to the volume slider area

        # Adjust the volume by simulating the UP key press 10 times (to increase volume)
        for _ in range(10):
            self.hover_over_video()  # Ensure hovering over video player
            video_player_container.send_keys(Keys.UP)  # Simulate pressing UP arrow key
            action.move_to_element(video_player_container).perform()
            time.sleep(0.2)  # Sleep for a short duration to simulate key press intervals

        # Adjust the volume by simulating the DOWN key press 5 times (to decrease volume)
        for _ in range(5):
            self.hover_over_video()  # Ensure hovering over video player
            video_player_container.send_keys(Keys.DOWN)  # Simulate pressing DOWN arrow key
            time.sleep(0.2)

        print("Volume set to 50%")  # Print the final volume level (50%)

    def change_resolution(self, resolution):
        """
        Change video resolution (480p or 720p).
        
        :param resolution: Resolution to change to ('480p' or '720p')
        """
        self.switch_to_video_iframe()  # Switch to the iframe containing the video player
        self.hover_over_video()  # Hover over the video player to activate controls
        self.click(*self.settings_menu)  # Click on the settings menu to open resolution options
        
        # Change resolution based on the argument passed (either 480p or 720p)
        if resolution == '480p':
            self.click(*self.resolution_480p)  # Click the 480p button to change resolution
        elif resolution == '720p':
            self.click(*self.resolution_720p)  # Click the 720p button to change resolution

    def navigate_back(self):
        """
        Click the back button to return to the previous page or video.
        """
        self.driver.switch_to.parent_frame()  # Switch back to the parent frame if inside an iframe
        self.click(*self.back_button)  # Click the back button to navigate backward

    def logout(self):
        """
        Click the logout button to log out from the application.
        """
        
        self.wait_for_element(*self.project_page)
        try:
            # Check if the browser is inside an iframe and handle it accordingly
            is_in_iframe = self.driver.execute_script("return window.self !== window.top;")
            if is_in_iframe:
                print("Currently inside an iframe.")
                self.driver.switch_to.default_content()  # Switch to main document if in iframe
            else:
                print("Not inside an iframe.")

            # Wait for the logout button to be clickable
            self.wait_for_element(*self.logout_button)

            # Click on the logout button to log out from the application
            self.click(*self.logout_button)
            print("Logout button clicked successfully.")

            time.sleep(3)  # Wait for a few seconds to ensure the logout process completes
        except Exception as e:
            print(f"Error during logout: {e}")  # Print error if something goes wrong
