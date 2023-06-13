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
        if "Study" in heading.text:
            print(heading.text)
            study_rooms.append(room)
    
    # schedule based on first room availability
    for study_room in study_rooms:
        # attribute lookup format for WebElement
        start_time = "12.00"
        end_time = "2.00"

        print(study_room)
        while start_time != end_time:
            st = time_to_attr(start_time)
            et = time_to_attr(end_time)

            if et == "8:45 pm":
                break

            if check_interval(study_room, start_time, end_time):
                print("We have found a good interval", st, et)
            else:
                print("interval", st, et, "Not Available")
            
            # increment start and end time by intervals of 15 minutes
            start_time = increment_time(start_time)
            end_time = increment_time(end_time)

def time_to_attr(time):
    time = str(time).split(".")

    hour = time[0]
    minutes = time[1]

    if len(minutes) == 1:
        minutes = minutes + "0"

    return hour + ":" + minutes + " pm"

def increment_time(time):
    time = str(time).split(".")

    hour = int(time[0])
    minutes = int(time[1]) + 15
    
    if minutes == 60:
        hour = hour + 1
        minutes = "00"
    
    if hour > 12:
        hour = 1

    return str(hour) + "." + str(minutes)

def check_interval(study_room, st, et):
    """
    study_room: webdriver element
    st: int
    et: int
    return: boolean
    """
    while st != et:
        time_block = time_to_attr(st)
        time_block_element = study_room.find_element(By.XPATH, "//div[@data-time='" + time_block + '\']')
        if "booked" in time_block_element.get_attribute("class"):
            return False
        st = increment_time(st)
    
    return "booked" not in study_room.find_element(By.XPATH, "//div[@data-time='" + time_to_attr(et) + '\']')

def handle_information_form():
    pass

def usage():
    pass


if __name__ == '__main__':
    main()
    