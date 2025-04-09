from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.decrypt_credentials import decrypt_credentials
import time

def login_to_amazon(driver, wait):
    username, password = decrypt_credentials()

    login_url = (
        "https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0"
        "&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3F_encoding%3DUTF8%26ref_%3Dnav_ya_signin"
        "&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select"
        "&openid.assoc_handle=inflex"
        "&openid.mode=checkid_setup"
        "&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select"
        "&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0"
    )
    driver.get(login_url)

    print(f"🌐 Current URL: {driver.current_url}")
    print(f"📄 Page Title: {driver.title}")

    email_input = wait.until(EC.presence_of_element_located((By.ID, "ap_email")))
    email_input.send_keys(username)
    driver.find_element(By.ID, "continue").click()

    password_input = wait.until(EC.presence_of_element_located((By.ID, "ap_password")))
    password_input.send_keys(password)
    driver.find_element(By.ID, "signInSubmit").click()

    print("⏳ Waiting 30 seconds for CAPTCHA or OTP if any...")
    time.sleep(30)

    # ✅ Automatically wait until the page shows your name
    try:
        wait.until(EC.text_to_be_present_in_element(
            (By.ID, "nav-link-accountList-nav-line-1"),
            "Hello, Mahima Shukla"
        ))
        print("✅ Login successful!")
    except:
        print("⚠️ Login might not have succeeded. Please check manually.")
