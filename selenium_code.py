import time
from selenium import webdriver
import os
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys



def xpath(add):
    try:
        time.sleep(5)
        element = driver.find_element_by_xpath(add)
        element.click()
    except Exception as e:
        print(e)
        time.sleep(5)
        xpath(add)


runingCodePath = os.path.split(os.path.realpath(__file__))[0]
firefoxPath = os.path.join(runingCodePath, r"geckodriver-v0.27.0-win32\geckodriver.exe")

while True:
    try:
        profile = webdriver.FirefoxProfile()
        options = Options()
        options.headless = True
        profile.set_preference("media.volume_scale", "0.0")
        b_path = os.path.join(runingCodePath, r"Mozilla Firefox\firefox.exe")
        binary = FirefoxBinary(b_path)
        driver = webdriver.Firefox(firefox_binary=binary, executable_path=firefoxPath, service_log_path=os.path.devnull, options = options, firefox_profile=profile)
        url = "https://www.google.co.in/"
        driver.get(url)
        time.sleep(5)
        inputElement = driver.find_element_by_xpath('//input[@title="Search"]')
        inputElement.send_keys('food art by ginny')
        time.sleep(5)
        inputElement.send_keys(Keys.RETURN)
        xpath('//a[@href="https://www.youtube.com/c/foodartbyginny/search"]')
        xpath('//paper-tab[contains(.,"Playlists")]')
        xpath('//a[@title="All in One"]')
        for i in range(1, 60):
            print("running for last " + str(i) + " minutes")
            time.sleep(60)
        driver.quit()
    except Exception as e:
        print(e)
        time.sleep(600)
