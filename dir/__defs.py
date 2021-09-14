from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.options import Options
from tkinter import * 
from tkinter import messagebox
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.chrome.options import Options
# from bs4 import BeautifulSoup

global driver

def change_location(map_coord = { "latitude": 42.1408845, "longitude": -72.5033907, "accuracy": 100}):
    #needs to be passed a dictionary structured as above
    globals()['driver'].execute_cdp_cmd('Emulation.setGeolocationOverride', {
        "latitude": map_coord['latitude'],
        "longitude": map_coord['longitude'],
        "accuracy": map_coord['accuracy']
    })

def pre_attack():
    #emulating a mobile device because if we admit we're an actual computer, google location services will not let us spoof our location.

    mobile_emulation = {"deviceMetrics": { "width": 1024, "height": 1366, "pixelRatio": 2.0 },"userAgent": "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1" }
    prefs = {"settings.resolve_timezone_by_geolocation_method":"DISABLED"}


    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--incognito")
    # chrome_options.add_argument("--disable-application-cache")
    # chrome_options.add_argument("--arc-disable-locale-sync")
    # chrome_options.add_argument("--disable-search-geolocation-disclosure")


    driver=webdriver.Chrome("/Users/persephone/chromedriver", options=chrome_options)
    globals()["driver"]=driver

    change_location()

    # driver.get("http://maps.google.com")
    driver.get("http://lite.tinder.com")
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME , "button")))
    login_opts = driver.find_elements(By.CLASS_NAME , "button")
    login = [a for a in login_opts if a.text == "LOG IN"][0]
    login.click()
