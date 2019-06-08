from selenium import webdriver
from instagram import Instagram
from env import USERNAME, PASSWORD

try:
   instagram = Instagram()

   instagram.open()

   instagram.login(USERNAME, PASSWORD)

   tags = ["puppy", "pequines", "cachorro", "animal", "dog"]
   for tag in tags:
      links = instagram.getPhotosIdByTag(tag)
      for link in links:
         instagram.likePhoto(link)
except Exception as e:
   print(e)
finally:
   pass
   # instagram.close()