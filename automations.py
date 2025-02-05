from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime

chrome_driver_path = r"C:\ProgramData\chocolatey\bin\chromedriver.exe" 

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

def time_to_wait_for_target(target_hour=23, target_minute=41):
    now = datetime.datetime.now()
    target_time = now.replace(hour=target_hour, minute=target_minute, second=0, microsecond=0)
    
    if now > target_time:
        target_time += datetime.timedelta(days=1) 

    time_diff = (target_time - now).total_seconds()
    return time_diff


wait_time = time_to_wait_for_target()
print(f"Waiting for {wait_time} seconds until 11:40 PM...")

time.sleep(wait_time)

service = Service(executable_path=chrome_driver_path)

web = webdriver.Chrome(service=service, options=options)

web.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

web.get('https://forms.gle/4YgHYxd6DsxJ3VB96')

try:
    form_element = WebDriverWait(web, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.freebirdFormviewerViewFormContent")) 
    )
    print("Form Loaded Successfully!")
except Exception as e:
    print("Error while loading the form:", e)

time.sleep(1)

Name="Chinmayee"
name=web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/input')
name.send_keys(Name)

Email="test@gmail.com"
email=web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
email.send_keys(Email)

submit=web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
submit.click()

input("Press Enter to close the browser window...")
web.quit()