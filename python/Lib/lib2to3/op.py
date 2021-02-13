from pathlib import *
import ctypes, hashlib, os, shutil, sys, time, warnings, requests, urllib, checksumdir

MessageBox = ctypes.windll.user32.MessageBoxW
warnings.filterwarnings("ignore")


mesa = 'Нет связи с сервером! Обеспечьте Помощнику доступ в интернет и запустите его заново.'
mesa2 = 'Что-то пошло не так. Скачайте Помощник заново с сайта BOT4.FUN.'


def connected_to_internet(url='https://bot4.fun/', timeout=5):
    try: xx = requests.get(url, timeout=timeout, verify=False); xx.close(); return True
    except (ValueError, Exception): MessageBox(32, mesa, 'ZERO CITY', 0x40000); return False


exe = sys.executable
dir_pyt = Path(exe).parent
os.chdir(dir_pyt)

litos = ''
drehash = []
dir_bota = Path(exe).parent.parent
dir_dlls = dir_pyt.joinpath('Dlls')
dir_lib = dir_pyt.joinpath('Lib')
dir_new = dir_pyt.joinpath('pythonnew')
dir_new_lib = dir_pyt.joinpath('pythonnew', 'Lib')
fil_arch_main = 'pythonNewM.zip'
fil_bota = 'ZCHelper.exe'
put_file_bot = dir_bota.joinpath(fil_bota)
put_file_new_bot = dir_pyt.joinpath(fil_bota)
put_file_new_arch_main = dir_pyt.joinpath(fil_arch_main)
put_file_dll_updwarnzip = dir_pyt.joinpath('DLLs', 'do.dll')
put_file_dll_updwarn = dir_pyt.joinpath('DLLs', 'UpdateZC.exe')
linkhashes = 'hashes'


def delete_content():
    q = 0
    try: put_file_new_bot.unlink()
    except (ValueError, Exception): q = 1
    try: put_file_new_arch_main.unlink()
    except (ValueError, Exception): q = 2
    try: shutil.rmtree(dir_new)
    except (ValueError, Exception): q = 3
    return q


def kill_all(q):
    if q == 1: os.system('taskkill /f /im ZCHelper.exe'); return True
    if q == 2:
        try:
            shutil.unpack_archive(put_file_dll_updwarnzip, dir_dlls, 'zip')
            os.startfile(put_file_dll_updwarn)
            return True
        except (ValueError, Exception): MessageBox(32, mesa2, 'ZERO CITY', 0x40000); sys.exit()
    os.system('taskkill /f /im UpdateZC.exe'); time.sleep(2)
    try: put_file_dll_updwarn.unlink(); return True
    except (ValueError, Exception): return False


def hashurl():
    return True


def hashurl_orig():
    try:
        with urllib.request.urlopen(litos + linkhashes) as f:
            for line in f: drehash.append(line.decode('utf-8').split()[0])
    except (ValueError, Exception): MessageBox(32, mesa2, 'ZERO CITY', 0x40000); sys.exit()
    if drehash[0] == '<!DOCTYPE' or len(drehash) != 5 or hashlib.md5(open(put_file_dll_updwarnzip, 'rb').read()).hexdigest().upper() != drehash[3]:
        MessageBox(32, mesa2, 'ZERO CITY', 0x40000); sys.exit()
    return True


def hashurl2():
    return True


def hashurl2_orig():
    try:
        with urllib.request.urlopen(litos + linkhashes) as f:
            for line in f: drehash.append(line.decode('utf-8').split()[0])
    except (ValueError, Exception): return False # sys.exit()
    if drehash[0] == '<!DOCTYPE' or len(drehash) != 5: return False
    return True


def download_new(q):
    with open(fil_bota, "wb") as f:
        ufor = requests.get(litos + fil_bota, verify=False)
        f.write(ufor.content)
    time.sleep(2)
    if hashlib.md5(open(fil_bota, 'rb').read()).hexdigest().upper() != drehash[2]:
        delete_content(); return -1
    if q == 1: return 1
    with open(fil_arch_main, "wb") as f:
        ufor = requests.get(litos + fil_arch_main, verify=False)
        f.write(ufor.content)
    time.sleep(2)
    if hashlib.md5(open(fil_arch_main, 'rb').read()).hexdigest().upper() != drehash[0]:
        delete_content(); return -1
    return 1


def zapscen(q):
    if q < 2:
        kill_all(2)
        if download_new(q) < 1: closer(1)
        try: shutil.move(str(put_file_new_bot), str(put_file_bot))
        except (ValueError, Exception): closer(1)
    if q == 0:
        os.chdir(dir_lib)
        for root, dirs, files in os.walk(".", topdown=False):
            for name in files:
                try: os.remove(os.path.join(root, name))
                except (ValueError, Exception): continue
            for name in dirs:
                try: shutil.rmtree(os.path.join(root, name))
                except (ValueError, Exception): continue
        os.chdir(dir_pyt)
        try: os.rename("Lib", "Libold")
        except (ValueError, Exception):
            try: os.rename("Lib", "Libold1")
            except (ValueError, Exception): pass
        try: shutil.unpack_archive(put_file_new_arch_main, dir_pyt)
        except (ValueError, Exception): closer(1)
        try: shutil.move(str(dir_new_lib), str(dir_pyt))
        except (ValueError, Exception): closer(1)
    closer(0)
    pass


def closer(q):
    delete_content()
    kill_all(0)
    if q > 0: MessageBox(32, mesa2, 'ZERO CITY', 0x40000)
    else: os.startfile(put_file_bot, 'runas')
    sys.exit()


def main(nil, scenar):
    pass


def main_orig(nil, scenar):
    global litos
    delete_content()
    if not connected_to_internet(): sys.exit()
    litos = nil
    hashurl()
    kill_all(1)
    zapscen(scenar)


def check(nil, pu):
    return True


def check_orig(nil, pu):
    global litos
    litos = nil
    if not hashurl2(): return False
    try:
        if checksumdir.dirhash(dir_pyt.joinpath(pu)) != drehash[4]: return False
    except (ValueError, Exception): return False
    return True


print('yes')
