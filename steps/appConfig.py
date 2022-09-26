app_android_desired_caps = {
	"lt:options": {
		"platformName": "android",
		"deviceName": "OnePlus 6",
		"platformVersion": "8",
      	"build": "Python Behave - Android",
		"name": "Sample Test Android",
		"app": "lt://proverbial-android", #Enter app_url here
		"visual": True,
		"video": True,
       	"w3c": True,
		"isRealMobile": True
	}
}

app_ios_desired_caps = {
  "lt:options": {
    "deviceName":"iPhone 12",
    "platformName":"ios",
    "platformVersion":"14",
    "build":"Python Behave - iOS",
    "name":"Sample Test iOS",
    "app":"lt://proverbial-ios" ,#Enter app_url here
    "isRealMobile":True,
    "network":True,
    "visual":True,
    "video":True,
    "w3c":True
  }
}
