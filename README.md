# 🛍️ SmartCart Project – Amazon Product Scraper

This is a Python automation project that logs into Amazon, searches for *Kurtis for Women*, extracts the first 5 non-sponsored products, captures their details, and saves screenshots of each product.

---

## 📁 Project Structure

```
smartcart_project/
│
├── tests/
│   ├── test_amazon_login.py         # Logs into Amazon
│   └── test_search_add_to_cart.py   # Searches Kurtis, extracts 5 valid products, takes screenshots
│
├── utils/
│   ├── __init__.py
│   ├── decrypt_credentials.py       # Decrypts email and password from secret files
│   ├── encryption.py                # Encrypts your username & password 
│   └── amazon_login.py              # Reusable login function
├── encrypted_credentials.py         #Stores encrypted credentials
├── generate_key.py                  #Generates a secret key
├── top_product.png / product_X.png  # Screenshots of top products

```

---

## 💡 Features

- 🔐 Secure login using encrypted credentials.
- 🔎 Searches for "Kurtis for Women".
- 🧹 Filters out sponsored items.
- 🛍 Extracts product title and price.
- 📸 Takes a screenshot of each product card.
- ✅ Clean and simple automation using Selenium.

---

## 🧪 How to Run

> ⚠️ Make sure you have `chromedriver` installed and in your PATH. Also, install dependencies via pip.

```bash
pip install selenium
```

### Step 1: Encrypt your Amazon credentials
Run this only once to securely save your email & password:

```bash
python utils/encrypted_credentials.py
```

It will generate `.key` and `.enc` files storing your encrypted credentials.

---

### Step 2: Run login test
This ensures that the login works:

```bash
python tests/test_amazon_login.py
```

---

### Step 3: Run product search + screenshot
This is the main script that fetches 5 non-sponsored *Kurtis*, prints their title + price, and takes screenshots:

```bash
python tests/test_search_add_to_cart.py
```

---

## 📂 Output Example

You’ll see logs like this:

```
🔍 Search submitted
✅ Product 1
🛍 Title : GoSriKi Women's Cotton Blend Kurti
💰 Price : ₹539
📸 Screenshot saved: product_1.png
...
```

And screenshots will be saved in the root folder.

## 🖥️ Output Screenshot
![output](https://github.com/user-attachments/assets/3da4c4be-1abe-4ebe-8429-236c53c0af9d)


---

## 📌 Notes

- This script handles CAPTCHA/OTP manually with a wait.
- Uses fallback CSS selectors to handle minor DOM changes.
- Currently supports **Amazon India (https://www.amazon.in)**.

---

## 🙌 Credits

Developed by Mahima Shukla 💛  
For learning, automation fun & practice!
