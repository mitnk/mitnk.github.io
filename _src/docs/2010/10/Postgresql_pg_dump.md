Dump一个数据库到一个sql文件

    $ pg_dump mydb > db.sql


把这个sql文件导入到一个新建的数据库中

    $ psql -d newdb -f db.sql


只dump一个单独的表

    $ pg_dump -t mytab mydb > db.sql


只dump一个单独表的结构（不含数据）

    $ pg_dump -t mytab -s mydb


只dump一个单独表的数据（不含结构）

    $ pg_dump -t mytab -a mydb

只dump特定行

    $ psql db_name
    # COPY (SELECT * FROM mytable WHERE ... ) TO '/path/to/myfile.sql';
    # COPY mytable FROM 'myfile.sql'

Restore：

    $ psql db_name -f mydb.sql