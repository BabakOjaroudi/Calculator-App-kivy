# Calculator-App-kivy
This is a sample of Calculator App with Python , Includes four main operations




#Packaging the App

####Packaging Your App for Android#####
 pip install buildozer

[app]

### (str) Title of your application
title = KvCalc

### (str) Package name
package.name = kvcalc

### (str) Package domain (needed for android/ios packaging)
package.domain = org.kvcalc



####Packaging Your App for Windows####
$ pip install pyinstaller
$ pyinstaller main.py -w
