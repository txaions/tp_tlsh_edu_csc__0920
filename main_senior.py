"""
台北市立大理高中
113年資訊研究社

Instgram自動發訊息-進階版

Github庫: https://github.com/txaions/tp_tlsh_edu_csc__0920
"""


import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager


class Client:
    """
    客戶端
    """
    
    def __init__(self, account:str=None, password:str=None):
        """
        初始化
        
        :params:
            account:str 帳號
            password:str 密碼
        """
        
        self.account = account
        self.password = password
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        
    def login(self) -> None:
        """
        登入
        """
        
        self.driver.get("https://www.instagram.com/")
        
        user_name_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "username")))
        user_password_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "password")))
        login_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']")))
        
        user_name_field.send_keys(self.account)
        user_password_field.send_keys(self.password)
        login_field.click()
        time.sleep(5)
        
    def send_message(self, goal:str=None, times:int=1, content:str="預設內容") -> None:
        """
        發送訊息
        
        :params:
            goal:str 目標ID
            times:int 次數
            content:str 內容
        """
        
        self.driver.get(f"https://www.instagram.com/direct/t/{goal}/")
        time.sleep(2)
        
        for i in range(times):
            
            message_type_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]")))
            message_type_field.send_keys(content)
            
            print(f'第{i+1}次發送 - <{content}>')
            time.sleep(1)
            
            send_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[3]")))
            send_button.click()
            time.sleep(1)
        
        print("發送完成")
        
    def close(self):
        """
        結束
        """
        
        self.driver.quit()


if __name__ == "__main__":
    
    client = Client(account="YOUR_ACCOUNT", password="YOUR_PASSWORD")    
    client.login()
    client.send_message(goal="INSTAGRAM_UID", times=10, content="YOUR_CONTENT")
    client.close()