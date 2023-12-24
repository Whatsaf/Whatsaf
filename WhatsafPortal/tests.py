from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
import smtplib
import psutil

id = "84586292"
number = "+916355853038"
email = "ceo@whatsaf.in"
temp_user_data_dir = f"C:\\Users\\A\\AppData\\Local\\Google\\Chrome\\User Data\\Profile {id}"

options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "localhost:8080")
wd = webdriver.Chrome(options=options)
wd.get("https://web.whatsapp.com")

text = wd.execute_script("""let textContent = document.querySelector('div').innerText;
                  return textContent""")
time.sleep(5)
if text.__contains__("Use WhatsApp on your computer"):
    print("Yes")
else:
    print("No")

