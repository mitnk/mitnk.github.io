My notes on reading <a href="http://www.freeos.com/guides/lsst/index.html">Linux Shell Scripting Tutorial</a>

Print a variable

    :::bash
    $ echo $HOME


Define User defined variable

    :::bash
    $ n=10
    $ vech=
    $ vech=""


Shell Arithmetic

    :::bash
    $ expr 1 + 3
    $ echo `expr 6 \* 3`


Quotes:

    :::bash
    $ echo "$HOME"
    /home/mintk

    $ echo '$HOME'
    $HOME

    $ echo "Today is `date`"
    Today is Tue Oct 12 13:50:47 CST 2010

    $ echo 'Today is `date`'
    Today is `date`


Exit Status

    :::bash
    $ rm unknown1file
    rm: cannot remove `unkown1file': No such file or directory
    $ echo $?
    1

    $ ls
    $ echo $?
    0


The read Statement

    :::bash
    $ vim sayH
    echo "Your name please:"
    read name
    echo "Hello $name, Lets be friend!"

    $ chmod 755 sayH
    $ ./sayH
    Your name please:mitnk
    Hello mitnk, Lets be friend!


Wild cards

    :::bash
    ? * [abc] [a-c] [!a-c] [^a-c]
    [[:digit:]] alnum, alpha, ascii, blank, cntrl, digit, graph, lower, print, punct, space, upper, word, xdigit


More command on one command line

    :::bash
    $date;who


Command arguments

    :::bash
    $ vi demo
    #!/bin/sh
    #
    # Script that demos, command line args
    #
    echo "Total number of command line argument are $#"
    echo "$0 is script name"
    echo "$1 is first argument"
    echo "$2 is second argument"
    echo "All of them are :- $* or $@"


Redirection of Standard output / input

    :::bash
    $ ls > myfile
    $ date >> myfile

    $ cat < myfile
    $ cat > myfile
    ab
    c
    (Ctrl + C to exit)


Pipes

    :::bash
    ls | wc -l


Process defined as:
<quote>
"A process is program (command given by user) to perform specific Job. In Linux when you start process, it gives a number to process (called PID or process-id), PID starts from 0 to 65535."
</quote>

Linux Command Related with Process
<quote>
ps - To see currently running process
kill {PID} - To stop process by PID
killall {Process-name} - To stop processes by name

ps -ag - To get information about all running progress
linux-command &amp; - Run background

ps ax | grep process-U-want-to-see
pstree
</quote>
