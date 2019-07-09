import os
import sys
import time
import json
import urllib

def pesan():

    try:
        while True:
            pes = raw_input(" [@] Saya: ")
            url = urllib.urlopen("http://sandbox.api.simsimi.com/request.p?key=KUNCI_API&lc=id&ft=1.0&text=" + pes)
            jsl = json.loads(url.read())
            print " [$] Bebeb: " + jsl["response"]
    
    except KeyboardInterrupt:
        print
        print " Keluar Dari Bot.."
        sys.exit()

def main():
    pesan()

if __name__=="__main__":
    main()



