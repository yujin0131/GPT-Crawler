import pymysql
import os
import time
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.parse import quote_plus

#####한글깨짐 방지###### 
os.environ["NLS_LANG"] = ".AL32UTF8"

# DB와 연결된 코드
conn = pymysql.connect(host = '152.67.200.79', user = 'yujin', password = 'Wlsehf0014@', db = 'gptCrawler', charset = 'utf8mb4', use_unicode=True)

db = conn.cursor()

def select_search():
    print("####### select_search #######")
    
    sql_select = 'select topic from quest_topic'
    db.execute(sql_select)
    quest_topic = db.fetchall()
    return quest_topic


def insert_search(data):
    
    sql_insert = 'insert into topic_content (topic_title,topic_content) values (%s, %s)'
    val = (data[0], data[1])
    
    db.execute(sql_insert, val)
    conn.commit()
    print("DB저장 성공 - topic_content")

