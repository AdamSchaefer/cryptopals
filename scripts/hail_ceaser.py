#!/usr/bin/env python3
import sys
import codecs
from pprint import pprint

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


def single_ch_xor(ceaser_ciphered, cutoff=5, include_key=False):
    # Create list to store results
    results = []

    for i in range(0, 256):
        # Create my ceaser cipher as a list of bytes equal to the length of my encoded hex string
        ceaser_cipher = bytes([i] * len(ceaser_ciphered))
        xor_result = xor(ceaser_ciphered, ceaser_cipher)
        decoded_result = codecs.decode(xor_result, 'hex')

        count = sum(decoded_result.count(ch) for ch in (b'etaoinshrdlu'))

        if include_key:
            results.append((count, bytes([i]), decoded_result))
        else:
            results.append((count, decoded_result))

    results.sort()

    return results[-cutoff:]

if __name__ == "__main__":
    # Prepare the hex encoded string to be XOR'd
    prepared_string = bytes(codecs.decode(input('Hex encoded string => '), 'hex'))
    pprint(single_ch_xor(prepared_string))
