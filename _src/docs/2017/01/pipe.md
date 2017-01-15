Pipe
====

在Unix中，Pipe line（管道）是用来将多个进程的输入输出连接到一块的工具。比如：

    :::
    ls | grep '\.txt' | wc -l

Pipe是系统内核中的一块内存；这块内存被多个进程共享。利用Pipe的好处是这块内存被
方便地标记为两个文件句柄，一个写入(W)一个读取(R)。

    :::python
    import os
    import subprocess

    r, w = os.pipe()
    pid = os.fork()

    if pid:  # Parent
        os.close(w)  # parent don't need to write
        p = subprocess.Popen(
            ['less', ],
            stdin=r,
        )
        p.wait()
    else:  # Child
        os.close(r)  # child don't need to read
        p = subprocess.Popen(
            ['ls', ],
            stdout=w,
        )
        p.wait()

也可以不用`fork`来示例。

    :::python
    import os
    import subprocess

    r, w = os.pipe()
    p1 = subprocess.Popen(
        ['ls', ],
        stdout=w,
    )
    p1.wait()
    os.close(w)
    p2 = subprocess.Popen(
        ['less', ],
        stdin=r,
    )
    p2.wait()
    os.close(r)

注意其中的 `os.close(w)` 比较关键。Pipe默认为阻塞的，如果没有这个 `close()`
的话，`less` 就拿不到 `EOF` 然后就会卡在那里等待管道中新数据的到来；
而这时 `ls` 进程已经退出了，不会再写入数据。

[1] [https://www.quora.com/How-do-pipes-in-Python-work](https://www.quora.com/How-do-pipes-in-Python-work)
