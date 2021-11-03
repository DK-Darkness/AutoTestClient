import pywifi
from pywifi import const

import sys

wifi = pywifi.PyWiFi()
ifaces = wifi.interfaces()[0]

def disconnect_wifi():
    ifaces.disconnect()
    wifistatus = ifaces.status()
    if wifistatus == const.IFACE_DISCONNECTED:
        return wifistatus

def connect_wifi(ssid,key):
    ifaces.scan()
    profile = pywifi.Profile()
    profile.ssid = ssid
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher=const.CIPHER_TYPE_CCMP
    profile.key = key
    tep_profile = ifaces.add_network_profile(profile)
    ifaces.connect(tep_profile)

def connect_wifi_open(ssid):
    ifaces.scan()
    profile = pywifi.Profile()
    profile.ssid = ssid
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_NONE)
    profile.cipher=const.CIPHER_TYPE_CCMP
    tep_profile = ifaces.add_network_profile(profile)
    ifaces.connect(tep_profile)


if __name__ == '__main__':
    if sys.argv[1] == 'connect_wifi':
        connect_wifi(sys.argv[2],sys.argv[3])
    if sys.argv[1] == 'connect_wifi_open':
        connect_wifi_open(sys.argv[2])
    if sys.argv[1] == 'disconnect_wifi':
        disconnect_wifi()