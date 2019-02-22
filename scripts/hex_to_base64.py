#!/usr/bin/env python3
import sys
import codecs

def convert(string):
    decoded = codecs.decode(string, 'hex')
    encoded = codecs.encode(decoded, 'base64')
    return encoded

string = input("String to decode => ")

print(convert(string).decode())
