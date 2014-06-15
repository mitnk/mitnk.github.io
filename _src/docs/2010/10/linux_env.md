只需要使用这一个命令就ok了：

    $ env


输入是这个样子的：

    :::bash
    TERM_PROGRAM=Apple_Terminal
    TERM=xterm-color
    SHELL=/bin/bash
    CLICOLOR=1
    TMPDIR=/var/folders/m7/kryzkc9s5bq29hc9jbdp0rg00000gn/T/
    Apple_PubSub_Socket_Render=/tmp/launch-sbz8Fx/Render
    TERM_PROGRAM_VERSION=297
    TERM_SESSION_ID=49D1A498-25B6-4087-8EC0-5FC16802CDC9
    USER=mitnk
    LS_COLORS=1
    COMMAND_MODE=unix2003
    ...


有什么用呢？可以这样:

    :::bash
    $ echo "$USER"
    mitnk
