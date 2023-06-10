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

    # select library
    libraries_deselect = driver.find_element(By.XPATH, "//label[normalize-space()='Check all']")
    libraries_deselect.click()

    selected_library = '\'' + selected_library + ' Library' + '\'' + ")]"

    library_button = driver.find_element(By.XPATH, "//div[@class='amnp-location-select']//label[contains(text()," + selected_library)
    library_button.click()

    print('\'')

    time.sleep(20)

    # based on
    


def usage():
    pass

if __name__ == '__main__':
    main()