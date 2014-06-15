这几天给Mac配开发环境真是折腾、  

周一刚到公司就发现我的Mac无法上网  
Yihua、Shuaiqi都出马还是没弄好  
最后还是得让Zhangcheng出马  
经过一票“隐晦”的Shell命令之后  
他说，是VmWare这个虚拟机搞的鬼  
因为它的虚拟网络Hook了192.168.1.1这个网址  
把这个软件卸载了就一切正常了  

接下来两天，我每天六点多就起床了  
折腾MBP以便让它跑起开发环境来  

项目用的是Django ＋ PostgreSQL  
需要Psycopg2这个东东  
通过编译它的源码后，发现import时总是报错  
试了网上所有人的解决方案后还是不行  
最后看到Psycopg2的官网说可以用Macports来装它  
下载安装了Macports  
用命令 sudo port install psycopg2 终于安装成功并能正常使用了  
但这条命令执行了几个小时，真是不可接受！  
因为Macports安装东西不会看你本机已有的lib  
而是从它自己的ports里下载安装依赖  
比如安装 psycopg2 这个小东西，就给我额外安装了 python2.6 postgresql8 等等等包或软件  
再加上不能指定用哪个Mirror，下载速度一直居低不上  
所以用几个小时才结束安装  

但也算是work了吧  
然后继续用 port 来安装项目需要的其它包  
在此过程中又它又给我装了其它没必要的东西  
比如我装 html5lib 时，它又给我装了 python2.7  
真是有让我汗颜！  

最后一个叫IP2Location 的Python lib实在成功不了  
而这个包在我们本地几乎不需要  
所以我实现了个类似mock的东东  
以便让项目代码能import这个名字就成了  
至此项目算是跑起来了  

周二下班后，跟张成聊到 Macports 时，他说这是个比较OUT的东西的  
现在大家都用 Homebrew 这个工具来装软件  

晚上回家后，我手贱把 Macports 卸载了  
这个卸载比较暴力，先是要卸载安装过的所有包  
然后sudo rm -rf 掉一系统文件夹  
也就是我辛辛苦苦配起来的环境又被干掉了  
这样也好！  

试试 Homebrew吧  
安装之后发现它库里没有 psycopg2 这个包  
就又试图通过 psycopg2 的源码安装上它  
因为这样天然，一个小东西，实在不用额外安装一堆不需要的lib  
最后还是失败。。。。。  

这时我看了一下另一个安装工具 fink  
这也是个老家伙了，很老了  
他的工作原理和Ubuntu下的 apt-get 类似  
它自己维护了一些安装包  
并不像 macports 那样通过源码安装  

也许是我太菜，试了半天也没有成功  
明明他有这个包，但 install 命令就是说没有这个东东  
各位selfupdate，什么cvs版的都更新了  
最后还是失望地暴力卸载掉 fink  

然后，终于，烦透了这些省事的工具们  
立了一个原则：除非别无他法，否则不去使用诸如 macports, fink, homebrew 这些省力工具  


－－－－－（有用的）正文开始 －－－－－－－

1) 先用psql官网找到的dmg包安装了postgresql  
建好数据库（postgres用户的密码也是postgres）  

2) 下载安装 macports 1.9   
用 sudo port install psycopg2 安装 psycopg2  
（这个过程需要几个小时才能完成）  
安装成功后，只用它生成的二进制lib包  

    sudo cp -r /opt/local/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/site-packages/psycopg2* /Library/Python/2.6/site-packages/

然后按照macports 官网提供的方法卸载掉 macports （当然也删除了它安装的一些包）

3) 用easy_install 安装pip  

然后用pip安装 PIL 和 pycrypto等其它包包。。。  
或者，尽可能地去包包的官网下载源码，自己make自己install  
这样最天然  

4) 值得说的几个开发工具  

<b>grep</b>  
系统(Mac OS X 10.6.6）带的grep是V2.5.1，并不是支持 --exclude-dir 参数  
而我离不了这个参数（用grep -v来替代并不是好的方案）  
去<a href="http://ftp.gnu.org/gnu/grep/">官网下载了最新的V2.7版本</a>，结果编译不成功  
因为 --exclude-dir 参数是V2.5.3 加入的  
所以我试了V2.6.3版本，结果幸运地安装成功了！  
在 ~/.bash_profile 加入下载代码（第一行是让bash本身用ls等命令时着色）：  

    export CLICOLOR=1
    GREP_OPTIONS="--exclude-dir=.svn --binary-file=without-match --color"
    export GREP_OPTIONS


<b>colordiff</b>  
因为我是重度 svn diff 用户  
所以需要它的着色功能（svn diff原生不带此功能）  
去<a href="http://colordiff.sourceforge.net/">官网下载 colordiff</a> （Ubuntu下直接 apt-get install colordiff 可得）  
下载的源码让我迷了。。。。  
这个没有configure 之类的东东呀？？  
后来认真读了下INSTALL文件说明才知道，不用make也成（也许在Unix类系统里能正常make吧）  
用以下命令安装即可：  

    sudo cp colordiff.pl /usr/local/bin/colordiff
    sudo cp colordiffrc /etc/

在 ~/.bash_profile 文件里加入以下命令

    svndiff()
    {
        svn diff "${@}" | colordiff
    }

新开一个Shell，在项目下试试svndiff吧（以后使用 svndiff 来代替 svn diff）

<b>Vim, MacVim</b>  
首先把<a href="/article/1/">我的vimrc配置</a>写入 ~/.vimrc 中（按需修改）  
然后下载安装MacVim就行了  
这个MacVim好像有好几个？？  
我随便下了一个，是个app，复制到Applications文件夹下就能用了  
再下载 <a href="http://www.vim.org/scripts/script.php?script_id=182">supertab</a> <a href="http://www.vim.org/scripts/script.php?script_id=1658">NERDTree</a> 之类  
编辑之绝品神器自此搭成！  

<b>tree</b>  
Tree is a recursive directory listing command that produces a depth indented listing of files.  
下载地址在<a href="http://mama.indstate.edu/users/ice/tree/">这里</a>  

1. 按照Makefile中的指导，去掉Mac OS X的相关配置处的注释  
2. make  
3. sudo make install  

Updated at 27th Sept. 2011

Added [an related wiki page](/wiki/228/)

Updated at 27th Mar 2012
