from selenium import webdriver
import random
from instagram import Instagram
from env import USERNAME, PASSWORD

try:
   instagram = Instagram()

   instagram.open()

   instagram.login(USERNAME, PASSWORD)

   while True:
      instagram.wait()
      instagram.follow_followers(USERNAME)
      instagram.wait()
      instagram.like_photos_with_tag_list(["puppy", "pequines", "cachorro", "animal", "dog", "cute"])
      
      # q = input("Press:\n1) Follow Followers\n2) Like photos by Tag list\n0) Quit\n")

      # if q == "1":
      #    instagram.follow_followers(USERNAME)

      # elif q == "2":
      #    instagram.like_photos_with_tag_list(["puppy", "pequines", "cachorro", "animal", "dog", "cute"])
      
      # else:
      #    break
except Exception as e:
   print("Aconteceu um erro: ")
   print(e)
   instagram.close()
finally:
   instagram.close()