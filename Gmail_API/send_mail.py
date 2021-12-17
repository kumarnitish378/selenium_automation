import imaplib
import email
print("Initiating main.py")
from selenium import webdriver
from time import sleep
from python_anticaptcha import AnticaptchaClient, NoCaptchaTaskProxylessTask
from multiprocessing import Process
import os
from random import randint
from threading import Thread


username = 'youremail@gmail.com'
password = 'yourpass6bjk'

x1 = '//*[@id="a-autoid-0-announce"]'
x2 = '//*[@id="a-autoid-0-announce"]'

def Approve_payments(url=""):
    url = "file:///" + url
    
    # Change these path to your path
    driver_path = "F:\\Sagar_m_Auto_Task\\chromedriver"
    brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
    
    option = webdriver.ChromeOptions()
    option.binary_location = brave_path
    option.add_argument("--incognito")
    search = webdriver.Chrome(executable_path=driver_path, options=option)
    search.get(url)
    sleep(10)
    try:
        search_button = search.find_element_by_xpath('//*[@id="a-autoid-0-announce"]')
        search_button.click()
        sleep(1)
        # one more line of code here to click Approve button.
        # 
        #
    except Exception as e:
        print("------------------------")
        print(e)
        print("------------------------")
    
def read_mail():
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(username, password)
    mail.list()
    mail.select('inbox')
    result, data = mail.uid('search', None, "UNSEEN")
    # print(data)
    # print(result)
    inbox_item_list = data[0].split()
    if len(inbox_item_list) == 0:
        return None
    # print(inbox_item_list)
    latest_email_uid = inbox_item_list[-1]
    result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
    # print(data)
    # print(result)
    raw_email = data[0][1]
    raw_email_string = raw_email.decode('utf-8')
    email_message = email.message_from_string(raw_email_string)
    email_subject = email_message['subject']
    email_from = email_message['from']
    # print(type(email_message))
    for part in email_message.walk():
        if part.get_content_type() == "text/html":
        # if part.get_content_type() == "text/plain" or part.get_content_type() == "text/html":
            body = part.get_payload(decode=True)
            temp = email.message_from_bytes(body).as_string()
            # print(type(temp))
            # print(temp)
            return temp
    return email_subject, email_from

'''
def send_mail(to, subject, text):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = to
    msg['Subject'] = subject

    msg.attach(MIMEText(text, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(username, password)
    text = msg.as_string()
    server.sendmail(username, to, text)
    # server.quit()
    server.quit()
    
'''
 
if __name__ == '__main__':

    '''
    Notes:
        it may be required some changes. I have not check this beacuse my system slow litil bit.
    '''
    print(os.getcwd())
    for _ in range(5):
        mode : int(input("Enter Mode you want!\n1.For one by one(1).\n2. Multi threading or multi processing(2).\n --> "))
        if mode == 1:
            print("Mode is One by one")
            while True:
                print("press ctrl+c to Exit/close")
                print("\nFetching Mial........")
                main_body = read_mail()
                print("Mail Fetched.!")
                try:
                    if "Please approve or deny" in str(main_body):
                        url_path = 'email{}.html'.format(randint(1, 100))
                        print("found Approval Link")
                        with open(url_path, 'w', encoding="utf-8") as f:
                            f.write(str(main_body))
                        file_path = os.getcwd()+"\\"+ url_path
                        print(file_path)
                        print("opening Approval Link in browser")
                        Approve_payments(file_path)
                    else:
                        with open('email.html', 'w', encoding="utf-8") as f:
                            f.write(str(main_body))
                        print("Approval Link Not Found")
                        
                except KeyboardInterrupt:
                    print("Error: KeyBoard Intrupt")
                    break
                sleep(10) # in second (you can increse the delay
                
            print('Mail Received')
            
        elif mode == 2:
            print("Multi threading or multi processing")
            while True:
                print("press ctrl+c to Exit/close")
                print("\nFetching Mial........")
                main_body = read_mail()
                print("Mail Fetched.!")
                try:
                    if "Please approve or deny" in str(main_body):
                        url_path = 'email{}.html'.format(randint(1, 100))
                        print("found Approval Link")
                        with open(url_path, 'w', encoding="utf-8") as f:
                            f.write(str(main_body))
                        file_path = os.getcwd()+"\\"+ url_path
                        print(file_path)
                        print("opening Approval Link in browser")
                        Thread(target=Approve_payments, args=(file_path,)).start()
                    else:
                        with open('email.html', 'w', encoding="utf-8") as f:
                            f.write(str(main_body))
                        print("Approval Link Not Found")
                        
                except KeyboardInterrupt:
                    print("Error: KeyBoard Intrupt")
                    break
                sleep(10) # in second (you can increse the delay
                
            print('Mail Received')
        else:
            print("Incorect Option!")
            print("Enter Vailed Option")
    print("Program Exit/close")
    print("Thanks")
    print("Run Again")
