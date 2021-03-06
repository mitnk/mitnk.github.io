在Linux上执行多个命令
=====================

在Linux下，我们常常会执行一系列的命令来完成某件事。通常我们一个命令一个命令地输入，
在等到前一个命令完成了，我们再输入后一个命令。

（这里讲的是BASH）

其实我们可以用分号 ; 来一次执行多个命令。比如

    :::bash
    cd; ls

这条命令是cd到HOME目录下，然后执行ls命令。

还有一种方法是用两个 & 号，即： `&&`。比如：

    :::bash
    ./configure && make && make install

和用分号的区别是，如果前一个命令执行失败了（返回值不是0），那么后一条命令就不会执行。

给多条命令计时：

    :::bash
    time { ./configure && make && make install; }

注意最后一条命令后面有个分号。

[1] [Command grouping](http://mywiki.wooledge.org/BashGuide/CompoundCommands#Command_grouping)  
[2] [http://guide.bash.academy/](http://guide.bash.academy/)
