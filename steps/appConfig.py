build = os.getenv("LT_BUILD_NAME")

app_android_desired_caps = {
    "platformName": "Android",
    "appium:deviceName": "Galaxy S20",
    "appium:platformVersion": "10",
    "appium:automationName": "UiAutomator2",
    "appium:app": "lt://proverbial-android",

    "lt:options": {
        "build": build,
        "name": "Sample Test Android",
        "isRealMobile": True,
        "visual": True,
        "video": True,
        "w3c": True
    }
}

app_ios_desired_caps = {
    "platformName": "iOS",
    "appium:deviceName": "iPhone 14",
    "appium:platformVersion": "16",
    "appium:automationName": "XCUITest",
    "appium:app": "lt://proverbial-ios",

    "lt:options": {
        "w3c": True,
        "build": build,
        "name": "iOS App Automation Test",
        "isRealMobile": True
    }
}
