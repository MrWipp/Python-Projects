from time import sleep
import random
from colorama.ansi import Fore
from fake_useragent import UserAgent
from selenium import webdriver
import colorama

def open_browser():
    global driver
    options = webdriver.ChromeOptions()
    options.add_argument("--log-level=3")
    ua = UserAgent()
    user_agent = ua.random
    options.add_argument(f'user-agent={user_agent}')
    driver = webdriver.Chrome(options=options, executable_path=r'D:\chromedriver_win32\chromedriver.exe')
    driver.get('https://en.wikipedia.org/wiki/')
    print(user_agent)
    maxlimit = 1500
    __scroll_down_page(random.uniform(1, 5), maxlimit)
    sleep(2)

def scroll(maxlimit):
    scroll.starting_point = 0
    scroll.ending_point = 0
    sleep_time = random.uniform(0.01, 0.1)
    while scroll.ending_point < maxlimit:
        sleep(sleep_time)
        scroll.ending_point+=1
        print(scroll.ending_point)
        driver.execute_script(f"window.scrollBy({scroll.starting_point},{scroll.ending_point})")
    if scroll.ending_point == maxlimit:
        scroll.starting_point = scroll.ending_point
        scroll.ending_point+=maxlimit

def __scroll_down_page(speed, maxlimit):
    current_scroll_position, new_height= 0, 1
    while current_scroll_position <= maxlimit:
        current_scroll_position += speed
        print(current_scroll_position)
        driver.execute_script("window.scrollTo(0, {});".format(current_scroll_position))
        new_height = driver.execute_script("return document.body.scrollHeight")

open_browser()