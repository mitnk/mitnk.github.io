首先按顺序下载编译下面三个包

1. GMP <a href="http://gmplib.org/">下载</a>
2. MPFR <a href="http://www.mpfr.org/">下载</a>
3. MPC <a href="http://www.multiprecision.org/index.php?prog=mpc&page=download">下载</a>

下载<a href="http://gcc.gnu.org/mirrors.html">GCC源码</a>, 
然后在shell里执行

<code>
$ export CC=/usr/bin/gcc-4.2
$ export CXX=/usr/bin/g++-4.2
$ export CPP=/usr/bin/cpp-4.2
$ export LD=/usr/bin/ld
</code>

接下来进行configure， make，和make install即可  
（make的时间比较长，2个多小时）

参考：<a href="http://beardedcodewarrior.net/2011/07/25/building-gcc-4-6-1-on-mac-os-x-lion/">http://beardedcodewarrior.net</a>