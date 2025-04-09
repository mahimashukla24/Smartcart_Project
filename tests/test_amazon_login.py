from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from utils.amazon_login import login_to_amazon

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)

login_to_amazon(driver, wait)

# Close browser after check
driver.quit()
