# 第一部分 Python基础篇（80题）

# 1.简述解释型和编译型编程语言

'''
解释型语言编写的程序不需要编译，在执行的时候，专门有一个解释器能够将VB语言翻译成机器语言，每个语句都是执行的时候才翻译。这样解释型语言每执行一次就要翻译一次，效率比较低。

用编译型语言写的程序执行之前，需要一个专门的编译过程，通过编译系统，把源高级程序编译成为机器语言文件，翻译只做了一次，运行时不需要翻译，所以编译型语言的程序执行效率高，但也不能一概而论，

部分解释型语言的解释器通过在运行时动态优化代码，甚至能够使解释型语言的性能超过编译型语言。
'''




# 2.Python解释器种类以及特点
'''
CPython当 从Python官方网站下载并安装好Python2.7后，就直接获得了一个官方版本的解释器：Cpython，这个解释器是用C语言开发的，
所以叫 CPython，在命名行下运行python，就是启动CPython解释器，CPython是使用最广的Python解释器。

IPythonIPython是基于CPython之上的一个交互式解释器，也就是说，IPython只是在交互方式上有所增强，但是执行Python代码的功能和CPython是完全一样的，
好比很多国产浏览器虽然外观不同，但内核其实是调用了IE。

PyPyPyPy是另一个Python解释器，它的目标是执行速度，PyPy采用JIT技术，对Python代码进行动态编译，所以可以显著提高Python代码的执行速度。
JythonJython是运行在Java平台上的Python解释器，可以直接把Python代码编译成Java字节码执行。
IronPythonIronPython和Jython类似，只不过IronPython是运行在微软.Net平台上的Python解释器，可以直接把Python代码编译成.Net的字节码。

---------------------
'''

# 3.位和字节的关系
'''
位：我们常说的bit，位就是传说中提到的计算机中的最小数据单位：说白了就是0或者1；计算机内存中的存储都是01这两个东西。

字节：英文单词：（byte），byte是存储空间的基本计量单位。1byte 存1个英文字母，2个byte存一个汉字。规定上是1个字节等于8个比特（1Byte = 8bit）。'''

# print(int('0b1111011',2))
# from socket import gethostname,gethostbyname_ex
#
# host = gethostname()
# ip = gethostbyname_ex(host)[2][0]
#
# def ipfunc(ip):
#     a = ip.split('.')
#     s = ''
#     l = []
#     for i in a:
#         i = bin(int(i))[2:]
#         # i = i.rjust(8, '0')
#         l.append(i)
#     return l
# end = ipfunc(ip)
# s = ''.join(end)
# print(s)v

a = 1
b = 2

b,a = a,b

print('a=',a)
print('b=',b)

