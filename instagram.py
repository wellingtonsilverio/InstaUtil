from selenium import webdriver
import time

class Instagram:
    browser = None
    delay = 5

    def __init__(self):
        pass

    def open(self):
        self.browser = webdriver.Chrome("./chromedriver")
        self.browser.get("http://instagram.com/")

    def getBrowser(self):
        return self.browser

    def close(self):
        self.browser.quit()

    def delayBrowser(self):
        time.sleep(self.delay)
        return self.browser
    
    def login(self, username, password):
        buttonGoLogin = self.delayBrowser().find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a')
        buttonGoLogin.click()

        inputUsername = self.delayBrowser().find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div/div/form/div/div/div/input[@name="username"]')
        inputUsername.send_keys(username)

        inputPassword = self.delayBrowser().find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div/div/form/div/div/div/input[@name="password"]')
        inputPassword.send_keys(password)

        buttonLogin = self.delayBrowser().find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button')
        buttonLogin.click()
    
    def getPhotosIdByTag(self, tag):
        photosLink = []
        self.delayBrowser().get("https://www.instagram.com/explore/tags/" + tag)

        for r in range(0, 10):
            self.delayBrowser().execute_script("window.scrollTo(0, 10000);")
            images = self.delayBrowser().find_elements_by_xpath('//*[@id="react-root"]/section/main/article/div/div/div/div/a')

            for link in images:
                photosLink.append(link.get_attribute("href"))

        return photosLink
    
    def getPhotosIdByLocation(self, location):
        self.delayBrowser().get("https://www.instagram.com/explore/tags/" + location)
    
    def getPhotosIdByUser(self, username):
        pass
    
    def getFollowrsByUser(self, username):
        pass
    
    def getFollowingsByUser(self, username):
        pass
    
    def likePhoto(self, linkPhoto):
        self.delayBrowser().get(linkPhoto)
        try:
            buttonLike = self.delayBrowser().find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[1]/span[1]/button/span[@aria-label="Like"]')
            buttonLike.click()
        except:
            print("Error like "+ linkPhoto)
            pass

    
    def followUser(self, username):
        pass