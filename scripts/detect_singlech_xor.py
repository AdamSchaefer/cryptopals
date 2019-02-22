#!/usr/bin/env python3
from hail_ceaser import single_ch_xor
from pprint import pprint
import codecs

with open("../challenge4_file.txt") as f:
    lines = [line.strip() for line in f]
    print(lines)

stored_result = []

for line in lines:
    results = single_ch_xor(codecs.decode(line, "hex"))
    stored_result += [result + (line,) for result in results]

pprint(sorted(stored_result))
