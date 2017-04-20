什么是反向代理
==============

大家应该都知道  
Nginx的通常角色是被用作反向代理  
你肯定**大概**知道它是什么意思  
什么是正向代理？  
什么是反向代理？  
你能试着给出精准定义吗？  

（正向）代理
------------

正向代理中的代理（Proxy）是以你（Client）的身份访问目标机器  
Proxy代表的是你（Client）  
对于目标机器来说  
它并不知道你的存在，而只知道是Proxy在请求资源  
而对你（Client）来说，你即知道Proxy也知道目标机器  
一个例子是你用一个国外HTTP代理访问Facebook网站  

反向代理
--------

反向代理从字面就可以大概知晓  
是反着为目标机器做代理的  
对于你（Client）来说  
你并不知道（或无从知道）目标机器的存在  
你访问的资源都像是Proxy本身直接提供的  
Proxy代表的是目标机器（群）  
像Nginx、HAProxy都是反向代理的例子  


[1] [http://stackoverflow.com/questions/224664/difference-between-proxy-server-and-reverse-proxy-server](http://stackoverflow.com/questions/224664/)
