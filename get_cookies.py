# get_cookies.py

"""
requires-python = "==3.11"
dependencies = [
   "selenium==4.22.0",
   "webdriver-manager>=4.0.2",
]
"""


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pickle

def main():
   driver_path = ChromeDriverManager().install()
   service = Service(executable_path=driver_path)
   X = webdriver.Chrome(service=service)
   X.get('https://x.com/i/flow/login') #対象ログインページ
   print("ログインしたら何か入力してください。")
   val = input()

   pickle.dump(X.get_cookies() , open("cookies.pkl","wb"))

   X.quit()


if __name__ == '__main__':
   main()