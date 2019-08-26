from selenium import webdriver
import time
from random import randrange

class Instagram:
    browser = None
    delay = 5

    def __init__(self):
        pass

    def open(self):
        chrome_options = webdriver.ChromeOptions()
        CHROMEDRIVER_PATH = "./chromedriver"

        # chrome_options.binary_location = CHROMEDRIVER_PATH
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')

        self.browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)

    def close(self):
        self.browser.quit()

    def delay_browser(self):
        time.sleep(self.delay)
        return self.browser
    
    def login(self, username, password):
        self.browser.get("https://www.instagram.com/accounts/login/?source=auth_switcher")

        input_username = self.delay_browser().find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div/div/form/div/div/label/input[@name="username"]')
        input_username.send_keys(username)

        input_password = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div/div/form/div/div/label/input[@name="password"]')
        input_password.send_keys(password)

        button_login = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div')
        button_login.click()
    
    def get_photos_id_by_tag(self, tag):
        photos_link = []
        self.browser.get("https://www.instagram.com/explore/tags/" + tag)

        for i in range(0, 20):
            self.delay_browser().execute_script("window.scrollTo(0, 10000);")
            images = self.delay_browser().find_elements_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div/div[1]/div/a')

            for link in images:
                photos_link.append(link.get_attribute("href"))

        return photos_link
    
    def get_photos_id_by_location(self, location):
        self.delay_browser().get("https://www.instagram.com/explore/tags/" + location)
    
    def get_photos_id_by_user(self, username):
        pass
    
    def get_followers_by_user(self, username):
        followers_username = []
        
        try:
            self.browser.get("https://www.instagram.com/" + username)

            followers_button = self.delay_browser().find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
            followers_button.click()

            followers = self.delay_browser().find_elements_by_xpath('/html/body/div[3]/div/div[2]/ul/div/li/div/div/div/div[1]')
            
            for follower in followers:
                followers_username.append(follower.text)
        except:
            print("Error get followers "+ username)
            
        
        return followers_username
    
    def get_followings_by_user(self, username):
        pass
    
    def like_photo(self, link_photo):
        self.delay_browser().get(link_photo)
        
        try:
            button_like = self.delay_browser().find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[1]/span[1]/button/span[@aria-label="Like"]')
            button_like.click()
        except:
            print("Error like "+ link_photo)
            

    
    def follow_user(self, username):
        self.browser.get("https://www.instagram.com/" + username)
        
        try:
            follow_nutton = self.delay_browser().find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button')
            if follow_nutton.text == "Follow Back" or follow_nutton.text == "Follow":
                follow_nutton.click()
                print("follow " + username)
        except:
            print("Error follow " + username)

    def follow_followers(self, username):
        try:
            followrs = self.get_followers_by_user(username)
            for follow in followrs:
                followeds = self.get_followers_by_user(follow)
                for followed in followeds:
                    self.follow_user(followed)
        except:
            print("Erro em follow followers")


    def like_photos_with_tag_list(self, tags):
        all_links = []
        try:
            number_tags = len(tags)
            for i in range(0, number_tags):
                random_tag = randrange(number_tags)
                links = self.get_photos_id_by_tag(tags[random_tag])
                for link in links:
                    all_links.append(link)
            for link in all_links:
                self.like_photo(link)
        except:
            print("Erro em like photos with tag list")
            