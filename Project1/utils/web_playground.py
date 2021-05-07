from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from time import sleep
from selenium.webdriver.remote.webelement import WebElement

driver: WebDriver = webdriver.Chrome("chromedriver.exe")
try:
    driver.get(r"C:\Users\User\PycharmProjects\Project1\FrontEnd\login.html")
    sleep(5)
    employeeID: WebElement = driver.find_element_by_id("eid")
    employeeID.send_keys("2")
    username: WebElement = driver.find_element_by_id("username")
    username.send_keys("moonlight")
    pwrd: WebElement = driver.find_element_by_id("inputPassword")
    pwrd.send_keys("moon")
    submit:WebElement = driver.find_element_by_id("submitBtn")
    submit.click()
    assert "Login" == driver.title
except AssertionError as e:
    print("Incorrect Title of Page Found")
finally:
    sleep(3)
    driver.close()