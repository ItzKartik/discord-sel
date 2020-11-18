from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import csv
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyperclip
from time import sleep

email = "guptapz111@gmail.com"
pass_word = "(kartik@737)"
path = "C://Users//itzka//AppData//Local//Google//Chrome//User Data//Profile 5"
join_url = "https://discord.gg/gAuSvQnR"

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
if path != None:
    chrome_options.add_argument('--user-data-dir={p}'.format(p=path))
data = []

def accept_invite(driver, url):
    if url == None:
        pass
    else:
        driver.get(url)
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="app-mount"]/div[2]/div/div/div/section/div/button'))
            )
            driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div/div/section/div/button').click()
        except TimeoutException as t:
            print(t)
            driver.quit()

def copyit(driver, xpath):
        driver.find_element_by_xpath('//*[@id="user-context-devmode-copy-id"]/div').click()

def save_to_csv():
    with open('users.csv', 'w+', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Username"])
        writer.writerows(data)

def login(driver):
    if pass_word == None:
        print("Please Fill Username & Password Variable")
        return False
    else:
        driver.get("https://discord.com/login")
        try:
            user_box = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[1]/div/div[2]/input').send_keys(email)
            pass_box = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[2]/div/input').send_keys(pass_word)
            driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/button[2]').click()
        except TimeoutException as t:
            print("Can't Logged In. More Information :", t)
            driver.quit()

def check_for_homepage(driver):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="private-channels-0"]/div/div[2]/div/div'))
    )

def right_click(chrome):
    try:
        WebDriverWait(chrome, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'member-3-YXUe'))
        )
        sleep(2)
        for i in range(1, 100):
            f = chrome.find_elements_by_class_name('member-3-YXUe')
            actionChains = ActionChains(chrome)
            actionChains.move_to_element(f[i]).context_click(f[i]).perform()
            chrome.find_element_by_xpath('//*[@id="user-context-devmode-copy-id"]/div').click()

            username = f[i].text
            i_d = pyperclip.paste()
            data.append([str(i_d), str(username)])
            scr1 = chrome.find_element_by_xpath('//*[@id="members-748648641811578881"]')
            chrome.execute_script("arguments[0].scrollTop = arguments[0].scrollWidth", scr1)
            sleep(2)
            
        save_to_csv()
        chrome.quit()
    except (StaleElementReferenceException, NoSuchElementException) as n:
        print("More Info :", n)

chrome = webdriver.Chrome('chrome/chromedriver.exe', options=chrome_options)
# login(chrome)
# check_for_homepage(chrome)
# accept_invite(chrome, join_url)
chrome.get("https://discord.com/channels/748647290994163723/748648641811578881")
right_click(chrome)