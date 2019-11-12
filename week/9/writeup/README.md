# Writeup 9 - Forensics II

Name: *PUT YOUR NAME HERE*
Section: *PUT YOUR SECTION NUMBER HERE*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: *PUT YOUR NAME HERE*


## Assignment details

### Part 1 (45 Pts)
1. Warmup: what IP address has been attacked?
`159.203.113.181`
2. What kind of assessment tool(s) were the attackers using against the victim machine? List the name(s) of the tool(s) as well.
`The attackers were using open ports; they were scanning ports. The tools they were using were nmap, NetScan`
3. What are the hackers' IP addresses, and where are they connecting from?
`142.93.136.81` 
`They are connecting from Clifton, New Jersey`
4. What port are they using to steal files on the server?
`They were using port number 21 or 22`
5. Which file did they steal? What kind of file is it? Do you recognize the file?
`They stole a find_me.jpeg file. Yes it's a image file`
6. Which file did the attackers leave behind on the server?
`They left behind a greetz.fpff file on the server`
7. What is a countermeasure to prevent this kind of intrusion from happening again? Note: disabling the vulnerable service is not an option.
`To pevent this, one can detect open ports on their network and close them`
### Part 2 (55 Pts)


1. When was greetz.fpff generated?
`2019-03-27 00:15:05`
2. Who authored greetz.fpff?
`b'fl1nch'`
3. List each section, giving us the data in it and its type.
`Section count = 5`
4. Report at least one flag hidden in greetz.fpff. Any other flag found will count as bonus points towards the competition portion of the syllabus.
`b'Hey you, keep looking :)'
b'}R983CSMC_perg_tndid_u0y_yllufep0h{-R983CSMC'
b'Q01TQzM4OVIte2hleV9oM3lfeTBVX3lvdV9JX2RvbnRfbGlrZV95b3VyX2Jhc2U2NF9lbmNvZGluZ30='`
`Hey you, keep looking :)`
`Hopefully_you_didnt_grep_CMSC389R{`

`In order to do this assignment I used packetTotal an online tool which gave me information as to what was happening, the IP address, what files were inputted into the server and grabbed from the server and what ports were being used. After this I knew I had to get the contents of the file from a stream so I went on wireshark and tested out different streams and after couple trial and errors: I found out it was 1009 from there I was able to follow the TCP and get the content of the files. Then I used stub.py and read through fpff-spec.md to understand what to do. From there I  didn't understand how to extract all the sections`

```#!/usr/bin/env python2

import sys
import struct
from datetime import datetime

# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)


# Some constants. You shouldn't need to change these.
MAGIC = 0x8BADF00D
VERSION = 1

if len(sys.argv) < 2:
    sys.exit("Usage: python stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
magic, version = struct.unpack("<LL", data[0:8])

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))

ts, author, secCount = struct.unpack("<L8sL", data[0:16])
ts = datetime.fromtimestamp(ts)
print("time: %s" % str(ts))
print("author: %s" % str(author[0:-2]))


# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!

print("-------  BODY  -------")

i = 0
while i < len(data):
    stype, slen = struct.unpack("<LL", data[0:8])
    i+=1
    if stype == 0x1:
        output = data[index: index + slen]
        print(output)
        i += slen
```
