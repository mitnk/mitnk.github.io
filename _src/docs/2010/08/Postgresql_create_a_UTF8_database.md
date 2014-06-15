我的vps上用apt-get命令安装的postgreSQL不知道为什么encoding是ASCII的
这样创建的数据库也是ASCII的

Google了下发现可以用这个命令创建utf-8数据库

    $ createdb -E UTF8 -T template0 foo
