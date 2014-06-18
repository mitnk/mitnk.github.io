1. psql db_name -c "\dt" > all_tables.txt
   修改之，使每行只有表名

2. 创建一个sh文件如下：
#!/bin/bash
fname="all_tables.txt"
var=`cat $fname`

for name in $var
do
    msg="select count(*) from $name;select '$name';"
    echo $msg
done

运行这个脚本：
./find_e_table.sh > t.sql

再运行psql：
psql db_name -f t.sql
运行后得到以下内容：
 count 
-------
     0
(1 row)

  ?column?  
------------
 auth_group
(1 row)

 count 
-------
     0
(1 row)

        ?column?        
------------------------
 auth_group_permissions
(1 row)

 count 
-------
     0
(1 row)

   ?column?   
--------------
 auth_message
(1 row)

 count 
-------
   303
(1 row)

    ?column?     
-----------------
 auth_permission
(1 row)

 count 
-------
     3
(1 row)

 ?column?  
-----------
 auth_user
(1 row)

 count 
-------
     0
(1 row)

     ?column?     
------------------
 auth_user_groups
(1 row)

以上内容存为t.txt

3. 用grep整理
  grep "[^a-z]count[^a-z]\|[^a-z]column[^a-z]\|--\|^$\|row)" . -rvn --include=t.txt > tt.txt

tt.txt 内容如下：
     0
 auth_group
     0
 auth_group_permissions
     0
 auth_message
   303
 auth_permission
     3
 auth_user
     0
 auth_user_groups


4. 用vim打开tt.txt，搜索/[1-9] 回车 dj 直到找不到结果为止。
   最后用grep 删除0行即可：
grep "0" . -rvn --include=tt.txt > empty.txt

这是我对postgresql和linux命令行编程不熟的解决方案。
肯定有更方便的方式，如果谁有，请告诉我谢谢。
About里有我的信箱地址。