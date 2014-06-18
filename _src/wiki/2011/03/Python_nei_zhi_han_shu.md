Python Built-in Functions

abs(x)
返回一个数字的绝对值，如果是复数返回其大小

all(iterable)
如果iterable里所有元素都为真，则返回True，否则返回False

any(iterable)
只要iterable里任何一个元素为真，就返回True，否则False

bin(x)
把一个数字转换为二进制字符串
New in Python 2.6

bool([x])
将一个值转换为布尔型

bytearray([source[, encoding[, errors]]])
返回一个字节数组

callable(object)
如果object是callable的，返回True，否则False

chr(i)
输入一个ASCII数值（0-255），输出其字符形式

classmethod(function)
classmethod装饰器

cmp(x, y)
当x < y, x == y, x > y时，分别返回 -1, 0, 1

complex([real[, imag]])
构造一个复数

delattr(object, name)
删除object的一个属性

dict([arg])
构造一个字典类型

dir([object])
输出当前作用域的可用数据，或object的所有属性

divmod(a, b)
把两个数字当作参数，返回两个数字的商和余数组成的值对

enumerate(seq[, start=0])
返回由 (0, seq[0]), (1, seq[1]), (2, seq[2]), ... 组成的枚举

eval(expression[, globals[, locals]])
计算expression的值，（在globals和locals的基础上）。

execfile(filename[, globals[, locals]])
和exec类似，执行一个文件内的python语句

file(filename[, mode[, bufsize]])
和open一样打开一个文件，但推荐用open

filter(function, iterable)
表达式 [item for item in iterable if function(item)] 的函数形式

float([x])
把一个数字或字符串转换为一个浮点数

format(value[, format_spec])
举个例子： '{2}, {1}, {0}'.format('a', 'b', 'c')
结果是： 'c, b, a'

getattr(obj, name[, default])
获取对象的一个属性值

globals()
返回一个字典，包含当前域可用符号表

hasattr(obj, name)
查看obj是否有name这个属性，是则返回True

hash(obj)
返回obj的hash值（一个数字）

hex(x)
转换一个数字为其十六进制字符串

id(obj)
返回obj的标识值

input([prompt])
和 eval(raw_input(prompt)) 一样

int([x[, base]])
转换x为int型

isinstance(obj, classinfo)
查看obj是否为classinfo类型的

issubclass(class, classinfo)
查看class是否是classinfo的子类

iter(o[, sentinel])
返回o的iterator对象

len(s)
返回s的长度（元素的个数）

list([iterable])
将iterable转化为list类型

locals()
返回描述当前标识表的字典

long([x[, base]])
将一个字符串或数字转化为一个长整数

map(fun, iterable, ...)
对iterable每个元素应用fun函数后返回结果

max(iterable[, args ...][, key])
返回iterable中最大的元素；如果参数是多个数值，则返回最大的

memoryview(obj)
返回obj的MemoryView对象

min(iterable[, args...][, key])
与max相烦，只是返回最小的元素

next(itrator[, default])
调用itrator的next方法，返回其值

oct(x)
将一个数字转换为一个十进制字符串

open(filename[, mode[, bufsize]])
打开一个文件，返回这个文件对象

ord(c)
与chr相反，提供一个字符，返回其Unicode数值

pow(x, y[, z])
返回x的y次方，并对z取模

print([obj,...]...)
将obj输出到流文件里

property([fget[, fset[, fdel[, doc]]]])
用法举例：
<code class="python">
class C(object):
  def __init__(self):
    self._x = None
  def getx(self):
    return self._x
  def setx(self, value):
    self._x = value

  x = property(getx, setx)
</code>

也可以使用装饰器
<code class="python">
class C(object):
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x
</code>

range([start], stop[, step])
根据起始条件生成一个list

raw_input([prompt])
<code class="python">
>>> s = raw_input('--> ')
--> Monty Python's Flying Circus
>>> s
'Monty Python's Flying Circus'
</code>

reduce(fun, iterable[, initializer])
将iterable中的元素，通过fun（两参函数）累加起来
如 reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) 的结果是 15
((((1+2)+3)+4)+5)

reload(module)
重新加载一个库

repr(obj)
返回一个obj的可打印形式，和``操作符一样

reversed(sed)
返回sed的反向itrator

round(x[, n])
返回x的n位小数精度的浮点数

set([iterable])
将iterable转化为set

setattr(obj, name, value)
给obj增加一个值为value名为name的属性

slice([start], stop[, step])
返回range()相对的一个slice对象

sorted(iteralbe[, cmp[, key[, reverse]]])
返回对iterable已经排好序的list

staticmethod(function)
返回function的静态形式

str([obj])
返回obj的可打印的字符串形式

sum(iterable[, start])
返回iterable中的元素累加值

super(type[, obj-or-type])
返回一个父类或兄弟类的对象代理（只在new style class里才有用）
例子：
<code class="python">
class C(B):
  def method(self, arg):
    super(C, self).method(arg)
</code>

tuple([iterable])
将iterable转化为tuple类

type(object)
返回object的类型

type(name, bases, dict)
以下两种声明X的方式是等价的
<code class="python">
>>> class X(object):
...     a = 1
...
>>> X = type('X', (object,), dict(a=1))
</code>

unichr(i)
返回一个Unicode code是i的Unicode字符

unicode([obj[, encoding[, errors]]])
返回obj的Unicode字符串

vars([obj])
返回包含obj的所有属性及其值的字典

zip([iterable, ...])
返回一个list，其中依次包括每个iterable的元素组成的元组