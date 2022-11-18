from selenium import webdriver
import time
import json
import os
from selenium.webdriver.common.by import By

js="window.open('{}','_blank');"
# 去cmd构建exe："pyinstaller -i 456.ico -F C:\Users\85099\PycharmProjects\pythonProject1\爬虫\Selenium.py"

driver=webdriver.Chrome(
    executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
)

driver.set_window_position(1920 / 5, 0)
driver.set_window_size(1100, 800)
url='https://y.qq.com/n/ryqq/search?w=%E5%91%A8%E6%9D%B0%E4%BC%A6%20-%20%E8%AF%B4%E4%BA%86%E5%86%8D%E8%A7%81&t=song'

driver.get(url)

list_cookies=[]


def get_cookie():
    print("请在浏览器登录音乐账号[可操作浏览器]")
    input("登录成功后，在这里回车继续：")
    cookieBefore=driver.get_cookies()
    # print(cookieBefore)
    jsonCookies=json.dumps(cookieBefore)
    fo=open("cookie.txt", "w")
    fo.write(jsonCookies)
    fo.close()
    print("保存cookie")
    login_check()


def read_cookie():
    global list_cookies
    with open('cookie.txt', 'r') as f:
        list_cookies=json.loads(f.read())
    for cookie in list_cookies:
        driver.add_cookie(cookie)
        # print(cookie)
    # time.sleep(2)
    print("注入cookie，请稍候[不要操作浏览器]")
    driver.refresh()
    time.sleep(2)

def login_check():
    print("登录检查中，请稍候[不要操作浏览器]")
    read_cookie()
    time.sleep(3)
    q1=driver.find_elements(By.CLASS_NAME, 'login-box')
    # print(q1)
    if len(q1) != 0:
        print('cookie已过期')
        get_cookie()
        read_cookie()
    else:
        print('登录成功！！[不要操作浏览器]')


login_check()



# list_cookies=cookieBefore
# list_cookies=[{'domain': '.qq.com', 'expiry': 1665911118, 'httpOnly': False, 'name': 'euin', 'path': '/', 'secure': False, 'value': 'oKSsoK6s7wcA7v**'}, {'domain': '.qq.com', 'expiry': 1658221518, 'httpOnly': False, 'name': 'qqmusic_key', 'path': '/', 'secure': False, 'value': 'Q_H_L_5T8s98_ryV-FIGQdyb3A2jsJleIAfbVcY2Y9wE7cAWMX-6bTIFUX3fQ'}, {'domain': '.qq.com', 'expiry': 1658221518, 'httpOnly': False, 'name': 'psrf_musickey_createtime', 'path': '/', 'secure': False, 'value': '1658135118'}, {'domain': '.y.qq.com', 'expiry': 1658136918, 'httpOnly': False, 'name': 'ts_last', 'path': '/', 'secure': False, 'value': 'y.qq.com/n/ryqq/search'}, {'domain': '.qq.com', 'expiry': 1665911118, 'httpOnly': False, 'name': 'psrf_qqunionid', 'path': '/', 'secure': False, 'value': '98FC1FE7B66D64BF326425409FD903C8'}, {'domain': '.qq.com', 'httpOnly': False, 'name': 'fqm_sessionid', 'path': '/', 'secure': False, 'value': 'd38b939b-0a36-4de2-9a06-bf800353e3ef'}, {'domain': '.qq.com', 'expiry': 1665911118, 'httpOnly': False, 'name': 'wxopenid', 'path': '/', 'secure': False, 'value': ''}, {'domain': '.qq.com', 'expiry': 1665911118, 'httpOnly': False, 'name': 'wxrefresh_token', 'path': '/', 'secure': False, 'value': ''}, {'domain': '.qq.com', 'httpOnly': False, 'name': 'login_type', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'httpOnly': False, 'name': '_qpsvr_localtk', 'path': '/', 'secure': False, 'value': '0.8641736728972611'}, {'domain': '.qq.com', 'expiry': 1665911118, 'httpOnly': False, 'name': 'wxunionid', 'path': '/', 'secure': False, 'value': ''}, {'domain': '.qq.com', 'expiry': 1665911118, 'httpOnly': False, 'name': 'psrf_qqopenid', 'path': '/', 'secure': False, 'value': 'E1ED718A3536084B1A9820D972004806'}, {'domain': '.qq.com', 'expiry': 1665911118, 'httpOnly': False, 'name': 'tmeLoginType', 'path': '/', 'secure': False, 'value': '2'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'fqm_pvqid', 'path': '/', 'secure': False, 'value': '96728496-58f5-4459-8053-0533d21b8c41'}, {'domain': '.y.qq.com', 'expiry': 1658221518, 'httpOnly': False, 'name': 'qm_keyst', 'path': '/', 'secure': False, 'value': 'Q_H_L_5T8s98_ryV-FIGQdyb3A2jsJleIAfbVcY2Y9wE7cAWMX-6bTIFUX3fQ'}, {'domain': '.qq.com', 'expiry': 2147483646, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'd7WALzswYS'}, {'domain': '.qq.com', 'expiry': 1665911118, 'httpOnly': False, 'name': 'psrf_qqrefresh_token', 'path': '/', 'secure': False, 'value': 'B191D680C3492CAB3197FEDA727E589D'}, {'domain': '.qq.com', 'expiry': 1665911118, 'httpOnly': False, 'name': 'psrf_access_token_expiresAt', 'path': '/', 'secure': False, 'value': '1665911118'}, {'domain': '.qq.com', 'expiry': 1665911118, 'httpOnly': False, 'name': 'uin', 'path': '/', 'secure': False, 'value': '1761166825'}, {'domain': '.qq.com', 'expiry': 2147483646, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': '85fa7f6b22f67a53a45df0f376fd223f2c4ecf9ef443e96ab440fe932044f6c8'}, {'domain': '.qq.com', 'expiry': 1658221518, 'httpOnly': False, 'name': 'qm_keyst', 'path': '/', 'secure': False, 'value': 'Q_H_L_5T8s98_ryV-FIGQdyb3A2jsJleIAfbVcY2Y9wE7cAWMX-6bTIFUX3fQ'}, {'domain': '.y.qq.com', 'expiry': 1721207118, 'httpOnly': False, 'name': 'ts_uid', 'path': '/', 'secure': False, 'value': '5893269412'}, {'domain': '.qq.com', 'httpOnly': False, 'name': 'pgv_info', 'path': '/', 'secure': False, 'value': 'ssid=s2881279537'}, {'domain': '.qq.com', 'expiry': 1665911118, 'httpOnly': False, 'name': 'psrf_qqaccess_token', 'path': '/', 'secure': False, 'value': '96C9CC48BE753EC611573CFF9BB5D49C'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '1327060342'}]

# 刷新页面即可更新cookie
driver.refresh()
time.sleep(2)
# driver.quit()
# 第二个标签
# driver.execute_script(js.format('https://y.qq.com/n/ryqq/search?w=%E5%91%A8%E6%9D%B0%E4%BC%A6%20-%20%E6%9C%80%E4%BC%9F%E5%A4%A7&t=album'))
# driver.switch_to.window(driver.window_handles[-1])

# time.sleep(2)
# driver.close()
