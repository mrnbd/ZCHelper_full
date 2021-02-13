from pathlib import *
import os, sys, shutil, time

exe = sys.executable
old = Path(exe).parent
dname = Path(exe).parent.parent.joinpath('key.txt')
oldlib = old.joinpath('Libold')
# oldlib2 = Path(dname, 'Libold') # то же самое
oldlib1 = old.joinpath('Libold1')
adbdir = old.joinpath('adb')
adbexe = old.joinpath('adb.exe')
adbdll = old.joinpath('AdbWinApi.dll')


def makekey_orig(put):
    # key = '''Все вопросы и покупка в личку админу (Fedor) *> DISCORD BotforFun https://discord.gg/ygeGnVj **> TELEGRAM @Botforfun
# Сайт https://bot4.fun

        # ВАШ КЛЮЧ:   <<     ''' + put + '''     >>

    # Это просто информация о Вашем ключе, который Вы сообщите, если решите купить Помощника.
    # Этот файл на работу Помощника никак не влияет.'''
    key = put
    
    dname.write_text(key)
    # try: os.system('taskkill /f /im adb.exe')
    # except (ValueError, Exception): pass
    try: shutil.rmtree(oldlib)
    except (ValueError, Exception): pass
    try: shutil.rmtree(oldlib1)
    except (ValueError, Exception): pass
    try: os.mkdir(adbdir)
    except (ValueError, Exception): pass
    try: shutil.copy2(adbexe, adbdir)
    except (ValueError, Exception): pass
    try: shutil.copy2(adbdll, adbdir)
    except (ValueError, Exception): pass
    try: os.remove(adbexe)
    except (ValueError, Exception): pass
    try: os.remove(adbdll)
    except (ValueError, Exception): pass
    pass


print('yes')
