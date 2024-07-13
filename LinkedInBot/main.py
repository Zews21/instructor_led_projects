from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import os
import time

PHONE = os.environ("PHONE")
EMAIL = os.environ("EMAIL")
PASSWORD = os.environ("PASSWORD")
LINKEDIN_LINK = os.environ("LINKEDIN_LINK")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(f'{LINKEDIN_LINK}')

time.sleep(2)

sign_in_button = driver.find_element(by=By.XPATH, value='/html/body/div[3]/header/nav/div/a[2]')

sign_in_button.click()

email = driver.find_element(by=By.XPATH, value='//*[@id="username"]')
email.click()
email.send_keys(f'{EMAIL}')

password = driver.find_element(by=By.XPATH, value='//*[@id="password"]')
password.click()
password.send_keys(f'{PASSWORD}')


def abort_application():

    close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()

    time.sleep(2)

    discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()


confirm = driver.find_element(by=By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')
confirm.click()
time.sleep(2)

all_jobs = driver.find_elements(by=By.CSS_SELECTOR, value='.jobs-search-results__list-item')

for job in all_jobs:
    job.click()
    time.sleep(1)
    try:
        easy_apply = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
        easy_apply.click()

        time.sleep(2)
        phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        if phone.text == "":
            phone.send_keys(PHONE)
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            abort_application()
            print("Complex application, skipped.")
            continue
        else:
            print("Submitting job application")
            submit_button.click()

        time.sleep(2)

        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        abort_application()
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()

