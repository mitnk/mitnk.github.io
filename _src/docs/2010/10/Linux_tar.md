tar 是Linux下的打包程序，可以在打包的同时调用其它程序进行压缩

<span class="cr">打包</span>当前目录下所有的txt文件为 all.tar

    $ tar cf all.tar *.txt

解压 all.tar 

    $ tar xf all.tar 

列出 all.tar 中的所有文件

    $ tar tf all.tar


打包时调用gzip进行压缩

    $ tar czf all.tar.gz *.txt

解压 all.tar.gz

    $ tar xzf all.tar.gz


使用bzip2来压缩

    $ tar cjf all.tar.bz2 *.txt

解压 all.tar.bz2

    $ tar xjf all.tar.gz2

