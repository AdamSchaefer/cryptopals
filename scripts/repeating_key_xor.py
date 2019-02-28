#!/usr/bin/env python3
import sys
import codecs

# Create variables to store the stanza and key from CLI arguments
stanza = sys.argv[1].encode()
key = sys.argv[2].encode()

# For each byte in stanza, calculate byte XOR key
result = b''.join(bytes([stanza[i] ^ key[i%3]]) for i in range(len(stanza)))

print(codecs.encode(result, 'hex'))
