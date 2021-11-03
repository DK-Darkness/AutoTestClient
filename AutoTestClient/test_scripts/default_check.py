import os
import time
import telnetlib
import re
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

def cmdInput():
    temp = tn.read_very_eager().decode('ascii')
    tn.write(b'\n')
    time.sleep(1)
    shell = tn.read_very_eager().decode('ascii')
    if '#' in shell:
        tn.write('exit'.encode('ascii') + b'\n')
    time.sleep(1)
    temp = tn.read_very_eager().decode('ascii')


def shellInput():
    temp = tn.read_very_eager().decode('ascii')
    tn.write(b'\n')
    time.sleep(1)
    shell = tn.read_very_eager().decode('ascii')
    if '>' in shell:
        tn.write('sh'.encode('ascii') + b'\n')
    time.sleep(1)
    temp = tn.read_very_eager().decode('ascii')


def getSN_178():
    cmdInput()
    tn.write(('serialnum'.encode('ascii') + b'\n'))
    time.sleep(2)
    sn = tn.read_very_eager().decode('ascii')
    # TODO 匹配sn
    return sn

def getSN_360():
    shellInput()
    tn.write(('mfgtools --sn'.encode('ascii') + b'\n'))
    time.sleep(2)
    sn = tn.read_very_eager().decode('ascii')
    sn = sn.split('\n')[1]
    partten = re.compile('\w+')
    sn = partten.findall(sn)[0]
    print(sn)
    return sn

def checkSSID(prefix,sn):
    shellInput()
    tn.write(('wl -i wl0 ssid'.encode('ascii') + b'\n'))
    time.sleep(2)
    ssid_src = tn.read_very_eager().decode('ascii')
    print(ssid_src)
    last4 = sn[-4:]
    ssid_tgt = prefix+last4
    print(ssid_tgt)
    if ssid_tgt in ssid_src:
        return True
    else:
        return False

def checkCountry(country_tgt):
    shellInput()
    tn.write(('wl -i wl0 country'.encode('ascii') + b'\n'))
    time.sleep(2)
    country = tn.read_very_eager().decode('ascii')
    if country_tgt in country:
        return True
    else:
        return False

def check_akm(akm_tgt):
    shellInput()
    tn.write(('nvram show | grep akm'.encode('ascii') + b'\n'))
    time.sleep(2)
    akm = tn.read_very_eager().decode('ascii')
    partten = re.compile('wl0_akm=(\w+)')
    for line in akm.split('\n'):
        if partten.findall(line):
            akm = partten.findall(line)[0]
    if akm == akm_tgt:
        return True
    else:
        return False

def restore_default():
    cmdInput()
    tn.write(('restoredefault'.encode('ascii') + b'\n'))

def restore_tofactory():
    cmdInput()
    tn.write(('restoredefault tofactory'.encode('ascii') + b'\n'))

def check_config_mode_360():
    shellInput()
    tn.write(('mfgtools -c "showconfigmode"'.encode('ascii') + b'\n'))
    time.sleep(2)
    config_mode = tn.read_very_eager().decode('ascii')
    config_mode = config_mode.split('\n')[1]
    return config_mode

def change_sn_mac_360(sn,mac):
    shellInput()
    tn.write(('mfgtools --sn {}'.format(sn).encode('ascii') + b'\n'))
    time.sleep(1)
    tn.write(('mfgtools ethaddr {}'.format(mac).encode('ascii') + b'\n'))
    time.sleep(1)
    tn.write(('reboot'.encode('ascii') + b'\n'))

def check_config_mode_178():
    # TODO check config mode
    pass

def change_sn_178():
    # TODO change SN
    pass

def change_mac_178():
    # TODO change MAC
    pass

def check_wifi_password():
    shellInput()
    tn.write(('nvram get wl0_wpa_psk'.encode('ascii') + b'\n'))
    time.sleep(2)
    wl0_password = tn.read_very_eager().decode('ascii')
    wl0_password = wl0_password.split('\n')[1]
    return wl0_password

def getMAC_360():
    shellInput()
    tn.write(('mfgtools --ethaddr'.encode('ascii') + b'\n'))
    time.sleep(2)
    mac = tn.read_very_eager().decode('ascii')
    mac = mac.split('\n')[1]
    return mac