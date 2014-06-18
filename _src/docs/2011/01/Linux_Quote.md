<b>反斜杠</b>   
你可以将一个 \ 放到一个字符的前面起转义作用。  

    $ echo hello world!
    hello world!
    $ rm file\ with\ spaces.txt
    $ echo This could be \
    a very \
    long line.
    This could be a very long line.


<b>单引号</b>  

    $ echo a       b
    a b
    $ echo a\ \ \ \ \ \ \ b
    a       b
    $ echo 'a       b'
    a       b
    $ echo 'can-quote*any $meta#chars'
    can-quote*any $meta#chars


<b>双引号</b>   

    $ echo 'Is your home directory $HOME?'
    Is your home directory $HOME?
    $ echo "Is your home directory $HOME?"
    Is your home directory /home/mitnk?
    $ echo "Current path is `pwd`"
    Current path is /home/mitnk/projects


<b>点号（`）</b>  

    $ echo "Current path is `pwd`"
    Current path is /home/mitnk/projects
    $ echo `pwd`
    /home/mitnk/projects
    $ echo "Today is `date`"
    Today is Wed Mar  2 00:51:50 CST 2011


<b>在文件名中使用引号</b>  

    1. cp /dev/null 'a file with spaces in the name'
    2. mv a\ file a_file
    3. mv a 'a?'
    (use "?" and "*" in a filename is playing with fire.)


<b>在引号中使用引号</b>  

    1. echo "Don't do that"
    2. echo 'The quote of the day is: "TGIF"'


<b>看看你引号是不是用错了</b>   
当你不确定引号是不是用对时  
可以在命令的前面加上echo试试  
（虽然echo不是总合适）  
<b>在引号中使用引用相同的引号</b>  

    1. echo "The word is \"Friday\""
    2. echo 'Don\'t quote me'
    3. echo 'a'b'c'
    3.1. echo 'a'$HOME'c'


<b>HERE IS documents</b>  

    % sort > file << EndOfSort
    zygote
    abacus
    EndOfSort


详细解説见： <a href="http://www.grymoire.com/Unix/Quote.html">www.grymoire.com</a>  
