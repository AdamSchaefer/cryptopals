#!/usr/bin/env python3
import sys
import codecs
import pprint

def xor(string1, string2):
    # Convert strings to lists of bytecodes 

    # Create list to store result
    b_result = []

    # Calculate the XORs
    for byte1, byte2 in zip(string1, string2):
        b_result.append(byte1 ^ byte2)

    # Get and print result
    result = codecs.encode(bytes(b_result), 'hex')
    return result

# Prepare the hex encoded string to be XOR'd
prepared_string = bytes(codecs.decode(input('Hex encoded string => '), 'hex'))

# Create list to store results
results = []

for i in range(0, 256):
    # Create my ceaser cipher as a list of bytes equal to the length of my encoded hex string
    ceaser_cipher = bytes([i] * len(prepared_string))
    xor_result = xor(prepared_string, ceaser_cipher)
    decoded_result = codecs.decode(xor_result, 'hex')

    count = sum(decoded_result.count(ch) for ch in (b'etaoinshrdlu'))

    results.append((count, decoded_result))

results.sort()

pprint.pprint(results[-10:])



