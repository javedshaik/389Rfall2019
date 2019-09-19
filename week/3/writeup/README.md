# Operational Security and Social Engineering

## Assignment details

This assignment has two parts. It is due by 9/20 at 11:59 PM.

**There will be a late penalty of 5% off per day late!**

### Part 1

You have been hired by a penetration testing firm and have been asked to collect some specific information about the Wattsamp employee from HW2, Eric Norman. Some of the information you're looking for seems to be unavailable or unlikely to be found through OSINT:

- What's his mother's maiden name?
- What browser does she primarily use?
- What city was she born in?
- What's her ATM pin number?
- What was the name of her first pet?

Write up a pretext that you would use to social engineer this information out of Eric Norman. What approach would you take and how would you present yourself to elicit this information under the radar? Use the slides and what we covered in lecture to come up with a plan to obtain this information.

```
In order to elicit this information under the radar I would chose the most famous techniques of social engineering, pretext and elictation. In this case we are focusing on writing a pretext. The approach I would take is send an email or make a phone call pretending to be a doctors office nurse of Eric Norman's mother. 

Pretext:
My email to Eric Norman or a phone call:

Hi Eric, 

This is Nurse Sha calling from Vipro medical center, your mother has visited the office in the past year and has not paid her remaining balance. Would you like to go ahead pay the remaining balance, or would you like to leave a message to your mother. I have called this number because this was given to hospital as an emergency number on the file. 

If Eric's mother accpets to pay I would ask for:
Her full name
ATM card details for the payment

Then I would mention to secure her account she has to fill out security questions so I would email her a forum
first name of her pet?
what city she was born in?
what browser does she primarily use?

This would be my approach in order to get information out of her.
```


### Part 2

Eric Norman has recently discovered that Watsam's web server has been broken into by the crafty CMSC389R ethical hackers. After reading your published report, he has reached out to you to seek guidance in how he can repair some of the vulnerabilities that you have discovered.
Choose 3 specific vulnerabilities from homework 2 that you have identified (ie. exposed ports, weak passwords, etc.) and write a brief summary of some suggestions you can provide Eric for the Wattsamp web server and admin server. Be as thorough as possible in your answer, use specific examples and citing online research into security techniques that could be applied to the servers (ie. firewall, IDS/IPS, password managers, etc.).

```
Three specific vulnerabilities that I have found from homework two are:
1. Not having Fail2Ban in place, which means I can try multiple attacks from the same IP address
2. Open ports -> exposed
3. Weak password

Some suggestions that I can provide Eric for the Wattsamp web server and admin server to make it fool proof are:
1. To use a public key authetication for SSH - remove unencrypted access, and use SSH keys where the user gets private key and a public key which is stored on the server, and when a user tries to login SSH makes sure the public and private key matches. This way there will be no successful brute force attack against a weak password
2. Strong passwords that has a capital characters, special character, numbers
3. Install and configure Fail2Ban - This will go through the server logs and find patterns of malicious connections, such as too many failed attempts for same IP address, and then it will block connections from that IP
4. Malware software to scan - a software like this will provide Eric insight into if there is a breach in his servers, and may possibly find if there is any malware that is installed.
5. Monitor Logs - this will allow to see any patterns of malicious behavior
6. Installing and configuring a firewall

All of these information is pulled from my own knowledge and mailchannels.com
```

### Format

The submission should be answered in bullet form or full, grammatical sentences. It should also be stored in `assignments/3_OPSEC_SE/writeup/README.md`. Push it to your GitHub repository by the deadline.

### Scoring

Part 1 is worth 40 points, part 2 is worth 60 points. The rubric with our expectations can be found on the ELMS assignment posting.

Good luck!
