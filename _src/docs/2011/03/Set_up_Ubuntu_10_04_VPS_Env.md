1) 用root用户登录, init locale, 创建用户等

    :::bash
    $ apt-get update
    $ apt-get upgrade

    $ locale-gen en_US.UTF-8

    #or

    $ dpkg-reconfigure locales

    $ adduser mitnk
    $ apt-get install sudo
    $ visudo 
    ## (Add mitnk intoto sudolist)


安装 ssh server

    :::bash
    $ apt-get install openssh-server
    ## problem: not auto start when reboot
    ## solution: update-rc.d ssh defaults
    $ reboot



2) 用第二用户mitnk ssh登录，安装需要的软件

    :::bash
    $ sudo apt-get install vim git-core python-flup python-httplib2 python-pygments nginx postgresql subversion
    $ sudo apt-get install libpq-dev python-dev

配置 postgresql

    :::bash
    $ sudo passwd postgres
    $ sudo login postgres
    $ createuser mitnk -s
    $ exit
    $ createdb mitnk
    ## 等等


Reload database
nginx site configs
<a href="/4/">配置nginx, 用fastcgi跑django及其它</a>
等等

