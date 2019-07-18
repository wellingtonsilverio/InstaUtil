from selenium import webdriver
from instagram import Instagram
from env import USERNAME, PASSWORD

def follow_followers(username):
   try:
      followrs = instagram.get_followers_by_user(username)
      for follow in followrs:
         followeds = instagram.get_followers_by_user(follow)
         for followed in followeds:
            instagram.follow_user(followed)
   except:
      print("Erro em follow_followers")


def like_photos_with_tag_list(tags):
   try:
      for tag in tags:
         links = instagram.get_photos_id_by_tag(tag)
         for link in links:
            instagram.like_photo(link)
   except:
      print("Erro em like_photos_with_tag_list")

try:
   instagram = Instagram()

   instagram.open()

   instagram.login(USERNAME, PASSWORD)

   while True:
      q = input("Press:\n1) Follow Followers\n2) Like photos by Tag list\n0) Quit\n")

      if q == "1":
         follow_followers(USERNAME)

      elif q == "2":
         like_photos_with_tag_list(["puppy", "pequines", "cachorro", "animal", "dog", "cute"])
      
      else:
         break
except Exception as e:
   print("Aconteceu um erro: ")
   print(e)
   instagram.close()
finally:
   instagram.close()