# file:///F:/Sagar_m_Auto_Task/Gmail_API/email.html

print("Initiating main.py")
from selenium import webdriver
from time import sleep
from python_anticaptcha import AnticaptchaClient, NoCaptchaTaskProxylessTask
from multiprocessing import Process


def Purchage_bill():
    url = "file:///F:/Sagar_m_Auto_Task/Gmail_API/email.html"

    driver_path = "F:\\Sagar_m_Auto_Task\\chromedriver"
    brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
    option = webdriver.ChromeOptions()
    option.binary_location = brave_path
    option.add_argument("--incognito")
    search = webdriver.Chrome(executable_path=driver_path, options=option)
    search.get(url)
    sleep(1)
    try:
        search_button = search.find_element_by_xpath('//*[@id="a-autoid-0-announce"]')
        search_button.click()
        sleep(1)
    except Exception as e:
        print("------------------------")
        print(e)
        print("------------------------")
    
Purchage_bill()