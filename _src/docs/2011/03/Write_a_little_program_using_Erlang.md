前几天同事为应聘自动化测试的同学出了 <a href="http://projecteuler.net/index.php?section=problems&id=9">projecteuler 上面的一道题</a>：  
一个直角三角形三个边 a b c 之和为 1000  
且 a b c 皆为整数  
求三边之积  

有兴趣的读者可以停下来试着写程序跑上一跑

用Python来写这个程序可以是这个样子：

    :::python
    def triangle(N):
        for a in range(1, N/4):
            for b in range(1, N/2):
                c = N - a - b
                if a * a + b * b == c * c:
                    return a * b * c

    if __name__ == "__main__":
        print triangle(1000)


（由题目可推得两条直角边a b不可能大于或等于 N/2 且 小边小于 N/4）

下面看看用 Erlang 语言如何解决这个问题  
按照<a href="/36/">惯例</a>，先说下Erlang的一个语法：List Comprehensions  
据说要译为 列表推导，请看代码  

    :::erl
    $ erl
    1> L = [1, 3, 5].
    2> lists:map(fun(X) -> X*X end, L).
    [1,9,25]
    3> [X*X || X <- L].
    [1,9,25]


句3即为列表推导

注：句2为一个方便的函数定义，类似Python语言中的 <a href="http://diveintopython.org/power_of_introspection/lambda_functions.html">lambda 函数</a>  
Out 一下，给个例子  

    :::erl
    1> Z = fun(X) -> X * 2 end.
    2> Z(3).
    6


下面回到正题，现在来看看如何用Erlang来计算直角边之积吧：

    :::erlang
    -module(tri).
    -export([triangle/1]).

    triangle(N) ->
        [{A * B * (N - A - B)} ||
            A <- lists:seq(1, N div 4),
            B <- lists:seq(1, N div 2),
            A*A + B*B == (N - A - B) *(N - A - B)].


测试：

    :::erl
    $ erlc tri.erl
    $ erl
    1> tri:triangle(1000).
    [{31875000}]


<b>注</b>：这个算法是比较直接的，多数人都可以想到  
开始我觉得大概这样已经是最优解了  
但我另一个同事在那里用数字公式算来算去  
仅仅用一层循环就搞定了。。。  
我后来在 stackoverflow 上看到也<a href="http://stackoverflow.com/questions/2817848/find-pythagorean-triplet-for-which-a-b-c-1000#3436152">有人提到这个算法</a>  
