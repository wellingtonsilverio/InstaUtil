from selenium import webdriver
from instagram import Instagram
from env import USERNAME, PASSWORD

try:
   instagram = Instagram()

   instagram.open()

   instagram.login(USERNAME, PASSWORD)

   followrs = instagram.getFollowersByUser(USERNAME)
   for follow in followrs:
      followeds = instagram.getFollowersByUser(follow)
      for followed in followeds:
         instagram.followUser(followed)

   # tags = ["puppy", "pequines", "cachorro", "animal", "dog", "cute"]
   # for tag in tags:
   #    links = instagram.getPhotosIdByTag(tag)
   #    for link in links:
   #       instagram.likePhoto(link)
except Exception as e:
   print(e)
finally:
   pass
   # instagram.close()