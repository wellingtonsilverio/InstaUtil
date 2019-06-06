from selenium import webdriver
from instagram import Instagram

try:
   instagram = Instagram()
   instagram.open()
except Exception as e:
   print(e)
finally:
   instagram.close()