# fptraffic_webdriver
Tools to help automatically label images in FPTraffic.  You'll need the following:

1) A [FPTraffic](https://fptraffic.com) (and Facebook) account.

2) [Google Chrome](https://www.google.com/chrome/)

3) [A Microsoft API Key](https://www.microsoft.com/cognitive-services/en-us/sign-up) (free for the first 5000 images)

4) Python 3.5+ with [Selenium](https://pypi.python.org/pypi/selenium/3.11.0) installed

 - You will also need the [Chrome webdriver](https://sites.google.com/a/chromium.org/chromedriver/downloads).
 - This may work with the Firefox or other webdrivers but haven't been tested.
 - This may also with with Python 2.7 but hasn't been tested either.

## How to Use:

##### Initial Setup (only need to do once):

Download and Install Python 3.6 ([recommend the Miniconda 3 or Anaconda 3 editions](https://www.anaconda.com/download/))

Open a terminal or command line window

Install selenium:

```
pip install selenium
```

Install the [Chrome webdriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) and put the folder you installed to in your OS's PATH variable (instructions vary based on your OS, please Google for them if you're not sure.)

##### Run each time you want to label images:

Navigate to the directory where this module is installed.

Launch python by opening a command line window and running the command *python*.

Use the following commands:

```
import main

from selenium import webdriver

browser = webdriver.Chrome()

```

A browser window will appear.  DON'T close it.  Instead, go to www.fptraffic.com in it and log in using your Facebook account.

Then navigate to the Scheduled Posts for the page you want to get image labels for.

Finally, run the following:

```
main.label(browser)
```

