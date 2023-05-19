from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time



def main():
    
    driver = webdriver.Chrome()
    driver.get("https://plano.libnet.info/reserve")
    
    

    time.sleep(100)

def usage():
    pass

if __name__ == '__main__':
    main()