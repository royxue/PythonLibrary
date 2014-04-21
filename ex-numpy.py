#coding: utf-8

import numpy as np 

'''array vs asarray
def asarray(a, dtype=None, order=None):
    return array(a, dtype, copy=False, order=order)
So it is like array, except it has fewer options, and copy = False. array has copy = True by default.
'''
#axis 轴方向 0方向 => 纵向 1方向 => 横向

a = np.array([1, 2, 3])
#print a
b = np.array([[1, 2, 3], [4, 5, 6]])
#print b
#print a.shape, b.shape

b.shape = 3, 2
#print b
d = a.reshape((3, 1))
#print d
#两种矩阵变换的方法

#print a.dtype

#可以使用dtype = 来定义数据类型.
#np.float 浮点数
#np.complex 复数,或使用typeDict来查询对应的类型

e = np.arange(0, 1, 0.1)
#print e
#初值,终值,步长

f = np.linspace(0, 1, 10, endpoint = True)
#print f
#设定初值,终值,步数 endpoint指定是否包含终值 this case True 步长 1/9 Flase 步长 1/10
g = np.logspace(0, 2, 5)
#print g
#等比数列 10的0次方 到 10的2次方

# print np.zeros((2, 4))
# print np.ones((3, 3))
# print np.empty((1, 4))  #直分配内存,不初始化

st = "abcdefg"
# print np.fromstring(st, dtype=np.int8)

def func1(i, j):
	return (i + 1) * (j + 1)
# print np.fromfunction(func1,(9, 9))

# array的存取 与 列表的方法累死
# 只是通过切片方法获取的新数组和原数组共享存储空间, 修改新的切片数组也会修改原数组
# 另一种可以用通过整数列表, 整数数组, 和布尔数组等高级存取方法, 这样获得不与原数组共享数据
h = a[[1, 2, 2]]
# print h
i = a[np.array([True, False, True])]
# print i

j = np.random.rand(10)
# print j[j > 0.5]


#多维数组读取
k = np.arange(0, 60, 10).reshape(-1, 1) + np.arange(0, 6) #利用自动补全
# print k

#slice对象存储下标元组
#slice(None, None, 2), slice(2, None)  = a[::2, 2:]
#numpy 通过 s_来创建
#print np.s_[::2, 2:]


#定义结构数组,类似C的struct
person = np.dtype({'names':['name', 'age', 'weight'], 'formats':['S32', 'i', 'f']}, align = True)
m = np.array([('Zhang', 32, 75.6)], dtype = person)
# 描述数据结构
#利用tostring()或者tofile()用二进制文件转换字符串或者写入文件.
# m.tofile('test.bin')
#读取 done!

#numpy默认用C语言的形式储存数据
n = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype = np.float32)
# print n.strides
#n.stride = (12 , 4) 意味着第0轴加1的时候,内存地址增加12(3个浮点数的字节数), 第1轴加1的时候内存地址增加4(1个浮点数的字节数)
#内存数据结构 1. dtype  2.dim count 3.dimentions 4.strides 5.data
# print n.flags
  # C_CONTIGUOUS : True		数据存储区域是否是C语言格式的连续区域
  # F_CONTIGUOUS : False	是否是Fortan语言格式的连续区域
  # OWNDATA : True			数组是否拥有这存储区域(如果是其他数组的视图则False)
  # WRITEABLE : True		
  # ALIGNED : True
  # UPDATEIFCOPY : False

o = n.T
# print o
# print o.flags
# print id(o.base)
# print id(n)

#直接利用属性来创建视图
p = np.arange(6)
# from numpy.lib.stride_tricks import as_strided
# q = as_strided(p, shape=(4, 3), strides=(4, 4))
# print b

#ufunc运算
#1.np.sin()  运算速度是math.sin的十几倍,得益于在C语言级别的循环运算. 返回float64  ///参数out = x,输出到x
#2.np.add() subtract减 multiply =加 divide整除 true_divide返回精确商  floor_divide返回值取整 negative负数 power乘方 remainder/mod余数
#参数(操作数1,操作数2,结果输出)

#逻辑运算 equal(),not_equal,less,less_equal,greater,greater_equal
#数组的布尔运算 logical_and , not, or, xor

#数组的自动拓展 => 广播
#numpy实际是用ogrid方法来快速广播计算

r, s = np.ogrid[:5, :5]
# print r, s

#ogrid的两种切片下标格式
#1. 开始:结束:步长   2. 开始:结束:长度j

#对已有不同轴取值的一位数组,计算网络点函数值,使用ix_()
x = np.array([1, 2, 3, 4])
y = np.array([0, 1, 2])
gy, gx = np.ix_(y, x)
# print gy, gx

#reduce 运算
#<op>.reduce(array, axis = 0, dtype = None)

#accumulate 类似reduce,但是返回的数组与输入数组结构类似,保存了运算的中间值

#reduceat 计算多组reuce结果,通过indices指定一系列的起始终止位置
v = np.array([1, 2, 3, 4])
res_v = np.add.reduceat(v, indices = [0, 1, 0, 2, 0, 3, 0])
# print res_v
# reduceat: if indices[i] < indices[i+1]:
#				result[i] = <op>.reduce(a[indices[i]:indices[i+1]])
# 			else:
#				result[i] = a[indices[i]] 

#out() 方法对每两对元素进行运算



#内存映射数组
#使用memmap() 创建
#调用参数为(filename, dtype = uint8, mode = 'r+', offset = 0,shape = None, order = 'C')
#filename  文件名, 除了'w+'模式之外,文件必须存在且存储了数据
#mode 'r' 只读, 'c' 修改但并不写入, 'r+' 读写并且自动保存, 'w+'创建或者覆盖已有文件

w = np.memmap("tmp.dat", mode='w+', shape=(2, 5))
print w
print file("tmp.dat").read()
w[:] = ord("a")
w.flush()
print w