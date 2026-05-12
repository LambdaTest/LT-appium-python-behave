# Behave With Python — TestMu AI (Formerly LambdaTest)

<p align="center">
<img height="500" src="https://user-images.githubusercontent.com/95698164/171990681-6d50db45-bf2b-4685-86d5-b83acedc60f0.png">
</p>

<p align="center">
  <a href="https://www.testmuai.com/blog/?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-python-behave" target="_bank">Blog</a>
  &nbsp; &#8901; &nbsp;
  <a href="https://www.testmuai.com/support/docs/?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-python-behave" target="_bank">Docs</a>
  &nbsp; &#8901; &nbsp;
  <a href="https://www.testmuai.com/learning-hub/?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-python-behave" target="_bank">Learning Hub</a>
  &nbsp; &#8901; &nbsp;
  <a href="https://www.testmuai.com/newsletter/?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-python-behave" target="_bank">Newsletter</a>
  &nbsp; &#8901; &nbsp;
  <a href="https://www.testmuai.com/certifications/?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-python-behave" target="_bank">Certifications</a>
  &nbsp; &#8901; &nbsp;
  <a href="https://www.youtube.com/@TestMuAI" target="_bank">YouTube</a>
</p>
&emsp;
&emsp;
&emsp;

_Behave is a tool made to be used with Python testing frameworks, such as PyTest and Nose. It enables you to write tests in a natural language-like manner and execute them against your code.Perform [JUnit test on TestMu AI's online cloud](https://www.testmuai.com/appium-mobile-testing?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-python-behave)._

_Learn the basics of [Appium testing on the TestMu AI platform](https://www.testmuai.com/support/docs/getting-started-with-appium-testing/?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-python-behave)._

[<img height="53" width="200" src="https://user-images.githubusercontent.com/70570645/171866795-52c11b49-0728-4229-b073-4b704209ddde.png">](https://accounts.lambdatest.com/register?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-python-behave)

## Table of Contents

- [Pre-requisites](#pre-requisites)
- [Run Your First Test](#run-your-first-test)
- [Executing The Test](#executing-the-test)

## Pre-requisites

Before you can start performing App automation testing with Appium, you would need to follow these steps:

- Install the latest stable Python build from the [official website](https://www.python.org/downloads/).
- Make sure **pip** is installed in your system. You can install **pip** from [here](https://pip.pypa.io/en/stable/installation/).

### Clone The Sample Project

Clone the TestMu AI’s :link: [LT-appium-python-behave](https://github.com/LambdaTest/LT-appium-python-behave) repository and navigate to the code directory as shown below:

```bash
git clone https://github.com/LambdaTest/LT-appium-python-behave
cd LT-appium-python-behave
```

### Setting Up Your Authentication

Make sure you have your TestMu AI credentials with you to run test automation scripts on LambdaTest. To obtain your access credentials, [purchase a plan](https://billing.lambdatest.com/billing/plans?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-python-behave) or access the [Automation Dashboard](https://appautomation.lambdatest.com/?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-python-behave).

Set TestMu AI `Username` and `Access Key` in environment variables.

**For Linux/macOS:**

```js
export LT_USERNAME=YOUR_LAMBDATEST_USERNAME \
export LT_ACCESS_KEY=YOUR_LAMBDATEST_ACCESS_KEY
```

**For Windows:**

```js
set LT_USERNAME=YOUR_LAMBDATEST_USERNAME `
set LT_ACCESS_KEY=YOUR_LAMBDATEST_ACCESS_KEY
```

### Upload Your Application

Upload your **_iOS_** application (.ipa file) or **_android_** application (.apk file) to the TestMu AI servers using our **REST API**. You need to provide your **Username** and **AccessKey** in the format `Username:AccessKey` in the **cURL** command for authentication. Make sure to add the path of the **appFile** in the cURL request. Here is an example cURL request to upload your app using our REST API:

**Using App File:**

**For Linux/macOS:**

```js
curl -u "YOUR_LAMBDATEST_USERNAME:YOUR_LAMBDATEST_ACCESS_KEY" \
--location --request POST 'https://manual-api.lambdatest.com/app/upload/realDevice' \
--form 'name="Android_App"' \
--form 'appFile=@"/Users/macuser/Downloads/proverbial_android.apk"'
```

**For Windows:**

```js
curl -u "YOUR_LAMBDATEST_USERNAME:YOUR_LAMBDATEST_ACCESS_KEY" -X POST "https://manual-api.lambdatest.com/app/upload/realDevice" -F "appFile=@"/Users/macuser/Downloads/proverbial_android.apk""
```

**Using App URL:**

**Linux/macOS:**

```js
curl -u "YOUR_LAMBDATEST_USERNAME:YOUR_LAMBDATEST_ACCESS_KEY" \
--location --request POST 'https://manual-api.lambdatest.com/app/upload/realDevice' \
--form 'name="Android_App"' \
--form 'url="https://prod-mobile-artefacts.lambdatest.com/assets/docs/proverbial_android.apk"'
```

**For Windows:**

```js
curl -u "YOUR_LAMBDATEST_USERNAME:YOUR_LAMBDATEST_ACCESS_KEY" -X POST "https://manual-api.lambdatest.com/app/upload/realDevice" -d "{"url":"https://prod-mobile-artefacts.lambdatest.com/assets/docs/proverbial_android.apk","name":"sample.apk"}"
```

**Tip:**

- If you do not have any **.apk** or **.ipa** file, you can run your sample tests on TestMu AI by using our sample :link: [Android app](https://prod-mobile-artefacts.lambdatest.com/assets/docs/proverbial_android.apk) or sample :link: [iOS app](https://prod-mobile-artefacts.lambdatest.com/assets/docs/proverbial_ios.ipa).
- Response of above cURL will be a **JSON** object containing the `App URL` of the format - <lt://APP123456789123456789> and will be used in the next step.

## Run Your First Test

Once you are done with the above-mentioned steps, you can initiate your first Behave test on LambdaTest.

**Test Scenario:** Check out [Android.py](https://github.com/LambdaTest/LT-appium-python-behave/blob/master/steps/AndroidStepDef.py) file to view the sample test script for android and [iOS.py](https://github.com/LambdaTest/LT-appium-python-behave/blob/master/steps/IosStepDef.py) for iOS.

### Configuring Your Test Capabilities

You need to update your capabilities in `appConfig.py` files. In this sample project, we have provided the examples for running tests on both **Android** and **iOS** apps. We are passing platform name, platform version, device name and app url (generated earlier) along with other capabilities like build name and test name via capabilities object. The capabilities object in the sample code for a single test are defined as:

<Tabs className="docs__val">

<TabItem value="ios-config" label="iOS" default>

```python title="appConfig.py"
app_ios_desired_caps = {
  "lt:options": {
    "deviceName":"iPhone 12",
    "platformName":"ios",
    "platformVersion":"14",
    "build":"Python Behave - iOS",
    "name":"Sample Test iOS",
    "app":"app_url" ,#Enter app_url here
    "isRealMobile":True,
    "network":True,
    "visual":True,
    "video":True,
    "w3c":True
  }
}
```

</TabItem>
<TabItem value="android-config" label="Android" default>

```python title="appConfig.py"
app_android_desired_caps = {
	"lt:options": {
		"platformName": "android",
		"deviceName": "OnePlus 6",
		"platformVersion": "8",
    "build": "Python Behave - Android",
		"name": "Sample Test Android",
		"app": "app_url", #Enter app_url here
		"visual": True,
		"video": True,
    "w3c": True,
		"isRealMobile": True
	}
}
```

</TabItem>

</Tabs>

**Info Note:**

- You must add the generated **APP_URL** to the `"app"` capability in the config file.
- You can generate capabilities for your test requirements with the help of our inbuilt :link: **[Capabilities Generator tool](https://www.testmuai.com/capabilities-generator/beta/index.html?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-python-behave)**. A more Detailed Capability Guide is available [here :page_facing_up:](https://www.testmuai.com/support/docs/desired-capabilities-in-appium/?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-python-behave) .

## Executing The Tests

Install the required dependencies using the following command:

```bash
pip3 install -r requirements.txt
```

Execute the following command to run your test on TestMu AI platform:

**Android:**

```bash
behave --tags @androidApp
```

**IOS:**

```bash
behave --tags @iosApp
```

**Info:** Your test results would be displayed on the test console (or command-line interface if you are using terminal/cmd) and on the :link: [TestMu AI App Automation Dashboard](https://appautomation.lambdatest.com/build?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-python-behave).

## Additional Links

- [Advanced Configuration for Capabilities](https://www.testmuai.com/support/docs/desired-capabilities-in-appium/?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-python-behave)
- [How to test locally hosted apps](https://www.testmuai.com/support/docs/testing-locally-hosted-pages/?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-python-behave)
- [How to integrate TestMu AI with CI/CD](https://www.testmuai.com/support/docs/integrations-with-ci-cd-tools/?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-python-behave)

## Documentation & Resources :books:

Visit the following links to learn more about TestMu AI's features, setup and tutorials around test automation, mobile app testing, responsive testing, and manual testing.

- [TestMu AI Documentation](https://www.testmuai.com/support/docs/?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-python-behave)
- [TestMu AI Blog](https://www.testmuai.com/blog/?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-python-behave)
- [TestMu AI Learning Hub](https://www.testmuai.com/learning-hub/?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-python-behave)

## TestMu AI Community :busts_in_silhouette:

The [TestMu AI Community](https://community.testmuai.com/?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-python-behave) allows people to interact with tech enthusiasts. Connect, ask questions, and learn from tech-savvy people. Discuss best practises in web development, testing, and DevOps with professionals from across the globe 🌎

## What's New At TestMu AI ❓

To stay updated with the latest features and product add-ons, visit [Changelog](https://changelog.lambdatest.com/)

## 🚀 [LambdaTest is Now TestMu AI](https://www.testmuai.com/lambdatest-is-now-testmuai/)

👋 Welcome to TestMu AI, the next evolution of LambdaTest. As of January 2026, LambdaTest has officially rebranded to TestMu AI. We have evolved from a cross-browser testing cloud into a unified, AI-native quality engineering platform designed for the modern DevOps era.

Whether you have been part of the LambdaTest community for years or are just discovering TestMu AI, our mission remains the same: to help you ship faster with high-scale test execution, autonomous testing, and deep quality analytics.

**🔄 Our Rebrand Journey**

We chose the name TestMu AI to reflect our shift towards intelligent, autonomous testing. While our identity has changed, our core technology and commitment to the testing community stay the same.

**✨ Specialties**

- 🤖 AI-Native Test Execution (Formerly LambdaTest)
- ⚡ Autonomous Test Automation
- 🌐 Cross-Browser & Mobile Testing
- 📊 Unified Quality Intelligence

👉 Find [LambdaTest's New Home](https://www.testmuai.com/).