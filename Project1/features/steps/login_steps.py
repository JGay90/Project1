from behave import given,when,then
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


@given(u'The User is on the HTML Webpage')
def step_impl(context):
    driver: WebDriver = context.driver
    driver.get(r"C:\Users\User\PycharmProjects\Project1\FrontEnd\login.html")
    # raise NotImplementedError(u'STEP: Given The User is on the HTML Webpage')


@when(u'The User inputs {eid} in the employeeID bar')
def step_impl(context):
    employeeID: WebElement = context.driver.find_element_by_id("eid")
    employeeID.send_keys("2")

    # raise NotImplementedError(u'STEP: When The User inputs {eid} in the employeeID bar')


@when(u'The User inputs {username} in the username bar')
def step_impl(context):
    username: WebElement = context.driver.find_element_by_id("username")
    username.send_keys("moonlight")
    # raise NotImplementedError(u'STEP: When The User inputs {username} in the username bar')


@when(u'The User inputs <password> in the inputPassword bar')
def step_impl(context):
    pwrd: WebElement = context.driver.find_element_by_id("inputPassword")
    pwrd.send_keys("moon")
    # raise NotImplementedError(u'STEP: When The User inputs {password} in the inputPassword bar')


@when(u'The User clicks the submit button')
def step_impl(context):
    submit: WebElement = context.driver.find_element_by_id("submitBtn")
    submit.click()
    # raise NotImplementedError(u'STEP: When The User clicks the submit button')


@then(u'The title of the page is now {title}')
def step_impl(context,title):
    driver: WebDriver = context.driver
    assert driver.title == title
    # raise NotImplementedError(u'STEP: Then The title of the page is now {title}')
