import requests, json, time, sys, inspect
from pathlib import *

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
           'Content-Type': 'application/x-www-form-urlencoded'}

resp_text = []
# keyPath = Path(sys.executable).parent.parent.joinpath('key.txt')
# try:
#     key = keyPath.read_text()

def statut_main(q, e, r):
    return 2 if (statut_main_orig(q, e, r) != 0) else 0


def statut_main_orig(q, e, r):
    try:
        with requests.get(q, headers=headers) as response:
            if response.status_code == 200:
                q = 1
                resp_text.append(response.text)
                if len(resp_text[0]) != 8: q = 0
    except: q = 0
    try:
        with requests.get(e, headers=headers) as response:
            if response.status_code == 200: e = 1
    except: e = 0
    try:
        with requests.get(r, headers=headers) as response:
            if response.status_code == 200: r = 1
    except: r = 0
    if e == 0 and r == 0: return 0
    try:
        if resp_text[0][0] == '2' and e > 0: return 2
        if resp_text[0][0] == '1' and r > 0: return 1
    except: pass
    if e > 0: return 2
    if r > 0: return 1
    return 0


def retru():
    return ' retry '


def retru_orig():
    try:
        a = resp_text[0][2:7]
    except: return ' no '
    return ' ' + a + ' '


def chige(q, e=0):
    # global key
    if str(q).find(f'https://helpserv.tk/Helps/ZCHelp/to/') != -1:
        # if key is None: key = str(q).split('/')[-1]
        return '<script language=JavaScript> '
    elif str(q).find('https://helpserv.tk/Helps/ZCHelp/upd01/word') != -1:
        return '0016 1 0 0 0 1'
    elif str(q).find(f'https://helpserv.tk/Helps/ZCHelp/tem/') != -1:
        return 'uxovsfpj ', 'j'
    else:
        return 'no'


def chige_orig(q, e=0):
    try:
        with requests.get(q, headers=headers) as response:
            if response.status_code != 200: return 'no'
            if e == 1:
                if len(response.text.split('\n')[0]) > 9: return 'no2'
                return response.text.split('\n')[0][:8] + ' ', response.text.split('\n')[0][-1]
            if e == 2:
                if response.text.split('\n')[0][0] == '<': return False
                return True
            return response.text.split('\n')[0]
    except: return 'no'


def chipo(q, e):
    try:
        if str(q).find('https://helpserv.tk/Helps/ZCHelp/tem/id/immg.php') != -1:
            return ''
        elif str(q).find('https://helpserv.tk/Helps/ZCHelp/tem/writer.php') != -1:
            if e['a'] == 'dat2':
                return '1610133458'
            elif e['a'] == 'del':
                return ''
            elif e['a'] == 'zap':
                return ''
    except: pass
    return 'no'


def chipo_orig(q, e):
    try:
        with requests.post(q, data=e, headers=headers) as response:
            if response.status_code != 200: return 'no'
            return response.text.split('\n')[0]
    except: return 'no'


print('yes')

