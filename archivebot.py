import socket
import sys
import time
from random import randint
from random import choice

server = "irc.freenode.net"
channel = "#partytrumpet"
botnick = "archivebot7000"
chanpass = "CHANNELPASSWORD"

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "connecting to:"+server
irc.connect((server, 6667))
irc.send("USER "+ botnick +"\n")
irc.send("NICK "+ botnick +"\n")
irc.send("PRIVMSG nickserv :iNOOPE\r\n")
irc.send("PRIVMSG nickserv :identify PASSWORD\n")
time.sleep(20)
irc.send("JOIN "+ channel +" "+ chanpass +"\n")
while 1:
	f=open("archive.txt","a")
	text=irc.recv(2040)
	print(text)
	if text.find('PING') != -1:
		irc.send('PONG' +text.split() [1] + '\r\n')
	if text.find('PRIVMSG') != -1:
		f.write(text + '\n')
	f.close
