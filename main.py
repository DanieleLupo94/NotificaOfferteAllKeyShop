from base64 import decode
import requests as req
import re
import sys
import time
import signal

def receiveSignal(signalNumber, frame):
    #print('Received:', signalNumber)
    raise SystemExit('Exiting')

if len(sys.argv) < 2:
    print("Bisogna impostare una soglia\nUso: " + str(sys.argv[0]) + " <soglia>")
    quit()

soglia = sys.argv[1]

def check():

    resp = req.get("https://www.allkeyshop.com/blog/catalogue/category-pc-games-all/search-elden+ring/")

    page = resp.content.decode('UTF-8').replace("\n", "").replace("\t", "").replace("\r", "").replace("  ", "")
    #print(page, file=open("result", "w+", encoding="utf-8"))

    matches = re.findall("<div class=\"search-results-row-price\">.....€</div>", page)
    prezzi = []
    for m in matches:
        prezzi.append(m.replace("<div class=\"search-results-row-price\">","").replace("</div>", "").replace("€", ""))

    print("Prezzi trovati: " + str(prezzi), file=open("log","a+"))
    '''for p in prezzi:
        print(p + "€")'''

    prezziOk = list(filter(lambda x: x < soglia, prezzi))
    msg = "Ci sono " + str(len(prezziOk)) + " offerte interessanti con soglia " + str(soglia) + ". -> " + str(prezziOk)
    print(msg, file=open("log","a+"))
    print(msg)
    '''for p in prezziOk:
        print(p, file=open("log","a+"))'''

def main():
    try:
        check()
        time.sleep(60*1)
        main()
    except SystemExit:
        exit()
    else:
        main()

if __name__=="__main__":
    signal.signal(signal.SIGINT, receiveSignal)
    signal.signal(signal.SIGILL, receiveSignal)
    signal.signal(signal.SIGABRT, receiveSignal)
    signal.signal(signal.SIGFPE, receiveSignal)
    #signal.signal(signal.SIGKILL, receiveSignal)
    signal.signal(signal.SIGSEGV, receiveSignal)
    signal.signal(signal.SIGTERM, receiveSignal)
    main()
