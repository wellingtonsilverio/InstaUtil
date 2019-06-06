from selenium import webdriver

class Instagram:
    browser = None

    def __init__(self):
        pass

    def open(self):
        self.browser = webdriver.Chrome("./chromedriver")
        self.browser.get("http://instagram.com/")

    def getBrowser(self):
        return self.browser

    def close(self):
        self.browser.quit()