# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 15:40:09 2020

@author: 71020
"""
import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

USERNAME = '' # 输入账号
PASSWORD = '' # 输入密码
seconds = random.randint(2, 5)

class Baidu(object):
    
    def __init__(self):
        print("selenium login...")
        pass
    
    def auto_login(self):
        
        chrome_options = Options()
        
        # 后台运行chrome
        chrome_options.add_argument('headless')
        
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)
        url = "https://www.baidu.com"
        driver.get(url)

        # 点击 登录 按钮
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#u1 > a.lb'))).click()
        # select 用户名登陆
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#TANGRAM__PSP_11__footerULoginBtn'))).click()
        time.sleep(seconds)
        
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#TANGRAM__PSP_11__userName'))).send_keys(USERNAME)
        time.sleep(seconds)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#TANGRAM__PSP_11__password'))).send_keys(PASSWORD)
        time.sleep(seconds)
        # 勾选取消下次自动登录
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#TANGRAM__PSP_11__memberPassLabel'))).click()
        time.sleep(seconds)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#TANGRAM__PSP_11__submit'))).click()

        print("login sucessfully")
        print(type(driver.page_source))
    pass

if __name__ == "__main__":
    baidu = Baidu()
    baidu.auto_login()
