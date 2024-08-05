from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep



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

   def option(self):
       self.boot()
       sleep(3)
       username = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
       username.send_keys("Admin")
       password = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')

       password.send_keys("admin123")
       loginbutton = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
       loginbutton.click()
       sleep(5)

       admin = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span')
       admin.click()
       sleep(5)
       pim = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a')
       pim.click()
       sleep(5)
       leave = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a')
       leave.click()
       sleep(5)
       time = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a')
       time.click()
       sleep(5)
       recruitment = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a')
       recruitment.click()
       sleep(5)
       myinfo = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a')
       myinfo.click()
       sleep(5)
       performance = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a/span')
       performance.click()
       sleep(5)
       dashboard = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a')
       dashboard.click()
       sleep(5)
       directory = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[9]/a')
       directory.click()
       sleep(5)
       maintenance = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[10]/a')
       maintenance.click()
       sleep(5)
       cancel = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/form/div[4]/button[1]')
       cancel.click()
       sleep(3)
       claim = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[11]/a/span')
       claim.click()
       sleep(5)
       buzz = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[12]/a')
       buzz.click()
       sleep(5)
       print("Actions have been performed successfully")

obj = Orangehrm("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
obj.option()