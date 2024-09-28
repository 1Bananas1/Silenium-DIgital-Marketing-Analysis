from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display
import time
from selenium.webdriver.chrome.options import Options
import os


def countdown(seconds):
  """Displays a countdown timer in minutes and seconds."""
  minutes_left = seconds // 60
  seconds_left = seconds % 60
  while seconds > 0:
    print(f"\n \n \n Site Down for Maintenance \n \n \n Time remaining: {minutes_left} minutes {seconds_left} seconds \n\n\n\n\n\n")
    time.sleep(1)
    seconds -= 1
    minutes_left = seconds // 60
    seconds_left = seconds % 60
USER = ""
PASS = ""

consecutive_failure = 0
tests = 7500
max_score = 81503
max_days = 31
average_impressions = 0


post_length_options = [50,500,750,1000,1250,1500,2500,5000,10000]
post_length_loc = ['//*[@id="post_length"]']
media_type = [
    '//*[@id="image"]'
]
posting_time = [
    '//*[@id="morning"]',
    '//*[@id="afternoon"]',
    '//*[@id="evening"]'
]
download_path = ['//*[@id="638713752765428643"]/button']
submit_button = ['//*[@id="638713752765428643"]/input[11]']
total_tests = len(media_type) * len(posting_time) * tests

for i in range(tests):
    print('Test: ' + str(i) +'/'+ str(tests))
    print('Current Max Score: ' + str(max_score))
    print('Previous Score: ' + str(average_impressions))
    print(f'Consecutive Errors: {consecutive_failure}')
    options = Options()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--start-maximized")
    # options.add_argument("--headless")
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service,options=options)
    driver.maximize_window()

    try:
        # Navigate to the webpage
        driver.get("https://www.gamelytics.net/digital-marketing-game.html")
        # Wait for the input element for username and password to be present
        input_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "wsite-page-membership-text-input"))
        )
        # Send keys to the input element
        input_element.send_keys(USER + Keys.TAB + PASS + Keys.ENTER)
        input_element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,post_length_loc[0]))
        )
        consecutive_failure = 0

        # start day
        for day in range(1,max_days):
            # post length
            
            # media type
            media_type_selected = media_type[0]
            media_type_driver = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,media_type_selected)))
            media_type_driver.click()
            # print('media type')

            # time.sleep(2)

            # posting time
            if day in [7]:
                posting_time_selected = posting_time[1]
                posting_time_driver = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,posting_time_selected)))
                posting_time_driver.click()
            elif day in [16,26,29]:
                posting_time_selected = posting_time[0]
                posting_time_driver = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,posting_time_selected)))
                posting_time_driver.click()
            else:
                posting_time_selected = posting_time[2]
                posting_time_driver = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,posting_time_selected)))
                posting_time_driver.click()
            # print('posting time')
            # time.sleep(2)

            post_length = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,post_length_loc[0])))
            
            if day in [30]:
                post_length_selected = post_length_options[0]
                post_length.send_keys(post_length_selected)
            if day in [3,8,9,10,11,19]:
                post_length_selected = post_length_options[1]
                post_length.send_keys(post_length_selected)
            if day in [5,7,17,18,28]:
                post_length_selected = post_length_options[2]
                post_length.send_keys(post_length_selected)
            if day in [1,2,16,20,26,27,29]:
                post_length_selected = post_length_options[3]
                post_length.clear()
                post_length.send_keys(post_length_selected)
            if day in [13,15,23]:
                post_length_selected = post_length_options[4]
                post_length.send_keys(post_length_selected)
            if day in [6,12,25]:
                post_length_selected = post_length_options[5]
                post_length.send_keys(post_length_selected)
            if day in [22,24]:
                post_length_selected = post_length_options[6]
                post_length.send_keys(post_length_selected)
            if day in [14,21]:
                post_length_selected = post_length_options[7]
                post_length.send_keys(post_length_selected)
            if day in [4]:
                post_length_selected = post_length_options[8]
                post_length.send_keys(post_length_selected)
            # print(day)
            # print('post length')
            # time.sleep(2)


            #submit button
            submit_button_driver = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,submit_button[0])))
            submit_button_driver.click()
            
            # print('submit')
            
        # time.sleep(1)    
        try:
            WebDriverWait(driver, 5).until(EC.alert_is_present())  # Wait for alert
            alert = driver.switch_to.alert  # Switch to alert
            # print(alert.text)
            average_impressions = float(alert.text.split("average of ")[1].rstrip(" impressions per day!"))
            # print(average_impressions)

            if average_impressions > max_score:
                max_score = average_impressions

                alert.accept()  # Accept the alert (click "OK")


                                # ------

                # SCROLL_PAUSE_TIME = 0.5

                # # Get scroll height
                # last_height = driver.execute_script("return document.body.scrollHeight")

                # while True:
                #     # Scroll down to bottom
                #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                #     # Wait to load page
                #     time.sleep(SCROLL_PAUSE_TIME)

                #     # Calculate new scroll height and compare with last scroll height
                #     new_height = driver.execute_script("return document.body.scrollHeight")
                #     if new_height == last_height:
                #         break
                #     last_height = new_height

                # # ----

                output = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="output"]')))
                for j in range(30):
                    output.send_keys(Keys.DOWN)
                
                driver.save_screenshot("C:/Users/jmacd/OneDrive - Saint Louis University/coding 2 large/marketing/final/screenshot.png")
    
                download = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="638713752765428643"]/button'))
                )
                download.click()
                time.sleep(2)
                
            else:
                print('nope')
                alert.accept()  # Accept the alert (click "OK")
                


            print("Alert accepted: ", alert.text)
        except Exception as e:
            print("No alert present or error occurred:", e)
    except Exception as e:
            print(f'Error has occured: {e}')
            consecutive_failure += 1
            if consecutive_failure == 3:
                print('\n \n \n Site Down for Maintenance \n \n \n')
                countdown(300)
                consecutive_failure = 0
            driver.quit()

import time





