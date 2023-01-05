from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


@given('launch chrome browser')
def launch_browser(context):
#   context.driver = webdriver.Chrome("../resources/chromedriver")
# brew install --cask chromedriver
    context.driver = webdriver.Chrome()


@when('open orange hrm homepage')
def open_homepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com")


@then('verify that the logo present on page')
def verify_logo(context):
    context.driver.implicitly_wait(10)
    status = context.driver.find_element(By.NAME, "password").is_displayed()
    assert status is True


@then('close browser')
def close_browser(context):
    context.driver.close()
