import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
import os

tests = 10

USER = ""
PASS = ""

day = 1
max_days = 30

post_length_options = [500,750,1000]



post_length_loc = ['//*[@id="post_length"]']

media_type = [
    '//*[@id="text"]',
    '//*[@id="image"]',
    '//*[@id="video"]',
    '//*[@id="poll"]'
]


posting_time = [
    '//*[@id="morning"]',
    '//*[@id="afternoon"]',
    '//*[@id="evening"]'
]
download_path = ['//*[@id="638713752765428643"]/button']

submit_button = ['//*[@id="638713752765428643"]/input[11]']

total_tests = len(media_type) * len(posting_time) * tests

for i in range(len(post_length_options)):
    for j in range(len(media_type)):
        for k in range(len(posting_time)):
            for l in range(tests):
                print('post length options ' + str(i) + '\nmedia type ' + str(j) + '\nposting time ' + str(k) + '\ntest no. ' + str(l))
                service = Service(executable_path="chromedriver.exe")
                driver = webdriver.Chrome(service=service)
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


                    # start day


                    for m in range(max_days):
                        post_length = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,post_length_loc[0])))
                        post_length.send_keys(post_length_options[i])


                        media_type_selected = media_type[j]
                        media_type_driver = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,media_type_selected)))
                        media_type_driver.click()

                        posting_time_selected = posting_time[k]
                        posting_time_driver = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,posting_time_selected)))
                        posting_time_driver.click()

                        submit_button_driver = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,submit_button[0])))
                        submit_button_driver.click()
                        

                    try:
                        WebDriverWait(driver, 5).until(EC.alert_is_present())
                        alert = driver.switch_to.alert
                        alert.accept()
                    except Exception as e:
                        print(e)

                    download = WebDriverWait(driver,5).until(
                        EC.presence_of_element_located((By.XPATH,download_path[0]))
                    )
                    download.click()
                    time.sleep(.5)
                except Exception as e:
                    print(f'Error has occured: {e}')
                    driver.quit()
                    

                # time.sleep(1)
                print()
                driver.quit()
