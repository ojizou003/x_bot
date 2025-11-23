# X_morning_bot.py

# 今日のひとこと(79文字以内。ただし、linkありの場合は59文字以内)
text = f''
link = 'https://weather.yahoo.co.jp/weather/'
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pickle


weather_url = 'https://weather.yahoo.co.jp/weather/jp/43/8610.html'
X_url = 'https://x.com'

options = Options()
options.add_argument("--headless")
# service = Service('C:/auto/chromedriver.exe')
# driver_path = ChromeDriverManager().install()
# service = Service(executable_path=driver_path)

# yahoo天気予報から本日の熊本市の天気、最高気温、最低気温を取得
y = webdriver.Chrome(options=options)
y.get(weather_url)
y.implicitly_wait(10)

day = y.find_element(By.XPATH, '//table/tbody/tr/td[1]/div/p[1]/span[1]').text
youbi = y.find_element(By.XPATH, '//table/tbody/tr/td[1]/div/p[1]/span[2]').text
today = f'{day}({youbi})'

weather = y.find_element(By.CLASS_NAME, 'pict').text
high = y.find_element(By.CLASS_NAME, 'high').text
low = y.find_element(By.CLASS_NAME, 'low').text

y.quit()

# Xにログイン
X = webdriver.Chrome(options=options)
cookies = pickle.load(open("cookies.pkl", "rb"))
X.get(X_url)
X.implicitly_wait(10)
for cookie in cookies:
    X.add_cookie(cookie)
X.get(X_url)
sleep(5)
# ポストの作成
post = f'おはようございます\u266a\n{today}、今日の熊本市は{weather}。\n最高気温{high}、最低気温{low}の予報です。\n{text}\n本日もよろしくお願いします\u263a\n{link}'
# ポストの入力
X.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-block.public-DraftStyleDefault-ltr').send_keys(post)
sleep(5)
# ポストの投稿
X.find_element(By.CSS_SELECTOR, 'button.css-175oi2r.r-sdzlij.r-1phboty.r-rs99b7.r-lrvibr.r-1cwvpvk.r-2yi16.r-1qi8awa.r-3pj75a.r-1loqt21.r-o7ynqc.r-6416eg.r-1ny4l3l').click()
sleep(5)

X.quit()
