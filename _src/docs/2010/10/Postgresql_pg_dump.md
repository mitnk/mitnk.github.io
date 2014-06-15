Dump一个数据库到一个sql文件

    $ pg_dump mydb > db.sql


把这个sql文件导入到一个新建的数据库中

    $ psql -d newdb -f db.sql


只dump一个单独的表

    $ pg_dump -t mytab mydb > db.sql


Dump 所以dtroit schema是以emp开始的表，但不包括employee_log这个表

    $ pg_dump -t 'detroit.emp*' -T detroit.employee_log mydb > db.sql


Dump 所有的 schemas 名字以east 或 west 开头并以gsm结束的，但不包括名字中包含test的scema

    $ pg_dump -n 'east*gsm' -n 'west*gsm' -N '*test*' mydb > db.sql
    $ pg_dump -n '(east|west)*gsm' -N '*test*' mydb > db.sql

只dump一个单独表的结构（不含数据）

    $ pg_dump -t mytab -s mydb


只dump一个单独表的数据（不含结构）

    $ pg_dump -t mytab -a mydb

