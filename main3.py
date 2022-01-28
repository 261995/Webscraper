import sqlite3
# biblioteka dla baz danych
from sys import argv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

EMAIL = 'zal.user@mytrashemail.com'
PASSWORD = 'zal.user.1234'

def scrape():
    PATH=Service("C:\Program Files (x86)\chromedriver.exe")
    driver = webdriver.Chrome(service=PATH)

    URL = 'https://accounts.zalando.com/authenticate?request=eyJjbGllbnRfaWQiOiJsb3VuZ2UiLCJyZXNwb25zZV90eXBlIjoiY29kZSIsInNjb3BlcyI6WyJvcGVuaWQiXSwicmVkaXJlY3RfdXJpIjoiaHR0cHM6Ly93d3cuemFsYW5kby1sb3VuZ2UucGwvc3NvL2NhbGxiYWNrIiwic3RhdGUiOiJleUp2Y21sbmFXNWhiRjl5WlhGMVpYTjBYM1Z5YVNJNkltaDBkSEJ6T2k4dmQzZDNMbnBoYkdGdVpHOHRiRzkxYm1kbExuQnNMeU12Ykc5bmFXNGlMQ0pqYkdsbGJuUmZjM1JoZEdVaU9pSmxlVXB0WWtjNU0wbHFiMmxpUnpreFltMWtiRWxwZDJsaU0wcHdXakpzZFZsWVVuQmliV1JSWTIwNWNWcFhUakJKYW05cFNXNHdJbjA9Iiwibm9uY2UiOiJkMjFjNTk5ZC1lYTBmLTQ2ODMtYWMzYy04MGFhY2RjODdkOGMiLCJ1aV9sb2NhbGVzIjpbInBsLVBMIl0sInJlcXVlc3RfaWQiOiJmbG93LWlkOjRjYTdiMTNkLTE4MzMtNGU2NC1hZDNhLWZmMmY3NDQ2M2MzNDpPRm43bnRGZUhleTlidlZzIiwicHJlbWlzZSI6IkxPVU5HRSJ9&ui_locales=pl-PL&premise=lounge&view=login'

    driver.get(URL)

    username = driver.find_element(By.ID, 'form-email')
    username.clear()
    username.send_keys(EMAIL)

    password = driver.find_element(By.ID, "form-password")
    password.clear()
    password.send_keys(PASSWORD)
    driver.find_element(By.ID, "login-form-submit").click()

    # driver.get('https://www.zalando-lounge.pl/event#')
    #
    wait = WebDriverWait(driver, 20)
    value_element = wait.until(
        EC.presence_of_all_elements_located((By.XPATH, "//span[@id='share-tradingdata-o' and text()!='']")))
    values = [x.text for x in value_element]
    print(values)

    # link = driver.find_element(By.LINK_TEXT, 'Odkryj')
    # link.click()

    # element = driver.find_element(By.CLASS_NAME, 'open-campaign___inner-wrapper___1b2pz')
    # select = Select(element)
    # driver.quit()

scrape()