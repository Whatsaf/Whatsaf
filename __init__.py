from selenium import webdriver
from time import sleep

chromeLoc = "C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\User Data\\Profile {profNum}"
options = webdriver.ChromeOptions()
options.add_argument(f'--user-data-dir={chromeLoc.format(profNum = "30082006")}')
wd = webdriver.Chrome(options=options)
wd.get(f"https://web.whatsapp.com/")
sleep(45345)