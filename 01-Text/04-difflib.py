#coding: utf-8

import difflib
#from difflib_data import *

text1 = '''
This week’s lecture segments are: Choosing ‘Selves’ Through Meditation; Meditation and Self-control;
 and The Experience of ‘Not-self’ (in which we hear firsthand reports from very experienced meditators).
'''
text1_lines = text1.splitlines()

text2 = '''
This week’s lecture segments is: Choosing ‘Selves’ Through Meditation; Meditation and Self-control;
 or The Experience of ‘Not-self’ (in which you will hear firsthand reports from very experienced meditators).
'''
text2_lines = text2.splitlines()

d = difflib.Differ()
diff = d.compare(text1_lines, text2_lines)

print '\n'.join(diff)

#ndiff()输出基本相同,但是会特别加工处理文本数据,删除输入噪声.

'''
  
- This week’s lecture segments are: Choosing ‘Selves’ Through Meditation; Meditation and Self-control;
?                                ^^^

+ This week’s lecture segments is: Choosing ‘Selves’ Through Meditation; Meditation and Self-control;
?                                ^^

-  and The Experience of ‘Not-self’ (in which we hear firsthand reports from very experienced meditators).
?  ^^^                                             ^

+  or The Experience of ‘Not-self’ (in which you will hear firsthand reports from very experienced meditators).
?  ^^                                            ++++ ^^^


***Repl Closed***

'''

diff2 = difflib.unified_diff(text1_lines, text2_lines, lineterm='',)
print '\n'.join(list(diff2))
#lineterm 说明不用添加换行符
#使用context_diff()会生成类似输出


#diff可以接受一些参数来只是忽略哪些行和那些数据
#默认情况下Differ类不会忽略任何行或者字符,而是依赖SequenceMatcher来去除噪声
#ndiff()默认忽略空格和tab

