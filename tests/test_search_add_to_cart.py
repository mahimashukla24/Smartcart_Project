import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.amazon_login import login_to_amazon

# 🚀 Step 1: Setup
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)

# 🔐 Step 2: Login
login_to_amazon(driver, wait)
time.sleep(5)

# 🔍 Step 3: Search for Kurtis for Women
try:
    search_box = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
    search_box.clear()
    search_box.send_keys("Kurtis for Women")
    search_box.send_keys(Keys.RETURN)
    print("🔍 Search triggered successfully.")
except Exception as e:
    print(f"❌ Could not find search box: {e}")
    driver.quit()
    sys.exit()

time.sleep(5)

# 🎯 Step 4: Select 5 non-sponsored products
products = driver.find_elements(By.CSS_SELECTOR, "div.s-main-slot div[data-component-type='s-search-result']")
print(f"🔢 Total products found: {len(products)}")

non_sponsored_products = []
for prod in products:
    try:
        if prod.find_elements(By.XPATH, ".//span[text()='Sponsored']"):
            continue
        non_sponsored_products.append(prod)
        if len(non_sponsored_products) == 5:
            break
    except:
        continue

print(f"✅ Non-sponsored products selected: {len(non_sponsored_products)}")

# 📸 Step 5: Print info + screenshots
for idx, product in enumerate(non_sponsored_products):
    try:
        # Scroll into view
        driver.execute_script("arguments[0].scrollIntoView();", product)
        time.sleep(2)

        # Title
        try:
            title_elem = product.find_element(By.CSS_SELECTOR, "h2 span")
            title = title_elem.text.strip()
        except:
            title = "N/A"

        # Price
        try:
            price_elem = product.find_element(By.CSS_SELECTOR, "span.a-price-whole")
            price = price_elem.text.strip()
        except:
            price = "N/A"

        print(f"\n✅ Product {idx+1}")
        print(f"🛍 Title: {title}")
        print(f"💰 Price: ₹{price}")

        # Screenshot
        screenshot_name = f"product_{idx+1}.png"
        product.screenshot(screenshot_name)
        print(f"📸 Screenshot saved: {screenshot_name}")

    except Exception as e:
        print(f"⚠ Failed to process product {idx+1}: {e}")

# ✅ Wrap-up
print("\n✅ All done! Closing browser in 5 seconds...")
time.sleep(5)
driver.quit()
