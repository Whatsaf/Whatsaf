import argparse
from selenium import webdriver
import time
import sqlite3
conn = sqlite3.connect("F:\\Whatsaf\\Whatsaf\\db.sqlite3")
cur = conn.cursor()
def actv(brid):
    id = brid
    temp_user_data_dir = f"C:\\Users\\A\\AppData\\Local\\Google\\Chrome\\User Data\\Profile {id}"
    options = webdriver.ChromeOptions()
    options.add_argument(f'--user-data-dir={temp_user_data_dir}')
    wd = webdriver.Chrome(options=options)
    wd.get("https://web.whatsapp.com")
    time.sleep(5)
    text = wd.execute_script("""let textContent = document.querySelector('div').innerText;
                      return textContent""")
    if text.__contains__("Use WhatsApp on your computer"):
        cur.execute('''UPDATE WhatsafPortal_userdetail SET Active = false''')
    else:
        cur.execute('''UPDATE WhatsafPortal_userdetail SET Active = true''')
    conn.commit()
    conn.close()
parser = argparse.ArgumentParser()
parser.add_argument("id")
args = parser.parse_args()
actv(args.id)