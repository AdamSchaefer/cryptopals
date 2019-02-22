#!/usr/bin/env python3
import sys
import codecs

# Let the user input the two strings to be XOR'd
string1 = input('Original string => ')
string2 = input('To be XOR\'d against => ')

# Convert strings to lists of bytecodes 
b_string1 = list(codecs.decode(string1, 'hex'))
b_string2 = list(codecs.decode(string2, 'hex'))

# Create list to store result
b_result = []

# Calculate the XORs
for byte1, byte2 in zip(b_string1, b_string2):
    b_result.append(byte1 ^ byte2)



# ugly optimized version
#print(bytes(byte1 ^ byte2 for byte1, byte2 in zip(
#    codecs.decode(string1, 'hex'),
#    codecs.decode(string2, 'hex')
#    )).decode()
#)


# Get and print result
result = codecs.encode(bytes(b_result), 'hex')
print(result.decode())
