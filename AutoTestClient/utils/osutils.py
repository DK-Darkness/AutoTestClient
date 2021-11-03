import os
import psutil
import signal
import subprocess

# for kill tftpd process when the task ends
def getAllPid():
    pid_dict={}
    pids = psutil.pids()
    for pid in pids:
        p = psutil.Process(pid)
        pid_dict[pid]=p.name()
    return pid_dict

def kill(pid):
    try:
        kill_pid = os.kill(pid, signal.SIGABRT)
        print('killed pid %s,　return %s' % (pid, kill_pid))
    except Exception as e:
        print('ERROR:kill subprocess failed,no such process!')

def kill_tftpd(p):
    dic=getAllPid()
    for t in dic.keys():
        if dic[t]=="tftpd64.exe":
            kill(t)
    p.terminate()

def is_up(IP):
    '''
    is_up : 0 up 1 down
    '''
    is_up = os.system('ping -n 1 ' + IP)
    return is_up

def dhcp_renew():
    os.system('ipconfig /release')
    os.system('ipconfig /renew')

def pppoe_on_pc(action,**args):
    '''
    args:
        conn_name 宽带连接名称
        pppUsername
        pppPassword
    '''
    if action == 'connect':
        os.system('@Rasdial {} {} {}'.format(args['conn_name'],args['pppUsername'],args['pppPassword']))
    elif action == 'disconnect':
        os.system('@Rasdial {} /DISCONNECT'.format(args['conn_name']))

def set_static_ip(intf,static_ip,gateway):
    os.system(' netsh interface ip set address name="{}" source=static addr={} mask=255.255.255.0 gateway={} 1'
        .format(intf,static_ip,gateway))

def set_dhcp(intf):
    os.system('netsh interface ip set address name="{}" source=dhcp'.format(intf))

def disable_intf(intf):
    os.system('netsh interface set interface "{}" disabled'.format(intf))

def enable_intf(intf):
    os.system('netsh interface set interface "{}" enable'.format(intf))

def wifi_connect(ssid,key):
    if key == '':
        subprocess.Popen('python utils/wifi_util.py connect_wifi_open {}'.format(ssid),shell=True)
    else:
        subprocess.Popen('python utils/wifi_util.py connect_wifi {} {}'.format(ssid,key),shell=True)

def disconnect_wifi():
    subprocess.Popen('python utils/wifi_util.py disconnect_wifi')
