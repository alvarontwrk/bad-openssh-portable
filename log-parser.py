#!/usr/bin/env python3

fc = open("/tmp/bad-openssh.log").read()

lines = fc.split("[bad-openssh] ")

prev = None
for i, t in enumerate(lines):
    if lines[i] == prev:
        lines[i] = None
    else:
        prev = t

clean_lines = list(filter(lambda x: x != None, lines))

print(len(clean_lines))

open("/tmp/bad-openssh2.log", "w").writelines(clean_lines)
