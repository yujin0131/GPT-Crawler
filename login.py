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
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, '#wf_frame_inputUserId').send_keys('lyujin@inswave.com')
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, '#wf_frame_inputPassWord').send_keys('Wlsehf0014@')
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '#wf_frame_btnLogin').click()
    
    detail_search()
    

def detail_search():
    searchText = select_search()
    
    for detail in searchText:
        print(detail[0])
        detail_page(detail[0])    



def detail_page(searchText):
    detail = 4;
    
    print(searchText)
    for i in range(1, 21):
        URL = "https://wtech.inswave.kr/websquare/websquare.html?w2xPath=/ws/index.xml&inPath=/ws/qna/qna_list.xml&searchType=title&searchText=" + searchText + "&curPage=" + str(i)
        driver.get(f"{URL}")
        print("################ URL : " + str(i) + " #######################3")
        print(URL)
        
        for j in range(detail, 10):
            
            img_name = '#wf_frame_grid1_cell_' + str(j) + '_1 > img'
            img = driver.find_element(By.CSS_SELECTOR, img_name)
            if img == '':
                continue
            else :
                img = img.get_attribute('src')

                blue = "https://wtech.inswave.kr/images/ico_grd_blu.gif"
                
                if img != blue:
                    continue
                else :
                
                    detail_name = '#wf_frame_grid1_cell_' + str(j) + '_2 > nobr > a';
                    data = []
                    
                    title = driver.find_element(By.CSS_SELECTOR, detail_name).text
                    print(title)
                    data.append(title)
                    driver.find_element(By.CSS_SELECTOR, detail_name).click()
                                
                    content = driver.find_element(By.CSS_SELECTOR, '#wf_frame_txtContent').text
                    
                    start = content.find('<< 개요 >>')
                    last = content.find('<< 버전 및 빌드일 >>')
                    final_content = content[start:last]
                    
                    data.append(final_content)
                    
                    reply_main_num = 0
                    reply_main_name = "#wf_frame_generator1_" + str(reply_main_num) + "_content"
                    final_reply_main = ""
                    final_reply_re = ""
                    while(True):
                        try:
                            reply_main = driver.find_element(By.CSS_SELECTOR, reply_main_name).text
                            
                            check = reply_main.find('?')
                            if check == -1:
                                temp = final_reply_main
                                final_reply_main = temp + reply_main + "\n\n" 
                            
                            reply_re_num = 0
                            reply_re_name = "#wf_frame_generator1_" + str(reply_main_num) + "_generator2_" + str(reply_re_num) + "_content"
                            
                            while(True):
                                try:
                                    reply_re = driver.find_element(By.CSS_SELECTOR, reply_re_name).text
                                    
                                    check = reply_re.find('?')
                                    
                                    if check == -1:
                                        temp = final_reply_re
                                        final_reply_re = temp + reply_re + "\n\n" 
                                        
                                    reply_re_num += 1
                                    reply_re_name = "#wf_frame_generator1_" + str(reply_main_num) + "_generator2_" + str(reply_re_num) + "_content"
                                except:
                                    break
                                
                            reply_main_num += 1
                            reply_main_name = "#wf_frame_generator1_" + str(reply_main_num) + "_content"
                            

                        except:
                            break
                    data.append(final_reply_main)
                    data.append(final_reply_re)
                    
                    insert_search(data)
                    
                    driver.back()
                
    
    
    