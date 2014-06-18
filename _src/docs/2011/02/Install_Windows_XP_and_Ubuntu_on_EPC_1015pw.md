最终还是入手了 EPC 1015PW ：）  
顺丰快递就是给力  
昨天在Taobao上定的(上海)，今天就到了！

折腾了一下午，历尽艰辛终于把系统装好了  
这次没有用光驱，用U盘安装的  
在这里把折腾的过程记录一下  
免得以后重蹈覆辙...  

准备一个1G或1G以上的U盘  
先下载一个Ghost安装版本的Windows XP iso文件  
在Windows下（其它机器上）用UltraISO 将这个iso写入U盘里：  

1. （菜单）文件 -> 打开 -> Windows XP iso 文件  
2.  （菜单）启动 -> 写入硬盘映像...  
3. 在弹出的窗口里格式化，选择写入方式为 USB-HDD 并执行写入操作  

然后用USB方式启动 EPC 上网本  
给硬盘分好区  
我分的是大概是30（C盘）, 20（D盘）, 270G  
前两个盘给WinXP用  
执行Ghost 软件把 WinXP.gho 文件Ghost到EPC的C盘里  
<span style="color:red;">最后用硬盘分区医生之类的软件对C盘执行“重建MBR”操作</span>  
重启机器（这次从硬盘引导）完成Windows XP的安装  

接下来是安装第二系统Ubuntu  
下载Ubuntu 10.10 iso文件  
我用上面写WinXP的方式来做Ubuntu启动盘并不能成功启动起EPC来  
又试了官方网站上用 Universal USB Installer 在Windows上制作的U盘启动也不行  
<span style="color:red;">最后在Ubuntu 10.10系统（另一台机器）下用 Startup Disk Creator创建成功了！</span>  
（这个工具在 System -> Administration 下面）  
用这个U盘启动EPC，顺利完成Ubuntu的安装  
我的Ubuntu分区是这样的（可以参考下）  

- / ext4 25G
- /boot ext2 256M
- swap 2G
- /home ext4 200G
- /tmp ext4 20G

最后20G的 /tmp 分法是抱着玩玩的心态分的 [1]  
也可以将这些空间分给 /home

[1] Update：这样给 /tmp 分区[是不对的](http://mitnk.com/72/)  