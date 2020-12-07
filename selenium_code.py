import time
from selenium import webdriver
import os
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


def xpath(add):
    try:
        time.sleep(10)
        element = driver.find_element_by_xpath(add)
        element.click()
    except Exception as e:
        print(e)
        time.sleep(10)
        xpath(add)


runingCodePath = os.path.split(os.path.realpath(__file__))[0]

firefoxPath = os.path.join(runingCodePath, r"geckodriver-v0.27.0-win32\geckodriver.exe")
print(firefoxPath)

while True:
    try:
        profile = webdriver.FirefoxProfile()
        options = Options()
        options.headless = True
        profile.set_preference("media.volume_scale", "0.0")
        binary = FirefoxBinary(os.path.join(runingCodePath, r"Mozilla Firefox\firefox.exe"))
        print(binary)
        driver = webdriver.Firefox(firefox_binary=binary, executable_path=firefoxPath, options=options, firefox_profile=profile, service_log_path=os.path.devnull)

        driver.get('https://indiandealin.wordpress.com/')
        xpath('//iframe[@class="youtube-player"]')
        for i in range(1, 60):
            print("running for last " + str(i) + " minutes")
            time.sleep(60)
        driver.quit()
    except Exception as e:
        print(e)
        time.sleep(600)


    # sound but no video
    # driver = webdriver.Firefox(executable_path="./bin/geckodriver", options=options)#, firefox_profile=profile)

    # no sound and no video
    # driver = webdriver.Firefox(executable_path="./geckodriver", options=options, firefox_profile=profile)

    # video but no sound
    # driver = webdriver.Firefox(executable_path="./bin/geckodriver", firefox_profile=profile)

    # video and sound
    # driver = webdriver.Firefox(executable_path="./bin/geckodriver")

