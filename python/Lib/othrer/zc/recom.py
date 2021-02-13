import re
from pathlib import *
from itertools import groupby


s_o = re.compile(r'o', re.I)
pattmain = re.compile(r'\d+[чhmcs]', re.I)
hh = re.compile(r'\d{1,2}[чh]', re.I)
mm = re.compile(r'\d{1,2}[m]', re.I)
ss = re.compile(r'\d{1,2}[cs]', re.I)


def search(teststring):
    teststring = teststring.encode()
    teststring = str(teststring, 'cp1251')
    hhres, mmres, ssres = [], [], []
    teststring = re.sub(s_o, '0', teststring)
    result = pattmain.findall(teststring)
    if len(result) < 1: return -7
    for i in range(len(result)):
        try:
            lo = [int(''.join(i)) for is_digit, i in groupby(result[i], str.isdigit) if is_digit]
        except: return -5
        result[i] = lo[0]
    for i in hh.finditer(teststring):
        hhres.append(i.start())
    if len(hhres) > 1: return -7
    if len(hhres) < 1: result.insert(0, 0)
    if result[0] > 23: return -7
    for i in mm.finditer(teststring):
        mmres.append(i.start())
    if len(mmres) > 1: return -7
    if len(mmres) < 1: result.insert(1, 0)
    if result[1] > 59: return -7
    for i in ss.finditer(teststring):
        ssres.append(i.start())
    if len(ssres) > 1: return -7
    if len(ssres) < 1: result.insert(2, 0)
    if result[2] > 59: return -7
    try:
        if hhres[0] > mmres[0]: return -7
    except: pass
    try:
        if hhres[0] > ssres[0]: return -7
    except: pass
    try:
        if mmres[0] > ssres[0]: return -7
    except: pass
    try:
        teststring = result[0] * 3600000
    except: return -4
    try:
        teststring = teststring + result[1] * 60000
    except: return -4
    try:
        teststring = teststring + result[2] * 1000
    except: return -4
    return teststring + 300000


print('yes')

