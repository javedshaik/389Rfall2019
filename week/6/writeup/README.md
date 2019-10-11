# Writeup 6 - Binaries I

Name: *PUT YOUR NAME HERE*
Section: *PUT YOUR SECTION NUMBER HERE*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: *PUT YOUR NAME HERE*

## Assignment Writeup

### Part 1 (50 pts)

*Please use this space to provide flag from program*

### Part 2 (50 pts)

*Please use this space to detail your approach and solutions for part 2. Include
descriptions of checks implemented as well as your final input to produce flag.*

```
Part 1
Flag : CMSC389R-{di5a55_0r_d13}

Part 2:

	To start this project I first opened the crackme file in Binary Ninja.
  Here I was able to see the control flow of the program.
  Using the side bar on the left, I jumped to main and here I wanted to see
  what the program was outputting if I just ran the file, after that
  I noticed that there were three checks it had to pass in order to extract the flag.

	The first input to get pass through the first check which required
  the passed in argument to match what was present (what is was comparing with)
  was “Oh God.” So when running the program I ran (./crackme “Oh God”).
  This returned to me “…you don’t care about the environment. This made me
  realize that I had to jump to see what the second check was doing. Then after
  reading through the MIPS code I realized I had to set an environmental
  variable for FOOBAR, so I input FOOBAR=” my eyes”. I input this in because
  I saw in the program that (my eyes) was spelled backwards. Lastly when
  I set this and inputted the string into terminal it returned open sesame.
  Here I took a look at check 3 and was able to notice that it was trying to
  open a file name sesame. So my thought process was to make a file called sesame.
  Then it was outputting hard-coded string matching and I knew this was

	First check – checked if the passed in argument string matched what was present (being compared to)
	Second check – check if the environment variable FOOBAR was set
	Third check – If there exists a file named sesame with the string “ they burn” inside it

What the checks had in common was control flow of the program they each
required some sort of input string to match inorder for the flow to pass through.
What they had different were how the control flow for each check was happening,
different ways of checking if the passed in argument was matching.
```
