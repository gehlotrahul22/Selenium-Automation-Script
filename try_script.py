'''

driver.find_element_by_partial_link_text("Python")
'''

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#chrome_options = Options()
#chrome_options.add_argument("--disable-extensions")
#chrome_options.add_experimental_option("debuggerAddress", "localhost:9014")

#driver = webdriver.Chrome(ChromeDriverManager().install() , chrome_options=chrome_options)

#driver = webdriver.Chrome()
#driver.get("https://www.linkedin.com/in/jramakrishnan/?originalSubdomain=in")

import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import json
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
appState = {
    "recentDestinations": [
        {
            "id": "Microsoft Print to PDF",
            "origin": "local",
            "account": ""
        }
    ],
    "selectedDestinationId": "Microsoft Print to PDF ",
    "version": 2
}

profile = {'printing.print_preview_sticky_settings.appState': json.dumps(appState)}

chrome_options = webdriver.ChromeOptions()

chrome_options.add_experimental_option('prefs', profile)


chrome_options.add_argument('--kiosk-printing')

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)


login = input("Enter yout login-ID ")
password = input("Enter your login-Password :- ")
count=input("Serial Number TO Start Saving Files:- ")
driver.implicitly_wait(1)
url = driver.command_executor._url       #"http://127.0.0.1:60622/hub"
session_id = driver.session_id
print("URL:-" ,url)
print("SSID:- ",session_id)

#driver = webdriver.Remote(command_executor="http://127.0.0.1:18839",desired_capabilities={})
#driver.session_id = "fd79f2a449bb798b3f076810ceaa29b7"

#'4e167f26-dc1d-4f51-a207-f761eaf73c31'
#driver.get('https://www.google.com/')
#driver = webdriver.Chrome(ChromeDriverManager().install())

#open linkedin in automated browser
driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
time.sleep(1)
#ActionChains(driver).key_down(Keys.CONTROL).send_keys('t').perform()
#driver.switch_to_window(driver.window_handles[1])
#logs you into Linkedin
driver.find_element_by_id("username").send_keys(str(login))
password = driver.find_element_by_id("password").send_keys(str(password))
driver.find_elements_by_tag_name('button')[0].click()
print("successfully logged in")
time.sleep(30)
from selenium.common.exceptions import NoSuchElementException        
def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True
#navigates to your connections
def wait_for_text(driver, text, timeout=1):
    max_time = time.time() + timeout
    actions = ActionChains(driver)
    
    while time.time() < max_time:
        try:
            target=driver.find_element_by_class_name(str(text))
            actions.move_to_element(target)
            actions.perform()
            #driver.execute_script('arguments[0].scrollIntoView(true);', target)
            target.click()
            return 0
        except :
            return 1
def wait_for_texts(driver, text, timeout=1):
    max_time = time.time() + timeout
    actions = ActionChains(driver)
    while time.time() < max_time:
        try:
            element = driver.find_element_by_id(str(text))
            webdriver.ActionChains(driver).move_to_element(element ).click(element ).perform()
            return 0
        except :
            return 1

   # throw Exception(f'Couldn\'t find text {text}')
#time.sleep(1)
#________________________________________________________________________________________________________________________________________________________________________
#l="http://in.linkedin.com/pub/ramakrishnan-j/24/547/651"
#l="http://in.linkedin.com/pub/ramakrishnan-j/7/b96/474"
#l="http://in.linkedin.com/pub/ramakrishnan-jaganathan/20/168/994"P
#l="http://in.linkedin.com/pub/ramakrishnan-jagathrakshakan/62/87b/509"P


'''L=["http://in.linkedin.com/pub/ramakrishnan-kr/16/a23/ba2",
"http://in.linkedin.com/in/krkrishnan",
"http://in.linkedin.com/pub/ramakrishnan-krishnan/11/a32/11a",
"http://in.linkedin.com/in/raamkii",
"http://in.linkedin.com/pub/ramakrishnan-krishnan/32/539/7a2",
"http://in.linkedin.com/pub/ramakrishnan-krishnan/4/983/599",
"http://in.linkedin.com/pub/ramakrishnan-krishnan/43/b9b/901",
"http://in.linkedin.com/in/krkram"]'''

n=[]

for z in open("links.txt", 'r'):
    #z=f.readline()
    driver.get(z)
    #time.sleep(2)
    driver.maximize_window()
    if check_exists_by_xpath("//h1[text()='Page not found']")==True:
       n.append(count)
       count=count+1
       continue

    #WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//a[@id="line-clamp-show-more-button"]'))).click()

    #element = driver.find_element_by_xpath('/a[@id="line-clamp-show-more-button"]')
    #webdriver.ActionChains(driver).move_to_element(element ).click(element ).perform()

    '''element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="line-clamp-show-more-button"]' )))
    element.click()'''
    '''actions = ActionChains(driver)
    target=driver.find_element_by_xpath('//*[@id="globalfooter-copyright"]')
    #driver.find_element_by_class_name(str(text))
    actions.move_to_element(target)
    actions.perform()'''


    #element = driver.find_element_by_tag_name("footer")
    #webdriver.ActionChains(driver).move_to_element(element ).perform()
    i=0
    while i<10000:
        print("Scrolling ",i)
        driver.execute_script("window.scrollBy("+str(i)+","+str(i+100)+")"," ")
        i=i+100
    print("Scrolling at 0")
    #driver.execute_script("window.scrollBy(0,0)"," ")
    #driver.find_element_by_xpath("//*[text()='see more']").click()

    time.sleep(1)
    #driver.find_element_by_partial_link_text("see more").click()

    #time.sleep(2)
    #time.sleep(2)
    while True:
        try:
            element = driver.find_element_by_xpath("//button[text()='see more']")
            webdriver.ActionChains(driver).move_to_element(element ).click(element ).perform()
            #WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='see more']"))).click()
            #element.click()
        except Exception as e:
            print(e)
            break

        
        

    #element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Show more']")))
    #element.click()

    #driver.find_element_by_xpath("//*[text()='see more']").click()


    for i in range(30):
        a=wait_for_text(driver,'pv-profile-section__see-more-inline')
        if a==1:
            print("Over")
            break
        print("Executeed ",i)
    for i in range(30):
        a=wait_for_texts(driver,'line-clamp-show-more-button')
        if a==1:
            print("Over")
            break
        print("Executeed ",i)
    time.sleep(0.5)
    print("Skills")
    while True:
        try:
            
            elem = driver.find_element_by_xpath("//h2[text()='Skills & Endorsements']")
            driver.execute_script("arguments[0].scrollIntoView();",elem)
            element = driver.find_element_by_xpath("//span[text()='Show more'][@aria-hidden='true']")
            
            webdriver.ActionChains(driver).move_to_element(element ).click(element ).perform()
            #WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='see more']"))).click()
            #element.click()
        except Exception as e:
            print(e)
            break
    driver.execute_script("document.title=" + str(count) + ";")
    driver.execute_script('window.print();')
    time.sleep(3)
    pyautogui.typewrite(str(count))
    pyautogui.hotkey('enter')
    
    count=count+1
    time.sleep(2)
for i in n:
    print(i)

