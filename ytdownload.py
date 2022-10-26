from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from time import sleep
from tqdm import tqdm

videoLink = input("Enter the youtube link: ")

option = Options()
option.add_argument('headless')
prefs = {'download.default_directory' : '/mahankhanal/Desktop/'}
option.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()),options = option)

print("Redirecting to webpage...")
driver.get("https://en.savefrom.net/1-youtube-video-downloader-225/")
time.sleep(3)

print("Inputting video link...")
searchInput = driver.find_element(By.XPATH,'//*[@id="sf_url"]')
searchInput.send_keys(videoLink)
print("Downloading video in 720p resolution...")
submit = driver.find_element(By.XPATH,'//*[@id="sf_submit"]').click()
time.sleep(3)

print("Your video should be downloaded shortly...")
vid = driver.find_element(By.XPATH,'//*[@id="sf_result"]/div/div[1]/div[2]/div[2]/div[1]/a')
vid.click()
for i in tqdm(range(100)):
    sleep(0.5)

dir = "/home/ayman/Desktop"
print("Video downloaded in "+dir)
