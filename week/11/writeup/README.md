# Writeup 1 - Web I

Name: *Javed Shaik*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: *Javed Shaik*


## Assignment details
This assignment has two parts. It is due by 11/27/19 at 11:59PM.

**There will be late penalty of 5% per day late!**

### Part 1 (40 Pts)

Such a Quick Little, website!


`The flag is CMSC389R-{y0u_ar3_th3_SQ1_ninj@} priced as $1337`

`My though process behind discovering this flag:`
`1. I read through the slides and discovered that this vulnerability could potentially be sql injection. Then I started to google more into what and how are SQL injections conducted; through my research I discovered that SQL injections, espescially query's can have user input data. 
2. I started to play around the website and clicked on the different links that were provided. I mainly paid attention to the url's since I read online that you can SQL inject into the URL
3. Through the research I also came to learn that this may be a Inband sql attack where the data is extracted using the same channel that is used to inject the SQL code. From this I was able to infer that SQL injections mostly had to with a database and retrieval of data.
4. From how the website was portrayed I was able to infer the images and prices had to be stored some where, and in the url I noticed that the "id" tag was changing everytime, hinting me towards that could potentially be the different row number in the database table.
5. So I started to play around with id to see if I can change it and maybe try to retrieve the flag.
6. This did not go to well, so I resorted back to reading online more on how I could poissbly manipulate id and through this I discovered that in order to gain access to authenticate a user, the query has to respond with a value and if it does then we know the user exist's in the DB with those credentials and the user is granted access.
7. After playing around and trying different formats of inputting "1=1" and "||1=1" etc, I was able to analyze that the condition is always true (OR 1=1).
8. So finally I tried "id='||'1=1" and this was able to grant access to the DB and print all the pictures in the DB and thats how I got the flag`

[http://142.93.136.81:5000/](http://142.93.136.81:5000/)

### Part 2 (60 Pts)
Complete all 6 levels of:

[https://xss-game.appspot.com](https://xss-game.appspot.com)

Produce a writeup. We will not take off points for viewing the source code and/or viewing hints, but we strongly discourage reading online write-ups as that defeats the purpose of the homework.

`In order to solve all the six levels of this I first read the slides on xss and also did tons of research on the internet and used the hints provided at each level`

`1. To get past the first task I used all the three hints provided. The third hint was the most helpful and just based off that I inputted "<script>alert(1)</script>" and I was able to produce a JS alert and move onto the next level. I chose alert(1) because it was level 1, nothing about that was intuitive, it was honestly just trial and error"`

`2. To unclock this level I again used all the 3 hints provided. From the hints I knew it had nothing to do with the script tag and from the third hint I knew it had to do with <img> tag and the onerror attribute.`
`Looking through the html code for level 2, and using the first hint I was able to figure that this had something to do with post-content id since the template doesn't escape the content of status messages.`
`So I tried doing this with the img and onerror attribute and post-content id post-content=<img src='cmsc' onerror='alert("cmsc")'>.`
`The bad thing here was it was DOM-based error where the vulnerability existed in client side code; so the JS function here was a type execution sink and it caused it to run that script provided.`
`This prompted me to the next level with an alert`

`3. For this one as well I used all the hints provided. I knew right off the back I had to manipulate the URL since that what it tells me to do.`
`After using the first hint and looking at the JavaScript code I was able to identify on this line of code " html += "<img src='/static/level3/cloud" + num + ".jpg' />";" the "num" was being used to get the img tag. The second hint tells me that "window.location.hash = num;" this line of code is what can be used/influenced for an attack.`
`Finally using the third hint I discovered that something needed to be injected into the HTML and so I went on trial and error and used the source code to make educated guesses. I also knew there were three images which refers to the frame number`
`After a couple tries, I was able to input this in https://xss-game.appspot.com/level3/frame#2' onerror='alert("cmsc")'>`

`4. Based on the hint given, I first went with using the third hint given which is trying to use "'" it gives me a syntax error which I'm able to see in the console.`
`After that I took at the code and tried to see how it was executing and why it was giving a syntax error. From here I again took a trail and error approach and started to insert different formats into the input box`
`So into the input I tried setting the timer and alert such as timer=');alert('cmsc, which helped me pass through`

`5. Here I used all the hints given, especially number 2 and 3. When I clicked on the "sign up" link, I was able to learn how the URL was being used. From what I read online about DOMbased XSS issues and have noticed earlier, I realized this vulnerability was closely related to that. After taking a look at this line setTimeout(function() { window.location = '{{ next }}'; }, 5000); I noticed "next" was being used as the parameter here which was being passed into the URL.`
`So from that I was able to use trial and error to input different things after the next="".`
`I also read what was provided in hint 4 and after next I inputted next=javascript:alert()`

`6. Here again I used all the hints and the text provided on what to do; I quickly learned that I had to host my JScode elsewhere. I googled different places I can host my JS code and came across the fact that I'm able to host code on pastebin. Instead I used hint number 4 and decided to just host it using this google.com/jsapi?callback=foo`
`The issue with the code here is that the code filters http/s and also the page adds a script with the src tag to the HTLM's attribute.`
`So I replaced foo with alert such as //www.google.com/jsapi?callback=alert and I was able to get the cake`

### Format

Part 1 and 2 can be answered in bullet form or full, grammatical sentences.

### Scoring

* Part 1 is worth 40 points
* Part 2 is worth 60 points

### Tips

Remember to document your thought process for maximum credit!

Review the slides for help with using any of the tools or libraries discussed in
class.
