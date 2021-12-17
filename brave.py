from selenium import webdriver
from time import sleep
from python_anticaptcha import AnticaptchaClient, NoCaptchaTaskProxylessTask
from selenium.webdriver.common.by import By

driver_path = "D:/Komparify/chromedriver"
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
option = webdriver.ChromeOptions()
option.binary_location = brave_path
option.add_argument("--incognito")
search = webdriver.Chrome(executable_path=driver_path, options=option)

url = "https://www.komparify.com/"


search.get(url)
sleep(10)
#wait for proxy to connect
search_button = search.find_element_by_xpath("/html/body/div[1]/div[5]/div/div/a[2]/span")
search_button.click()
sleep(1)
login = search.find_element_by_xpath('//*[@id="user_email"]')
login.send_keys('Sagkrs9@outlook.com')
# sleep(1)

password = search.find_element_by_xpath('//*[@id="user_password"]')
password.send_keys('Sagar28*')
# sleep(1)

api_key = '4a27760ccb2a74b1860b6ff07dd00ab8'
# site_key = '6LdUQnIUAAAAAM_pYgzYhqdgL3w6xH5SMty7XMhb'  # grab from site
# 6LdUQnIUAAAAAM_pYgzYhqdgL3w6xH5SMty7XMhb
site_key = search.find_element_by_class_name('g-recaptcha').get_attribute('data-sitekey')



print(site_key)
url = 'https://www.komparify.com'

client = AnticaptchaClient(api_key) 
task = NoCaptchaTaskProxylessTask(url, site_key)
job = client.createTask(task)
job.join()
print(job.get_solution_response())
response = job.get_solution_response()

# Inject response in webpage
# search.execute_script('document.getElementById("recaptcha-token").innerHTML = "%s"' % response)
search.execute_script('document.getElementById("g-recaptcha-response").innerHTML = "{}";'.format(response))
# target textarea that is supposed to be injected with the token, I found upon some research

print("INjecting Response")
search.execute_script('document.getElementById("g-recaptcha-response").innerHTML = "{}";'.format(response))
print("Response Injected")
# search.execute_script("onSuccess('{}')".format(response))
# sleep(1)

# Wait a moment to execute the script (just in case).
# sleep(1)

# Press submit button
search.find_element_by_xpath('/html/body/div[3]/div/div/form/p/input').click()
sleep(5)

#Press recharge button
search.find_element_by_xpath('//*[@id="nav-mainwrap"]/a[1]/div[1]/span[1]').click()
sleep(5)

#Choose Electricity
bill = search.find_element_by_xpath('//*[@id="recharge-types"]/ul[1]/li[6]/a[1]/div[1]')
bill.click()

sleep(1)
Electricity1 = search.find_element_by_xpath('//*[@id="recharge_param_number"]')
Electricity1.clear()
Electricity1.send_keys('9147957842')
sleep(1)

broadband2 = search.find_element_by_xpath('//*[@id="recharge_param_param_1"]')
broadband2.send_keys('9147957842')


amount = search.find_element_by_xpath('//*[@id="recharge_param_value"]')
amount.send_keys('49')
sleep(1)

pay_bill = search.find_element_by_xpath('//*[@id="new_recharge_param"]/div[13]/button[1]')
pay_bill.click()
sleep(5)

search.find_element_by_xpath("(//a[contains(@class,'payment_type paymentoption')])[2]").click()
sleep(5)

pay = search.find_element_by_xpath('//*[@id="gotopayubutton"]')
pay.click()

amazon_email = "rajur31@gatur.online"
amazon_password = "Sagar6686@"
sleep(1)
a_id = search.find_element_by_xpath('//*[@id="ap_email"]')
a_id.clear()
sleep(1)
a_id.send_keys(amazon_email)
sleep(1)
a_password = search.find_element_by_xpath('//*[@id="ap_password"]')
sleep(1)
a_password.send_keys(amazon_password)

sign_in = search.find_element_by_xpath('//*[@id="signInSubmit"]')
sleep(1)
sign_in.click()
sleep(1)

auth=  "AIzaSyC_7et_Sg07JbxWko5acmAItXEkuC3yDWA"

confirm = search.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/div/div/div[2]/div/div[1]/div/div[2]/div[2]/form/div[2]/div[1]/div[1]/div/span/span/input')
confirm.click()

print("Hello World")
