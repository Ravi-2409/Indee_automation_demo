Feature: Video Playback and Control Automation

  Scenario: Automate video playback and control actions
    Given I am on the login page
    When I login with the provided PIN
    And I navigate to the Test Automation Project
    And I switch to the Details tab
    And I return to the Videos tab
    And I play the video
    And I pause the video
    And I continue watching the video
    
    And I change the resolution to 480p and back to 720p
    And I pause the video and navigate back
    And I log out
    Then I should see the logout successful
