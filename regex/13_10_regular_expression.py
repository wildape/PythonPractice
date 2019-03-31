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
print(re.search(r"r[A-Z]n", "dog runs to cat"))  # None
print(re.search(r"r[a-z]n", "dog runs to cat"))  # <_sre.SRE_Match object; span=(4, 7), match='run'>
print(re.search(r"r[0-9]n", "dog r2ns to cat"))  # <_sre.SRE_Match object; span=(4, 7), match='r2n'>
print(re.search(r"r[0-9a-z]n", "dog runs to cat"))  # <_sre.SRE_Match object; span=(4, 7), match='run'>

# 按类型匹配
'''
# 预定义字符集（可以写在字符集[...]中)
\d : 数字[0-9]
\D : 非数字[^\d]
\s : 空白字符 [<空格>\t\r\n\f\v]
\S : 非空白字符 [^\s]
\w : 单词字符 [0-9a-zA-Z_]
\W : 非单词字符 [^\w]
.  : 匹配任意除换行符之外的字符            a.c          abc
\  : 转义字符                          a\.c          a.c
'''
print(re.search(r"a\dc", "abc a1c"))  # <_sre.SRE_Match object; span=(4, 7), match='a1c'>
print(re.search(r"r\Dn", "run r2n"))  # <_sre.SRE_Match object; span=(0, 3), match='run'>
print(re.search(r"r\sn", "r\nn r4n"))  # <_sre.SRE_Match object; span=(0, 3), match='r\nn'>
print(re.search(r"r\Sn", "r\nn r4n"))  # <_sre.SRE_Match object; span=(4, 7), match='r4n'>
print(re.search(r"r\wn", "r\nn r4n"))  # <_sre.SRE_Match object; span=(4, 7), match='r4n'>
print(re.search(r"r\Wn", "r\nn r4n"))  # <_sre.SRE_Match object; span=(0, 3), match='r\nn'>

'''
# 数量词（用在字符或者(...)之后）
* : 匹配前一个字符0次或者无限次   abc*      eg. ab / abccc
+ : 匹配前一个字符1次或无限次     abc+          abc / abccc
? : 匹配前一个字符0次或者1次     abc?          ab  / abc
{m}: 匹配前一个字符m次          ab{2}c        abbc
{m,n}:匹配前一个字符m至n次      ab{1,2}c      abc/abbc
'''

'''
匹配边界（不消耗匹配字符串中的字符串）
^ : 匹配字符串开头，多行模式中匹配每一行的开头    ^abc       abc
$ : 匹配字符串末尾，多行模式中匹配每一行的末尾    abc$       abc
\A: 仅匹配字符串开头                         \Aabc      abc
\Z: 仅匹配字符串末尾                         abc\Z      abc
\b: 匹配\w和\W之间                          a\b!bc     a!bc
\B: [^\b]                                 a\Bbc      abc
'''

# 分组
match = re.search(r"(\d+), Date:(.+)", "ID: 021523, Date: Feb/3/2019")
print(match.group())  # 021523, Date: Feb/3/2019
print(match.group(1))  # 021523
print(match.group(2))  # Feb/3/2019

# 有时候, 组会很多, 光用数字可能比较难找到自己想要的组, 这时候, 如果有一个名字当做索引,
# 会是一件很容易的事. 我们字需要在括号的开头写上这样的形式 ?P<名字> 就给这个组定义了一个名字. 然后就能用这个名字找到这个组的内容.
match = re.search(r"(?P<id>\d+), Date: (?P<date>.+)", "ID: 021523, Date: Feb/12/2017")
print(match.group("id"))  # 021523
print(match.group("date"))  # Feb/12/2017

# findall
print(re.findall(r"r[ua]n", "run ran ren"))  # ['run', 'ran']

# | :or
print(re.findall(r"(run|ran)", "run ran ren"))  # ['run', 'ran']

# replace
# 使用这种匹配 re.sub(), 将会比 python 自带的 string.replace() 要灵活多变
print(re.sub(r"r[au]ns", "catches", "dog runs to cat"))  # dog catches to cat

# split
print(re.split(r"[,;\.]", "a;b,c.d;e"))  # ['a', 'b', 'c', 'd', 'e']

# compile
compiled_re = re.compile(r"r[ua]n")
print(compiled_re.search("dog ran to cat"))  # <_sre.SRE_Match object; span=(4, 7), match='ran'>
