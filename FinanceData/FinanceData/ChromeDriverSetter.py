from selenium import webdriver
import os


def printCWD():
    cwd = os.getcwd()
    print(cwd)


def webDriverWithCustimizedDownloadLocaiton(downloadPath: str = "") -> webdriver:
    """
    This method return a chromedriver object with a customized download path
    By default, if you left the input variable empty, the default downaload folder will be the current working directory
    :param downloadPath:
    :return: webdriver
    """
    if not downloadPath:
        downloadPath = os.getcwd()

    chrome_options = webdriver.ChromeOptions()
    prefs = {'download.default_directory': downloadPath}
    chrome_options.add_experimental_option('prefs', prefs)
    # driver = webdriver.Chrome(chrome_options=chrome_options)
    driver = webdriver.Chrome(options=chrome_options)
    return driver


if __name__ == "__main__":
    webDriverWithCustimizedDownloadLocaiton()
