# Writeup 8 - Binaries II

Name: *PUT YOUR NAME HERE*
Section: *PUT YOUR SECTION NUMBER HERE*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: *PUT YOUR NAME HERE*

## Assignment Writeup

### Part 1 (100 pts)
Answer the following questions regarding the server executable (for which source is provided).

1. How is the per-session administrator password generated? Are there any inherent weaknesses in this implementation?

`The per-session adminstration password is generated randomly. The program uses a random string generator. The inherent weaknesses in this implementation  is storing the password on the stack, which is not a safe practice. To prevent this don't store the passcode on the stack`

2. Describe two vulnerabilities in this program. Provide specific line numbers and classifications of the vulnerability. Explain potential ramifications as well as ways to avoid these vulnerabilities when writing code.
`1. Buffer overflow on line 68; The exec_command function on line 60 in server.c uses 'gets' and this could be broken with a buffer overflow. To prevent this, one can change the language of the code; handle cases for string input;`
`2. Storing the passcode on stack - very unsafe can be cracked; To crack the passcode you have to use decrypt with %29$f`

3. What is the flag?

`CMSC389R-{expl017-2-wln}`

4. Describe the process you followed to obtain the flag: vulnerabilities exploited, your inputs to the server in a human-readable format, etc. If you create any helper code please include it.

```My steps to get the flag were:

1. nc ec2-18-222-89-163.us-east-2.compute-amazonaws.com pc
After I was prompted in, I noticed that I'm able to gain what I wanted through debugging of the program and using breakpoints. From this I learned I had to decrpyt. 
2. So I decrypted %29$f
After this step I was able to gain the password -> entered the password to gain server access
From what we learned in previous lectures, my "go-to" approach was command injection. So I tried to put in various commands and use a "trial-and-error" approach
After a couple different tries and reading online about various approaches to command inject I realized buffer overflow was a popular approach and so:
3. I finally tried the command `ls (bunch of spaces) ls (bunch of spaces)` 
From this I saw that there existed a folder called flag 
4. Then I tried accessing the directory and gaining access to get the flag `cat flag (bunch of spaces) cat flag (bunch of spaces)`

All of this led to the execution of the command on the server and from that I noticed the vulnerabilites were buffer overflow```



