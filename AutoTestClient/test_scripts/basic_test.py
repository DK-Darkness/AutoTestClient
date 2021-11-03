from data_model import *
import time

def disable_dhcp(status):
    '''
    bool status : True disable False enable
    '''
    browser.get(URL+'/root/main.html')
    time.sleep(1)
    browser.switch_to.frame('menufrm')
    try:
        advence_menu = browser.find_element_by_xpath(ADVENCE_MENU)
        advence_menu.click()
        lan_menu = browser.find_element_by_xpath(LAN_MENU)
        lan_menu.click()
        lan_ipv4_autoconfig_menu = browser.find_element_by_xpath(LAN_IPV4_AUTOCONFIG_MENU)
        lan_ipv4_autoconfig_menu.click()
    except:
        advence_menu = browser.find_element_by_xpath(ADVENCE_MENU_NO_DHCP)
        advence_menu.click()
        lan_menu = browser.find_element_by_xpath(LAN_MENU_NO_DHCP)
        lan_menu.click()
        lan_ipv4_autoconfig_menu = browser.find_element_by_xpath(LAN_IPV4_AUTOCONFIG_MENU_NO_DHCP)
        lan_ipv4_autoconfig_menu.click()
    browser.switch_to.default_content()
    browser.switch_to.frame('basefrm')
    if status:
        disable_button = browser.find_element_by_xpath(DHCP_DISABLE_BUTTON)
        disable_button.click()
    else:
        enable_button = browser.find_element_by_xpath(DHCP_ENABLE_BUTTON)
        enable_button.click()
    apply_button = browser.find_element_by_xpath(DHCP_APPLY_BUTTON)
    apply_button.click()

def backup_setting():
    browser.get(URL+'/root/main.html')
    time.sleep(1)
    browser.switch_to.frame('menufrm')
    management_menu =  browser.find_element_by_xpath(MANAGEMENT_MENU)
    management_menu.click()
    setting_menu =  browser.find_element_by_xpath(SETTING_MENU)
    setting_menu.click()
    backup_menu =  browser.find_element_by_xpath(BACKUP_SETTING_MENU)
    backup_menu.click() 
    browser.switch_to.default_content()
    browser.switch_to.frame('basefrm')
    backup_setting_button = browser.find_element_by_xpath(BACKUP_SETTING_BUTTON)
    backup_setting_button.click()

def update_setting(file):
    browser.get(URL+'/root/main.html')
    time.sleep(1)
    browser.switch_to.frame('menufrm')
    management_menu =  browser.find_element_by_xpath(MANAGEMENT_MENU)
    management_menu.click()
    setting_menu =  browser.find_element_by_xpath(SETTING_MENU)
    setting_menu.click()
    update_setting_menu =browser.find_element_by_xpath(UPDATE_SETTING_MENU)
    update_setting_menu.click()
    browser.switch_to.default_content()
    browser.switch_to.frame('basefrm')
    update_input = browser.find_element_by_xpath(UPDATE_SETTING_INPUT)
    update_input.send_keys(file)
    update_setting_button = browser.find_element_by_xpath(UPDATE_SETTING_BUTTON)
    update_setting_button.click()

def upgrade_sw(file):
    browser.get(URL+'/root/main.html')
    time.sleep(1)
    browser.switch_to.frame('menufrm')
    try:
        mngt_menu = browser.find_element_by_xpath(MANAGEMENT_MENU)
        mngt_menu.click()
        update_menu = browser.find_element_by_xpath(UPDATE_FW_MENU)
        update_menu.click()
    except:
        mngt_menu = browser.find_element_by_xpath(MANAGEMENT_MENU_NO_DHCP)
        mngt_menu.click()
        update_menu = browser.find_element_by_xpath(UPDATE_FW_MENU_NO_DHCP)
        update_menu.click()
    browser.switch_to.default_content()
    browser.switch_to.frame('basefrm')
    uploadinput = browser.find_element_by_xpath(UPDATE_FW_INPUT)
    uploadinput.send_keys(file)
    update_button = browser.find_element_by_xpath(UPDATE_FW_BUTTON)
    update_button.click()

def smb_create():
    browser.get(URL+'/root/main.html')
    time.sleep(1)
    browser.switch_to.frame('menufrm')
    try:
        advence_menu = browser.find_element_by_xpath(ADVENCE_MENU)
        advence_menu.click()
        storage_service_menu = browser.find_element_by_xpath(STORAGE_SERVICE_MENU)
        storage_service_menu.click()
        storage_device_info_menu = browser.find_element_by_xpath(STORAGE_DEVICE_INFO_MENU)
        storage_device_info_menu.click()
    except:
        advence_menu = browser.find_element_by_xpath(ADVENCE_MENU_NO_DHCP)
        advence_menu.click()
        storage_service_menu = browser.find_element_by_xpath(STORAGE_SERVICE_MENU_NO_DHCP)
        storage_service_menu.click()
        storage_device_info_menu = browser.find_element_by_xpath(STORAGE_DEVICE_INFO_MENU_NO_DHCP)
        storage_device_info_menu.click()
    browser.switch_to.default_content()
    browser.switch_to.frame('basefrm')
    volumename = browser.find_element_by_xpath(STORAGE_DEVICE_INFO_VOLUMENAME_1).text
    browser.switch_to.default_content()
    browser.switch_to.frame('menufrm')
    try:
        user_account_menu = browser.find_element_by_xpath(STORAGE_SERVICE_USER_ACCOUNT_MENU)
        user_account_menu.click()
    except:
        user_account_menu = browser.find_element_by_xpath(STORAGE_SERVICE_USER_ACCOUNT_MENU_NO_DHCP)
        user_account_menu.click()
    browser.switch_to.default_content()
    browser.switch_to.frame('basefrm')
    add_button = browser.find_element_by_xpath(STORAGE_SERVICE_USER_ACCOUNT_ADD_BUTTON)
    add_button.click()
    username_input = browser.find_element_by_xpath(STORAGE_SERVICE_USER_ACCOUNT_USERNAME_INPUT)
    username_input.send_keys('admin')
    password_input = browser.find_element_by_xpath(STORAGE_SERVICE_USER_ACCOUNT_PASSWORD_INPUT)
    password_input.send_keys('123')
    confrim_pass_input = browser.find_element_by_xpath(STORAGE_SERVICE_USER_ACCOUNT_CONFIRM_PASSWORD_INPUT)
    confrim_pass_input.send_keys('123')
    volumename_input = browser.find_element_by_xpath(STORAGE_SERVICE_USER_ACCOUNT_VOLUMENAME_INPUT)
    volumename_input.send_keys(volumename)
    apply_button = browser.find_element_by_xpath(STORAGE_SERVICE_USER_ACCOUNT_APPLY_BUTTON)
    apply_button.click()

    return volumename

def smb_remove():
    browser.get(URL+'/root/main.html')
    time.sleep(1)
    browser.switch_to.frame('menufrm')
    try:
        advence_menu = browser.find_element_by_xpath(ADVENCE_MENU)
        advence_menu.click()
        storage_service_menu = browser.find_element_by_xpath(STORAGE_SERVICE_MENU)
        storage_service_menu.click()
        user_account_menu = browser.find_element_by_xpath(STORAGE_SERVICE_USER_ACCOUNT_MENU)
        user_account_menu.click()
    except:
        advence_menu = browser.find_element_by_xpath(ADVENCE_MENU_NO_DHCP)
        advence_menu.click()
        storage_service_menu = browser.find_element_by_xpath(STORAGE_SERVICE_MENU_NO_DHCP)
        storage_service_menu.click()
        user_account_menu = browser.find_element_by_xpath(STORAGE_SERVICE_USER_ACCOUNT_MENU_NO_DHCP)
        user_account_menu.click()
    browser.switch_to.default_content()
    browser.switch_to.frame('basefrm')
    remove_checkbox = browser.find_element_by_xpath(STORAGE_SERVICE_USER_ACCOUNT_REMOVE_CHECKBOX)
    remove_checkbox.click()
    remove_button = browser.find_element_by_xpath(STORAGE_SERVICE_USER_ACCOUNT_REMOVE_BUTTON)
    remove_button.click()