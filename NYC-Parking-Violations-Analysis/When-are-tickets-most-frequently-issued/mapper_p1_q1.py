#!/usr/bin/python
# --*-- coding:utf-8 --*--
import sys

for line in sys.stdin:
    line = line.strip()
    violationtime = line.split(",")[19]
    if violationtime != "Violation Time":
        if violationtime != "":
                 print('%s\t%s' % (violationtime, '1'))
