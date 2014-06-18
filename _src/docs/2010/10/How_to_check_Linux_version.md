a) uname 命令 `uname -a`

b) /proc 文件夹下的 version 文件 `cat /proc/version` 或 `cat /etc/issue`

c) /etc 目录下的 xxx-release 文件 `cat /etc/*release`

PS. 用 uname 还可以分辨一个系统是32位还是64位。如果在我的MBP上的结果是：

    $ uname -a
    Darwin localhost 11.3.0 Darwin Kernel Version 11.3.0: Thu Jan 12 18:47:41 PST 2012; root:xnu-1699.24.23~1/RELEASE_X86_64 x86_64

结尾处的 x86_64 说明这个 Mac OS X 是64位的。