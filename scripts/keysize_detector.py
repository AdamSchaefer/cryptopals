#!/usr/bin/env python3
import sys
import codecs
import base64

from hail_ceaser import single_ch_xor
from repeating_key_xor import key_xor

def hamm(s1, s2):
    hamming_distance = 0
    for i in range(len(s1)):
        hamming_distance += hamm_byte(s1[i], s2[i])
    return hamming_distance


def hamm_byte(b1, b2):
    # b1, b2 are integers (single bytes)
    result = 0
    combined = b1 ^ b2

    # count the 1 bits in 'combined'
    for exponent in range(8):
        if (combined & 2**exponent) != 0:
            result += 1

    return result


def get_key_size_guesses(data):
    guesses = []
    for keysize in range(2, 41):
        slice1 = data[:keysize]
        slice2 = data[keysize:2*keysize]
        slice3 = data[2*keysize:3*keysize]
        slice4 = data[3*keysize:4*keysize]

        normed1 = hamm(slice1, slice2) / keysize
        normed2 = hamm(slice3, slice4) / keysize
        normed3 = hamm(slice1, slice3) / keysize
        normed4 = hamm(slice1, slice4) / keysize
        normed5 = hamm(slice2, slice3) / keysize
        normed6 = hamm(slice2, slice4) / keysize
        avg = (normed1 + normed2 + normed3 + normed4 + normed5 + normed6) / 6
        guesses.append((avg, keysize))
    return guesses


#string1 = "this is a test"
#string2 = "wokka wokka!!!"
#
#b_string1 = string1.encode()
#b_string2 = string2.encode()
#
#print(hamm(b_string1, b_string2))

with open('../challenge_6.txt') as f:
    data = base64.b64decode(f.read())

#guesses = get_key_size_guesses(data)
#guesses.sort()
#for line in guesses[:5]:
#    print(line)

keysize_guess = 29  # obtained from the commented block above (other likely size: 29)

slices = [data[i::keysize_guess] for i in range(keysize_guess)]

top_guesses = []
for bytestring in slices:
    guess = single_ch_xor(bytestring, cutoff=1, include_key=True)[0]
    top_guesses.append(guess[1])

key_guess = b''.join(top_guesses)
print(key_guess)

print(key_xor(data, key_guess))
