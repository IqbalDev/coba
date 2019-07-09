import os

try:
    import requests
    import json
except:
       os.system('pip2 install requests')
       print 'please run again'


class main(object):

      def __init__(self):

          def chatkuy(user,bots):
              self.key = "32556fbb-a9ad-41ea-9def-ccf78e0f8f4e"
              while True:
                     self.msg = raw_input('[\033[93m%s\033[97m] : '%(user))
                     self.url = 'http://sandbox.api.simsimi.com/request.p?key=%s&lc=id&ft=1.0&text=%s'%(self.key,self.msg)
                     self.reqs = json.loads(requests.get(self.url).text)
                     print '[\033[92m%s\033[97m] : %s'%(bots,self.reqs['response'])



          user = raw_input('enter your name : ')
          bots = raw_input('enter bot name : ')
          print ''
          chatkuy(user,bots)

if __name__=='__main__':
   os.system('clear')
   main()
