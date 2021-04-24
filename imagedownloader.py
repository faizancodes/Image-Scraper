#Imports Packages
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
import signal
from pathlib import Path
from bs4 import BeautifulSoup
from itertools import cycle


####################################################


# # Get Proxies 
def getProxies(inURL):
    
    page = requests.get(inURL)
    soup = BeautifulSoup(page.text, 'html.parser')
    terms = soup.find_all('tr')
    IPs = []

    for x in range(len(terms)):  
        
        term = str(terms[x])        
        
        if '<tr><td>' in str(terms[x]):
            pos1 = term.find('d>') + 2
            pos2 = term.find('</td>')

            pos3 = term.find('</td><td>') + 9
            pos4 = term.find('</td><td>US<')
            
            IP = term[pos1:pos2]
            port = term[pos3:pos4]
            
            if '.' in IP and len(port) < 6:
                IPs.append(IP + ":" + port)
                #print(IP + ":" + port)

    return IPs 


#Cycle through the proxies and get one to use 
proxyURL = "https://www.us-proxy.org/"
pxs = getProxies(proxyURL)
proxyPool = cycle(pxs)



#########################################################################


# Opens up web driver and goes to Google Images
driver = webdriver.Chrome('C:\\Program Files (x86)\\chromedriver.exe')

# To maximize the browser window
driver.maximize_window()

# Google Image search
driver.get('https://www.google.ca/imghp?hl=en&tab=ri&authuser=0&ogbl')

box = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/form/div[1]/div[1]/div[1]/div/div[2]/input")
box.send_keys('astronaught wallpaper')
box.send_keys(Keys.ENTER)

highres = driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[2]/c-wiz[2]/scrolling-carousel/div[1]/span/span/div[2]/a")
highres.click()

#Will keep scrolling down the webpage until it cannot scroll no more

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
    

images_url = []

for i in range(1, 100):
    try:
        
        '''
        driver.find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/div[' + str(i) + ']/a[1]/div[1]/img').screenshot('C:\\Users\\faiza\\GANArt\\img\\space (' + str(i) +').png')
        '''
        
        time.sleep(1)
        
        img = driver.find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/div[' + str(i) + ']/a[1]/div[1]/img')
        
        img.click()
        
        enlargedImg = driver.find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div/div[2]/a/img')
        
        
        images_url.append(enlargedImg.get_attribute("src"))
        folder_path = 'C:\\Users\\faiza\\GANArt\\img\\'
        
        '''
        # write image to file
        reponse = requests.get(images_url[i-1])
        
        
        if reponse.status_code == 200:
            with open('C:\\Users\\faiza\\GANArt\\img\\space ' + str(i) + '.png',"wb") as file:
                file.write(reponse.content)
        
        print(response.content)
        print()
        print()
        '''
        
        
        '''
        image_content = requests.get(enlargedImg.get_attribute("src"), proxies = {"http": next(proxyPool)}).content
        folder_path = 'C:\\Users\\faiza\\GANArt\\img\\'
        
        try:
                
            # Convert the image into a bit stream, then save it.
            
            image_file = io.BytesIO(image_content)
            image = Image.open(image_file).convert('RGB')
            
            # Create a unique filepath from the contents of the image.
            file_path = pathlib.Path(
                folder_path, hashlib.sha1(image_content).hexdigest()[:10] + ".png"
            )
            
            image.save(file_path, "PNG", quality=80)
            
            print(f"SUCCESS - saved {url} - as {file_path}")
            
        except Exception as e:
            
            print(f"ERROR - Could not save {url} - {e}")

        '''
        
        src = enlargedImg.get_attribute('src')
        
        try:
            
            if src != None:
                
                src  = str(src)
                print(src)
                
                urllib.request.urlretrieve(src, os.path.join(folder_path, 'space ' + str(i) + '.png'))
            
            else:
                raise TypeError
        
        except TypeError:
            print('fail')

        
        
    except:
        pass