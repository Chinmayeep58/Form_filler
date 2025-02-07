# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import datetime

# # Path to your ChromeDriver
# chrome_driver_path = r"C:\ProgramData\chocolatey\bin\chromedriver.exe"

# # Your Naukri login details
# naukri_email = "devikamya43@gmail.com"
# naukri_password = "Test@123"

# # Job search criteria
# job_keyword = "Python Developer"
# job_location = "Bangalore"

# # Function to calculate wait time until 11 AM
# def time_to_wait_for_target(target_hour=10, target_minute=56):
#     now = datetime.datetime.now()
#     target_time = now.replace(hour=target_hour, minute=target_minute, second=0, microsecond=0)
    
#     if now > target_time:
#         target_time += datetime.timedelta(days=1)  # Schedule for the next day if it's already past 11 AM

#     time_diff = (target_time - now).total_seconds()
#     return time_diff

# # Wait until 11 AM
# wait_time = time_to_wait_for_target()
# print(f"Waiting for {wait_time} seconds until 11 AM...")
# time.sleep(wait_time)

# # Configure Selenium WebDriver
# options = webdriver.ChromeOptions()
# options.add_argument("--start-maximized")
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option("useAutomationExtension", False)
# options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

# service = Service(executable_path=chrome_driver_path)
# web = webdriver.Chrome(service=service, options=options)

# # Open Naukri.com
# web.get("https://www.naukri.com/nlogin/login")

# # Log in to Naukri
# try:
#     email_field = WebDriverWait(web, 10).until(EC.presence_of_element_located((By.ID, "usernameField")))
#     email_field.send_keys(naukri_email)
    
#     password_field = web.find_element(By.ID, "passwordField")
#     password_field.send_keys(naukri_password)
    
#     login_button = web.find_element(By.XPATH, '//button[contains(text(), "Login")]')
#     login_button.click()
#     print("Logged in successfully!")
# except Exception as e:
#     print("Error during login:", e)
#     web.quit()
#     exit()

# time.sleep(5)

# # Search for jobs
# try:
#     search_box = WebDriverWait(web, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Enter skills / designations / companies"]')))
#     search_box.send_keys(job_keyword)
    
#     location_box = web.find_element(By.XPATH, '//input[@placeholder="Enter location"]')
#     location_box.send_keys(job_location)

#     search_box.send_keys(Keys.ENTER)
#     print("Searching for jobs...")
# except Exception as e:
#     print("Error while searching for jobs:", e)
#     web.quit()
#     exit()

# time.sleep(5)

# # Apply for jobs
# applied_count = 0
# try:
#     job_listings = web.find_elements(By.XPATH, '//div[@class="list"]/descendant::a[@class="title fw500 ellipsis"]')
    
#     for job in job_listings[:5]:  # Apply to first 5 jobs
#         job.click()
#         time.sleep(3)

#         # Switch to the new job tab
#         web.switch_to.window(web.window_handles[1])

#         try:
#             apply_button = WebDriverWait(web, 5).until(
#                 EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "Easy Apply")]'))
#             )
#             apply_button.click()
#             applied_count += 1
#             print(f"Applied to job {applied_count}")

#         except Exception:
#             print("No Easy Apply button found, skipping this job.")

#         web.close()  # Close job tab
#         web.switch_to.window(web.window_handles[0])  # Switch back to main tab

# except Exception as e:
#     print("Error while applying for jobs:", e)

# # Log out
# try:
#     web.get("https://www.naukri.com/mnjuser/homepage")
#     profile_dropdown = WebDriverWait(web, 10).until(
#         EC.presence_of_element_located((By.XPATH, '//div[@class="nI-gNb-drawer__icon"]'))
#     )
#     profile_dropdown.click()

#     logout_button = WebDriverWait(web, 5).until(
#         EC.presence_of_element_located((By.XPATH, '//a[text()="Logout"]'))
#     )
#     logout_button.click()
#     print("Logged out successfully.")
# except Exception as e:
#     print("Error during logout:", e)

# # Close browser
# web.quit()


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime

# Path to your ChromeDriver
chrome_driver_path = r"C:\ProgramData\chocolatey\bin\chromedriver.exe"

# Your Naukri login details
naukri_email = "devikamya43@gmail.com"
naukri_password = "Test@123"

# Job search criteria
job_keyword = "Python Developer"
job_location = "Bangalore"

# Function to calculate wait time until 11 AM
def time_to_wait_for_target(target_hour=11, target_minute=8):
    now = datetime.datetime.now()
    target_time = now.replace(hour=target_hour, minute=target_minute, second=0, microsecond=0)
    
    if now > target_time:
        target_time += datetime.timedelta(days=1)  # Schedule for the next day if it's already past 11 AM

    time_diff = (target_time - now).total_seconds()
    return time_diff

# Wait until 11 AM
wait_time = time_to_wait_for_target()
print(f"Waiting for {wait_time} seconds until 11 AM...")
time.sleep(wait_time)

# Configure Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

service = Service(executable_path=chrome_driver_path)
web = webdriver.Chrome(service=service, options=options)

# Open Naukri.com
web.get("https://www.naukri.com/nlogin/login")

# Log in to Naukri
try:
    email_field = WebDriverWait(web, 10).until(EC.presence_of_element_located((By.ID, "usernameField")))
    email_field.send_keys(naukri_email)
    
    password_field = web.find_element(By.ID, "passwordField")
    password_field.send_keys(naukri_password)
    
    login_button = web.find_element(By.XPATH, '//button[contains(text(), "Login")]')
    login_button.click()
    print("Logged in successfully!")
except Exception as e:
    print("Error during login:", e)
    web.quit()
    exit()

time.sleep(5)

# Search for jobs
try:
    search_box = WebDriverWait(web, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[3]/div[2]/div[1]/div/div/div[2]/div/div/div/input'))
    )
    search_box.send_keys(job_keyword)
    
    location_box = web.find_element(By.XPATH, '//*[@id="root"]/div[3]/div[2]/div[1]/div/div/div[6]/div/div/div/input')
    location_box.send_keys(job_location)
    location_box.send_keys(Keys.ENTER)  # Trigger search
    
    print("Searching for jobs...")
except Exception as e:
    print("Error while searching for jobs:", e)
    web.quit()
    exit()

time.sleep(5)

# Apply for jobs
applied_count = 0
try:
    job_listings = web.find_elements(By.XPATH, '//article[@class="jobTuple bgWhite br4 mb-8"]')  # Adjusted XPath

    for job in job_listings[:5]:  # Apply to first 5 jobs
        try:
            job.click()
            time.sleep(3)

            # Switch to the new job tab
            web.switch_to.window(web.window_handles[1])

            apply_button = WebDriverWait(web, 5).until(
                EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "Apply")]'))
            )
            apply_button.click()
            applied_count += 1
            print(f"Applied to job {applied_count}")

            web.close()  # Close job tab
            web.switch_to.window(web.window_handles[0])  # Switch back to main tab

        except Exception:
            print(f"Could not apply to job {applied_count + 1}. Moving to the next job.")
            web.close()  # Close job tab
            web.switch_to.window(web.window_handles[0])  # Switch back to main tab

except Exception as e:
    print("Error while applying for jobs:", e)

# Log out
try:
    profile_dropdown = WebDriverWait(web, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "nI-gNb-drawer__icon")]'))
    )
    profile_dropdown.click()

    logout_button = WebDriverWait(web, 5).until(
        EC.presence_of_element_located((By.XPATH, '//a[text()="Logout"]'))
    )
    logout_button.click()
    print("Logged out successfully.")
except Exception as e:
    print("Error during logout:", e)

# Close browser
web.quit()
