from selenium import webdriver
from selenium.webdriver.support.ui import Select
import os
import telnetlib
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
    usrname_input = browser.find_element_by_name(LOGIN_PASSWORD_IPUNT_ELEMENT_NAME)
    usrname_input.send_keys(PASSWORD)
    login_button = browser.find_element_by_class_name(LOGIN_BUTTON_INPUT_CLASS_NAME)
    login_button.click()
    time.sleep(1)

def config_wan(wan_inf,wan_type,**args):
    '''
    配置WAN连接
    wan_inf eg：eth4
    wan_type 1 pppoe 2 ipoe 3 bridge
    args:
        wan_proc 可选值：IPV4/IPv4&IPv6/IPv6 # 不为桥接时必选
        vlan 必选
        pppUsername # 为pppoe时必选
        pppPassword # 为pppoe时必选
    '''
    browser.get(URL)
    browser.get(URL+'/root/main.html')
    time.sleep(1)
    browser.switch_to.frame('menufrm')
    try:
        advence_menu = browser.find_element_by_xpath(ADVENCE_MENU)
        advence_menu.click()
        wan_service_menu = browser.find_element_by_xpath(WAN_SERVICE_MENU)
        wan_service_menu.click()
    except:
        advence_menu = browser.find_element_by_xpath(ADVENCE_MENU_NO_DHCP)
        advence_menu.click()
        wan_service_menu = browser.find_element_by_xpath(WAN_SERVICE_MENU_NO_DHCP)
        wan_service_menu.click()
    browser.switch_to.default_content()
    browser.switch_to.frame('basefrm')
    add_button = browser.find_element_by_xpath(WAN_SERVICE_ADD_BUTTON)
    add_button.click()
    wan_inf_select = Select(browser.find_element_by_xpath(WAN_SERVICE_INTF_SELECT))
    wan_inf_select.select_by_value(wan_inf)
    next_button_1 = browser.find_element_by_xpath(WAN_SERVICE_NEXT_BUTTON_1)
    next_button_1.click()
    wan_type_radio = browser.find_element_by_xpath('/html/body/blockquote/form/table[1]/tbody/tr[{}]/td/input'.format(str(wan_type+1)))
    wan_type_radio.click()
    if wan_type != 3:
        wan_proc_select = Select(browser.find_element_by_xpath(WAN_SERVICE_PROTOCAL_SELECT))
        wan_proc_select.select_by_value(args['wan_proc'])
    if args['vlan'] != '':
        vlan_priority = browser.find_element_by_xpath(WAN_SERVICE_VLAN_PRIORITY)
        vlan_priority.clear()
        vlan_priority.send_keys('0')
        vlan_id = browser.find_element_by_xpath(WAN_SERVICE_VLAN_ID)
        vlan_id.clear()
        vlan_id.send_keys(args['vlan'])
    next_button_2 = browser.find_element_by_xpath(WAN_SERVICE_NEXT_BUTTON_2)
    next_button_2.click()
    if wan_type == 1:
        pppUsername = browser.find_element_by_xpath(WAN_SERVICE_PPPOE_USRNAME)
        pppUsername.send_keys(args['pppUsername'])
        pppPassword = browser.find_element_by_xpath(WAN_SERVICE_PPPOE_PASSWORD)
        pppPassword.send_keys(args['pppPassword'])
        next_button_3 = browser.find_element_by_xpath(WAN_SERVICE_PPPOE_NEXT_BUTTON_3)
        next_button_3.click()
        next_button_4 = browser.find_element_by_xpath(WAN_SERVICE_PPPOE_NEXT_BUTTON_4)
        next_button_4.click()
        next_button_5 = browser.find_element_by_xpath(WAN_SERVICE_PPPOE_NEXT_BUTTON_5)
        next_button_5.click()
        apply_button = browser.find_element_by_xpath(WAN_SERVICE_APPLY_BUTTON)
        apply_button.click()
    elif wan_type == 2:
        next_button_3 = browser.find_element_by_xpath(WAN_SERVICE_IPOE_NEXT_BUTTON_3)
        next_button_3.click()
        next_button_4 = browser.find_element_by_xpath(WAN_SERVICE_IPOE_NEXT_BUTTON_4)
        next_button_4.click()
        next_button_5 = browser.find_element_by_xpath(WAN_SERVICE_IPOE_NEXT_BUTTON_5)
        next_button_5.click()
        next_button_6 = browser.find_element_by_xpath(WAN_SERVICE_IPOE_NEXT_BUTTON_6)
        next_button_6.click()
        apply_button = browser.find_element_by_xpath(WAN_SERVICE_APPLY_BUTTON)
        apply_button.click()
    elif wan_type == 3:
        apply_button = browser.find_element_by_xpath(WAN_SERVICE_APPLY_BUTTON)
        apply_button.click()

def remove_all_wan_services():
    browser.get(URL)
    browser.get(URL+'/root/main.html')
    time.sleep(1)
    browser.switch_to.frame('menufrm')
    try:
        advence_menu = browser.find_element_by_xpath(ADVENCE_MENU)
        advence_menu.click()
        wan_service_menu = browser.find_element_by_xpath(WAN_SERVICE_MENU)
        wan_service_menu.click()
    except:
        advence_menu = browser.find_element_by_xpath(ADVENCE_MENU_NO_DHCP)
        advence_menu.click()
        wan_service_menu = browser.find_element_by_xpath(WAN_SERVICE_MENU_NO_DHCP)
        wan_service_menu.click()
    browser.switch_to.default_content()
    browser.switch_to.frame('basefrm')
    i = 1
    while True:
        if i == 1:
            i = i + 1
            continue
        try:
            rm_checkbox = browser.find_element_by_xpath('/html/body/blockquote/form/center/table/tbody/tr[{}]/td[14]/input'.format(str(i)))
            rm_checkbox.click()
            i = i + 1
        except:
            break
    remove_button = browser.find_element_by_xpath(WAN_SERVICE_REMOVE_BUTTON)
    remove_button.click()

# Login()
# config_wan('eth4',1,wan_proc='IPv6',vlan='',pppUsername='123456',pppPassword='987654')

