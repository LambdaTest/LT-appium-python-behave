from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common import AppiumOptions
import time
from appium import webdriver
from behave import given
import appConfig as appConf
import sys
import os

path = os.getcwd()
sys.path.append(os.path.abspath(os.path.join(path, os.pardir)))


@given("Start the ios app automation test")
def startIOSAppAutomationTest(context):

    # LambdaTest Credentials
    if os.environ.get("LT_USERNAME") is None:
        username = "username"
    else:
        username = os.environ.get("LT_USERNAME")

    if os.environ.get("LT_ACCESS_KEY") is None:
        accesskey = "accesskey"
    else:
        accesskey = os.environ.get("LT_ACCESS_KEY")

    # Appium Options (New way for capabilities)
    options = AppiumOptions()
    options.load_capabilities(appConf.app_ios_desired_caps)

    # Driver Initialization
    driver = webdriver.Remote(
        command_executor="https://" + username + ":" + accesskey + "@mobile-hub.lambdatest.com/wd/hub",
        options=options
    )

    try:
        colorElement = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "color"))
        )
        colorElement.click()

        textElement = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Text"))
        )
        textElement.click()

        toastElement = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "toast"))
        )
        toastElement.click()

        notification = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "notification"))
        )
        notification.click()

        time.sleep(3)

        geolocation = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "geoLocation"))
        )
        geolocation.click()

        time.sleep(3)

        home = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Back"))
        )
        home.click()

        speedTest = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "speedTest"))
        )
        speedTest.click()

        time.sleep(3)

        home = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Back"))
        )
        home.click()

        driver.quit()

    except Exception as e:
        print("Test failed:", e)
        driver.quit()