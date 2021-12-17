import imaplib
import email
print("Initiating main.py")
from selenium import webdriver
from time import sleep
from python_anticaptcha import AnticaptchaClient, NoCaptchaTaskProxylessTask
from multiprocessing import Process
import os


username = 'raysachin817@gmail.com'
password = 'Sagar123*'

x1 = '//*[@id="a-autoid-0-announce"]'
x2 = '//*[@id="a-autoid-0-announce"]'

def Approve_payments(url=""):
    url = "file:///" + url
    
    # Change these path to your path
    driver_path = "D:/Komparify/chromedriver"
    brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"

    # UserAgent
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0'
    
    option = webdriver.ChromeOptions()
    option.add_argument("--headless")
    option.binary_location = brave_path
    option.add_argument("user-agent=" + user_agent)
    option.add_argument("--incognito")
    option.add_argument("--no-sandbox")
    option.add_argument("--window-size=400,600")
    search = webdriver.Chrome(executable_path=driver_path, options=option)
    search.get(url)
    sleep(10)
    try:
        search_button = search.find_element_by_xpath('/html/body/table/tbody/tr/td/table/tbody/tr[5]/td/a')
        search_button.click()
        sleep(5)
        approve_button = search.find_element_by_xpath('//*[@id="a-autoid-0"]/span/input')
        approve_button.click()
        sleep(2)
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
    while True:
        print("press ctrl+c to Exit/close")
        print("\nFetching Mail........")
        main_body = read_mail()
        print("Mail Fetched.!")
        try:
            if "Please approve or deny" in str(main_body):
                print("found Approval Link")
                with open('email.html', 'w', encoding="utf-8") as f:
                    f.write(str(main_body))
                file_path = os.getcwd()+"\\"+ "email.html"
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
