from selenium import webdriver
from selenium.webdriver.support.ui import Select
import telnetlib
import os
import yaml

with open('data_model/config.yaml','r',encoding='utf-8') as f:
    config = f.read()
    config = yaml.load(config,Loader=yaml.FullLoader)

HOST_IP = config['HOST_IP']
USERNAME = config['USERNAME']
PASSWORD = config['PASSWORD']
TEMPLATE = config['TEMPLATE']
IMG = config['IMG']
SN = config['SN']
MAC = config['MAC']
URL = 'http://' + HOST_IP
WAN_GATEWAY_IPOE = config['WAN_GATEWAY_IPOE']
WAN_GATEWAY_PPPOE = config['WAN_GATEWAY_PPPOE']
PC_LAN_INTF_NAME = config['PC_LAN_INTF_NAME']
STATIC_IP_IF_NO_DHCP = config['STATIC_IP_IF_NO_DHCP']
PC_PPPOE_NAME = config['PC_PPPOE_NAME']
WAN_INTF = config['WAN_INTF']
VLAN_PPPOE = config['VLAN_PPPOE']
VLAN_IPOE = config['VLAN_IPOE']
VLAN_BRIDGE = config['VLAN_BRIDGE']
PPPUSERNAME = config['PPPUSERNAME']
PPPPASSWORD = config['PPPPASSWORD']
PC_WIFI_INTF_NAME = config['PC_WIFI_INTF_NAME']
WIFI_PREFIX = config['WIFI_PREFIX']

with open('data_model/'+TEMPLATE,'r',encoding='utf-8') as f:
    template_ = f.read()
    template_ = yaml.load(template_,Loader=yaml.FullLoader)

ADVENCE_MENU = template_['ADVENCE_MENU']
ADVENCE_MENU_NO_DHCP = template_['ADVENCE_MENU_NO_DHCP']
BACKUP_SETTING_BUTTON = template_['BACKUP_SETTING_BUTTON']
BACKUP_SETTING_MENU = template_['BACKUP_SETTING_MENU']
DHCP_APPLY_BUTTON = template_['DHCP_APPLY_BUTTON']
DHCP_DISABLE_BUTTON = template_['DHCP_DISABLE_BUTTON']
DHCP_ENABLE_BUTTON = template_['DHCP_ENABLE_BUTTON']
LAN_IPV4_AUTOCONFIG_MENU = template_['LAN_IPV4_AUTOCONFIG_MENU']
LAN_IPV4_AUTOCONFIG_MENU_NO_DHCP = template_['LAN_IPV4_AUTOCONFIG_MENU_NO_DHCP']
LAN_MENU = template_['LAN_MENU']
LAN_MENU_NO_DHCP = template_['LAN_MENU_NO_DHCP']
LOGIN_BUTTON_INPUT_CLASS_NAME = template_['LOGIN_BUTTON_INPUT_CLASS_NAME']
LOGIN_PASSWORD_IPUNT_ELEMENT_NAME = template_['LOGIN_PASSWORD_IPUNT_ELEMENT_NAME']
MANAGEMENT_MENU = template_['MANAGEMENT_MENU']
MANAGEMENT_MENU_NO_DHCP = template_['MANAGEMENT_MENU_NO_DHCP']
SETTING_MENU = template_['SETTING_MENU']
STORAGE_DEVICE_INFO_MENU = template_['STORAGE_DEVICE_INFO_MENU']
STORAGE_DEVICE_INFO_MENU_NO_DHCP = template_['STORAGE_DEVICE_INFO_MENU_NO_DHCP']
STORAGE_DEVICE_INFO_VOLUMENAME_1 = template_['STORAGE_DEVICE_INFO_VOLUMENAME_1']
STORAGE_SERVICE_MENU = template_['STORAGE_SERVICE_MENU']
STORAGE_SERVICE_MENU_NO_DHCP = template_['STORAGE_SERVICE_MENU_NO_DHCP']
STORAGE_SERVICE_USER_ACCOUNT_ADD_BUTTON = template_['STORAGE_SERVICE_USER_ACCOUNT_ADD_BUTTON']
STORAGE_SERVICE_USER_ACCOUNT_APPLY_BUTTON = template_['STORAGE_SERVICE_USER_ACCOUNT_APPLY_BUTTON']
STORAGE_SERVICE_USER_ACCOUNT_CONFIRM_PASSWORD_INPUT = template_['STORAGE_SERVICE_USER_ACCOUNT_CONFIRM_PASSWORD_INPUT']
STORAGE_SERVICE_USER_ACCOUNT_MENU = template_['STORAGE_SERVICE_USER_ACCOUNT_MENU']
STORAGE_SERVICE_USER_ACCOUNT_MENU_NO_DHCP = template_['STORAGE_SERVICE_USER_ACCOUNT_MENU_NO_DHCP']
STORAGE_SERVICE_USER_ACCOUNT_PASSWORD_INPUT = template_['STORAGE_SERVICE_USER_ACCOUNT_PASSWORD_INPUT']
STORAGE_SERVICE_USER_ACCOUNT_REMOVE_BUTTON = template_['STORAGE_SERVICE_USER_ACCOUNT_REMOVE_BUTTON']
STORAGE_SERVICE_USER_ACCOUNT_REMOVE_CHECKBOX = template_['STORAGE_SERVICE_USER_ACCOUNT_REMOVE_CHECKBOX']
STORAGE_SERVICE_USER_ACCOUNT_USERNAME_INPUT = template_['STORAGE_SERVICE_USER_ACCOUNT_USERNAME_INPUT']
STORAGE_SERVICE_USER_ACCOUNT_VOLUMENAME_INPUT = template_['STORAGE_SERVICE_USER_ACCOUNT_VOLUMENAME_INPUT']
UPDATE_FW_BUTTON = template_['UPDATE_FW_BUTTON']
UPDATE_FW_INPUT = template_['UPDATE_FW_INPUT']
UPDATE_FW_MENU = template_['UPDATE_FW_MENU']
UPDATE_FW_MENU_NO_DHCP = template_['UPDATE_FW_MENU_NO_DHCP']
UPDATE_SETTING_BUTTON = template_['UPDATE_SETTING_BUTTON']
UPDATE_SETTING_INPUT = template_['UPDATE_SETTING_INPUT']
UPDATE_SETTING_MENU = template_['UPDATE_SETTING_MENU']
WAN_SERVICE_ADD_BUTTON = template_['WAN_SERVICE_ADD_BUTTON']
WAN_SERVICE_APPLY_BUTTON = template_['WAN_SERVICE_APPLY_BUTTON']
WAN_SERVICE_INTF_SELECT = template_['WAN_SERVICE_INTF_SELECT']
WAN_SERVICE_IPOE_NEXT_BUTTON_3 = template_['WAN_SERVICE_IPOE_NEXT_BUTTON_3']
WAN_SERVICE_IPOE_NEXT_BUTTON_4 = template_['WAN_SERVICE_IPOE_NEXT_BUTTON_4']
WAN_SERVICE_IPOE_NEXT_BUTTON_5 = template_['WAN_SERVICE_IPOE_NEXT_BUTTON_5']
WAN_SERVICE_IPOE_NEXT_BUTTON_6 = template_['WAN_SERVICE_IPOE_NEXT_BUTTON_6']
WAN_SERVICE_MENU = template_['WAN_SERVICE_MENU']
WAN_SERVICE_MENU_NO_DHCP = template_['WAN_SERVICE_MENU_NO_DHCP']
WAN_SERVICE_NEXT_BUTTON_1 = template_['WAN_SERVICE_NEXT_BUTTON_1']
WAN_SERVICE_NEXT_BUTTON_2 = template_['WAN_SERVICE_NEXT_BUTTON_2']
WAN_SERVICE_PPPOE_NEXT_BUTTON_3 = template_['WAN_SERVICE_PPPOE_NEXT_BUTTON_3']
WAN_SERVICE_PPPOE_NEXT_BUTTON_4 = template_['WAN_SERVICE_PPPOE_NEXT_BUTTON_4']
WAN_SERVICE_PPPOE_NEXT_BUTTON_5 = template_['WAN_SERVICE_PPPOE_NEXT_BUTTON_5']
WAN_SERVICE_PPPOE_PASSWORD = template_['WAN_SERVICE_PPPOE_PASSWORD']
WAN_SERVICE_PPPOE_USRNAME = template_['WAN_SERVICE_PPPOE_USRNAME']
WAN_SERVICE_PROTOCAL_SELECT = template_['WAN_SERVICE_PROTOCAL_SELECT']
WAN_SERVICE_REMOVE_BUTTON = template_['WAN_SERVICE_REMOVE_BUTTON']
WAN_SERVICE_VLAN_ID = template_['WAN_SERVICE_VLAN_ID']
WAN_SERVICE_VLAN_PRIORITY = template_['WAN_SERVICE_VLAN_PRIORITY']
WIRELESS_CONTINUE_BUTTON = template_['WIRELESS_CONTINUE_BUTTON']
WIRELESS_MENU = template_['WIRELESS_MENU']
WIRELESS_SECURITY_APPLY_BUTTON = template_['WIRELESS_SECURITY_APPLY_BUTTON']
WIRELESS_SECURITY_KEYPHRASE_INPUT = template_['WIRELESS_SECURITY_KEYPHRASE_INPUT']
WIRELESS_SECURITY_MENU = template_['WIRELESS_SECURITY_MENU']
WIRELESS_SECURITY_WPA2PSK_SELECT_ELEMENT_NAME = template_['WIRELESS_SECURITY_WPA2PSK_SELECT_ELEMENT_NAME']

tn = telnetlib.Telnet(HOST_IP, port=23)
os.system("set path=%path%;{}".format(os.getcwd()))
options = webdriver.ChromeOptions()
prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': os.getcwd()}
options.add_experimental_option('prefs', prefs)
browser = webdriver.Chrome(chrome_options=options)  # 声明浏览器
browser.maximize_window()  # 最大化窗口