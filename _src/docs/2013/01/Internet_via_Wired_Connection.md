Short answer: Run `sudo dhcpcd`.

Original Investigating Article
------------------------------

I was in a cafe called XiangRiKui, where is weird that without wireless network. If you want to connect to the Internet, they will provide you a Ethernet cable. This time, I only took my EPC with Arch Linux installed. And I didn't config any wired connection.

![Xiangrikui Cafe](/images/2013/01/xiangrikui_cafe.jpg)

I had to connect to internet with my iPhone's personal hotspot, and open Arch Linux's guide page[1]. And here is the instructions:

    $ ip link

The output was:

    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 16436 qdisc noqueue state UNKNOWN mode DEFAULT 
        link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    2: enp1s0: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN mode DEFAULT qlen 1000
        link/ether bc:ae:c6:3e:b3:70 brd ff:ff:ff:ff:ff:ff
    3: wlan0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP mode DORMANT qlen 1000
        link/ether 46:5e:a0:b3:d4:ec brd ff:ff:ff:ff:ff:ff

The interface `enp1s0` should be wired interface, since Ethernet interfaces are begin with a letter `e`. If we're unsure, try:

    $ iwconfig

The output was:

    wlan0     IEEE 802.11bgn  ESSID:"mitnk's iPhone"  
          Mode:Managed  Frequency:2.417 GHz  Access Point: EE:7D:28:E3:E1:88   
          Bit Rate=6 Mb/s   Tx-Power=19 dBm   
          Retry  long limit:7   RTS thr:off   Fragment thr:off
          Power Management:off
          Link Quality=65/70  Signal level=-45 dBm  
          Rx invalid nwid:0  Rx invalid crypt:0  Rx invalid frag:0
          Tx excessive retries:5  Invalid misc:17   Missed beacon:0

    lo        no wireless extensions.

    enp1s0    no wireless extensions.

This indicated that `lo` and `enp1s0` is NOT wireless interfaces.

Now we activate this interface:

    $ sudo ip link set enp1s0 up

Genericly, we need to know **Subnet mask**, **Gateway's IP address**, etc. But
we can use `dhcpcd` do this for us. Just type:

    $ sudo dhcpcd

To check, run command `ifconfig`, if you can see something like
`inet 192.168.11.168` under `enp1s0`, the wired connection was done successfully.

[1] [Arch Linux Beginners' Guide](https://wiki.archlinux.org/index.php/Beginners'_Guide#Wired)