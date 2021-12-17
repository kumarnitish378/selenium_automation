print("Initiating main.py")
from selenium import webdriver
from time import sleep
from python_anticaptcha import AnticaptchaClient, NoCaptchaTaskProxylessTask
from multiprocessing import Process
from threading import Thread
import random


def Purchage_bill(k_email, k_password, mobile_number, a_id, a_pass):
    url = "https://www.komparify.com/"
    account_number = mobile_number
    a_pass = a_pass.replace("\n", "")
    
    # proxy
    PROXY = "127.0.0.1:24000"
    
    # Change these path to your path
    driver_path = "D:/Komparify/chromedriver"
    brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"

    # proxy
    PROXY = "127.0.0.1:24000"
    
    # UserAgent
    # user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/72.0'
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:{}.0) Gecko/20100101 Firefox/72.0'.format(random.randint(70, 80))
    print("\n-------user_agent----------")
    print(user_agent)
    print("\n-----------------")
    option = webdriver.ChromeOptions()
    #option.add_argument("--headless")
    option.binary_location = brave_path
    option.add_argument("--disable-software-rasterizer")
    option.add_argument('--proxy-server=%s' % PROXY)
    option.add_argument("user-agent=" + user_agent)
    option.add_argument("--incognito")
    option.add_argument("--no-sandbox")
    #option.add_argument("--window-size=1920,1080")
    
    search = webdriver.Chrome(executable_path=driver_path, options=option)

    try:
        search.get(url)
        sleep(1)
        search_button = search.find_element_by_xpath("/html/body/div[1]/div[5]/div/div/a[2]/span")
        search_button.click()
        sleep(1)
        login = search.find_element_by_xpath('//*[@id="user_email"]')
        login.send_keys(k_email)
        # sleep(1)

        password = search.find_element_by_xpath('//*[@id="user_password"]')
        #password.send_keys('Sagar28*')
        password.send_keys(k_password)
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
        sleep(1)

        #Press recharge button
        search.find_element_by_xpath('//*[@id="nav-mainwrap"]/a[1]/div[1]/span[1]').click()
        sleep(5)

        #Choose Electricity
        bill = search.find_element_by_xpath('//*[@id="recharge-types"]/ul[1]/li[6]/a[1]/div[1]')
        bill.click()
    # 
        sleep(1)
        mobile1 = search.find_element_by_xpath('//*[@id="recharge_param_number"]')
        mobile1.clear()
        # mobile1.send_keys('9178978898')
        mobile1.send_keys(account_number)
        sleep(1)

        mobile2 = search.find_element_by_xpath('//*[@id="recharge_param_param_1"]')
        # mobile2.send_keys('9178978898')
        mobile2.send_keys(mobile_number)

        amount = search.find_element_by_xpath('//*[@id="recharge_param_value"]')
        # Change Amount if required
        amount.send_keys('49')
        sleep(1)

        pay_bill = search.find_element_by_xpath('//*[@id="new_recharge_param"]/div[13]/button[1]')
        pay_bill.click()
        sleep(5)
        # 

        select_method = search.find_element_by_xpath('//*[@id="rechargeformholder"]/div[4]/a[2]')
        select_method.click()

        sleep(1)
        pay = search.find_element_by_xpath('//*[@id="gotopayubutton"]')
        pay.click()

        # amazon_email = "Rajur51@gatur.online"
        amazon_email = a_id
        # amazon_password = "Sagar6686@"
        amazon_password = a_pass
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

        search.refresh()
        sleep(3)
        search.refresh()
        sleep(3)
        confirm = search.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/div/div/div[2]/div/div[1]/div/div[2]/div[2]/form/div[2]/div[1]/div[1]/div/span/span/input')
        confirm.click()
        sleep(100)
    except Exception as e:
        print("Eror Found")
        print(e)
        sleep(100)
        #search.quit()

    print("Hello World")
    

if __name__ == "__main__":
    
    # Write all credential in credential.txt file in same dorectory. if not provide full path,
    # Write All information withou any space between them.
    try:
        file = open("credential.txt")
        file_data = file.readlines()
        file_data = [tuple(i.split(",")) for i in file_data]
        print(file_data[0][-1].replace("\n",""))
    except Exception as e:
        print("Error in file reading")
        print(e)
        exit(0)
        
    # Recomended: Use one by one method
    while True:
        thred_list = []
        print("-----------------------------")
        mode = int(input("\nSelect Mode: \n1. press 1 for one by one.\n2. enter 2 for multithreading.\n3. Enter 3 for multiprocessing\n4. Enter 0 for Quit.\n--> "))
        if mode == 1:
            # code to run aone by one each account, Automatically
            for p1_data in file_data:
                print(p1_data)
                Purchage_bill(p1_data[0], p1_data[1], p1_data[2], p1_data[3], p1_data[4].replace("\n",""))
        
        elif mode==2:
            # Below Code create multiple thread and run all at the same time
            for p1_data in file_data:
                print(p1_data)
                # Purchage_bill(p1_data[0], p1_data[1], p1_data[2], p1_data[2], p1_data[3], p1_data[4].replace("\n",""))
                thred_list.append(Thread(target=Purchage_bill, args=p1_data))
                print("DONE ")
            for th in thred_list:
                th.start()
                sleep(1)
            for th in thred_list:
                th.join()

        elif mode == 3:
            # Below Code create multiple Process and run all at the same time
            print("create multiple Process and run all at the same time")
            for p1_data in file_data:
                print(p1_data)
                # Purchage_bill(p1_data[0], p1_data[1], p1_data[2], p1_data[2], p1_data[3], p1_data[4].replace("\n",""))
                thred_list.append(Process(target=Purchage_bill, args=p1_data))
                print("DONE ")
            for th in thred_list:
                th.start()
                sleep(1)
            for th in thred_list:
                th.join()
            p1_data = ('Sagkrs10@outlook.com', 'Sagar28*', '9178978898', '7004969879', "Rajur2@gatur.online","Sagar6686@",) 
        elif mode == 0:
            print("Exit program")
            break
        else:
            print("Enter corrent Choice: ")
            
    print("Done")
    print("Done")
