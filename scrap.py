import numpy as np
from selenium import webdriver
import xlrd, time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import urllib
from hanziconv import HanziConv
import random
import os
import re
import pprint


Navigateur = "Chrome"
driver = webdriver.Chrome('/Users/roger/Drive_Artefact/TMALL/Code/chromedrive/chromedriver')

timeout = np.random.randint(1, 10)

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


        
driver.set_page_load_timeout(5)
Link_1 = "https://lorealoumeisi.world.tmall.com/search.htm?spm=a312a.7700824.w4011-16312946027.93.4670278ct1vy4J&search=y&pageNo=1&tsearch=y#anchor"


try:
    driver.get(Link_1)
except:
    pass

Title = [] 
css_pt ="dl[class^='item']>dd[class^='detail']>a[class^='item-name']"
for p in Recherches_css(css_pt):
    txt = p.text
    txt = txt.replace('/', '')
    txt = HanziConv.toSimplified(txt)
    Title.append(txt)


links = []
css_links = "a[class^='J_TGoldData']"
for p in Recherches_css(css_links):
    links.append(p.get_attribute('href'))

for link in links:
    timeout = 3*random.random()
    time.sleep(timeout)
    
    try:
        driver.get(link)
    except:
        pass
    
    try:
        css_stop = "i[class^='tm-video-stop']"
        Double_Click(css_stop)
    except:
        pass
    
    time.sleep(timeout)
    css_img = "img[id^='J_ImgBooth']"
    img = Recherches_css(css_img)[0].get_attribute('src')
    
    prod_info = {}
    css_pt ="ul[id^='J_AttrUL']>li"
    for p in Recherches_css(css_pt):
        name = p.text
        name = re.split(':', name)[0]
        name = re.split('：', name)[0]
        name = HanziConv.toSimplified(name)
        txt = p.get_attribute('title')
        txt = txt.replace('/', '')
        txt = txt.replace(u'\xa0', u'')
        txt = HanziConv.toSimplified(txt)
        prod_info[name] = txt

    
    try:
        if not os.path.exists('data/' + prod_info['产品名称']):
            os.mkdir('data/' + prod_info['产品名称'])
            file_name = 'data/' + prod_info['产品名称'] + '/' + prod_info['产品名称']
        else:
            continue
        
    except:
        time_err = str(datetime.datetime.now().strftime('%Y%m%d_%H%M%S'))
        os.mkdir('data/error_'+time_err)
        file_name = 'data/error_' + time_err + '/' + time_err
        
    
    urllib.request.urlretrieve(img, file_name +".jpg")
    f = open(file_name + ".txt","w")
    f.write(pprint.pformat(prod_info))
    f.close()