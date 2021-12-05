# RSAcma.py - RSA Common Modulus Attack

## Retro

---

### General information

This script allows you to exploit che common modulus vulnerability of RSA. 

What you will need is:

- the modulus n

- 2 different ciphertexts of the same text 

- 2 public exponents used to encrypt the original messages

and they have to be put in a file in this exact order.

You could choose to put them as integers or hexadecimal values, this will be specified as an argument while calling the script.

It will also be necessary that the exponents are coprimes and that at least one of the two ciphertexts is coprime with the modulus.

### How to use the script

```shell
Usage:
        python3 RSAcma.py <int/hex> <filename>

The file should contain on each line:
Modulus
First Ciphertext
Second Ciphertext
First Exponent
Second Exponent
```

It is pretty accurate and clear to understand: you just call the script, tell if the content of the file is integer or hexadecimal, and provide the file.

Hint: it generally doesn't take too much time to decrypt a file. If it is taking forever (or at least more than one minute), press CTRL+C to try new combination: just don't spam it and remember that the program exits only if it has decrypted the ciphertext or has given as output Decryption failed. 

Hint2: if at the end of the procedure the decryption has failed, try to invert manually into the file the first ciphertext with the second and clearly the first exponent with the second. The script is correct but not perfect.

### Examples

The script is provided with a pair of examples: one for the hexadecimal strings, one for the integer strings. Here you can see the output for both of them:

```shell
>> python3 RSAcma.py int RSAint.txt
[+]Components have been correctly read

[+]Parameter s1: -8
[+]Parameter s2: 7

[=]Decrypting: if the operation takes too much time(>1 minute), press Ctrl+C to try another combination

[-]The file could not be converted to ASCII
'ascii' codec can't decode byte 0xc9 in position 4: ordinal not in range(128)

[=]Trying another combination

[=]Ciphertexts inverted

[=]Decrypting: if the operation takes too much time(>1 minute), press Ctrl+C to try another combination

[+]The integer decrypted message is:
126207244316550804821666916

[+]The hexadecimal decrypted message is:
68656c6c6f20776f726c64

[+]The decrypted message is:
        hello world

Time elapsed: 00:00
```

and following for the hexadecimal ciphertexts:

```shell
>> python3 RSAcma.py hex RSAhex.txt
[+]Components have been correctly read

[+]Parameter s1: -381
[+]Parameter s2: 370

[=]Decrypting: if the operation takes too much time(>1 minute), press Ctrl+C to try another combination

[+]The integer decrypted message is:
617260313807931307283322352322677753710489515280014716039544653153138804

[+]The hexadecimal decrypted message is:
596f7520646973636f766572656420746865207365637265742074657874

[+]The decrypted message is:
        You discovered the secret text

Time elapsed: 00:00
```

### Contacts

Well in the end remember that it's not a perfect script, but I've  tried to manage all the possible exceptions I've found, in the most efficient way. If you find any bug, or have any implementation suggestion you can contact me here:

  *retro4hack@gmail.com*


