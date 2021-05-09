from selenium import webdriver
from decouple import config


class Driver:
    # chrome_path = config(r'chrome_path')
    # chrome_driver_path = config(r'chrome_driver_path')
    edge_driver_path = config(r'edge_driver_path')

    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.binary_location = chrome_path

    def __init__(self):
        self.driver = webdriver.Edge(executable_path=Driver.edge_driver_path)
        # self.driver = webdriver.Chrome(Driver.chrome_driver_path, options=Driver.chrome_options)

    def get(self, url):
        self.driver.get(url)


if __name__ == "__main__":
    driver = Driver()
    # driver.get("https://www.bithumb.com/")
    # driver.get('https://coinone.co.kr/')
    driver.get('https://upbit.com/home')
    # driver.get('https://www.binance.com/ko')
    # driver.get('https://id.upbit.com/home')
    # driver.get('https://m.vglobalex.com/main')
