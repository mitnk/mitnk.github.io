为了弄明白PostgreSQL和MySQL的差别，我搜索了关键字：MySQL vs PostgreSQL，并看了第一页的几个文章。以下是简单总结：

MySQL与PostgreSQL的区别
------------------

MySQL是应用开发者创建出来的DBMS；而PostgreSQL是由数据库开发者创建出来的DBMS [1]。

换句话说，MySQL倾向于使用者的角度，回答的问题是 “你想解决的是什么问题”；而PostgreSQL倾向于理论角度，回答的问题是 “数据库应该如何来解决问题” [2]。

MySQL一般会将数据合法性验证交给客户；PostgreSQL在合法性难方面做得比较严格。比如MySQL里插入 "2012-02-30" 这个时间时，会成功，但结果会是 "0000-00-00"；PostgreSQL不允许插入此值。

通常，PostgreSQL 被认为特性丰富，而MySQL被认为速度更快。但这个观点基本是在 MySQL 4.x / PostgreSQL 7.x 的事情，现在情况已经变了，PostgreSQL 在9.x版本速度上有了很大的改进，而MySQL特性也在增加[3]。

在架构上，MySQL分为两层：上层的SQL层和几个存储引擎（比如InnoDB，MyISAM）。PostgreSQL 只有一个存储引擎提供这两个功能。

这两个数据库系统都可以针对应用的情境被优化、定制，精确的说哪个性能更好很难。MySQL项目一开始焦点就在速度上，而PostgreSQL一开始焦点在特性和规范标准上。

选哪个？
-----

可能是由于历史原因MySQL在开发者中更流行一些。至少我们上学时没听说过PostgreSQL，当时不是MS SQL Server就是MySQL，而MySQL是开源的。实事上PostgreSQL直到8.0才官方支持了Windows系统。

如果没有什么历史原因（比如系统已经基于MySQL多年了），或技术积累原因（同事中MySQL高手多），那么我觉得选择PostgreSQL不会有错。

有趣的是，我在Google上搜索 "switch postgresql to mysql" 时，结果中第一页全是 "Switch to PostgreSQL from MySQL"，第二页终于有个是from PostgreSQL to MySQL，不过只有它一个，而且原因不是说PostgreSQL不好，而是因为作者MySQL经验多些[4]。

附录：简单测试
--------------

最后附上我自己对**MySQL v5.5** 和 **PostgreSQL v9.1** 在Mac OS，ML上的简单测试。MySQL是用brew安装的，PostgreSQL用的是[Heroku提供的app绿色版本](http://mitnk.com/98/)。因为都是默认安装，默认的配置，所以比较结果只是拿来参考。

表结构：

    Column       |           Type           | Modifiers 
    -------------------+--------------------------+-----------
     id                | bigint                   | not null
     created_at        | timestamp with time zone | not null
     from_user         | character varying(40)    | not null
     from_user_id      | bigint                   | not null
     from_user_name    | character varying(40)    | not null
     geo               | character varying(256)   | not null
     iso_language_code | character varying(8)     | not null
     source            | character varying(64)    | not null
     text              | character varying(170)   | not null
     to_user           | character varying(40)    | not null
     to_user_id        | bigint                   | not null
     to_user_name      | character varying(40)    | not null
    Indexes:
        "tweets_tweet_test_pkey" PRIMARY KEY, btree (id)


测试数据为100w多行真实Twitter数据：

    $ head -n4 out_pg.sql
    INSERT INTO tweets_tweet_test VALUES (287343655826624513, '2013-01-05 07:44:00+08', 'KevinPetrollini', 395657199, 'Kevin', '', 'zh', 'web', '给我的鞭子。', '', 0, '');
    INSERT INTO tweets_tweet_test VALUES (287142303481597952, '2013-01-04 18:23:54+08', 'mikaweixian', 65584780, 'M I K A. ', '', 'zh', 'Instagram', '唔知點解旅行返來日日都覺得好悶 ✈ 我重係不習慣一個人 😒 http://t.co/qC610DU6', '', 0, '');
    INSERT INTO tweets_tweet_test VALUES (287142333198266368, '2013-01-04 18:24:01+08', 'ShermaineChonq', 336528260, 'sнéямaїйε', '', 'zh', 'Twitter for Android', '"@MaymayBabyman: 心会累，因为自己不知道该坚持还是放弃。"', '', 0, '');
    INSERT INTO tweets_tweet_test VALUES (287142517768593408, '2013-01-04 18:24:45+08', 'mottled_shadow', 135373449, '斑驳的阴影', '', 'zh', 'twicca', '走路撸手姬差点一头撞停着的面包车上…', '', 0, '');

**INSERT 1,000,000行记录的速度**

MySQL: 8m22s  
PostgreSQL: 9m7s

**select count(id) from tweets_tweet_test where iso_language_code = 'zh'**

MySQL: 8.3s  
PostgreSQL: 0.5s


**select count(id) from tweets_tweet_test where id > 286894731655512065**

MySQL: 6.3s  
PostgreSQL: 1.5s


**select count(id) from tweets_tweet_test where text like '%好的%'**

MySQL: 9.4s  
PostgreSQL: 1.0s


**select id, text from tweets_tweet_test where text like '%xysdfljhsdf%'**

MySQL: 8.3s  
PostgreSQL: 0.84s

[1] [O/R modelling interlude: PostgreSQL vs MySQL](http://ledgersmbdev.blogspot.co.uk/2012/09/or-modelling-interlude-postgresql-vs.html)  
[2] [MYSQL VS POSTGRES (VS MONGODB)](http://dieswaytoofast.blogspot.jp/2012/09/mysql-vs-postgres-vs-mongodb.html)  
[3] [WikiVS: MySQL vs PostgreSQL](http://www.wikivs.com/wiki/MySQL_vs_PostgreSQL)  
[4] [How to move Bitnami OSQA stack from postgresql to mysql](http://meta.osqa.net/questions/12614/how-to-move-bitnami-osqa-stack-from-postgresql-to-mysql)