from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

# Add account details of your facebook account that we use to sign in to tinder
EMAIL = "..."
PASS = "..."
DRIVER_PATH = "C:/Selenium/chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), executable_path=DRIVER_PATH,
                          chrome_options=options)
driver.get("https://tinder.com/")

log_in = driver.find_element(By.LINK_TEXT, "Log in")
log_in.click()
time.sleep(3)
log_in_facebook = driver.find_element(By.XPATH,
                                      '//*[@id="o1912386320"]/div/div/div[1]/div/div/div[3]/span/div[2]/button/span[2]')
log_in_facebook.click()
time.sleep(8)
driver.switch_to.window(driver.window_handles[1])
email_form = driver.find_element(By.CSS_SELECTOR, '#email')
email_form.send_keys(EMAIL)
pass_form = driver.find_element(By.CSS_SELECTOR, '#pass')
pass_form.send_keys(PASS)
pass_form.send_keys(Keys.ENTER)
time.sleep(15)
driver.switch_to.window(driver.window_handles[0])
time.sleep(5)
allow_link = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[3]/button[1]/span')
allow_link.click()
time.sleep(5)
enable_noti = driver.find_element(By.XPATH,
                                  '/html/body/div[2]/div/div/div/div/div[3]/button[2]/span')
enable_noti.click()
time.sleep(5)
while True:
    like = pass_form = driver.find_element(By.XPATH,
                                           '//*[@id="o-654199900"]/div/div[1]/div/div/main/div/div/div[1]/div/div[5]/div/div[4]/button/span/span/svg/path')
    like.click()
    time.sleep(5)
