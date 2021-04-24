# Faizan Ahmed
# 4/24/2021

#Import Packages
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from PIL import Image
import time 
import urllib.request
import pyperclip
import requests

import os
import time
import io
import hashlib
from pathlib import Path
from bs4 import BeautifulSoup


def scrapeImages(searchPhrases, imgPerSearch, saveToFolder):
    
    for phrase in searchPhrases:
        
        # Opens up web driver and goes to Google Images
        driver = webdriver.Chrome('C:\\Program Files (x86)\\chromedriver.exe')

        # Google Image search
        driver.get('https://www.google.ca/imghp?hl=en&tab=ri&authuser=0&ogbl')

        box = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/form/div[1]/div[1]/div[1]/div/div[2]/input")
        
        box.send_keys(phrase)
        box.send_keys(Keys.ENTER)

        #highres = driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[2]/c-wiz[2]/scrolling-carousel/div[1]/span/span/div[2]/a")
        #highres.click()

        # Will keep scrolling down the webpage until it cannot scroll no more

        last_height = driver.execute_script('return document.body.scrollHeight')

        while True:
            
            driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            
            time.sleep(2)
            
            new_height = driver.execute_script('return document.body.scrollHeight')
            
            try:
                driver.find_element_by_xpath('//*[@id="islmp"]/div/div/div/div/div[5]/input').click()
                time.sleep(2)
            
            except:
                pass
            
            if new_height == last_height:
                break
            
            last_height = new_height



        for i in range(1, imgPerSearch):

            try:

                time.sleep(1)

                img = driver.find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/div[' + str(i) + ']/a[1]/div[1]/img')

                img.click()

                enlargedImg = driver.find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div/div[2]/a/img')


                src = enlargedImg.get_attribute('src')

                # Not all images will be downloaded! 
                try:

                    if src != None:

                        src  = str(src)
                        print(src)

                        urllib.request.urlretrieve(src, os.path.join(saveToFolder, phrase + ' ' + str(i) + '.png'))

                    else:
                        raise TypeError

                except TypeError:
                    print('fail')


            except:
                pass
    

saveToFolder = 'C:\\Users\\faiza\\GANArt\\img\\'
searchPhrases = ['space wallpaper 4k', 'galaxy wallpaper 4k', 'star wallpaper 4k']
imgPerSearch = 100

scrapeImages(searchPhrases, imgPerSearch, saveToFolder)
