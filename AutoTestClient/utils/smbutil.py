from smb.SMBConnection import SMBConnection
from smb.smb_structs import OperationFailure

def samba_test(host,volume):
    samba = SMBConnection('admin', '123', '', '', use_ntlm_v2=True)
    samba.connect(host, 139)
    try:
        samba.createDirectory('storage','{}/admin/i'.format(volume))
        return True
    except:
        return False

# print(samba_test('10.100.0.138','disk6_1_1'))