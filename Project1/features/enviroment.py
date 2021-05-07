from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


def before_all(context):
    driver: WebDriver = webdriver.Chrome("../utils/chromedriver.exe")
    context.driver = driver
    print("started")


def after_all(context):
    context.driver.quit()
    print("ended")
