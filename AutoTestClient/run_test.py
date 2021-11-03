'''
需要下载对应浏览器版本的webdriver放置到本脚本同级目录下
当前附带版本：91.0.4472.19

chrom浏览器的web driver（chromedriver.exe），可以在下面网址访问：
http://npm.taobao.org/mirrors/chromedriver/


其他浏览器驱动可以见下面列表:

firefox（火狐浏览器）的web driver （geckodriver.exe）在这里访问：
https://github.com/mozilla/geckodriver/releases

Edge:https://developer.microsoft.com/en-us/micrsosft-edage/tools/webdriver

Safari:https://webkit.org/blog/6900/webdriver-support-in-safari-10/

如果使用非google浏览器请修改data_model/config.py中的webdriver声明
'''
from data_model import *
from test_scripts import basic_test, default_check, wan_test, wifi_test,speedtest
from utils import osutils,smbutil
from utils import create_report
import time,os

import pickle

with open('data_model/test_case.pickle','rb') as f:
    test_case_all = pickle.load(f)

def process_test(id):
    if id == 1:
        test_case_all[0]['result'] = 'ABSENCE'
    if id == 2:
        test_case_all[1]['result'] = 'PASS'
        test_case_all[5]['result'] = 'PASS'
        default_check.Login()
        sn = default_check.getSN_360()
        if default_check.checkSSID('WIFI_PREFIX',sn):
            pass
        else:
            test_case_all[1]['result'] = 'FAIL'
            test_case_all[5]['result'] = 'FAIL'
        if default_check.check_akm('psk2'):
            pass
        else:
            test_case_all[1]['result'] = 'FAIL'
            test_case_all[5]['result'] = 'FAIL'
    if id == 3:
        test_case_all[2]['result'] = 'ABSENCE'
    ################################# WIFI TEST START ######################################
    if id == 4:
        wifi_test.Login()
        wifi_test.set_WIFI_security_WPA2PSK('disabled')
        sn = default_check.getSN_360()
        time.sleep(60)
        osutils.disable_intf(PC_LAN_INTF_NAME)
        osutils.disable_intf(PC_WIFI_INTF_NAME)
        osutils.enable_intf(PC_WIFI_INTF_NAME)
        osutils.disconnect_wifi()
        time.sleep(20)
        osutils.wifi_connect('WIFI_PREFIX'+sn[-4:],'')
        time.sleep(5)
        if osutils.is_up(HOST_IP):
            test_case_all[3]['result'] = 'FAIL'
            test_case_all[7]['result'] = 'FAIL'
        else:
            test_case_all[3]['result'] = 'PASS'
            test_case_all[7]['result'] = 'PASS'
    if id == 5:
        test_case_all[4]['result'] = 'PASS'
        test_case_all[8]['result'] = 'PASS'
        osutils.enable_intf(PC_LAN_INTF_NAME)
        time.sleep(20)
        try:
            wifi_test.Login()
        except:
            default_check.Login()  # 重连telnet, 下同
    ################ 连接异常 #####################
        wifi_test.set_WIFI_security_WPA2PSK('enabled')
        wifi_test.change_wifi_pwd('asdfghjk')
        sn = default_check.getSN_360()
        time.sleep(60)
        osutils.disable_intf(PC_LAN_INTF_NAME)
        osutils.disable_intf(PC_WIFI_INTF_NAME)
        osutils.enable_intf(PC_WIFI_INTF_NAME)
        osutils.disconnect_wifi()
        time.sleep(20)
        osutils.wifi_connect('WIFI_PREFIX'+sn[-4:],'asdfghjk')
        time.sleep(20)
        osutils.wifi_connect('WIFI_PREFIX'+sn[-4:],'asdfghjk')
        time.sleep(5)
        # if osutils.is_up(HOST_IP):
        #     test_case_all[4]['result'] = 'FAIL'
        #     test_case_all[8]['result'] = 'FAIL'
        # else:
        #     pass
    ################################################
        osutils.enable_intf(PC_LAN_INTF_NAME)
        time.sleep(20)
        try:
            wifi_test.Login()
        except:
            default_check.Login()
        wifi_test.change_wifi_pwd('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
        time.sleep(60)
        osutils.disable_intf(PC_LAN_INTF_NAME)
        osutils.disable_intf(PC_WIFI_INTF_NAME)
        osutils.enable_intf(PC_WIFI_INTF_NAME)
        osutils.disconnect_wifi()
        time.sleep(20)
        osutils.wifi_connect('WIFI_PREFIX'+sn[-4:],'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
        time.sleep(5)
        if osutils.is_up(HOST_IP):
            test_case_all[4]['result'] = 'FAIL'
            test_case_all[8]['result'] = 'FAIL'
        else:
            pass
        osutils.disconnect_wifi()
    ###########无法成功建立64位密码的profile#########
        # osutils.enable_intf('以太网 2')
        # time.sleep(15)
        # try:
        #     wifi_test.Login()
        # except:
        #     default_check.Login()
        # wifi_test.change_wifi_pwd('1111111111111111111111111111111111111111111111111111111111111111')
        # time.sleep(60)
        # osutils.disable_intf('以太网 2')
        # osutils.disable_intf('WLAN')
        # osutils.enable_intf('WLAN')
        # time.sleep(20)
        # osutils.wifi_connect('WIFI_PREFIX'+sn[-4:],'1111111111111111111111111111111111111111111111111111111111111111')
        # time.sleep(5)
        # if osutils.is_up(HOST_IP):
        #     test_case_all[4]['result'] = 'FAIL'
        #     test_case_all[8]['result'] = 'FAIL'
        # else:
        #     pass
    #####################################
    # 6 is checked in 2
    if id == 7:
        osutils.enable_intf(PC_LAN_INTF_NAME)
        osutils.disable_intf(PC_WIFI_INTF_NAME)  # 防止连接到办公网影响测试结果
        time.sleep(20)
        try:
            wifi_test.Login()
        except:
            default_check.Login()
        test_case_all[6]['result'] = 'ABSENCE'
    # 8 & 9 is checked in 4 & 5

    ################################# WIFI TEST END ######################################

    if id == 10:
        test_case_all[9]['result'] = 'ABSENCE'
    if id == 11:
        test_case_all[10]['result'] = 'ABSENCE'
    if id == 12:
        test_case_all[11]['result'] = 'ABSENCE'
    if id == 13:
        test_case_all[12]['result'] = 'ABSENCE'
    if id == 14:
        test_case_all[13]['result'] = 'ABSENCE'
    if id == 15:
        test_case_all[14]['result'] = 'ABSENCE'
    ############################# WAN TEST START ########################################

    if id == 16:
        test_case_all[15]['result'] = 'PASS'
        try:
            wan_test.remove_all_wan_services()
        except:
            pass
        wan_test.config_wan(WAN_INTF,3,vlan=VLAN_BRIDGE)
        time.sleep(5)
        osutils.pppoe_on_pc('connect',conn_name=PC_PPPOE_NAME,pppUsername=PPPUSERNAME,pppPassword=PPPPASSWORD)
        time.sleep(5)
        if osutils.is_up(WAN_GATEWAY_PPPOE):
            test_case_all[15]['result'] = 'FAIL'
        else:
            pass
        osutils.pppoe_on_pc('disconnect',conn_name=PC_PPPOE_NAME)
        if osutils.is_up(WAN_GATEWAY_PPPOE):
            pass
        else:
            test_case_all[15]['result'] = 'FAIL'
        osutils.pppoe_on_pc('connect',conn_name=PC_PPPOE_NAME,pppUsername='8888',pppPassword='8888')
        time.sleep(5)
        if osutils.is_up(WAN_GATEWAY_PPPOE):
            pass
        else:
            test_case_all[15]['result'] = 'FAIL'

    if id == 17:
        test_case_all[16]['result'] = 'PASS'
        osutils.set_static_ip(PC_LAN_INTF_NAME,STATIC_IP_IF_NO_DHCP,HOST_IP)
        time.sleep(10)
        try:
            wifi_test.Login()
        except:
            pass
        wan_test.remove_all_wan_services()
        osutils.set_dhcp(PC_LAN_INTF_NAME)
        osutils.dhcp_renew()
        time.sleep(15)
        wan_test.config_wan(WAN_INTF,1,vlan=VLAN_PPPOE,wan_proc='IPV4',pppUsername=PPPUSERNAME,pppPassword=PPPPASSWORD)
        time.sleep(15)
        if osutils.is_up(WAN_GATEWAY_PPPOE):
            test_case_all[16]['result'] = 'FAIL'
        else:
            pass
        wan_test.remove_all_wan_services()
        wan_test.config_wan(WAN_INTF,1,vlan=VLAN_PPPOE,wan_proc='IPV4',pppUsername='8888',pppPassword='8888')
        time.sleep(15)
        if osutils.is_up(WAN_GATEWAY_PPPOE):
            pass
        else:
            test_case_all[15]['result'] = 'FAIL'

    if id == 18:
        wan_test.remove_all_wan_services()
        test_case_all[17]['result'] = 'PASS'
        wan_test.config_wan(WAN_INTF,2,vlan=VLAN_IPOE,wan_proc='IPV4')
        time.sleep(5)
        if osutils.is_up(WAN_GATEWAY_IPOE):
            test_case_all[17]['result'] = 'FAIL'
        else:
            pass

    ###################################### WAN TEST END #############################################
    if id == 19:
        test_case_all[18]['result'] = 'ABSENCE'
    if id == 20:
        test_case_all[19]['result'] = 'ABSENCE'
    if id == 21 or id == 22 or id == 23 or id == 24:
        test_case_all[20]['result'] = 'ABSENCE'
        test_case_all[21]['result'] = 'ABSENCE'
        test_case_all[22]['result'] = 'ABSENCE'
        test_case_all[23]['result'] = 'ABSENCE'
    if id == 25:
        test_case_all[24]['result'] = 'PASS'
        basic_test.disable_dhcp(True)
        osutils.dhcp_renew()
        time.sleep(15)
        if osutils.is_up(HOST_IP):
            pass
        else:
            test_case_all[24]['result'] = 'FAIL'
        osutils.set_static_ip(PC_LAN_INTF_NAME,STATIC_IP_IF_NO_DHCP,HOST_IP)
        osutils.disable_intf(PC_LAN_INTF_NAME)
        osutils.enable_intf(PC_LAN_INTF_NAME)
        time.sleep(15)
        basic_test.disable_dhcp(False)
        osutils.set_dhcp(PC_LAN_INTF_NAME)
        osutils.dhcp_renew()
        time.sleep(15)
        if osutils.is_up(HOST_IP):
            test_case_all[24]['result'] = 'FAIL'
        else:
            pass
    if id == 26:
        default_check.Login()
        test_case_all[25]['result'] = 'PASS'
        basic_test.backup_setting()
        time.sleep(1)
        if os.path.exists('backupsettings.conf'):
            pass
        else:
            test_case_all[25]['result'] = 'FAIL'
    if id == 27:
        test_case_all[26]['result'] = 'PASS'
        default_check.restore_default()
        time.sleep(60)
        while True:
           if not osutils.is_up(HOST_IP):
               break
        time.sleep(20)
        try:
            wifi_test.Login()
        except:
            pass
        basic_test.update_setting(os.getcwd()+'\\backupsettings.conf')
        time.sleep(60)
        while True:
           if not osutils.is_up(HOST_IP):
               break
        time.sleep(20)
        wifi_test.Login()
        pass_src = default_check.check_wifi_password()
        print(pass_src)
        pass_tgt = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
        if pass_tgt in pass_src:
            pass
        else:
            test_case_all[26]['result'] = 'FAIL'
    if id == 28:
        test_case_all[27]['result'] = 'FAIL'
        for i in range(0,1):
            basic_test.upgrade_sw(IMG)
            while True:
                if osutils.is_up(HOST_IP):
                    break
            time.sleep(60)
            while True:
                if not osutils.is_up(HOST_IP):
                    break
            time.sleep(20)
            wifi_test.Login()  # 如果失败，程序将会异常结束
        test_case_all[27]['result'] = 'PASS'
    if id == 29:
        test_case_all[28]['result'] = 'ABSENCE'
    if id == 30:
        test_case_all[29]['result'] = 'ABSENCE'
    if id == 31:
        test_case_all[30]['result'] = 'PASS'
        try:
            volume = basic_test.smb_create()  
            if smbutil.samba_test(HOST_IP,volume):
                pass
            else:
                test_case_all[30]['result'] = 'FAIL'
            basic_test.smb_remove()
            if smbutil.samba_test(HOST_IP,volume):
                test_case_all[30]['result'] = 'FAIL'
            else:
                pass
        except:
            test_case_all[30]['result'] = 'ABSENCE'
    if id >= 32 and id < 37:
        # TODO TR069 TEST
        pass
    if id == 37:
        test_case_all[36]['result'] = 'ABSENCE'
    if id == 38 or id == 39:
        test_case_all[37]['result'] = 'ABSENCE'
        test_case_all[38]['result'] = 'ABSENCE'
    if id == 40:
        test_case_all[39]['result'] = 'PASS'
        config_model = default_check.check_config_mode_360()
        if 'user_settings' in config_model:
            pass
        else:
            test_case_all[39]['result'] = 'FAIL'
        default_check.restore_tofactory()
        time.sleep(60)
        while True:
           if not osutils.is_up(HOST_IP):
               break
        osutils.set_static_ip(PC_LAN_INTF_NAME,STATIC_IP_IF_NO_DHCP,HOST_IP)
        osutils.disable_intf(PC_LAN_INTF_NAME)
        osutils.enable_intf(PC_LAN_INTF_NAME)
        time.sleep(15)
        default_check.Login()
        config_model = default_check.check_config_mode_360()
        if 'manufacturing_settings' in config_model:
            pass
        else:
            test_case_all[39]['result'] = 'FAIL'
        default_check.restore_default()
        time.sleep(60)
        while True:
           if not osutils.is_up(HOST_IP):
               break
        time.sleep(20)
        osutils.set_dhcp(PC_LAN_INTF_NAME)
        osutils.dhcp_renew()
        time.sleep(20)
        default_check.Login()
        config_model = default_check.check_config_mode_360()
        if 'default_settings' in config_model:
            pass
        else:
            test_case_all[39]['result'] = 'FAIL'
        osutils.set_dhcp(PC_LAN_INTF_NAME)
        osutils.dhcp_renew()
        time.sleep(15)
    if id == 41:
        default_check.Login()
        test_case_all[40]['result'] = 'PASS'
        default_check.change_sn_mac_360('111111111111','11:11:11:11:11:11')
        time.sleep(60)
        while True:
            if not osutils.is_up(HOST_IP):
                break
        time.sleep(20)
        default_check.Login()
        if '11:11:11:11:11:11' in default_check.getMAC_360():
            pass
        else:
            test_case_all[40]['result'] = 'FAIL'
        if '111111111111' in default_check.getSN_360():
            pass
        else:
            test_case_all[40]['result'] = 'FAIL'
        default_check.change_sn_mac_360(SN,MAC)
        time.sleep(60)
        while True:
            if not osutils.is_up(HOST_IP):
                break
        time.sleep(20)
        default_check.Login()
    if id == 42:
        test_case_all[41]['result'] = 'PASS'
        test_case_all[42]['result'] = 'PASS'
        default_check.restore_default()
        time.sleep(60)
        while True:
           if not osutils.is_up(HOST_IP):
               break
        time.sleep(20)
        default_check.Login()
        osutils.enable_intf(PC_WIFI_INTF_NAME)
        time.sleep(20)
        osutils.wifi_connect('WIFI_PREFIX'+SN[-4:],SN[-8:])
        dl_speed,ul_speed = speedtest.getSpeedTest()
        if float(dl_speed) > 800 and float(ul_speed) > 800:
            pass
        else:
            test_case_all[41]['result'] = 'FAIL'
            test_case_all[42]['result'] = 'FAIL'
    # 43 is tested in 42
    if id == 44 or id == 45:
        test_case_all[43]['result'] = 'ABSENCE'
        test_case_all[44]['result'] = 'ABSENCE'

for item in test_case_all:
    process_test(item['id'])
    create_report.write_to_report(test_case_all)

browser.get('file:///{}/test_report.html'.format(os.getcwd()))