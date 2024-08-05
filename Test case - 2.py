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

   def adminpage(self):
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
# title of the webpage
        title = self.driver.title
# title
        expected_title = "OrangeHRM"
        if expected_title in title:
            print("Validation successful: Title is OrangeHRM")
        else:
            print("Validation failed: Title is not OrangeHRM")
        sleep(5)
        user_management = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span')
        user_management.click()
        sleep(5)
        job = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span')
        job.click()
        sleep(5)
        organisation = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/span')
        organisation.click()
        sleep(5)
        qualification = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]/span')
        qualification.click()
        sleep(5)
        nationality = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[5]')
        nationality.click()
        sleep(5)
        corporate_branding = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[6]')
        corporate_branding.click()
        sleep(5)
        configuration = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[7]')
        configuration.click()
        sleep(5)
        print("Above actions has been sucesufully performed")


obj = Orangehrm("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
obj.adminpage()