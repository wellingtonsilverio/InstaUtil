from selenium import webdriver
import time

class Instagram:
    browser = None
    delay = 5

    def __init__(self):
        pass

    def open(self):
        self.browser = webdriver.Chrome("./chromedriver")

    def getBrowser(self):
        return self.browser

    def close(self):
        self.browser.quit()

    def delayBrowser(self):
        time.sleep(self.delay)
        return self.browser
    
    def login(self, username, password):
        self.browser.get("https://www.instagram.com/accounts/login/?source=auth_switcher")

        inputUsername = self.delayBrowser().find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div/div/form/div/div/label/input[@name="username"]')
        inputUsername.send_keys(username)

        inputPassword = self.delayBrowser().find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div/div/form/div/div/label/input[@name="password"]')
        inputPassword.send_keys(password)

        buttonLogin = self.delayBrowser().find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div')
        buttonLogin.click()

        input("Press Enter to continue...")
    
    def getPhotosIdByTag(self, tag):
        photosLink = []
        self.browser.get("https://www.instagram.com/explore/tags/" + tag)

        for r in range(0, 5):
            self.delayBrowser().execute_script("window.scrollTo(0, 10000);")
            images = self.delayBrowser().find_elements_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div/div[1]/div/a')

            for link in images:
                photosLink.append(link.get_attribute("href"))

        return photosLink
    
    def getPhotosIdByLocation(self, location):
        self.delayBrowser().get("https://www.instagram.com/explore/tags/" + location)
    
    def getPhotosIdByUser(self, username):
        pass
    
    def getFollowersByUser(self, username):
        followersUsername = []
        
        try:
            self.browser.get("https://www.instagram.com/" + username)

            followersButton = self.delayBrowser().find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
            followersButton.click()

            followers = self.delayBrowser().find_elements_by_xpath('/html/body/div[3]/div/div[2]/ul/div/li/div/div/div/div[1]')
            
            for follower in followers:
                followersUsername.append(follower.text)
        except:
            print("Error get followers "+ username)
            pass
        
        return followersUsername
    
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
        self.browser.get("https://www.instagram.com/" + username)
        
        try:
            followButton = self.delayBrowser().find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/button')
            if followButton.text == "Follow Back" or followButton.text == "Follow":
                followButton.click()
        except:
            print("Error follow " + username)
            pass