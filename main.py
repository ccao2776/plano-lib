from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time
import sys
from datetime import date

def main():

    # ensure that user is scheduling two days in advance at the most
    # today = str(date.today()).split("-")

    selected_library = str(sys.argv[1])

    driver = webdriver.Chrome()
    driver.get('https://plano.libnet.info/reserve')

    # close resident form
    popup_form_close = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@class='btn btn-primary']")))
    popup_form_close.click()
    
    time.sleep(1)
    # select library
    libraries_deselect = driver.find_element(By.XPATH, "//label[normalize-space()='Check all']")
    libraries_deselect.click()
    selected_library = '\'' + selected_library + ' Library' + '\'' + ")]"
    library_button = driver.find_element(By.XPATH, "//div[@class='amnp-location-select']//label[contains(text()," + selected_library)
    library_button.click()

    time.sleep(2)
    handle_scheduling(driver)


    # input login
    # form_username = driver.find_element(By.XPATH, "//input[@id='login_card']")
    # form_username.send_keys('USERNAME')
    # form_password = driver.find_element(By.XPATH, "//input[@id='login_pin']")
    # form_password.send_keys('PASSWORD')
    # form_continue = driver.find_element(By.XPATH, "//span[@class='btn btn-edit amnp-lookup input-group-addon']")
    # form_continue.click()

    time.sleep(20)


# create a greedy scheduling algorithm based on 11am-12PM start timeframe
def handle_scheduling(driver):
    rooms = driver.find_elements(By.XPATH, "//div[@class='amnp-room-holder']")
    study_rooms = []

    # append WebElements that contains parasable studyrooms
    for room in rooms:
        heading = room.find_element(By.TAG_NAME, "h3")
        if "Study" in heading:
            study_rooms.append(room)
    
    # schedule based on first room availability
    for study_room in study_rooms:
        
    

def handle_information_form():
    pass

def usage():
    pass

if __name__ == '__main__':
    main()