家中mbp升级10.8ML后一直没有配置Postgresql  
今天在家工作发现 sqlite3 不支援 Django 的 distinct 操作  
终于懒人不得不用真刀真剑了  -- PostgreSQL

首先要知道OS X上已经自带了 psql 和 pg_dump 等命令行工具了  
(**Update**: psql这些工具我们也不会用系统提供的，见下面配置小节)  
我们需要的仅仅是 PostgreSQL 的服务端  
除了不方便的从源码编译（我没试过这个。。）  
还有就是下载 EnterpriseDB 提供的OS X安装包了  

但今天发现还有另一个选择： The PostgreSQL APP.  

> Postgres.app is the easiest way to get started with PostgreSQL on the Mac. 
> Open the app, and you have a PostgreSQL server ready and awaiting new connections. 
> Close the app, and the server shuts down.

相对于安装版本，这个app版有很多优点  

- 不用安装，下载解压、拖到应用程序文件夹里即可
- 不会给你创建新的用户，如 postgres 用户

算得上是**沙盒**版的 PostgreSQL 服务了  
现在去下载吧！  
<http://postgresapp.com>

配置
---

将app的命令行工具目录加到 PATH 中：

    :::bash
    PATH="/Applications/Postgres.app/Contents/MacOS/bin:$PATH"

Django的配置：

    :::python
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": "[YOUR_DATABASE_NAME]",
            "USER": "",
            "PASSWORD": "",
            "HOST": "localhost",
            "PORT": "",
        }
    }

更多配置选项见[官方文档](http://postgresapp.com/documentation).