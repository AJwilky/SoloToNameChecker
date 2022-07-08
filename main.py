import time
import colorama
from colorama import Fore
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
colorama.init()

input("Press enter to start: ")

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)



with open("names.txt", 'r') as f:
    for name in f:
        names = name[:-1]

        driver.get(f"https://solo.to/{names}")
        time.sleep(1)
        if ("Hmm..." not in driver.page_source):
            print(Fore.RED + f"{names} is taken")
        else:
            print(Fore.GREEN + f"Name not taken")
        
driver.quit()
