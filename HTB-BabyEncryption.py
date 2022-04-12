# https://app.hackthebox.com/challenges/228
# The encryption is just some simple math:
# 123 * [ascii code] + 18
# and then result is divided by 256 and the remainder is
# converted back to ascii and makes up the msg.enc file.
# Here we're just bruteforcing each character by running
# through 1 to 256 and doing the math, then comparing the
# result to the value in the msg.enc file to see if we've
# found the decrypted value. If we find a match it gets
# appended to the decrypted variable and then returned append
# written to a message.txt file

import string

def encryption(msg):
    msg = bytes.fromhex(msg)

    decrypted = ''
    for char in msg:

        i = 1
        while(i<=256):
            test = (123 * i + 18) % 256
            if(char == test):
                deccode = chr(i)
                decrypted = decrypted + deccode
            i = i + 1

    return decrypted

# This is the encyrpted message from the msg.enc file they provide
decrypted = encryption('6e0a9372ec49a3f6930ed8723f9df6f6720ed8d89dc4937222ec7214d89d1e0e352ce0aa6ec82bf622227bb70e7fb7352249b7d893c493d8539dec8fb7935d490e7f9d22ec89b7a322ec8fd80e7f8921')
f = open('./message.txt','w')
f.write(decrypted)
f.close()
