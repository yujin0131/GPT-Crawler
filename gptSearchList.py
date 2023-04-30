import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

URL_BASE = "https://wtech.inswave.kr/websquare/websquare.html?w2xPath=/ws/index.xml&inPath=/ws/qna/qna_list.xml"
# https://wtech.inswave.kr/websquare/websquare.html?w2xPath=/ws/index.xml&inPath=/ws/qna/qna_list.xml&searchType=content&searchText=gridView&curPage=1
def get_last_page():
    set_last_page = 1
    return int(set_last_page)

def get_search_infos(Query):
    last_page = get_last_page()
    search_infos  = search_idx(last_page, Query)
    print(search_infos)
    return search_infos

def search_idx(last_page, Query):
    search_infos = {}
    room_infos = []
    for page in range(last_page):
        print("Scraping the titles of page", page+1,"...")
        URL_TYPE= "&searchType=" + Query['searchType']
        URL_SEARCH = "&searchText=" + Query['searchText']
        
        URL = URL_BASE + URL_TYPE + URL_SEARCH + "&curPage=1"
        print(URL)
        
        result = requests.get(f"{URL}")
        html = result.content.decode('utf-8','replace') 
        print("##################### html ###################")
        print(html)
        soup = BeautifulSoup(result.content, "html.parser")
        print("##################### soup ###################")
        print(soup)
        results = soup.find_all("div", {"id":"wq_uuid_64"})
        print("##################### results ###################")
        print(results)
        
        driver = webdriver.Chrome('/Users/beomi/Downloads/chromedriver')
        driver.implicitly_wait(3)
        ## url에 접근한다.
        driver.get(f"{URL}")
        
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        
        
        
        noticeTest = driver.find_element(By.CSS_SELECTOR, '#wf_frame_grid1_cell_4_2 > nobr > a').click
        print("      ")
        print("##################### noticeTest ###################")
        print(noticeTest)
        
        inner = driver.find_element(By.CSS_SELECTOR, '#wf_frame_txtContent').text
        print("############## inner : " + inner +" ##################")
    
        
        #  
        # for result in notices2:
        #     print("##########")
        #     print(result.string)
        #     # result_url = result.find("a")["href"]
        #     text = result.find("div", {"class":"gridHeaderTDDefault"})
        #     print("############### text ################")
        #     print(text)
        #     # room_idx = result_url[result_url.index('s/')+2:result_url.index('?')]
            # room_info = {"room_idx":room_idx, "room_price":room_price}
            # if room_info not in room_infos:
            #     room_infos.append(room_info)
    
        #search_infos['search'] = Query
        
    #return search_infos