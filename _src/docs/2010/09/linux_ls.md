Name:

ls - List directory contents

Synopsis:

    ls [-ABCFGHLOPRSTUW@abcdefghiklmnopqrstuwx1] [file ...]


Options:

每行只列一个文件  
列出所有文件  
列出所有文件但不输出 . ..  

    ls -1
    ls -a
    ls -A


列出所有文件详细信息  
让文件的大小增加可读性  
列出文件的修改时间详情  

    ls -l
    ls -lh
    ls -lT


只列出所有文件夹

    ls -d */


递归列出所有文件夹下的所有文件

    ls -R


如果想在文件夹后面加 /, 有两个命令可以做到：

    ls -F
    ls -p


列出文件的id号

    ls -i


用逗号分割文件名

    ls -m


让文件以行排序

    ls -x


以修改时间排序；以修改时间倒序排列；列出时间详情

    ls -t
    ls -tr
    ls -tT


以文件大小排序；倒序

    ls -S
    ls -Sr

