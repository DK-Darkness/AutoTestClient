from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

def getSpeedTest():

    browser = webdriver.Chrome()  # 声明浏览器
    browser.maximize_window()  # 最大化窗口

    URL='http://10.8.8.88:8032'

    browser.get(URL)  # 打开浏览器预设网址

    start_stop_button = browser.find_element_by_id('startStopBtn')  # 查找按钮

    start_stop_button.click()  # 点击按钮

    time.sleep(20)  # 等待20s

    dlSpeed = browser.find_element_by_id('dlText').text  # 获取下载速度并输出
    ulSpeed = browser.find_element_by_id('ulText').text  # 获取上传速度并输出

    browser.close()  # 关闭浏览器

    return dlSpeed,ulSpeed