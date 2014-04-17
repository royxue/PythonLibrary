#coding: utf-8

import string

text = 'i am learning python library'

print string.capwords(text)

#所有单词首字母大写
#结果等于先调用split(),然后各单词首字母大写,再join()


leet = string.maketrans('abegiloprstz', '463611092572')

print text.translate(leet)

#maketrans建立转换表, 使用translate方法转换


#template

value = {'var': 'foo'}

t = string.Template("""
	Variables	: $var
	Escape	    : $$
	Var in Text : {$var}iable
	""")

print t.substitute(value)

s = """
	Variables	: %(var)s
	Escape	    : %%
	Var in Text : %(var)siable
	"""

print s % value

#采用template 不用考虑参数的类型,值会自动转换成字符串; 缺点是没有格式换选项, 无法控制float精确位
#使用safe_subtitute 避免未能提供全部模板参数产生异常


#高级模板之后补完.