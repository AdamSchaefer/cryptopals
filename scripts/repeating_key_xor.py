#!/usr/bin/env python3
import sys
import codecs

def key_xor(plaintext, key):
    # For each byte in plaintext, calculate byte XOR key
    result = b''.join(bytes([plaintext[i] ^ key[i%len(key)]]) for i in range(len(plaintext)))
    return result


if __name__ == "__main__":
    # Create variables to store the stanza and key from CLI arguments
    stanza = sys.argv[1].encode()
    key = sys.argv[2].encode()

    result = key_xor(stanza, key)
    print(codecs.encode(result, 'hex'))
