from time import sleep

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Orangehrm:
   def __init__(self, url):
       self.url = url
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

   def boot(self):

       self.driver.get(self.url)
       sleep(3)
       self.driver.maximize_window()

   def quit(self):
       self.driver.quit()

   def passwordreset(self):

       self.boot()
       sleep(3)
       forgetpassword = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p')
       forgetpassword.click()
       sleep(3)
       username = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/form/div[1]/div/div[2]/input')
       username.send_keys("Admin")
       sleep(5)
       reset = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/form/div[2]/button[2]')
       reset.click()
       sleep(5)
       print("Reset Password link sent successfully")


obj = Orangehrm('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
obj.passwordreset()