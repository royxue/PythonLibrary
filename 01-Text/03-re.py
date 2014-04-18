#coding: utf-8

import re

pat1 = 'this'
text = 'hello, this is my sublime'
match1 = re.search(pat1, text)

print match1.re.pattern, match1.string, match1.start(), match1.end()

#search() 搜索文本中的pattern,返回Match 对象

pat2 = re.compile('this')
if pat2.search(text):
	print 'Match'

#compile() 将字符串转换为 RegexObject

pat3 = 'is'
match2 = re.findall(pat3, text)
print match2

#findall返回匹配的字符串组

match3 = re.finditer(pat3, text)
print match3
for match in match3:
	print match.start(), match.end()

#finditer()返回迭代器, 生成Match对象

'''
重复语法
'ab*' a followed by 0 and more b
'ab+'               1
'ab?'               0 or 1
'ab{3}'             3 b
'ab{2, 3}'          2 to 3 b 
利用问号关系consume 的贪心行为 仅输出满足要求的部分
abbb
=> abbb (ab*)
=> a ('ab*?')
'''

'''
字符集
'[ab]' either a or b
^ 字符表示查找未在随后字符集出现的字符
'[^-. ]'  不含- . 空格的序列
'[a-zA-Z]' 长字符集
'.' 表示匹配任意字符
'''

'''
转义码
r''
\d 数字
\D 非数字
\s 空白符
\S 非空白符
\w 字母数字
\W 非字母数字
使用时要\\d 先对\转义,再正则
对于匹配正则式的字符
采用\ 对其转移 \. \\
'''

pat4 = re.compile('\\w+')
match4 = re.findall(pat4, text)
print match4

'''
锚定
锚定码
^ 字符串或者行的开始
$ 字符串或者行的结束
\A 字符串
\Z 字符串结束 
\b 单词开头或结尾的空串
\B 不在开头或结尾的空船
'''

'''组解析匹配
a(ab)*  ab变成一个组合
'''
'''
命名组 (?<name>pattern)
'''

pat5 = (r'(?P<end_with_s>\w+s\b)')
match5 = re.search(pat5, text)
print match5.group()
print match5.groupdict()
print match5.groups()


'''
re.compile 参数设置
1. re.INGORECASE  不区分大小写 									i
2. re.MULTILINE   开启多行模式, 每一行都会应用锚定规则				m
3. re.DOTALL      .字符可以匹配换行符								s 	
4. re.UNICODE     启用unicode匹配									u 
5. re.VERBOSE     Verbose 模式,分行正则匹配式,加入相应注释			x

正则表达式
在开头加入 (?i) 也可以开启不区分大小写匹配.
缩写见上面 (?isx)开启多模式 
前向断言和后向断言晕了... 
头脑清醒再看完,消化一下
'''

#Name & Email 匹配 自引用
pat6 = re.compile('[\w\d.+-]+@([\w\d.]+\.)+(com|org|edu)', re.UNICODE)

candi = 'xljroy@gmail.com'

match = pat6.search(candi)

print match.group()