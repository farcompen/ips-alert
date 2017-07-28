#! usr/bin/env python
# -*- coding:utf-8 -*-


import smtplib
from pexpect import pxssh
import getpass
import sys
from timeit import Timer
import time
from datetime import datetime
from FortiMail import mail_gonder
hosgeldin="""
                  ***************************
                  Fortigate Firewall IPS Alert 
                  By: Faruk GÜNGÖR
                  July 2017 
                  *************************** 



"""


print (hosgeldin)

def baglan():
  try:
    session=pxssh.pxssh()
    session.force_password=True
    ip_adres="firewall ip adress"
    kullanici="firewall username "
    parola="firewall password"
    session.login(ip_adres,kullanici,parola,auto_prompt_reset=False)
    print("Bağlantı kuruluyor. Bir kaç saniye sürebilir ...")
    session.sendline("get system performance status")
    session.prompt()
    dosya=open("session.txt","w")
    dosya.write(session.before)
    dosya.flush()
    dosya.close()
    session.logout()
    session.close()
  except pxssh.ExceptionPexpect as e :
      print(e)
      sys.exit()

def oku():
    dosya=open("session.txt","r")
    a=0
    while(a==0):
        okunan=dosya.readline()
        if okunan.startswith("IPS"):
            print(okunan)
            ips=okunan.strip()
            if(ips!="IPS attacks blocked: 0 total in 1 minute"):
               ml=mail_gonder(ips)
               ml.mail()
            a=1

def islem():
    a=0

    while(a==0):

      baglan()
      oku()
      zaman=datetime.now()
      print(zaman)
      print(50*"*")
      time.sleep(600)
islem()
