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