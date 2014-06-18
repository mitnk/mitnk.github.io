0) `$ man find`

1) 查找当前目录下所有.jpg文件：

    $ find . -name "*.jpg" -type f

注1： 可以使用Shell Pattern with * ? [ ]  
注2： -type 的选项是f d l 等  
注3： 可以用 -iname 代替 -name 以去除大小写敏感问题  
注3： 当前目录 . 可以省略  

2) 查找home目录下大于100M的文件

    $ find ~ -type f -size +100M

注：+n -n n 分别表示大于n，小于n，等于n

3) 查找当前目录24小时内改动过的py文件

    $find -name "*.py" -ctime -1

注1： -atime 为访问时间  
注2： -cmin -amin 为以分钟计算的时间  
注3： 相关参数还有 -anewer file -cnewer file （查找比file查改时间更新的）  

4) 修改时间为7天以前的文件

    $ find . -mtime +7

5) 查找当前目录下所有的隐藏（普遍）文件

    $ find -regex ".*\/\.[^/]*" -type f

注：可以 -iregex 来去除大小写敏感

6) 查找空文件（夹）

    $ find -empty

7) 查找用户mitnk所属的所有文件

    $ find -user mitnk

8) 查找当前目录中以及一级子目录中的py文件

    $ find -name "*.py" -maxdepth 2

注： 还有一个相关参数为 -mindepth

9) 查找名字不以txt结尾的文件
    $ find -not -name "*txt"

或

    $ find ! -name "*txt"

10) 查找当前目录下带a或b的文件

    $ find . -name "*a*" -or -name "*b*"

11) 查找当前目录下除.svn子目录以外的所有文件

    $ find . -path "*.svn" -prune -o -print

12) 查找权限是755的文件

    $ find . -perm 755

13) 输出当前目录下所有txt文件的内容

    $ find . -type f -name "*.txt" -exec cat {} \;

或

    $ find . -type f -name "*.txt" | xargs cat

14) 只搜索最小深度为3，最大尝试为5的所有文件夹 ( -maxdepth参数需要放在最前面 ）

    $ find . -mindepth 3 -maxdepth 5 -type d

