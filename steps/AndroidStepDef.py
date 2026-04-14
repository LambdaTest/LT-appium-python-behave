from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from appium import webdriver
from behave import given
import appConfig as appConf
import sys
import os

path = os.getcwd()
sys.path.append(os.path.abspath(os.path.join(path, os.pardir)))


@given("Start the android app automation test")
def startAndroidAppAutomationTest(context):

    username = os.environ.get("LT_USERNAME") or "username"
    accesskey = os.environ.get("LT_ACCESS_KEY") or "accesskey"

    caps = appConf.app_android_desired_caps

    # Add LambdaTest credentials inside lt:options
    if "lt:options" not in caps:
        caps["lt:options"] = {}

    caps["lt:options"]["user"] = username
    caps["lt:options"]["accessKey"] = accesskey

    options = UiAutomator2Options().load_capabilities(caps)

    driver = webdriver.Remote(
        command_executor="https://mobile-hub.lambdatest.com/wd/hub",
        options=options
    )

    try:

        colorElement = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((AppiumBy.ID, "com.lambdatest.proverbial:id/color"))
        )
        colorElement.click()

        textElement = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((AppiumBy.ID, "com.lambdatest.proverbial:id/Text"))
        )
        textElement.click()

        toastElement = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((AppiumBy.ID, "com.lambdatest.proverbial:id/toast"))
        )
        toastElement.click()

        notification = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((AppiumBy.ID, "com.lambdatest.proverbial:id/notification"))
        )
        notification.click()

        geolocation = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((AppiumBy.ID, "com.lambdatest.proverbial:id/geoLocation"))
        )
        geolocation.click()

        home = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((AppiumBy.ID, "com.lambdatest.proverbial:id/Home"))
        )
        home.click()

        speedTest = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((AppiumBy.ID, "com.lambdatest.proverbial:id/speedTest"))
        )
        speedTest.click()

        home = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((AppiumBy.ID, "com.lambdatest.proverbial:id/Home"))
        )
        home.click()

        driver.quit()

    except Exception as e:
        print("Test failed:", e)
        driver.quit()