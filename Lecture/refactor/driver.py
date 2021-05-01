from selenium import webdriver
from decouple import config
import time


class Driver:
    chrome_path = config(r'chrome_path')
    chrome_driver_path = config(r'chrome_driver_path')

    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = chrome_path

    def __init__(self):
        self.driver = webdriver.Chrome(Driver.chrome_driver_path, chrome_options=Driver.chrome_options)

    def get(self, url):
        self.driver.get(url)


if __name__ == "__main__":
    driver = Driver()
    # driver.get('https://upbit.com/exchange?code=CRIX.UPBIT.KRW-BTC')
    driver.get("https://www.naver.com/")
