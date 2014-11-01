Linux xargs 的用法
=================

xargs是一个非常有用的工具，用来构建另一个命令的参数并执行它。

比如将一个文件夹下所有的.sh文件加上可执行权限，可以这样做：

    $ ls *.sh | xargs chmod +x


在Unix中 cp 这样的命令可以接收多个参数，这时最后一个参数会是目标文件夹。命令

    $ cp a b c d/

是将文件a， b， 和c 分别复制一份到d文件夹。但如果有很多文件，手动输入就非常麻烦了。这时就轮到xargs出手了，我们需要让它来提供前面的参数。

比如将Home目录下所有.mobi文件复制一份到 ebooks 文件夹。我们先尝试这样：

    $ cd
    $ find . -type f -name "*.mobi" | xargs cp ebooks/


但这样不行，报错。怎么办？

现在，我们<a href="http://unix.stackexchange.com/questions/24846/provide-params-to-scp-with-xargs">可以问stackoverflow</a>，可以google，可以man xargs
（我当时遇到这个问题时，竟然用的是这个顺序，明显反了嘛！！！）

正确的命令 (最易被人类或程序员理解的方案) 是这样的：

    $ find . -type f -name "*.mobi" | xargs -Iz cp z ebooks/

当然z可以换成别的东东（Unix命令中的Option与其数值之间有无空格均可）：

    $ find . -type f -name "*.mobi" | xargs -I{} cp '{}' ebooks/

学会xargs的这两种用法也就够用了。
