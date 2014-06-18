有时我们会频繁地用ssh登录一台机器做事情  
有时因为ssh登录时需要密码使得一些自动化脚本不能很好的来撰写  
本篇简单说下如何使得ssh登录时不用密码  

<b>目标：</b>  
有两台机器 系统都为Linux  
本地机器A（自己的工作平台）  
远程机器B（拥有用户b，装有 openssh-server）  
从A ssh 到 B 时不需要密码  

<b>解决方步骤：</b>  
1) 查看A机器下有无此文件：  

    ~/.ssh/id_rsa.pub

如果有，跳到第2步； 如果没有使用下面命令生成之  

    $ ssh-keygen
    ( 提示输入passphrase时，直接回车，不要输入任何内容 )


2) 用下面命令将上面 public_key 放到机器B上（使它认识你的机器A）  

    $ ssh b@B mkdir -p .ssh
    ( -p 参数告诉 mkdir 如果文件夹已经存在也不要抱怨 )
    $ cat .ssh/id_rsa.pub | ssh b@B 'cat >> .ssh/authorized_keys'
    ( 上面两条命令都需要输入b用户的密码 )


从此，世界变得清静了！！  
ssh 时不再需要b的密码了！！  

----  

如果遇有问题（跟ssh版本有关系）可以尝试以下几条  
1) 把public key 也放到 .ssh/authorized_keys2 里面一份  
2) 把B中 .ssh 文件夹属性改为 700  
3) 把B中 .ssh/authorized_keys2 属性改为 640  

出处: <a href="http://linuxproblem.org/art_9.html">linuxproblem.org</a>  
