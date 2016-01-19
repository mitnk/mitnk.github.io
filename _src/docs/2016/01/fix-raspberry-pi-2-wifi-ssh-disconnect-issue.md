树莓派2用Wifi时SSH总断开的问题及解决方案
========================================

前段时间入手一个闻名已久，但一直没有放在心上的树莓派。
我买的是第2代，4核Arm7 CPU + 1G RAM。使它当一个入门
家用服务器是够用了。

但这段时间一个问题一直困扰着我：连接Pi的网络很不稳定，
经常断。且我给其设置的静态IP常常Ping不通。搭建的SS服务
也时好时不好。甚至连上Pi干活的SSH连接也会在你停止输入
一段时间后断开。

我自己是发现在后台如screen里一直跑个`ping cn.bing.com` 会好点。
但这个终究不是最佳解决方案。

今天又想起这个事儿就在网上搜索了下，貌似真有终极解决方案的。

### 确定你的无线驱动

    :::bash
    $ ls /sys/class/net/
    eth0  lo  wlan0
    $ ls /sys/class/net/wlan0/device/driver/module/drivers
    usb:rtl8192cu

我的是`8192cu`，所以按搜索的方案如下：

    :::bash
    $ cat /sys/module/8192cu/parameters/rtw_power_mgnt
    1

### 关闭无线网卡电源管理

这个说明你的无线网卡的电源处于管理之下，为了省电会在不必要
的时候关闭无线网卡。为了关闭电源管理，我们需要新建以下文件：

    :::bash
    sudo touch /etc/modprobe.d/8192cu.conf

并其内容设置为：

    :::
    # Disable power management
    options 8192cu rtw_power_mgnt=0

之后重启Pi。然后检查一下是否无线电源管理已经关闭：

    :::bash
    $ cat /sys/module/8192cu/parameters/rtw_power_mgnt
    0

至此我们在Pi上的SSH连接终于开始稳定！

注：我用的无线网卡是EDUP EP-N8508GS黄金版。
如你的无线驱动不同，请用它+树莓派为关键字（英文）搜索，应该也有相应方案。


参考：

[1] [http://askubuntu.com/questions/96333/what-wireless-driver-am-i-using](http://askubuntu.com/questions/96333/what-wireless-driver-am-i-using)  
[2] [https://www.raspberrypi.org/forums/viewtopic.php?f=28&t=51543](https://www.raspberrypi.org/forums/viewtopic.php?f=28&t=51543)
