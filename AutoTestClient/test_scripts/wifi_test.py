from selenium import webdriver
from selenium.webdriver.support.ui import Select
import telnetlib
import os
import time
from data_model import *

def Login():

    try:
        tn.open(HOST_IP, port=23)
    except:
        print('{}网络连接失败'.format(HOST_IP))
    tn.read_until(b'Login: ', timeout=10)
    tn.write(USERNAME.encode('ascii') + b'\n')
    tn.read_until(b'Password: ', timeout=10)
    tn.write(PASSWORD.encode('ascii') + b'\n')
    time.sleep(2)
    command_result = tn.read_very_eager().decode('ascii')
    if 'Login incorrect' not in command_result:
        print('{}登录成功'.format(HOST_IP))
    else:
        print('{}登录失败，用户名或密码错误'.format(HOST_IP))
    
    tn.write(('echo > /data/debug'.encode('ascii') + b'\n'))
    browser.get(URL)  # 打开浏览器预设网址
    password_input = browser.find_element_by_name(LOGIN_PASSWORD_IPUNT_ELEMENT_NAME)
    password_input.send_keys(PASSWORD)
    login_button = browser.find_element_by_class_name(LOGIN_BUTTON_INPUT_CLASS_NAME)
    login_button.click()
    time.sleep(1)

def set_WIFI_security_WPA2PSK(enable):
    browser.get(URL)
    browser.get(URL+'/root/main.html')
    time.sleep(1)
    browser.switch_to.frame('menufrm')
    wifi_menu = browser.find_element_by_xpath(WIRELESS_MENU)
    wifi_menu.click()
    security_menu = browser.find_element_by_xpath(WIRELESS_SECURITY_MENU)
    security_menu.click()
    time.sleep(12)
    browser.switch_to.default_content()
    browser.switch_to.frame('basefrm')
    wpa2psk_select = Select(browser.find_element_by_name(WIRELESS_SECURITY_WPA2PSK_SELECT_ELEMENT_NAME))
    wpa2psk_select.select_by_value(enable)
    time.sleep(1)
    apply_button = browser.find_element_by_xpath(WIRELESS_SECURITY_APPLY_BUTTON)
    apply_button.click()
    time.sleep(10)
    continue_button = browser.find_element_by_xpath(WIRELESS_CONTINUE_BUTTON)
    continue_button.click()
    time.sleep(20)

def change_wifi_pwd(keyphrase):
    browser.get(URL)
    browser.get(URL+'/root/main.html')
    time.sleep(1)
    browser.switch_to.frame('menufrm')
    wifi_menu = browser.find_element_by_xpath(WIRELESS_MENU)
    wifi_menu.click()
    security_menu = browser.find_element_by_xpath(WIRELESS_SECURITY_MENU)
    security_menu.click()
    time.sleep(24)
    browser.switch_to.default_content()
    browser.switch_to.frame('basefrm')
    keyphrase_input = browser.find_element_by_xpath(WIRELESS_SECURITY_KEYPHRASE_INPUT)
    keyphrase_input.send_keys(keyphrase)
    time.sleep(1)
    apply_button = browser.find_element_by_xpath(WIRELESS_SECURITY_APPLY_BUTTON)
    apply_button.click()
    time.sleep(20)
    continue_button = browser.find_element_by_xpath(WIRELESS_CONTINUE_BUTTON)
    continue_button.click()
    time.sleep(20)

