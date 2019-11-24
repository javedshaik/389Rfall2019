# Writeup 10 - Crypto I

Name: *PUT YOUR NAME HERE*
Section: *PUT YOUR SECTION NUMBER HERE*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: *PUT YOUR NAME HERE*


## Assignment details

### Part 1 (45 Pts)
What is the structure of the ledger file format? Include exact byte offsets when static.
`The file format is a 16 byte hash`

What specific cryptographic implementations are used by the program? I.e. not "hashing", but a specific algorithm. Why might this pose a risk?
`Based on the cypto.h file provided and reading through the ledger.c file I was able to see the algorithm uses a md5_hash (Dynamically allocates and returns an md5 hash of the provided plaintext with
size message_len.), aes128_encrypt (Dynamically allocates and returns the result of aes128cbc encryption on a
plaintext with provided key and iv.) and aes128_decrypt(Dynamically allocates and returns the result of aes128cbc decryption on a ciphertext with provided key and iv.)`

What information, if any, are you able to derive from ledger.bin without decrypting it at all?
`We were able to figure out the ledger file format without decrypting it all`

How does the application ensure Confidentiality? How is the encryption key derived?
`The application ensures confidentiality by encrypting the messages prior to writing to a file using the md5_hash and aes128_encrypt. The encryption key is derived by first sending in the argv[1] and length to the md5_hash which returns a hash, but then to get the final key you only keep the first two bytes and turn all the other bytes to zero`

How does the application ensure Integrity? Is this flawed in any way?
`The application ensures Integrity by checking if the ciphertext hash from the file is equal to the actual hash file. The flaw to this is that its possible to modify the message`

How does the application ensure Authenticity? Is this flawed in any way?
`The application ensures Authenticity by checking if the hash from the file is equal to the hash of the provided key. The flaw to this is to make sure that the message is coming from the right place.`

How is the initialization vector generated and subsequently stored? Are there any issues with this implementation?
`The initialization vector is being generated randomly and it is being stored in the buffer.`
### Part 2 (45 Pts)

### Part 3 (10 Pts)
Explain where you think the deal balance lies between security through obscurity and converse ideologies such as Kerckhoff's principle. Examine and refute one counter argument to your point, referencing concrete examples from class.

`I think the balance between security through obscurity and converse idealogies is if we have came across known security breaches and know how to prevent those then we should build systems to prevent those and not follow security through obscurity, but without unknown factors I think security through obscurity is totally fine. A counter argument to this obscurity idealogy is that its very weak and we should do everything in our hands to have good security. The counter to this proposal is that it could be very expensive to research and come across the best systems without knowing the different types of security breaches`
