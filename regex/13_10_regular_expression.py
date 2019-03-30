#!/usr/bin/env python3
# encoding: utf-8
import re

"""
正则表达式
https://morvanzhou.github.io/tutorials/python-basic/basic/13-10-regular-expression/
"""
# 简单的匹配
pattern1 = 'cat'
pattern2 = 'bird'
string = 'dog runs to cat'
print(pattern1 in string)  # True
print(pattern2 in string)  # False

print(re.search(pattern1, string))  # <_sre.SRE_Match object; span=(12, 15), match='cat'>
print(re.search(pattern2, string))  # None

# 灵活匹配
# multiple patterns ("run" or "ran")
ptn = r"r[au]n"
print(re.search(ptn, "dog runs to cat"))  # <_sre.SRE_Match object; span=(4, 7), match='run'>
