#!/usr/local/bin/python
#coding=utf-8
import os, sys, telnetlib
def zalyshok(sim):
    host = '172.16.0.11'
    tn = telnetlib.Telnet(host)
    tn.write("\n\r")
    tn.read_until('SG login: ',5)
    tn.write("2n\r")
    tn.read_until('Password: ',5)
    tn.write("2n\r")
    out_ok = tn.read_until('OK',5)
    ussd112='at&g' + str(sim) + '=xtd*112#;\r'
    tn.write(ussd112)
    out_sms = tn.read_until('DLIA',6)
    tn.close()
    if out_sms.find('ZALYSHOK')== -1:
        zal = zalyshok(sim)
    else:
        zal = out_sms[out_sms.find('ZALYSHOK'):-1]
        zal = zal[-18:-15]
    return zal

sim = sys.argv[1]
balance = zalyshok(sim)
if int(balance) > 15:
    mess = 'OK - balance ' + balance + ' minutes on INTERNATIONAL'
    print mess
    sys.exit(0)
elif int(balance) > 10:
    mess = 'WARNING - balance ' + balance + ' minutes on INTERNATIONAL'
    print mess
    sys.exit(1)
elif int(balance) < 5:
    mess = 'CRITICAL - balance ' + balance + ' minutes on INTERNATIONAL'
    print mess
    sys.exit(2)
else:
    mess = 'UNKNOWN - balance ' + balance + ' minutes on INTERNATIONAL'
    print mess
    sys.exit(3)

