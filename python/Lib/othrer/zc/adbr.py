from pathlib import *
from winreg import *
import subprocess, time, os, re, sys


a, ot, devic, adbcommand = 0, '', [], []
exe = sys.executable
# pathtest = 0

adbpath = 0
adbpathdir = 0

# dname = Path(exe).parent
# dname = Path(dname, 'adb')
# fil = [Path(dname, 'adb.exe'), Path(dname, 'AdbWinApi.dll')]
# try: os.chdir(dname)
# except (ValueError, Exception): pass


def spr(q):
    global adbpath, adbpathdir
    flag = 0
    if q == 1:
        try:
            a = OpenKey(HKEY_LOCAL_MACHINE, 'SOFTWARE\\BlueStacks', 0, KEY_WOW64_64KEY | KEY_ALL_ACCESS)
        except WindowsError: return False
        try:
            m = 0
            while True:
                if EnumValue(a, m)[0] == 'InstallDir':
                    adbpath = Path(EnumValue(a, m)[1] + '\\HD-Adb.exe')
                    flag += 1
                    CloseKey(HKEY_LOCAL_MACHINE)
                    break
                m += 1
        except WindowsError: CloseKey(HKEY_LOCAL_MACHINE)
        if flag == 0: return False
    else:
        try:
            a = OpenKey(HKEY_LOCAL_MACHINE, r'SOFTWARE\DuoDianOnline\SetupInfo', 0, KEY_WOW64_32KEY | KEY_ALL_ACCESS)
        except WindowsError: return False
        try:
            m = 0
            while True:
                if EnumValue(a, m)[0] == 'InstallPath':
                    adbpath = Path(EnumValue(a, m)[1]+'\\bin\\nox_adb.exe')
                    flag += 1
                    CloseKey(HKEY_LOCAL_MACHINE)
                    break
                m += 1
        except WindowsError: CloseKey(HKEY_LOCAL_MACHINE)
        if flag == 0: return False
    try:
        adbpathdir = Path(adbpath).parent
        if not adbpath.is_file(): return False
    except: return False
    os.chdir(adbpathdir)
    return True


def sear(pr, em):
    global a
    a = 1
    if em == 1:
        if re.findall('emulator-[0-9]{1,6}', pr): devic.append(re.findall('emulator-[0-9]{1,6}', pr)); a = 3; return a
    if em == 2:
        if re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:[0-9]{1,6}', pr):
            devic.append(re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:[0-9]{1,6}', pr)); a = 3; return a
    return a


def adbad(q, pu):
    global ot
    for i in range(0, q):
        process = subprocess.Popen(pu, stdout=subprocess.PIPE)
        output, error = process.communicate()
        ot = str(output)
        if q > 1: time.sleep(1)
    pass


def comanda(q, pu):
    global adbcommand
    adbcommand.clear()
    # adbcommand = [adbpath]
    adbcommand = pu.split()
    adbcommand.insert(0, adbpath)
    # print(adbcommand)
    # adbcommand = [adbpath, lst]
    adbad(q, adbcommand)


def main(q):
    global adbcommand
    adbcommand.clear()
    adbcommand = [adbpath, 'devices']
    # adbcommand = [adbpath, '-s', 'emulator-5564', 'shell', 'input', 'tap', '50', '50']
    # print(adbcommand)
    # if q > 0:
    #     try: os.system('taskkill /F /IM adb.exe')
    #     except (ValueError, Exception): pass
    #     return True
    # adbad(1, 'adb.exe kill-server')
    # time.sleep(1.5)
    # adbad(1, 'adb.exe start-server')
    # time.sleep(8)
    adbad(3, adbcommand)
    time.sleep(0.5)
    # adbad(1, adbcommand)
    # time.sleep(0.5)
    # adbad(1, adbcommand)
    # time.sleep(0.5)
    # adbad(1, adbcommand)
    # time.sleep(1)
    sear(ot, q)
    pass


# for i in fil:
#     if i.is_file(): a += 1
#
#
# if a > 1:
#     a = 0
#     print('yes')
# else: print('no')
print('yes')
# print(spr(1))
# print(adbpath)
# print(Path.cwd())
# main(1)
# print(ot)
# sear(ot, 2)
# print(a)
# comanda(1, '-s emulator-5564 shell input tap 50 50')


# print(devic)
