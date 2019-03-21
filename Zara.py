# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 13:06:53 2018

@author: lenovo
"""
import numpy as np
from selenium import webdriver
import pandas as pd
import xlrd, time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# 1- Browser Choice
Navigateur = "Firefox"
if Navigateur == "Chrome": 
    chrome_path = r"C:\Users\lenovo\Documents\Samir\64- Data Analysis Tools\18- Selenium\chromedriver\chromedriver.exe"
    chromeOptions = webdriver.ChromeOptions()
    #chromeOptions.add_argument('headless')
    prefs = {"profile.managed_default_content_settings.images":2}
    chromeOptions.add_experimental_option("prefs",prefs)
    driver = webdriver.Chrome(chrome_path)
else:
    profile = webdriver.FirefoxProfile()
#    # 1 - Allow all images
#    # 2 - Block all images
#    # 3 - Block 3rd party images 
    firefox_profile = webdriver.FirefoxProfile()
    ## Disable CSS
    firefox_profile.set_preference('permissions.default.stylesheet', 1)
    ## Disable images
    firefox_profile.set_preference('permissions.default.image', 1)
    ## Disable JavaScript
    firefox_profile.set_preference('javascript.enabled', True)
    ## Disable Flash
    firefox_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so','true')
    #os.environ['MOZ_HEADLESS'] = '1'  # <- this line
    driver = webdriver.Firefox(firefox_profile=firefox_profile)

timeout = 12

def Recherches_css(css):
    return driver.find_elements_by_css_selector(css)
def Recherche_css(css):
    return driver.find_element_by_css_selector(css) 
def Recherche_xpath(xpath):
    return driver.find_element_by_xpath(xpath)
def Recherches_xpath(xpath):
    return driver.find_elements_by_xpath(xpath)
def Wait_path(path_selector):
    WebDriverWait(driver, timeout).until(EC.visibility_of_all_elements_located((By.XPATH,path_selector)))
def Wait_css(path_selector):
    WebDriverWait(driver, timeout).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,path_selector)))
def find_start( s,last ):
    try:
        end = s.index( last)
        return s[0:end]
    except ValueError:
        return ""
def find_end( s, first):
    try:
        start = s.index( first ) + len( first ); end = len(s)
        return s[start:end]
    except ValueError:
        return ""
def pages_count(s):
    try:
        end = s.index('页')
        return s[1:end]
    except ValueError:
        return ""
def Double_Click(css):
    Element = Recherche_css(css)
    Element.click()

        
# Liens
Link_1 = "https://s.taobao.com/search?q=Zara&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180801&ie=utf8&sort=credit-desc&bcoffset=30&p4ppushleft=%2C44&ntoffset=30&fs=1&filter_tianmao=tmall"
Title = []
Price = []
Sales = []
Page = []

def Lancement(Link):
    driver.get(Link)
    
    css_pt ="div[class='items']>div>div[class^='ctx-box']>div[class^='row']>a"
    css_ps ="div[class='items']>div>div[class^='ctx-box']>div[class^='row']>div[class^='price']"
    css_sales = "div[class='items']>div>div[class^='ctx-box']>div[class^='row']>div[class^='deal-cnt']"
    
    TotalPage_Xpath = "/html/body/div[1]/div[2]/div[3]/div[1]/div[26]/div/div/div/div[1]"
    CurrentPage_Xpath = "/html/body/div[1]/div[2]/div[3]/div[1]/div[26]/div/div/div/div[2]/input"
    PageSuivante_css = "div[class='pager']>ul[class='items']>li[class='item']>a[title='下一页']"

    
    CurrentPage = int(Recherche_xpath(CurrentPage_Xpath).get_attribute('value'))
    CurrentPage = 0
    TotalPage = int(pages_count(Recherche_xpath(TotalPage_Xpath).text))
    
    while CurrentPage<TotalPage-1:
        
        
        Wait_path(CurrentPage_Xpath)
        Wait_css(css_pt)
        CurrentPage = CurrentPage + 1
        PageSuivante = Recherche_css(PageSuivante_css)
        
        for p in Recherches_css(css_pt):
            Title.append(p.text)
        
        for p in Recherches_css(css_ps):
            Price.append(p.text)
        
        for p in Recherches_css(css_sales):
            Sales.append(p.text)
            Page.append(CurrentPage)
        
        PageSuivante.click()
        print("Page Actuelle: "+ str(CurrentPage))
            

def Export():
    
    df_results = pd.DataFrame({
    'SKU' : Title,
    'Sales' : Sales,
    'Price' : Price,
    'Page' : Page,
    })
    
    Name = "180801 - Zara Sales Data.xlsx"
    writer2 = pd.ExcelWriter(Name, engine='xlsxwriter')
    df_results.to_excel(writer2,sheet_name = "Sales")
    writer2.save()
    writer2.close()

Lancement(Link_1)
Export()   
        
    

