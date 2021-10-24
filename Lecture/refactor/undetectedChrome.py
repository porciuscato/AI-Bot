if __name__ == '__main__':
    import undetected_chromedriver.v2 as uc
    import time

    site_url = 'https://www.naver.com'

    driver = uc.Chrome()
    driver.get(site_url)
    time.sleep(10)
    # driver.close()

