"""
台北市立大理高中
113年資訊研究社

Instgram自動發訊息-基礎版

Github庫: https://github.com/txaions/tp_tlsh_edu_csc__0920

考量到教學目的，本程式以最基礎的語法撰寫，並以最直觀的方式呈現。故無按照約定俗成的寫法撰寫。
建議有基礎的同學可以參考進階版。並且參考Python-PEP8規範讓你的程式碼更具可讀性、可維護性、可擴展性。
"""

#=======================================================================#
"""
導入模組

:note:
    這段程式碼的作用是導入我們需要的模組。
"""

import time # 時間

from selenium import webdriver # 驅動
from selenium.webdriver.chrome.service import Service # 服務
from selenium.webdriver.common.by import By # 定位
from selenium.webdriver.support import expected_conditions as EC # 等待條件
from selenium.webdriver.support.wait import WebDriverWait # 等待

from webdriver_manager.chrome import ChromeDriverManager # 自動安裝ChromeDriver

#=======================================================================#
"""
定義變數

:note:
    尚未有基礎的同學對於 變數、常數 定義可能還不是很熟悉，推薦可以參考以下文章。
    https://hackmd.io/@amostsai/Syg8494LW?type=view
"""

ACCOUNT = "YOUR_ACCOUNT" # 帳號
PASSWORD = "YOUR_PASSWORD" # 密碼
INS_UID = "YOUR_GOAL" # 目標
TIMES = 10 # 次數
CONTENT = "YOUR_CONTENT" # 內容

#=======================================================================#

"""
初始化

:note:
    粗略來說，這段程式碼的作用是：
    1. 開啟瀏覽器
    2. 前往Instagram
:warning:
    本文皆以簡單白話文解釋，非透過專業術語解釋，同學們可以自行搜尋 ChromeDriver 的相關資訊。
"""
#----------------------------------------------------------------------#
"""
my_chrome_driver_path = ChromeDriverManager().install()

:note:
    用於下載ChromeDriver，並將其 路徑 存入 my_chrome_driver_path 變數中。
    同學們可以 print 出來看看。
"""
my_chrome_driver_path = ChromeDriverManager().install() # 下載ChromeDriver
#----------------------------------------------------------------------#
"""
BROWSER = webdriver.Chrome(service=Service(my_chrome_driver_path))

:note:
    用於建立瀏覽器，可以看到我們將 my_chrome_driver_path 變數傳入 service 參數中。
    同學可以簡單理解為 webdriver.Chrome(service=Service("路經")) 就是我們人類開啟瀏覽器的方式。
    只是我們是透過程式碼去開啟瀏覽器。
"""
BROWSER = webdriver.Chrome(service=Service(my_chrome_driver_path)) # 建立瀏覽器
#----------------------------------------------------------------------#
"""
BROWSER.get("https://www.instagram.com/")
用於前往 Instagram 首頁。

:note:
    這段程式碼的作用是前往 Instagram 首頁。簡單來說我們剛剛已經開啟瀏覽器並將他保存到 BROWSER 變數中。
    所以我們可以將 BROWSER 當作我們瀏覽器的代表，而語法 .get("網址") 就是我們用瀏覽器前往到 目標網址。
"""
BROWSER.get("https://www.instagram.com/") # 前往Instagram
#=======================================================================#

"""
現在我們想想，如果我們要登入 Instagram 需要做什麼事情？

1. 輸入帳號、密碼
2. 點擊登入

我們再想想我們人類在登入 Instagram 的時候，我們會做什麼事情？

1. 找到 帳號、密碼 欄位在哪裡，找到後輸入帳號、密碼
2. 找到 登入 按鈕在哪裡，找到後點擊

我們再把他細分下來

STEP 1. 找到位置
1. 帳號、密碼 欄位在哪裡?
2. 登入 按鈕在哪裡?

STEP 2. 做什麼
1. 輸入帳號、密碼
2. 點擊登入

ok，我們現在開始實作
"""

#----------------------------------------------------------------------#
"""
程式語言，顧名思義就是和機器溝通的語言，機器看得懂，人類看不懂。因此我將這段程式碼拆解成兩個部分並翻譯成人類語言。
各位有發現嗎? 其實工程師更像是翻譯員，將人類的語言翻譯成機器看得懂的語言。當然，這只是比喻，實際上工程師的工作內容遠比這複雜。

所以，我會將下方的程式碼翻譯成 人類語言 並解釋給各位聽。

WebDriverWait(BROWSER, 10).until(EC.visibility_of_element_located((By.NAME, "username")))

第一部分，我們先來簡單談談 單詞 的意義
    WebDriverWait 中文，等待瀏覽器
    EC.visibility_of_element_located 中文，元素可見
    By.NAME 中文，透過元素名稱定位
    By.XPATH 中文，透過元素路徑定位
    By.CSS_SELECTOR 中文，透過CSS選擇器定位
    By.ID 中文，透過元素ID定位
    By.CLASS_NAME 中文，透過元素類名定位
    By.TAG_NAME 中文，透過元素標籤定位
    By.LINK_TEXT 中文，透過元素連結文字定位
    By.PARTIAL_LINK_TEXT 中文，透過元素部分連結文字定位

第二部分，我們來談談 語法 的意義
    1. WebDriverWait(BROWSER, 10)
        人類語言: 等待瀏覽器 10秒
        
    2. .until(EC.visibility_of_element_located((By.NAME, "username")))
        人類語言: 直到透過元素名稱定位到username元素
    
    現在最後一部，我們整句話來看並翻譯成 人類語言
    3. WebDriverWait(BROWSER, 10).until(EC.visibility_of_element_located((By.NAME, "username")))
        人類語言: 等待瀏覽器 10秒直到透過元素名稱定位到username元素
        
第三部分，現在試者幫我看看你能不能看懂剩下的 USER_PASSWORD_FIELD, LOGIN_FIELD 人類語言該怎麼說。
"""

USER_NAME_FIELD = WebDriverWait(BROWSER, 10).until(EC.visibility_of_element_located((By.NAME, "username"))) # 帳號欄位
USER_PASSWORD_FIELD = WebDriverWait(BROWSER, 10).until(EC.visibility_of_element_located((By.NAME, "password"))) # 密碼欄位
LOGIN_FIELD = WebDriverWait(BROWSER, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']"))) # 登入按鈕

#=======================================================================#
"""
還記得我們剛剛拆分的步驟嗎? 

STEP 1. 找到位置
1. 帳號、密碼 欄位在哪裡?
2. 登入 按鈕在哪裡?

STEP 2. 做什麼
1. 輸入帳號、密碼
2. 點擊登入

第一步，我們剛剛已經找到位置了，現在讓我們來輸入帳號、密碼吧!

:note:
    有了剛剛的概念，我們直接來翻譯看看，這段程式碼吧!
    語法 .send_keys(內容) 的作用是將內容輸入到元素中。
    語法 .click() 的作用是點擊元素。
    語法 .send_keys(ACCOUNT) 的作用是將 ACCOUNT 變數的內容輸入到 USER_NAME_FIELD 元素中。
    語法 .send_keys(PASSWORD) 的作用是將 PASSWORD 變數的內容輸入到 USER_PASSWORD_FIELD 元素中。
"""

USER_NAME_FIELD.send_keys(ACCOUNT) # 輸入帳號
USER_PASSWORD_FIELD.send_keys(PASSWORD) # 輸入密碼
LOGIN_FIELD.click() # 點擊登入

#=======================================================================#
"""
接下來，我們要前往目標的 Instagram 帳號，並且發送訊息。

:note:
    剛剛我已經告訴你們，怎麼翻譯成 人類語言 了，所以現在來試試看你能翻譯出來嗎?
"""
time.sleep(5) # 等待登入

BROWSER.get(f"https://www.instagram.com/direct/t/{INS_UID}/") # 前往目標

time.sleep(2) # 等待

for i in range(TIMES):
    
    message_type_field = WebDriverWait(BROWSER, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]"))) # 輸入欄位
    message_type_field.send_keys(CONTENT) # 輸入內容
    
    print(f'第{i+1}次發送 = <{CONTENT}>') # 顯示發送次數
    time.sleep(1) # 等待
    
    send_button = WebDriverWait(BROWSER, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[3]"))) # 發送按鈕
    
    send_button.click() # 點擊發送
    
    time.sleep(1) # 等待
    
BROWSER.quit() # 關閉驅動
print("發送完成") # 顯示發送完成