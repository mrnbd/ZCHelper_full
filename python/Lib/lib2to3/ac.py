import re, win32process, win32gui, psutil, json, subprocess, time
from subprocess import check_output
from winreg import *
from pathlib import *


hwndd = 0
fproc = ''
fproc_hdplayer = 'HD-Player.exe'
fprocpid = []
fprocpid_hdplayer = []
windows_name = []
windows_hwnd = []
cmd_strok_proc = []
blureestr_software = []
blureestr_software_slesh = []
blureestr_conf_vmlist = []
blureestr_monitors = []
blureestr = re.compile('BlueStacks')
andrguest = re.compile('Android')
noxreclone = re.compile('-clone')
noxrezord = re.compile('\d')
noxexe = []
bluestacksexe = []
blueres_global = []
blue_monitor_dict = {}
blue_winname_dict = {}
zord = []
argblue1 = '-vmname'
argblue2 = 'Android'
argblue3 = '-json'
paketblue = {"app_pkg": "com.beingame.zc.zombie.shelter.survival"}
argnox1 = '-clone:Nox_'
paketnox = '-startPackage:com.beingame.zc.zombie.shelter.survival'

curProcesses = psutil.process_iter()


def list_in_order_nox():
    o = 0
    while o < len(windows_name):
        if windows_name[o] == 'Form' or windows_name[o] == 'Dialog':
            windows_hwnd.pop(o)
            windows_name.pop(o)
            cmd_strok_proc.pop(o)
        else:
            o += 1
    for i in cmd_strok_proc:
        if len(i) > 1:
            result = noxreclone.match(i[1])
            if result is not None:
                result = noxrezord.findall(i[1])
                if len(result) > 0: zord.append(result[0])
                else: zord.append('0')
            else: zord.append('0')
        else: zord.append('0')
    return True


def list_in_order_bluestacks():
    global windows_name
    obrabot_win(0)
    for o in range(len(cmd_strok_proc)):
        for f in range(len(blureestr_software_slesh)):
            if not re.search(blureestr_software_slesh[f], cmd_strok_proc[o][0]) is None:
                zord.append([f])
    for o in range(len(zord)):
        keys = list(blueres_global[zord[o][0]][1].keys())
        if windows_name[o] == 'BlueStacks':
            for t in fprocpid_hdplayer:
                if str(t) == keys[0]:
                    zord[o].append(0)
                    windows_name[o] = blueres_global[zord[o][0]][1][keys[0]]
                    fprocpid_hdplayer.remove(t)
        else:
            for i in range(1, len(keys)):
                if blueres_global[zord[o][0]][1][keys[i]] == windows_name[o]:
                    zord[o].append(i)
    return True


def obrabot_win(q):
    d, r = 0, 0
    if q == 0:
        sa = ['ContainerWindow', 'CustomMessageWindow', 'DimOverlay', 'KeymapCanvasWindow']
        for u in range(0, len(sa)):
            for i in windows_name:
                if i == sa[u]:
                    windows_hwnd.pop(d)
                    windows_name.remove(i)
                    cmd_strok_proc.pop(d)
                d += 1
            d = 0
        return True
    if q == 1:
        sa = ['ContainerWindow', 'CustomMessageWindow']
        for u in range(0, len(sa)):
            for i in windows_name:
                d += 1
                if i == sa[u]:
                    r += 1
                    break
            if r > 0: break
            d = 0; r = 0
        return d


def read_reestr_help(da, ta, pa):
    flag = 0
    try: a = OpenKey(HKEY_LOCAL_MACHINE, 'SOFTWARE\\' + da + '\\Guests\\' + ta + '\\Config', 0,  KEY_WOW64_64KEY | KEY_ALL_ACCESS)
    except WindowsError: CloseKey(HKEY_LOCAL_MACHINE); blue_monitor_dict.update({pa: 'Bluestacks'}); return False
    try:
        m = 0
        while True:
            if EnumValue(a, m)[0] == 'DisplayName':
                blue_monitor_dict.update({pa: EnumValue(a, m)[1]})
                flag += 1
            m += 1
    except WindowsError: pass
    if flag == 0: blue_monitor_dict.update({pa: 'BlueStacks'})
    return True


def read_reestr(q):
    listemp = []
    lst = []
    dictempandroid = []
    tempun = 0
    if q == 1:
        try: a = OpenKey(HKEY_LOCAL_MACHINE, 'SOFTWARE\\BlueStacks', 0, KEY_WOW64_64KEY | KEY_ALL_ACCESS)
        except WindowsError: CloseKey(HKEY_LOCAL_MACHINE); return False
        try:
            i = 0
            while True:
                if EnumValue(a, i)[0] == 'ClientVersion':
                    tempun = 1
                    temu = EnumValue(a, i)[1]
                    temu = temu.split('.', maxsplit=2)
                    try: temu = int(temu[0] + temu[1])
                    except (ValueError, Exception): return 'minver'
                    if temu < 4150: return 'minver'
                i += 1
        except WindowsError:
            CloseKey(HKEY_LOCAL_MACHINE)
            if tempun == 0: return 'minver'
        try: a = OpenKey(HKEY_LOCAL_MACHINE, 'SOFTWARE', 0, KEY_WOW64_64KEY | KEY_ALL_ACCESS)
        except WindowsError: CloseKey(HKEY_LOCAL_MACHINE); return False
        try:
            i = 0
            while True:
                if blureestr.match(EnumKey(a, i)) is not None and EnumKey(a, i) != 'BlueStacksInstaller':
                    blureestr_software.append(EnumKey(a, i))
                i += 1
        except WindowsError: CloseKey(HKEY_LOCAL_MACHINE)
        if len(blureestr_software) < 1: return False
        #
        for i in range(len(blureestr_software)):
            blureestr_software_slesh.append(blureestr_software[i] + '\\\\')
            listemp.append(blureestr_software[i])
            try: a = OpenKey(HKEY_LOCAL_MACHINE, 'SOFTWARE\\' + blureestr_software[i] + '\\Monitors', 0, KEY_WOW64_64KEY | KEY_ALL_ACCESS)
            except WindowsError: CloseKey(HKEY_LOCAL_MACHINE); return False
            try:
                u = 0
                while True:
                    dictempandroid.append(str(EnumValue(a, u)[0]) + ' ' + str(EnumValue(a, u)[1]))
                    u += 1
            except:
                if len(dictempandroid) < 1: return False
            dictempandroid.sort()
            for z in range(len(dictempandroid)):
                lst.append(dictempandroid[z].split()[1])
                lst.append(dictempandroid[z].split()[0])
            for z in range(0, len(lst), 2):
                read_reestr_help(blureestr_software[i], lst[z + 1], lst[z])
            listemp.append(blue_monitor_dict.copy()); blue_monitor_dict.clear(); dictempandroid.clear(); lst.clear()
            try: a = OpenKey(HKEY_LOCAL_MACHINE, 'SOFTWARE\\' + blureestr_software[i] + '\\Config', 0, KEY_WOW64_64KEY | KEY_ALL_ACCESS)
            except WindowsError: CloseKey(HKEY_LOCAL_MACHINE); return False
            try:
                m = 0
                while True:
                    if EnumValue(a, m)[0] == 'PartnerExePath':
                        listemp.append(Path(EnumValue(a, m)[1]))
                    m += 1
            except WindowsError: CloseKey(HKEY_LOCAL_MACHINE)
            blueres_global.append(listemp.copy()); listemp.clear()
    if q == 2:
        try:
            a = OpenKey(HKEY_LOCAL_MACHINE, r'SOFTWARE\DuoDianOnline\SetupInfo', 0, KEY_WOW64_32KEY | KEY_ALL_ACCESS)
        except WindowsError: CloseKey(HKEY_LOCAL_MACHINE); return False
        try:
            i = 0
            while True:
                if EnumValue(a, i)[0] == 'InstallPath':
                    noxexe.append(Path(EnumValue(a, i)[1]+'\\bin\\Nox.exe'))
                    break
                i += 1
        except WindowsError: CloseKey(HKEY_LOCAL_MACHINE)
        if len(noxexe) < 1: return False
    return True


def running(q):
    prog = [line.split() for line in check_output("tasklist").splitlines()]
    [prog.pop(e) for e in [0, 1, 2]]
    for task in prog:
        if task[0].decode('Windows-1251') == fproc:
            fprocpid.append(int(task[1].decode('Windows-1251')))
        if q < 2:
            if task[0].decode('Windows-1251') == fproc_hdplayer:
                fprocpid_hdplayer.append(int(task[1].decode('Windows-1251')))
    if len(fprocpid) > 0: return True
    else: return False


def enum_window_callback(hwnd, pidd):
    tid, current_pid = win32process.GetWindowThreadProcessId(hwnd)
    if pidd == current_pid and win32gui.IsWindowVisible(hwnd):
        windows_hwnd.append(hwnd)
        cmd_strok_proc.append(psutil.Process(pidd).cmdline())


def collect_inform():
    global windows_name
    for pid in fprocpid:
        win32gui.EnumWindows(enum_window_callback, pid)
    windows_name = list(win32gui.GetWindowText(item) for item in windows_hwnd)
    if len(windows_name) < 1: return False
    return True


def zapusk_emul(q, r, w, e):
    global fproc, hwndd
    a = ''
    if q == 1: fproc = 'Bluestacks.exe'
    else: fproc = 'Nox.exe'
    tem = read_reestr(q)
    if tem == 'minver' or tem is False: return tem
    if q == 1 and r == 1:
        if not running(q): return False
        if not collect_inform(): return False
        nw = obrabot_win(1)
        if nw == 0: return False
        fproc = windows_name[nw - 1]
        hwndd = windows_hwnd[nw - 1]
        return True
    if q == 1 and r == 0:
        if isinstance(blueres_global[w][2], Path):
            if e > 0: a = '_' + str(e)
            bluestacksexe.append(blueres_global[w][2])
            bluestacksexe.append(argblue1)
            bluestacksexe.append(argblue2 + a)
            bluestacksexe.append(argblue3)
            bluestacksexe.append(json.dumps(paketblue))
        else: return False
        subprocess.Popen(bluestacksexe)
    if q == 2:
        if isinstance(noxexe[0], Path):
            noxexe.append(argnox1 + str(e))
            noxexe.append(paketnox)
        else: return False
        subprocess.Popen(noxexe)
    return True


def vibor_emul(q):
    global fproc, windows_name
    if q == 1: fproc = 'Bluestacks.exe'
    else: fproc = 'Nox.exe'
    tem = read_reestr(q)
    if tem == 'minver' or tem is False: return tem
    if not running(q): return False
    if not collect_inform(): return False
    if q == 1: list_in_order_bluestacks()
    else: list_in_order_nox()
    return True


print('yes')
