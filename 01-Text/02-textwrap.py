#coding: utf-8
import textwrap

text = '''
	You just joined tens of thousands of 
professional and community translators translating 10K+ projects on Transifex. 
Pretty neat!'''

print textwrap.fill(text, 60)
# 生成格式化文本

print

print textwrap.dedent(text)
#去除缩进
#删除各行都有的空白缩进(公共)

print

de_text = textwrap.dedent(text).strip()
print de_text

print

print textwrap.fill(de_text, initial_indent='', subsequent_indent=' ' * 4, width=50,)
#悬挂锁紧,第一行的缩进小于其他行