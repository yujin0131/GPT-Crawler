import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


url = "https://wtech.inswave.kr/websquare/websquare.html?w2xPath=/ws/index.xml&inPath=/ws/member/login.xml"


def login_click():
    print("############### eee #########")
    #wf_frame_inputUserId
    driver = webdriver.Chrome('/Users/beomi/Downloads/chromedriver')
    driver.implicitly_wait(3)
    driver.get(url)
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '#wf_frame_inputUserId').send_keys('lyujin@inswave.com')
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '#wf_frame_inputPassWord').send_keys('Wlsehf0014@')
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '#wf_frame_btnLogin').click()
    time.sleep(1)
    #wf_frame_grid1_cell_4_1 > img
    
    for i in range(1, 10):
        URL = "https://wtech.inswave.kr/websquare/websquare.html?w2xPath=/ws/index.xml&inPath=/ws/qna/qna_list.xml&searchType=title&searchText=gridView&curPage=" + str(i)
        driver.get(f"{URL}")
        print("################ URL ##################")
        print(URL)
        detail = 4;
        
        for j in range(detail, 9):
            detail_name = '#wf_frame_grid1_cell_' + str(j) + '_2 > nobr > a';
            driver.find_element(By.CSS_SELECTOR, detail_name).click()
                        
            print("##################### detail_name ###################")
            print(detail_name)
            
            title = driver.find_element(By.CLASS_NAME, 'w2textbox').text
            print("############## title :  ##################")
            print(title)
            content = driver.find_element(By.CSS_SELECTOR, '#wf_frame_txtContent').text
            print("############## content  ##################")
             
            print(content)
            driver.back()
            
    
    while(True):
        pass
    