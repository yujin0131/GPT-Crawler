import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from sql import select_search, insert_search
from selenium.webdriver.common.by import By


url = "https://wtech.inswave.kr/websquare/websquare.html?w2xPath=/ws/index.xml&inPath=/ws/member/login.xml"

driver = webdriver.Chrome('/Users/beomi/Downloads/chromedriver')
driver.implicitly_wait(3)

def login_click():
    
    driver.get(url)
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '#wf_frame_inputUserId').send_keys('lyujin@inswave.com')
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '#wf_frame_inputPassWord').send_keys('Wlsehf0014@')
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '#wf_frame_btnLogin').click()
    
    detail_search()
    

def detail_search():
    searchText = select_search()
    print("############### searchText ##############")
    print(searchText[0][0])
    print("############### searchText.size ##############")
    print(len(searchText))
    for detail in searchText:
        detail_page(detail[0])    



def detail_page(searchText):
    detail = 4;
    print("############ detail_page ################")
    print(searchText)
    for i in range(1, 11):
        URL = "https://wtech.inswave.kr/websquare/websquare.html?w2xPath=/ws/index.xml&inPath=/ws/qna/qna_list.xml&searchType=title&searchText=" + searchText + "&curPage=" + str(i)
        driver.get(f"{URL}")
        print("################ URL ##################")
        print(URL)
        
        for j in range(detail, 10):
            
            img_name = '#wf_frame_grid1_cell_' + str(j) + '_1 > img'
            img = driver.find_element(By.CSS_SELECTOR, img_name)
            if img == '':
                continue
            else :
                img = img.get_attribute('src')
                print("############ img ############3333")
                print(img)

                blue = "https://wtech.inswave.kr/images/ico_grd_blu.gif"
                
                if img != blue:
                    continue
                else :
                
                    detail_name = '#wf_frame_grid1_cell_' + str(j) + '_2 > nobr > a';
                    data = []
                    
                    title = driver.find_element(By.CSS_SELECTOR, detail_name).text
                    print("################## title ################")
                    print(title)
                    data.append(title)
                    driver.find_element(By.CSS_SELECTOR, detail_name).click()
                                
                    content = driver.find_element(By.CSS_SELECTOR, '#wf_frame_txtContent').text
                    
                    start = content.find('<< 개요 >>')
                    last = content.find('<< 버전 및 빌드일 >>')
                    final_content = content[start:last]
                    data.append(final_content)
                    
                    insert_search(data)
                    
                    driver.back()
                
    
    
    