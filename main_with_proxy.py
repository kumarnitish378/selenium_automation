from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time
# import Alert 
from selenium.webdriver.common.alert import Alert
'''
Proxy: zproxy.lum-superproxy.io
Port: 22225
User: lum-customer-hl_f80d2051-zone-data_center-route_err-pass_dyn
Password: Sagar123

free proxy list: https://spys.one/en/

'''
# change 'ip:port' with your proxy's ip and port
proxy_ip_port = '190.214.52.226:53281'
proxy_ip_port = '82.147.118.164:8080'
proxy_ip_port = ' zproxy.lum-superproxy.io:22225'

proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = proxy_ip_port
proxy.ssl_proxy = proxy_ip_port

proxy.socksUsername  = 'lum-customer-hl_f80d2051-zone-data_center-route_err-pass_dyn'
proxy.socks_password = 'Sagar123'


capabilities = webdriver.DesiredCapabilities.CHROME
proxy.add_to_capabilities(capabilities)
proxy.add_to_capabilities(capabilities)

# replace 'your_absolute_path' with your chrome binary absolute path
driver = webdriver.Chrome('./chromedriver', desired_capabilities=capabilities)
# driver = webdriver.Chrome('./chromedriver')


driver.get('http://whatismyipaddress.com')
# driver.get('https://free-proxy-list.net/')
alert = Alert(driver)
print(alert.text)
alert.accept()
time.sleep(2)

time.sleep(8)
