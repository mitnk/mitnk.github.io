Django第一次公开发布是在2005年7月，svn版本号是8825。而在同年12月Django BDFL Jacob 就写过一个关于Django的性能指南[1]. 在技术领域，很多东东，比如框架，比如语言过时很快，但有些东西是不变的。而这篇指南我认为就是不变的东西，它不只是关于Django性能指南，我觉得它可以做为所有Web Server的性能参考。


**用一个独立的media文件服务器**

Django不是设计来Host静态文件的。如果你用一个Apache实例来serve Django和静态文件，那性能一定不会好到哪去。如果你买不起一个额外服务器，那至少用一个额外的进程。

**用一个独立的数据库服务器**

如果允许，用一个独立的数据库服务器。因为Apache和PostgreSQL（或MySQL等）会抢占系统各种资源。

**用PostgreSQL**

这个大概就会MySQL社区骂，但以我的经验，PostgreSQL几乎在所有方面都比MySQL快。

**内存越大越好**

内存的价格大概 $200 每G，但和程序员的价格比起来，太便宜了。买你能负担得起的最大内存，然后再多买一点。

更快的CPU并不会给性能带来多大提升，90%服务器都是在等IO。如果你有多台Server，那内存尽量给数据库服务器用。如果可能将整个数据库都放到内存里。

**关掉 keep-alive选项**

我真不知道这个选项是干什么的，但关掉它，你能提升大概50%的Django服务器性能。当然你可不要将serve静态文件服务器这个选项给关掉了。。

**用Memcached**

虽然Django支持不同的Cache后端，但一秒钟都不要想，直接用Memcached吧。

**微调、微调再微调**

Web服务，数据库引擎，机器本身的默认配置都不够好，你总能将它们调得更好。有N多文章介绍这些主题，以下几个文章仅是其中很少一部分：

- [Performance Tuning PostgreSQL by Frank Wiles](http://www.revsys.com/writings/postgresql-performance.html)
- [High Performance MySQL (if you’re the MySQL type)](http://www.bookpool.com/sm/0596003064).
- [Power PostgreSQL performance tips](http://www.powerpostgresql.com/PerfList).
- [The annotated postgresql.conf](http://www.varlena.com/GeneralBits/Tidbits/annotated_conf_e.html).
- The [postgresql-performance](http://archives.postgresql.org/pgsql-performance/) mailing list.
- ONLamp’s [Introducing LAMP Tuning Techniques](http://www.onlamp.com/pub/a/onlamp/2004/02/05/lamp_tuning.html).
- [Fixing an overloaded web server](http://alumnus.caltech.edu/~dank/fixing-overloaded-web-server.html).

[1] <http://jacobian.org/writing/django-performance-tips/>