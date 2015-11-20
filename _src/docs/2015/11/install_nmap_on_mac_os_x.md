在Mac OS X上安装nmap
====================

[nmap](https://nmap.org/)是一个网络（端口）扫描工具。最基本的用途是这样的：

    :::bash
    $ nmap mitnk.com

    Starting Nmap 7.00 ( https://nmap.org ) at 2015-11-20 09:32 CST
    Nmap scan report for mitnk.com (212.47.241.150)
    Host is up (0.30s latency).
    rDNS record for 212.47.241.150: 150-241-47-212.rev.cloud.scaleway.com
    Not shown: 997 closed ports
    PORT    STATE SERVICE
    22/tcp  open  ssh
    80/tcp  open  http
    443/tcp open  https

    Nmap done: 1 IP address (1 host up) scanned in 49.03 seconds

今天nmap出了7.0版本，然后从官方网站下载了源码进行安装。 本来很简单的
`./configure && make` 就可以了。但因为我系统上的几个小问题，没有成功。

原因有两个

1. 我想编辑nmap时enable通过brew安装的openssl
2. 系统的 gcc 被我替换成了最新的5.2.0，而nmap在用一个参数已经有存在了

用`brew info openssl`查看openssl的信息

    :::bash
    $ brew info openssl

    ...
    Generally there are no consequences of this for you. If you build your
    own software and it requires this formula, you'll need to add to your
    build variables:

        LDFLAGS:  -L/usr/local/opt/openssl/lib
        CPPFLAGS: -I/usr/local/opt/openssl/include

然后告诉make我们要用 `/usr/bin/gcc` 而不是 `/usr/local/bin/gcc`

    :::bash
    $ CC=/usr/bin/gcc LDFLAGS="-L/usr/local/opt/openssl/lib" CPPFLAGS="-I/usr/local/opt/openssl/include" ./configure
    $ make
    $ make install

如果你当前用户对 `/usr/local` 没有写限制的话，最后一行要改为 `sudo make install`。

