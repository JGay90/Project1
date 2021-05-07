from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from time import sleep

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

driver: WebDriver = webdriver.Chrome(
    "C:\Users\User\PycharmProjects\Project1\utils\chromedriver.exe")
